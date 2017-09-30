##############################################################################
#
# Copyright (c) 2001-2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Global Authentication Utility or Principal Registry
"""
from zope.component import getUtility
from zope.interface import implementer
import zope.security.management
from zope.security.interfaces import IGroupAwarePrincipal
from zope.password.interfaces import IPasswordManager

from zope.authentication.interfaces import (
    IAuthentication,
    PrincipalLookupError,
    ILoginPassword,
    ILogout,
    IUnauthenticatedPrincipal,
    IUnauthenticatedGroup,
    IAuthenticatedGroup,
    IEveryoneGroup,
    )

def _as_text(s):
    return s.decode('utf-8') if isinstance(s, bytes) else s

class DuplicateLogin(Exception):
    pass


class DuplicateId(Exception):
    pass


@implementer(IAuthentication, ILogout)
class PrincipalRegistry(object):
    """
    An in-memory implementation of :class:`zope.authentication.interfaces.IAuthentication`
    and :class:`zope.authentication.interfaces.ILogout`.
    """

    # Methods implementing IAuthentication

    def authenticate(self, request):
        a = ILoginPassword(request, None)
        if a is not None:
            login = a.getLogin()
            if login is not None:
                # The login will be in bytes, but the registry stores them
                # using strings.
                p = self.__principalsByLogin.get(_as_text(login), None)
                if p is not None:
                    password = a.getPassword()
                    if p.validate(password):
                        return p
        return None

    __defaultid = None
    __defaultObject = None

    def defineDefaultPrincipal(self, id, title, description=u'',
                               principal=None):
        id = _as_text(id)
        title = _as_text(title)
        description = _as_text(description)

        if id in self.__principalsById:
            raise DuplicateId(id)
        self.__defaultid = id
        if principal is None:
            principal = UnauthenticatedPrincipal(id, title, description)
        principal.__name__ = id
        principal.__parent__ = self
        self.__defaultObject = principal
        return principal

    def unauthenticatedPrincipal(self):
        return self.__defaultObject

    def unauthorized(self, id, request):
        if id is None or id == self.__defaultid:
            a = ILoginPassword(request)
            a.needLogin(realm="Zope")

    def getPrincipal(self, id):
        r = self.__principalsById.get(id)
        if r is None:
            if id == self.__defaultid:
                return self.__defaultObject
            if id == zope.security.management.system_user.id:
                return zope.security.management.system_user
            raise PrincipalLookupError(id)
        return r

    def getPrincipalByLogin(self, login):
        return self.__principalsByLogin[login]

    def getPrincipals(self, name):
        name = name.lower()
        return [p for p in self.__principalsById.values()
                if (p.title.lower().startswith(name) or
                    p.getLogin().lower().startswith(name))]

    def logout(self, request):
        # not supporting basic auth logout -- no such thing
        pass

    # Management methods

    def __init__(self):
        self.__principalsById = {}
        self.__principalsByLogin = {}

    def definePrincipal(self, principal, title, description=u'',
                        login=u'', password=b'', passwordManagerName='Plain Text'):
        id = _as_text(principal)
        title = _as_text(title)
        description = _as_text(description)
        login = _as_text(login)
        if login in self.__principalsByLogin:
            raise DuplicateLogin(login)

        if id in self.__principalsById or id == self.__defaultid:
            raise DuplicateId(id)

        p = Principal(id, title, description,
                      login, password, passwordManagerName)
        p.__name__ = id
        p.__parent__ = self

        self.__principalsByLogin[login] = p
        self.__principalsById[id] = p

        return p

    def registerGroup(self, group):
        id = _as_text(group.id)
        if id in self.__principalsById or id == self.__defaultid:
            raise DuplicateId(id)

        self.__principalsById[group.id] = group

    def _clear(self):
        self.__init__()
        self.__defaultid = None
        self.__defaultObject = None

#: The global registry that the ZCML directives will
#: modify.
principalRegistry = PrincipalRegistry()

# Register our cleanup with Testing.CleanUp to make writing unit tests
# simpler.
try:
    from zope.testing.cleanup import addCleanUp
except ImportError: # pragma: no cover
    pass
else:
    addCleanUp(principalRegistry._clear)
    del addCleanUp

class PrincipalBase(object):

    __name__ = __parent__ = None

    def __init__(self, id, title, description):
        self.id = _as_text(id)
        self.title = _as_text(title)
        self.description = _as_text(description)
        self.groups = []

class Group(PrincipalBase):

    def getLogin(self):
        return u'' # to make registry search happy

@implementer(IGroupAwarePrincipal)
class Principal(PrincipalBase):
    """
    The default implementation of :class:`zope.security.interfaces.IGroupAwarePrincipal`
    that :class:`PrincipalRegistry` will create.
    """

    def __init__(self, id, title, description, login,
                 pw, pwManagerName="Plain Text"):
        super(Principal, self).__init__(id, title, description)
        self.__login = _as_text(login)
        self.__pwManagerName = pwManagerName
        self.__pw = pw

    def __getPasswordManager(self):
        return getUtility(IPasswordManager, self.__pwManagerName)

    def getLogin(self):
        return self.__login

    def validate(self, pw):
        pwManager = self.__getPasswordManager()
        return pwManager.checkPassword(self.__pw, pw)


@implementer(IUnauthenticatedPrincipal)
class UnauthenticatedPrincipal(PrincipalBase):
    """An implementation of :class:`zope.authentication.interfaces.IUnauthenticatedPrincipal`."""


fallback_unauthenticated_principal = (
    UnauthenticatedPrincipal(
        __name__+'.fallback_unauthenticated_principal',
        'Fallback unauthenticated principal',
        'The default unauthenticated principal. Used as a fallback to '
        'allow challenging for a user even if the IAuthentication returned '
        'None as the unauthenticated principal.'))


@implementer(IUnauthenticatedGroup)
class UnauthenticatedGroup(Group):
    """An implementation of :class:`zope.authentication.interfaces.IUnauthenticatedGroup`."""

@implementer(IAuthenticatedGroup)
class AuthenticatedGroup(Group):
    """An implementation of :class:`zope.authentication.interfaces.IAuthenticatedGroup`."""

@implementer(IEveryoneGroup)
class EverybodyGroup(Group):
    """An implementation of :class:`zope.authentication.interfaces.IEverybodyGroup`."""

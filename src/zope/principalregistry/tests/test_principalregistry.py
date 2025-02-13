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
"""Tests for the principal registry
"""
import unittest

from zope.authentication.interfaces import PrincipalLookupError
from zope.authentication.loginpassword import LoginPassword
from zope.password.testing import setUpPasswordManagers

from zope.principalregistry.principalregistry import DuplicateId
from zope.principalregistry.principalregistry import DuplicateLogin
from zope.principalregistry.principalregistry import PrincipalRegistry


class Request(LoginPassword):

    challenge = None

    def __init__(self, lpw):
        if lpw is not None:
            login, password = lpw
        else:
            login = password = None
        super().__init__(login, password)

    def needLogin(self, realm):
        self.challenge = 'basic realm="%s"' % realm


class Test(unittest.TestCase):

    def setUp(self):
        setUpPasswordManagers()
        self.reg = PrincipalRegistry()
        # Passwords are provided in encoded form, which means they must be
        # bytes.
        self.reg.definePrincipal('1', 'Tim Peters', 'Sir Tim Peters',
                                 'tim', b'123')
        self.reg.definePrincipal('2', 'Jim Fulton', 'Sir Jim Fulton',
                                 'jim', b'456')

    def testRegistered(self):
        p = self.reg.getPrincipal('1')
        self.assertEqual(p.id, '1')
        self.assertEqual(p.title, 'Tim Peters')
        self.assertEqual(p.description, 'Sir Tim Peters')
        p = self.reg.getPrincipal('2')
        self.assertEqual(p.id, '2')
        self.assertEqual(p.title, 'Jim Fulton')
        self.assertEqual(p.description, 'Sir Jim Fulton')

        self.assertEqual(len(self.reg.getPrincipals('')), 2)

    def testUnRegistered(self):
        self.assertRaises(PrincipalLookupError, self.reg.getPrincipal, '3')

    def testDupPrincipal(self):
        self.assertRaises(DuplicateId,
                          self.reg.definePrincipal,
                          '1', 'Tim Peters', 'Sir Tim Peters',
                          'tim2', b'123')
        self.assertRaises(DuplicateLogin,
                          self.reg.definePrincipal,
                          '3', 'Tim Peters', 'Sir Tim Peters',
                          'tim', b'123')
        self.assertRaises(PrincipalLookupError, self.reg.getPrincipal, '3')
        self.assertEqual(len(self.reg.getPrincipals('')), 2)

    def testSearch(self):
        r = self.reg.getPrincipals('J')
        self.assertEqual(len(r), 1)
        self.assertIs(r[0], self.reg.getPrincipal('2'))

    def testByLogin(self):
        tim = self.reg.getPrincipalByLogin('tim')
        self.assertEqual(tim.getLogin(), 'tim')
        jim = self.reg.getPrincipalByLogin('jim')
        self.assertEqual(jim.getLogin(), 'jim')
        self.assertRaises(KeyError,
                          self.reg.getPrincipalByLogin, 'kim')

    def testValidation(self):
        tim = self.reg.getPrincipalByLogin('tim')
        self.assertTrue(tim.validate('123'))
        self.assertFalse(tim.validate('456'))
        self.assertFalse(tim.validate(''))
        self.assertFalse(tim.validate('1234'))
        self.assertFalse(tim.validate('12'))

    def _validatePrincipal(self, principal):
        from zope.interface.verify import verifyObject
        from zope.schema import getValidationErrors
        from zope.security.interfaces import IPrincipal

        self.assertTrue(verifyObject(IPrincipal, principal))

        errors = getValidationErrors(IPrincipal, principal)
        self.assertEqual([], errors)

    def testSchemaValidation(self):
        # Registered objects comply with IPrincipal
        tim = self.reg.getPrincipalByLogin('tim')
        self._validatePrincipal(tim)

    def testAuthenticate(self):
        req = Request((b'tim', b'123'))
        pid = self.reg.authenticate(req).id
        self.assertEqual(pid, '1')
        req = Request((b'tim', b'1234'))
        p = self.reg.authenticate(req)
        self.assertEqual(p, None)
        req = Request((b'kim', b'123'))
        p = self.reg.authenticate(req)
        self.assertEqual(p, None)

    def testUnauthorized(self):
        request = Request(None)
        self.reg.unauthorized(self.reg.unauthenticatedPrincipal(), request)
        self.assertEqual(request.challenge, 'basic realm="Zope"')
        request = Request(None)
        self.reg.unauthorized(None, request)
        self.assertEqual(request.challenge, 'basic realm="Zope"')
        request = Request(None)
        self.reg.unauthorized("1", request)
        self.assertEqual(request.challenge, None)

    def testDefaultPrincipal(self):
        self.assertEqual(self.reg.unauthenticatedPrincipal(), None)
        self.assertRaises(DuplicateId, self.reg.defineDefaultPrincipal,
                          "1", "tim")
        self.reg.defineDefaultPrincipal("everybody", "Default Principal")
        self.assertEqual(self.reg.unauthenticatedPrincipal().id, "everybody")
        anybody = self.reg.defineDefaultPrincipal(
            "anybody", "Default Principal", "This is the default headmaster")
        self.assertIs(anybody, self.reg.unauthenticatedPrincipal())
        self.assertEqual(anybody.id, "anybody")
        self.assertRaises(PrincipalLookupError,
                          self.reg.getPrincipal, "everybody")
        p = self.reg.getPrincipal("anybody")
        self.assertIs(p, anybody)
        self.assertEqual(p.id, "anybody")
        self.assertEqual(p.title, "Default Principal")
        self.assertRaises(DuplicateId, self.reg.definePrincipal,
                          "anybody", "title")

        # It complies with IPrincipal
        self._validatePrincipal(anybody)

    def test_logout(self):
        self.assertIsNone(self.reg.logout(None))

    def test_duplicate_group(self):
        class Group:
            id = "id"

        self.reg.registerGroup(Group)

        with self.assertRaises(DuplicateId):
            self.reg.registerGroup(Group)


class TestGroup(unittest.TestCase):

    def _getTargetClass(self):
        from zope.principalregistry.principalregistry import Group
        return Group

    def _getTargetInterface(self):
        from zope.interface import Interface
        return Interface

    def test_login(self):
        cls = self._getTargetClass()
        self.assertEqual('', cls("id", "title", "desc").getLogin())

    def test_valid(self):
        from zope.interface.verify import verifyObject
        from zope.schema import getValidationErrors

        schema = self._getTargetInterface()
        group = self._getTargetClass()("id", "title", "desc")

        self.assertTrue(verifyObject(schema, group))

        errors = getValidationErrors(schema, group)
        self.assertEqual([], errors)


class TestUnauthenticatedGroup(TestGroup):

    def _getTargetClass(self):
        from zope.principalregistry.principalregistry import \
            UnauthenticatedGroup
        return UnauthenticatedGroup

    def _getTargetInterface(self):
        from zope.authentication.interfaces import IUnauthenticatedGroup
        return IUnauthenticatedGroup


class TestAuthenticatedGroup(TestGroup):

    def _getTargetClass(self):
        from zope.principalregistry.principalregistry import AuthenticatedGroup
        return AuthenticatedGroup

    def _getTargetInterface(self):
        from zope.authentication.interfaces import IAuthenticatedGroup
        return IAuthenticatedGroup


class TestEverybodyGroup(TestGroup):

    def _getTargetClass(self):
        from zope.principalregistry.principalregistry import EverybodyGroup
        return EverybodyGroup

    def _getTargetInterface(self):
        from zope.authentication.interfaces import IEveryoneGroup
        return IEveryoneGroup


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

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
"""Directives for defining principals and groups
"""
from zope import component
from zope.component.zcml import utility
from zope.authentication import interfaces

from zope.principalregistry import principalregistry


def _principal():
    group = component.queryUtility(interfaces.IAuthenticatedGroup)
    if group is not None:
        _authenticatedGroup(group.id)
    group = component.queryUtility(interfaces.IEveryoneGroup)
    if group is not None:
        _everybodyGroup(group.id)

def principal(_context, id, title, login,
        password, description='', password_manager="Plain Text"):
    _context.action(
        discriminator = ('principal', id),
        callable = principalregistry.principalRegistry.definePrincipal,
        args = (id, title, description, login, password, password_manager) )
    _context.action(discriminator = None, callable = _principal, args = ())


def _unauthenticatedPrincipal():
    group = component.queryUtility(interfaces.IUnauthenticatedGroup)
    if group is not None:
        _unauthenticatedGroup(group.id)
    group = component.queryUtility(interfaces.IEveryoneGroup)
    if group is not None:
        _everybodyGroup(group.id)

def unauthenticatedPrincipal(_context, id, title, description=''):
    principal = principalregistry.UnauthenticatedPrincipal(
        id, title, description)
    _context.action(
        discriminator = 'unauthenticatedPrincipal',
        callable = principalregistry.principalRegistry.defineDefaultPrincipal,
        args = (id, title, description, principal) )
    utility(_context, interfaces.IUnauthenticatedPrincipal, principal)
    _context.action(
        discriminator = None,
        callable = _unauthenticatedPrincipal,
        args = (),
        )

def _unauthenticatedGroup(group):
    p = principalregistry.principalRegistry.unauthenticatedPrincipal()
    if p is not None:
        p.groups.append(group)

def unauthenticatedGroup(_context, id, title, description=''):
    principal = principalregistry.UnauthenticatedGroup(
        id, title, description)
    utility(_context, interfaces.IUnauthenticatedGroup, principal)
    _context.action(
        discriminator = None,
        callable = _unauthenticatedGroup,
        args = (principal.id, ),
        )
    _context.action(
        discriminator = None,
        callable = principalregistry.principalRegistry.registerGroup,
        args = (principal, ),
        )

def _authenticatedGroup(group):
    for p in principalregistry.principalRegistry.getPrincipals(''):
        if not isinstance(p, principalregistry.Principal):
            continue
        if group not in p.groups:
            p.groups.append(group)

def authenticatedGroup(_context, id, title, description=''):
    principal = principalregistry.AuthenticatedGroup(
        id, title, description)
    utility(_context, interfaces.IAuthenticatedGroup, principal)
    _context.action(
        discriminator = None,
        callable = _authenticatedGroup,
        args = (principal.id, ),
        )
    _context.action(
        discriminator = None,
        callable = principalregistry.principalRegistry.registerGroup,
        args = (principal, ),
        )

def _everybodyGroup(group):
    for p in principalregistry.principalRegistry.getPrincipals(''):
        if not isinstance(p, principalregistry.Principal):
            continue
        if group not in p.groups:
            p.groups.append(group)
    p = principalregistry.principalRegistry.unauthenticatedPrincipal()
    if p is not None:
        p.groups.append(group)

def everybodyGroup(_context, id, title, description=''):
    principal = principalregistry.EverybodyGroup(
        id, title, description)
    utility(_context, interfaces.IEveryoneGroup, principal)
    _context.action(
        discriminator = None,
        callable = _everybodyGroup,
        args = (principal.id, ),
        )
    _context.action(
        discriminator = None,
        callable = principalregistry.principalRegistry.registerGroup,
        args = (principal, ),
        )

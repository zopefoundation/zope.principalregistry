##############################################################################
#
# Copyright (c) 2009 Zope Corporation and Contributors.
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
"""Test importability of BBB interfaces

$Id$
"""
import unittest
from zope.testing import doctest

def test_bbb_imports():
    """
    Let's check that permission vocabularies that were moved to
    zope.security are still importable from original place.

      >>> import zope.app.security.interfaces as old
      >>> import zope.authentication.interfaces as new
      
      >>> old.PrincipalLookupError is new.PrincipalLookupError
      True
      >>> old.IUnauthenticatedPrincipal is new.IUnauthenticatedPrincipal
      True
      >>> old.IFallbackUnauthenticatedPrincipal is new.IFallbackUnauthenticatedPrincipal
      True
      >>> old.IUnauthenticatedGroup is new.IUnauthenticatedGroup
      True
      >>> old.IAuthenticatedGroup is new.IAuthenticatedGroup
      True
      >>> old.IEveryoneGroup is new.IEveryoneGroup
      True
      >>> old.IAuthentication is new.IAuthentication
      True
      >>> old.ILoginPassword is new.ILoginPassword
      True
      >>> old.IPrincipalSource is new.IPrincipalSource
      True
      >>> old.ILogout is new.ILogout
      True
      >>> old.ILogoutSupported is new.ILogoutSupported
      True
      
      >>> import zope.security.interfaces as new

      >>> old.IPrincipal is new.IPrincipal
      True
      >>> old.IPermission is new.IPermission
      True
      >>> old.IGroup is new.IGroup
      True
    
    """

def test_suite():
    return unittest.TestSuite((
        doctest.DocTestSuite(),
        ))

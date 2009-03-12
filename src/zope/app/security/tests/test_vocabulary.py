##############################################################################
#
# Copyright (c) 2003 Zope Corporation and Contributors.
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
"""Permission vocabluary doc tests.

$Id$
"""
import unittest
from zope.testing import doctest

def test_bbb_imports():
    """
    Let's check that permission vocabularies that were moved to
    zope.security are still importable from original place.
    
      >>> import zope.security.permission as new
      >>> import zope.app.security.vocabulary as old
      >>> old.PermissionsVocabulary is new.PermissionsVocabulary
      True
      >>> old.PermissionIdsVocabulary is new.PermissionIdsVocabulary
      True

      >>> import zope.authentication.principal as new
      >>> old.PrincipalSource is new.PrincipalSource
      True
    
    """

def test_suite():
    return unittest.TestSuite((
        doctest.DocTestSuite(),
        ))

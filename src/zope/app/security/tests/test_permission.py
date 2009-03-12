##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
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
"""Doctests for 'permission' module.

$Id$
"""
import unittest
import doctest

def test_bbb_imports():
    """
    Let's test that backward-compatibility imports still work:
    
      >>> from zope.app.security import permission as old
      >>> from zope.localpermission import permission as new
    
      >>> old.NULL_ID is new.NULL_ID
      True
      >>> old.LocalPermission is new.LocalPermission
      True
      >>> old.setIdOnActivation is new.setIdOnActivation
      True
      >>> old.unsetIdOnDeactivation is new.unsetIdOnDeactivation
      True

    """

def test_suite():
    return unittest.TestSuite((
        doctest.DocTestSuite(),
        ))

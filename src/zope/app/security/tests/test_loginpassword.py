##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
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
"""Test Login and Password

$Id$
"""
import unittest
from zope.testing import doctest

def test_bbb_imports():
    """
    Let's check that permission vocabularies that were moved to
    zope.security are still importable from original place.
    
      >>> import zope.authentication.loginpassword as new
      >>> import zope.app.security.loginpassword as old
      >>> old.LoginPassword is new.LoginPassword
      True
    
    """

def test_suite():
    return unittest.TestSuite((
        doctest.DocTestSuite(),
        ))

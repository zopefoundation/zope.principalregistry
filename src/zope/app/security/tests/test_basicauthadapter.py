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
"""Test Basic Authentication Adapter

$Id$
"""
import unittest
from zope.testing import doctest

def test_bbb_imports():
    """XXX: the place may change
    Let's check if original imports still work:
    
      >>> import zope.app.security.basicauthadapter as old
      >>> import zope.authentication.basicauthadapter as new
      
      >>> old.BasicAuthAdapter is new.BasicAuthAdapter
      True
    
    """

def test_suite():
    return unittest.TestSuite((
        doctest.DocTestSuite(),
        ))

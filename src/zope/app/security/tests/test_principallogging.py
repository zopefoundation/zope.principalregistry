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
"""Test for PrincipalLogging.

$Id$
"""
import unittest
from zope.testing.doctestunit import DocTestSuite

def test_bbb_imports():
    """
    Let's check that permission vocabularies that were moved to
    zope.security are still importable from original place.
    
      >>> import zope.publisher.principallogging as new
      >>> import zope.app.security.principallogging as old
      >>> old.PrincipalLogging is new.PrincipalLogging
      True
    
    """

def test_suite():
    return unittest.TestSuite((
        DocTestSuite(),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')

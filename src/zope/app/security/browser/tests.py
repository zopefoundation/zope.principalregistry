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
"""Security Views Tests

$Id$
"""
__docformat__ = "reStructuredText"
import unittest
from zope.testing import doctest
from zope.app.testing import placelesssetup

def test_bbb_imports():
    """
      >>> import zope.app.security.browser.principalterms as old
      >>> import zope.authentication.principal as new
      
      >>> old.PrincipalTerms is new.PrincipalTerms
      True
      >>> old.Term is new.PrincipalTerm
      True
    
    """

def test_suite():
    return unittest.TestSuite((
        doctest.DocTestSuite(),
        doctest.DocFileSuite('authutilitysearchview.txt',
                             setUp=placelesssetup.setUp,
                             tearDown=placelesssetup.tearDown),
        doctest.DocFileSuite('loginlogout.txt',
                             setUp=placelesssetup.setUp,
                             tearDown=placelesssetup.tearDown),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')


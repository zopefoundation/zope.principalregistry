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
"""Tests for the principal registry ZCML directives
"""

import doctest
import unittest

from zope.component.testing import setUp as setUpComponent
from zope.component.testing import tearDown as tearDownComponent
from zope.configuration import xmlconfig
from zope.password.testing import setUpPasswordManagers


def setUp(test=None):
    setUpComponent()
    setUpPasswordManagers()


def tearDown(test=None):
    tearDownComponent()


def zcml(s):
    import zope.principalregistry
    context = xmlconfig.file('meta.zcml', zope.principalregistry)
    xmlconfig.string(s, context)


def reset():
    tearDown()
    setUp()


def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite(
            '../README.rst',
            setUp=setUp, tearDown=tearDown,
            globs={
                'zcml': zcml,
                'reset': reset,
            }),
    ))

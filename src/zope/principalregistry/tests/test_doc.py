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
from __future__ import print_function

import doctest
import re
import unittest

from zope.component.testing import setUp as setUpComponent
from zope.component.testing import tearDown as tearDownComponent
from zope.configuration import xmlconfig
from zope.password.testing import setUpPasswordManagers
from zope.testing import renormalizing


checker = renormalizing.RENormalizing([
    # Python 3 unicode removed the "u".
    (re.compile("u('.*?')"),
     r"\1"),
    (re.compile('u(".*?")'),
     r"\1"),
])


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
            setUp=setUp, tearDown=tearDown, checker=checker,
            globs={
                'zcml': zcml,
                'reset': reset,
                'print_function': print_function,
            }),
    ))

##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
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
"""Setup for zope.app.security package

$Id$
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(name='zope.app.security',
      version = '3.7.0dev',
      author='Zope Corporation and Contributors',
      author_email='zope-dev@zope.org',
      description='Security Components for Zope 3 Applications',
      long_description=(
          read('README.txt')
          + '\n\n' +
          'Detailed Documentation\n' +
          '======================\n'
          + '\n\n' +
          read('src', 'zope', 'app', 'security', 'globalprincipals.txt')
          + '\n\n' +
          read('src', 'zope', 'app', 'security', 'browser',
               'authutilitysearchview.txt')
          + '\n\n' +
          read('src', 'zope', 'app', 'security', 'browser', 'loginlogout.txt')
          + '\n\n' +
          read('CHANGES.txt')
          ),
      keywords = "zope3 security authentication principal ftp http",
      classifiers = [
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope3'],
      url='http://pypi.python.org/pypi/zope.app.security',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['zope', 'zope.app'],
      extras_require=dict(test=['zope.app.testing']),
      install_requires=['setuptools',
                        'zope.browser',
                        'zope.app.component',
                        'zope.app.form',
                        'zope.app.pagetemplate',
                        'zope.app.publisher',
                        'zope.authentication',
                        'zope.component',
                        'zope.configuration',
                        'zope.container',
                        'zope.i18n',
                        'zope.i18nmessageid',
                        'zope.interface',
                        'zope.localpermission',
                        'zope.password',
                        'zope.publisher',
                        'zope.schema',
                        'zope.security',
                        'zope.site',
                        'ZODB3',
                        ],
      include_package_data = True,
      zip_safe = False,
      )

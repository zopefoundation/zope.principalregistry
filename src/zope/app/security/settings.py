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
"""Backward-compatibility import for security policy constants to allow
unpickling of old pickled security settings.

$Id$
"""
try:
    from zope.securitypolicy.settings import Allow, Deny, Unset
except ImportError:
    import logging
    logging.error('Allow, Unset and Deny constants are now '
                  'moved from zope.app.security.settings to '
                  'zope.securitypolicy.settings and you don\'t '
                  'seem to have it installed. This is very rare '
                  'case and you should manually install '
                  'the ``zope.securitypolicy`` package.')

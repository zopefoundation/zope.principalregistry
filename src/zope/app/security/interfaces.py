##############################################################################
#
# Copyright (c) 2009 Zope Corporation and Contributors.
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
"""Backward-compatibility imports for authentication interfaces

$Id$
"""

# BBB
from zope.security.interfaces import IPrincipal, IPermission, IGroup
from zope.authentication.interfaces import (
    PrincipalLookupError,
    IUnauthenticatedPrincipal,
    IFallbackUnauthenticatedPrincipal,
    IUnauthenticatedGroup,
    IAuthenticatedGroup,
    IEveryoneGroup,
    IAuthentication,
    ILoginPassword,
    IPrincipalSource,
    ILogout,
    ILogoutSupported,
    )

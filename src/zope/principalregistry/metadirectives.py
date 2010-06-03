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
"""Schemas for directives that define principals and groups
"""
from zope.interface import Interface
from zope.schema import Id, TextLine


class IBasePrincipalDirective(Interface):
    """Base interface for principal definition directives."""

    id = Id(
        title=u"Id",
        description=u"Id as which this object will be known and used.",
        required=True)

    title = TextLine(
        title=u"Title",
        description=u"Provides a title for the object.",
        required=True)

    description = TextLine(
        title=u"Title",
        description=u"Provides a description for the object.",
        required=False)

class IDefinePrincipalDirective(IBasePrincipalDirective):
    """Define a new principal."""

    login = TextLine(
        title=u"Username/Login",
        description=u"Specifies the Principal's Username/Login.",
        required=True)

    password = TextLine(
        title=u"Password",
        description=u"Specifies the Principal's Password.",
        required=True)

    password_manager = TextLine(
        title=u"Password Manager Name",
        description=(u"Name of the password manager will be used"
            " for encode/check the password"),
        default=u"Plain Text"
        )

class IDefineUnauthenticatedPrincipalDirective(IBasePrincipalDirective):
    """Define a new unauthenticated principal."""

class IDefineUnauthenticatedGroupDirective(IBasePrincipalDirective):
    """Define the unauthenticated group."""

class IDefineAuthenticatedGroupDirective(IBasePrincipalDirective):
    """Define the authenticated group."""

class IDefineEverybodyGroupDirective(IBasePrincipalDirective):
    """Define the everybody group."""

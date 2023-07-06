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
from zope.schema import Id
from zope.schema import TextLine


class TextId(Id):
    """
    An Id that is the text type instead of a native string.

    This is required because ``IPrincipal`` defines *id* to be
    the text type.
    """

    _type = str


class IBasePrincipalDirective(Interface):
    """Base interface for principal definition directives."""

    id = TextId(
        title="Id",
        description="Id as which this object will be known and used.",
        required=True)

    title = TextLine(
        title="Title",
        description="Provides a title for the object.",
        required=True)

    description = TextLine(
        title="Title",
        description="Provides a description for the object.",
        required=False)


class IDefinePrincipalDirective(IBasePrincipalDirective):
    """Define a new principal."""

    login = TextLine(
        title="Username/Login",
        description="Specifies the Principal's Username/Login.",
        required=True)

    password = TextLine(
        title="Password",
        description="Specifies the Principal's Password.",
        required=True)

    password_manager = TextLine(
        title="Password Manager Name",
        description=("Name of the password manager will be used"
                     " for encode/check the password"),
        default="Plain Text"
    )


class IDefineUnauthenticatedPrincipalDirective(IBasePrincipalDirective):
    """Define a new unauthenticated principal."""


class IDefineUnauthenticatedGroupDirective(IBasePrincipalDirective):
    """Define the unauthenticated group."""


class IDefineAuthenticatedGroupDirective(IBasePrincipalDirective):
    """Define the authenticated group."""


class IDefineEverybodyGroupDirective(IBasePrincipalDirective):
    """Define the everybody group."""

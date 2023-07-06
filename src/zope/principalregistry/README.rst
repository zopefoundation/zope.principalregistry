=============================
 Global principal definition
=============================

Global principals are defined via ZCML and are placed in
:data:`zope.principalregistry.principalregistry.principalRegistry`.
There are several kinds of principals that can be defined.

When you use ZCML to configure this package (load its
``configure.zcml``) that registry becomes a global utility
implementing :class:`zope.authentication.interfaces.IAuthentication`.

Authenticated Users
===================

There are principals that can log in:

    >>> zcml("""
    ...    <configure xmlns="http://namespaces.zope.org/zope">
    ...
    ...      <principal
    ...         id="zope.manager"
    ...         title="Manager"
    ...         description="System Manager"
    ...         login="admin"
    ...         password_manager="SHA1"
    ...         password="40bd001563085fc35165329ea1ff5c5ecbdbbeef"
    ...         />
    ...
    ...    </configure>
    ... """)

    >>> from zope.principalregistry.principalregistry import principalRegistry
    >>> [p] = principalRegistry.getPrincipals('')
    >>> p.id, p.title, p.description, p.getLogin(), p.validate('123')
    ('zope.manager', 'Manager', 'System Manager', 'admin', True)

We can verify that it conforms to the
:class:`zope.security.interfaces.IPrincipal` interface:

    >>> from zope.security.interfaces import IPrincipal
    >>> from zope.interface.verify import verifyObject
    >>> from zope.schema import getValidationErrors
    >>> verifyObject(IPrincipal, p)
    True
    >>> getValidationErrors(IPrincipal, p)
    []

In fact, it's actually a
:class:`zope.security.interfaces.IGroupAwarePrincipal`:

    >>> from zope.security.interfaces import IGroupAwarePrincipal
    >>> verifyObject(IGroupAwarePrincipal, p)
    True
    >>> getValidationErrors(IGroupAwarePrincipal, p)
    []


The unauthenticated principal
=============================

There is the unauthenticated principal:

    >>> zcml("""
    ...    <configure
    ...        xmlns="http://namespaces.zope.org/zope"
    ...        >
    ...
    ...      <unauthenticatedPrincipal
    ...         id="zope.unknown"
    ...         title="Anonymous user"
    ...         description="A person we don't know"
    ...         />
    ...
    ...    </configure>
    ... """)

    >>> p = principalRegistry.unauthenticatedPrincipal()
    >>> p.id, p.title, p.description
    ('zope.unknown', 'Anonymous user', "A person we don't know")

It implements :class:`zope.authentication.interfaces.IUnauthenticatedPrincipal`:

    >>> from zope.authentication import interfaces
    >>> verifyObject(interfaces.IUnauthenticatedPrincipal, p)
    True
    >>> getValidationErrors(interfaces.IUnauthenticatedPrincipal, p)
    []


The unauthenticated principal will also be registered as a utility.
This is to provide easy access to the data defined for the principal so
that other (more featureful) principal objects can be created for the
same principal.

    >>> from zope import component
    >>> p = component.getUtility(interfaces.IUnauthenticatedPrincipal)
    >>> p.id, p.title, p.description
    ('zope.unknown', 'Anonymous user', "A person we don't know")

The unauthenticated group
=========================

An unauthenticated group can also be defined in ZCML:

    >>> zcml("""
    ...    <configure
    ...        xmlns="http://namespaces.zope.org/zope"
    ...        >
    ...
    ...      <unauthenticatedGroup
    ...         id="zope.unknowngroup"
    ...         title="Anonymous users"
    ...         description="People we don't know"
    ...         />
    ...
    ...    </configure>
    ... """)

This directive creates a group and registers it as a utility providing
IUnauthenticatedGroup:

    >>> g = component.getUtility(interfaces.IUnauthenticatedGroup)
    >>> g.id, g.title, g.description
    ('zope.unknowngroup', 'Anonymous users', "People we don't know")

It implements :class:`zope.authentication.interfaces.IUnauthenticatedGroup`:

    >>> verifyObject(interfaces.IUnauthenticatedGroup, g)
    True
    >>> getValidationErrors(interfaces.IUnauthenticatedGroup, g)
    []

The unauthenticatedGroup directive also updates the group of the
unauthenticated principal:

    >>> p = principalRegistry.unauthenticatedPrincipal()
    >>> g.id in p.groups
    True
    >>> p = component.getUtility(interfaces.IUnauthenticatedPrincipal)
    >>> g.id in p.groups
    True

If the unauthenticated principal is defined after the unauthenticated
group, it will likewise have the group added to it:

    >>> reset()
    >>> zcml("""
    ...    <configure xmlns="http://namespaces.zope.org/zope">
    ...
    ...      <unauthenticatedGroup
    ...         id="zope.unknowngroup2"
    ...         title="Anonymous users"
    ...         description="People we don't know"
    ...         />
    ...      <unauthenticatedPrincipal
    ...         id="zope.unknown2"
    ...         title="Anonymous user"
    ...         description="A person we don't know"
    ...         />
    ...
    ...    </configure>
    ... """)

    >>> g = component.getUtility(interfaces.IUnauthenticatedGroup)
    >>> g.id, g.title, g.description
    ('zope.unknowngroup2', 'Anonymous users', "People we don't know")
    >>> p = principalRegistry.unauthenticatedPrincipal()
    >>> p.id, g.id in p.groups
    ('zope.unknown2', True)
    >>> p = component.getUtility(interfaces.IUnauthenticatedPrincipal)
    >>> p.id, g.id in p.groups
    ('zope.unknown2', True)

The unauthenticated group shows up as a principal in the principal
registry:

    >>> principalRegistry.getPrincipal(g.id) == g
    True

    >>> list(principalRegistry.getPrincipals("Anonymous")) == [g]
    True

The authenticated group
=======================

There is an authenticated group:

    >>> reset()
    >>> zcml("""
    ...    <configure xmlns="http://namespaces.zope.org/zope">
    ...
    ...      <unauthenticatedPrincipal
    ...         id="zope.unknown3"
    ...         title="Anonymous user"
    ...         description="A person we don't know"
    ...         />
    ...      <principal
    ...         id="zope.manager2"
    ...         title="Manager"
    ...         description="System Manager"
    ...         login="admin"
    ...         password="123"
    ...         />
    ...      <authenticatedGroup
    ...         id="zope.authenticated"
    ...         title="Authenticated users"
    ...         description="People we know"
    ...         />
    ...      <principal
    ...         id="zope.manager3"
    ...         title="Manager 3"
    ...         login="admin3"
    ...         password="123"
    ...         />
    ...
    ...    </configure>
    ... """)

It defines an IAuthenticatedGroup utility:

    >>> g = component.getUtility(interfaces.IAuthenticatedGroup)
    >>> g.id, g.title, g.description
    ('zope.authenticated', 'Authenticated users', 'People we know')

It implements :class:`zope.authentication.interfaces.IUnauthenticatedGroup`:

    >>> verifyObject(interfaces.IAuthenticatedGroup, g)
    True
    >>> getValidationErrors(interfaces.IAuthenticatedGroup, g)
    []

It also adds it self to the groups of any non-group principals already
defined, and, when non-group principals are defined, they put
themselves in the group if it's defined:

    >>> principals = sorted(principalRegistry.getPrincipals(''),
    ...                     key=lambda p: p.id)
    >>> for p in principals:
    ...    print(p.id, p.groups == [g.id])
    zope.authenticated False
    zope.manager2 True
    zope.manager3 True

Excluding unauthenticated principals, of course:

    >>> p = principalRegistry.unauthenticatedPrincipal()
    >>> p.id, g.id in p.groups
    ('zope.unknown3', False)
    >>> p = component.getUtility(interfaces.IUnauthenticatedPrincipal)
    >>> p.id, g.id in p.groups
    ('zope.unknown3', False)


The everybody group
===================

Finally, there is an everybody group:

    >>> reset()
    >>> zcml("""
    ...    <configure xmlns="http://namespaces.zope.org/zope">
    ...
    ...      <unauthenticatedPrincipal
    ...         id="zope.unknown4"
    ...         title="Anonymous user"
    ...         description="A person we don't know"
    ...         />
    ...      <principal
    ...         id="zope.manager4"
    ...         title="Manager"
    ...         description="System Manager"
    ...         login="admin"
    ...         password="123"
    ...         />
    ...      <everybodyGroup
    ...         id="zope.everybody"
    ...         title="Everybody"
    ...         description="All People"
    ...         />
    ...      <principal
    ...         id="zope.manager5"
    ...         title="Manager 5"
    ...         login="admin5"
    ...         password="123"
    ...         />
    ...
    ...    </configure>
    ... """)

The everybodyGroup directive defines an IEveryoneGroup utility:

    >>> g = component.getUtility(interfaces.IEveryoneGroup)
    >>> g.id, g.title, g.description
    ('zope.everybody', 'Everybody', 'All People')

It implements :class:`zope.authentication.interfaces.IEveryoneGroup`:

    >>> verifyObject(interfaces.IEveryoneGroup, g)
    True
    >>> getValidationErrors(interfaces.IEveryoneGroup, g)
    []

It also adds it self to the groups of any non-group principals already
defined, and, when non-group principals are defined, they put
themselves in the group if it's defined:

    >>> principals = sorted(principalRegistry.getPrincipals(''),
    ...                     key=lambda p: p.id)
    >>> for p in principals:
    ...    print(p.id, p.groups == [g.id])
    zope.everybody False
    zope.manager4 True
    zope.manager5 True

Including unauthenticated principals, of course:

    >>> p = principalRegistry.unauthenticatedPrincipal()
    >>> p.id, g.id in p.groups
    ('zope.unknown4', True)
    >>> p = component.getUtility(interfaces.IUnauthenticatedPrincipal)
    >>> p.id, g.id in p.groups
    ('zope.unknown4', True)

Note that it is up to IAuthentication implementations to associate
these groups with their principals, as appropriate.

In our case, if we define an unauthenticated principal after having
defined the everybody group, the principal will be automatically
added:

    >>> zcml("""
    ...    <configure xmlns="http://namespaces.zope.org/zope">
    ...
    ...      <unauthenticatedPrincipal
    ...         id="zope.unknown5"
    ...         title="Anonymous user"
    ...         description="A person we don't know"
    ...         />
    ...
    ...    </configure>
    ... """)
    >>> p = component.getUtility(interfaces.IUnauthenticatedPrincipal)
    >>> p.id, g.id in p.groups
    ('zope.unknown5', True)


The system_user
===============

There is also a system_user that is defined in the code.  It will be returned
from the getPrincipal method of the registry.

    >>> import zope.security.management
    >>> import zope.principalregistry.principalregistry
    >>> auth = zope.principalregistry.principalregistry.PrincipalRegistry()
    >>> system_user = auth.getPrincipal('zope.security.management.system_user')
    >>> system_user is zope.security.management.system_user
    True

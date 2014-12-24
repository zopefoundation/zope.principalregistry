Changes
=======

4.0.0 (unreleased)
------------------

- Add support for Python 3.4.

- Add support for testing under Travis.


4.0.0a2 (2013-03-03)
--------------------

- Make sure that the password is always bytes when passed into the principal
  registry.

- Fix deprecation warnings.


4.0.0a1 (2013-02-22)
--------------------

- Add support for Python 3.3.

- Replace deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Dropd support for Python 2.4 and 2.5.


3.7.1 (2010-09-25)
------------------

- Add test extra to declare test dependency on ``zope.component [test]``.

- Use Python's ``doctest`` module instead of depreacted
  ``zope.testing.doctest``.


3.7.0 (2009-03-14)
------------------

- Remove ``zope.container`` dependency, as contained principals didn't make any
  sense, since PrincipalRegistry never provided IContainer. Also, zope.container
  pulls a number dependencies, that are not needed for non-persistent principal
  registry (like, ZCML, for example).

  Set __name__ and __parent__ by hand to provide some backward-compatibility and
  to save a pointer to registry from principal objects.

- Initial release. This package was splitted from zope.app.security as a part
  of the refactoring process to provide global principal registry without extra
  dependencies.

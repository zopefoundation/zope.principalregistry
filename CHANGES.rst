=========
 Changes
=========

6.0 (2025-09-12)
================

- Replace ``pkg_resources`` namespace with PEP 420 native namespace.


5.1 (2025-02-14)
================

- Add support for Python 3.12, 3.13.

- Drop support for Python 3.7, 3.8.


5.0 (2023-07-06)
================

- Drop support for Python 2.7, 3.5, 3.6.

- Drop support for deprecated ``python setup.py test``.

- Add support for Python 3.11.


4.3 (2022-07-14)
================

- Drop support for Python 3.4.

- Add support for Python 3.7, 3.8, 3.9, 3.10.


4.2.0 (2017-10-01)
==================

- Fix principal and group objects registered in ZCML or directly with
  the principalregistry being invalid under Python 2 (having byte
  strings for ``id`` instead of text strings).
  See https://github.com/zopefoundation/zope.principalregistry/issues/7


4.1.0 (2017-09-04)
==================

- Add support for Python 3.5 and 3.6.

- Drop support for Python 2.6 and 3.3.

- Host documentation at https://zopeprincipalregistry.readthedocs.io

- Reach 100% test coverage and ensure we remain there.

- Test PyPy3 on Travis CI.

4.0.0 (2014-12-24)
==================

- Add support for PyPy.  (PyPy3 is pending release of a fix for:
  https://bitbucket.org/pypy/pypy/issue/1946)

- Add support for Python 3.4.

- Add support for testing under Travis.


4.0.0a2 (2013-03-03)
====================

- Make sure that the password is always bytes when passed into the principal
  registry.

- Fix deprecation warnings.


4.0.0a1 (2013-02-22)
====================

- Add support for Python 3.3.

- Replace deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Dropd support for Python 2.4 and 2.5.


3.7.1 (2010-09-25)
==================

- Add test extra to declare test dependency on ``zope.component [test]``.

- Use Python's ``doctest`` module instead of deprecated
  ``zope.testing.doctest``.


3.7.0 (2009-03-14)
==================

- Remove ``zope.container`` dependency, as contained principals didn't make any
  sense, since PrincipalRegistry never provided IContainer. Also, zope.container
  pulls a number dependencies, that are not needed for non-persistent principal
  registry (like, ZCML, for example).

  Set ``__name__`` and ``__parent__`` by hand to provide some backward-compatibility and
  to save a pointer to registry from principal objects.

- Initial release. This package was split from zope.app.security as a part
  of the refactoring process to provide global principal registry without extra
  dependencies.

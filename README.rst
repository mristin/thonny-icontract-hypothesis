***************************
thonny-icontract-hypothesis
***************************

.. image:: https://github.com/mristin/thonny-icontract-hypothesis/workflows/Continuous%20Integration%20-%20Ubuntu/badge.svg
    :alt: Continuous Integration - Ubuntu

.. image:: https://github.com/mristin/thonny-icontract-hypothesis/workflows/Continuous%20Integration%20-%20OSX/badge.svg
    :alt: Continuous Integration - OSX

.. image:: https://github.com/mristin/thonny-icontract-hypothesis/workflows/Continuous%20Integration%20-%20Windows/badge.svg
    :alt: Continuous Integration - Windows

.. image:: https://coveralls.io/repos/github/mristin/thonny-icontract-hypothesis/badge.svg?branch=main
    :target: https://coveralls.io/github/mristin/thonny-icontract-hypothesis?branch=main
    :alt: Test coverage

.. image:: https://badge.fury.io/py/thonny-icontract-hypothesis.svg
    :target: https://badge.fury.io/py/thonny-icontract-hypothesis
    :alt: PyPI - version

.. image:: https://img.shields.io/pypi/pyversions/thonny-icontract-hypothesis.svg
    :alt: PyPI - Python Version


thonny-icontract-hypothesis is a plug-in for `Thonny IDE`_ to automatically test
Python code using `icontract-hypothesis`_.

.. _Thonny IDE: https://thonny.org/
.. _icontract-hypothesis: https://github.com/mristin/icontract-hypothesis


Installation
============
In Thonny
---------
The plug-in can be easily installed *via* Thonny.
Go to ``Tools`` menu and select ``Manage plug-ins...``:

.. image:: https://raw.githubusercontent.com/mristin/thonny-icontract-hypothesis/main/readme/manage_plugins.png
    :alt: Tools -> Manage plug-ins...
    :width: 916
    :height: 472

Search for ``thonny-icontract-hypothesis`` on PyPI and click on the link to install it:

.. image:: https://raw.githubusercontent.com/mristin/thonny-icontract-hypothesis/main/readme/search_on_pypi.png
    :alt: Search on PyPI
    :width: 1251
    :height: 984

With pip
--------
In your virtual environment, invoke:

.. code-block::

    pip install --user thonny-icontract-hypothesis

Usage
=====
To check all the functions in the file with `icontract-hypothesis`, go to ``Tools``
menu and select ``Test the current file with icontract-hypothesis``:

.. image:: https://raw.githubusercontent.com/mristin/thonny-icontract-hypothesis/main/readme/tools_test.png
    :alt: Tools->Test
    :width: 909
    :height: 475

All changes to the file will be saved prior to executing the tests.
If you prefer, you can undo them.

The tests will be executed in the Thonny shell:

.. image:: https://raw.githubusercontent.com/mristin/thonny-icontract-hypothesis/main/readme/shell.png
    :alt: Shell running the tests
    :width: 1317
    :height: 1045

You can stop the tests with the "Stop" sign:

.. image:: https://raw.githubusercontent.com/mristin/thonny-icontract-hypothesis/main/readme/stop.png
    :alt: Stop the tests
    :width: 741
    :height: 378

Sometimes it is practical to test only a single function (*e.g.*, if it takes too long
to test the whole file).
In that case, move the caret to the body of the function that you would like to test,
go to ``Tools`` menu and select ``Test the function under the caret with
icontract-hypothesis``:

.. image:: https://raw.githubusercontent.com/mristin/thonny-icontract-hypothesis/main/readme/tools_test_at.png
    :alt: Tools->Test at
    :width: 917
    :height: 471

Contributing
============

Feature requests or bug reports are always very, very welcome!

Please see quickly if the issue does not already exist in the `issue section`_ and,
if not, create `a new issue`_.

.. _issue section: https://github.com/mristin/thonny-icontract-hypothesis/issues
.. _a new issue: https://github.com/mristin/thonny-icontract-hypothesis/issues/new

You can also contribute in code.
Please see `contributing.rst`_.

.. _contributing.rst: https://github.com/mristin/thonny-icontract-hypothesis/blob/main/contributing.rst

Versioning
==========
We follow a bit unusual semantic versioning schema:

* X is the oldest supported version of `icontract-hypothesis`_,
* Y is the minor version (new or modified features), and
* Z is the patch version (only bug fixes).

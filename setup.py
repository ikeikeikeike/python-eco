import os
from setuptools import setup


version = '0.9'
name = 'eco'
short_description = 'python-eco is a bridge to the ECO Template compiler'
long_description = """\
``python-eco is a bridge to the ECO Template compiler.``

Description
===========
python-eco is a bridge to the ECO Template compiler.

Requirements
============
* CoffeeScript

Setup
=====

.. highlight:: bash

::

    $ pip install eco


**Python Eco**
~~~~~~~~~~~~~~~

.. highlight:: python

::

    import eco

    eco.compile(open("template.eco"))
    # Out: u"function(...) {...}"

    context = eco.context_for("Hello <%= @name %>")
    context.call("render", {"name": "Sam"})
    # Out: u'Hello Sam'

    eco.render("Hello <%= @name %>", name="world")
    # Out: u'Hello world'


History
========
0.9 (2012-06-17)
~~~~~~~~~~~~~~~~~
* first release

License
========
MIT License
"""

root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)

setup(
    name=name,
    version=version,
    description=short_description,
    long_description=long_description,
    classifiers=[
       "Development Status :: 4 - Beta",
       "Development Status :: 5 - Production/Stable",
       'Environment :: Console'
       "Environment :: Web Environment",
       "Intended Audience :: Developers",
       'License :: OSI Approved :: MIT License',
       "Programming Language :: Python :: 2"
       "Programming Language :: Python :: 2.6",
       "Programming Language :: Python :: 2.7",
       "Programming Language :: Python :: 3"
       "Programming Language :: Python :: 3.1"
       "Programming Language :: Python :: 3.2"
       'Topic :: Utilities',
       'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['javascript', 'coffeescript', 'eco', 'compiler'],
    author='Tatsuo Ikeda',
    author_email='jp.ne.co.jp at gmail',
    url='https://github.com/ikeikeikeike/python-eco',
    license='MIT License',
    packages=['eco'],
    package_dir={'eco': 'eco'},
    package_data={'eco': ['eco.js', '__init__.py'],},
    py_modules=['eco'],
    install_requires=['CoffeeScript'],
    test_suite="test_eco",
)

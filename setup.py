import os
from setuptools import setup

name = 'eco'
version = '1.1.0'
short_description = 'Python Eco is a bridge to the ECO(CoffeeScript Template) Compiler.'
long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)

setup(
    name=name,
    version=version,
    description=short_description,
    long_description=long_description,
    classifiers=[
       "Development Status :: 5 - Production/Stable",
       'Environment :: Console',
       "Environment :: Web Environment",
       "Intended Audience :: Developers",
       'License :: OSI Approved :: MIT License',
       "Programming Language :: Python :: 2",
       "Programming Language :: Python :: 2.6",
       "Programming Language :: Python :: 2.7",
       "Programming Language :: Python :: 3",
       "Programming Language :: Python :: 3.1",
       "Programming Language :: Python :: 3.2",
       'Topic :: Utilities',
       'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['javascript', 'coffeescript', 'eco', 'compiler'],
    packages=['eco'],
    package_dir={'eco': 'eco'},
    package_data={'eco': ['eco.js']},
    install_requires=['CoffeeScript', 'six'],
    test_suite="test_eco",
    author='Tatsuo Ikeda',
    author_email='jp.ne.co.jp at gmail',
    url='https://github.com/ikeikeikeike/python-eco',
    license='MIT License',
)

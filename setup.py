#! /usr/bin/env python
# encoding: utf-8


"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
# To use a consistent encoding
from codecs import open
from os import path
import sys


here = path.abspath(path.dirname(__file__))


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


cmdclass = {}
cmdclass['test'] = PyTest

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]

setup(
    name='pyallinpay',
    version='1.1.4',
    keywords='pyallinpay, SDK, 通联支付',
    description='AllInPay SDK for Python',
    long_description=long_description,
    url='https://github.com/007gzs/pyallinpay',
    author='007gzs',
    author_email='007gzs@sina.com',
    license='LGPL v3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(exclude=('tests', )),
    install_requires=requirements,
    zip_safe=False,
    include_package_data=True,
    tests_require=[
        'pytest',
    ],
    cmdclass=cmdclass,
)

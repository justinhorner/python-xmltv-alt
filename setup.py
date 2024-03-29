#!/usr/bin/env python
from setuptools import setup
from xmltv_alt import VERSION

setup(
    name="python-xmltvalt",
    description="A Python Module for Reading and Writing XMLTV Files",
    version=VERSION,
    author="Justin Horner, James Oakley",
    author_email="mail@justinhorner.me, jfunk@funktronics.ca",
    url="https://github.com/justinhorner/python-xmltv-alt",
    py_modules=['xmltv_alt'],
    long_description=open('README.txt').read() + '\n\n' +
                     open('CHANGELOG.txt').read(),
    long_description_content_type='text/plain',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license="LGPL-3.0+",
)

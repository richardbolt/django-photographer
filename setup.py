#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

import photographer


setup(
    name='django-photographer',
    version=photographer.__version__,
    description='A Photographers Website built for easy Heroku deployment.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read().decode('utf-8'),
    author='Richard Bolt',
    author_email='richard@richardbolt.com',
    url='https://github.com/richardbolt/django-photographer/',
    license='BSD License',
    platforms=['OS Independent'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ),
)
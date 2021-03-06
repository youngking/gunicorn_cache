#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'gunicorn',
    'redis',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='gunicorn_cache',
    version='0.1.5',
    description="Cache worker for gunicorn",
    long_description=readme + '\n\n' + history,
    author="Young King",
    author_email='yanckin@gmail.com',
    url='https://github.com/youngking/gunicorn_cache',
    packages=[
        'gunicorn_cache',
    ],
    package_dir={'gunicorn_cache':
                 'gunicorn_cache'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='gunicorn_cache',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    tests_require=test_requirements
)

#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django-swagger',
    version='0.0.2',
    url='https://bitbucket.org/quein/django-swagger/',
    license='MIT',
    author='Geraldo Andrade',
    author_email='geraldo@geraldoandrade.com',
    description='A Django extension to Extension to manage users in django application.',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    download_url='https://bitbucket.org/quein/django-swagger/get/master.zip',
    zip_safe=True,
    platforms='any',
    install_requires=[
        'django>=1.5.4'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
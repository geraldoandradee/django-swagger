#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django-swagger',
    version='0.1.0',
    url='https://github.com/geraldoandradee/django-swagger',
    license='MIT',
    author='Geraldo Andrade',
    author_email='geraldo@geraldoandrade.com',
    description='A Django extension Swagger UI to mapping REST API\'s in django application.',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    download_url='https://github.com/geraldoandradee/django-swagger/archive/master.zip',
    zip_safe=True,
    platforms='any',
    install_requires=[
        'django>=1.5.4',
        'PyYAML>=3.11'
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
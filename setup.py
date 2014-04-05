#!/usr/bin/env python3
try: from setuptools import setup
except ImportError: from distutils.core import setup

setup(
	name = 'knotch',
	description = 'Turns literally *any* integer into English in compliance with British usage & the Conway-Wechsler system',
	version = '1.0',

	author = 'Kye W. Shi',
	author_email = 'shi.kye@gmail.com',

	install_requires = [],
	packages = ['knotch'],
	scripts = ['bin/knotch']
)

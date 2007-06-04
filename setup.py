##############################################################################
#
# Copyright (c) 2007 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for the Acquisition egg package
"""
import os
from setuptools import setup, find_packages, Extension

setup(name='tempstorage',
      version = '2.11.0a1',
      url='http://svn.zope.org/tempstorage',
      license='ZPL 2.1',
      description='',
      author='Zope Corporation and Contributors',
      author_email='zope-dev@zope.org',
      long_description='',
      
	  packages=find_packages('src'),
	  package_dir={'': 'src'},

      include_package_data=True,
      zip_safe=False,
      )
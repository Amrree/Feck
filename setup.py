#!/usr/bin/env python
from setuptools import setup, find_packages
import pkg_resources
import sys
import os
import fastentrypoints


try:
    if int(pkg_resources.get_distribution("pip").version.split('.')[0]) < 6:
        print('pip older than 6.0 not supported, please upgrade pip with:\n\n'
              '    pip install -U pip')
        sys.exit(-1)
except pkg_resources.DistributionNotFound:
    pass

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

version = sys.version_info[:2]
if version < (2, 7):
    print('thefeck requires Python version 2.7 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)
elif (3, 0) < version < (3, 5):
    print('thefeck requires Python version 3.5 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)

VERSION = '3.32'

install_requires = ['psutil', 'colorama', 'six']
extras_require = {':python_version<"3.4"': ['pathlib2'],
                  ':python_version<"3.3"': ['backports.shutil_get_terminal_size'],
                  ':python_version<="2.7"': ['decorator<5', 'pyte<0.8.1'],
                  ':python_version>"2.7"': ['decorator', 'pyte'],
                  ":sys_platform=='win32'": ['win_unicode_console']}

if sys.platform == "win32":
    scripts = ['scripts\\feck.bat', 'scripts\\feck.ps1']
    entry_points = {'console_scripts': [
                  'thefeck = thefeck.entrypoints.main:main',
                  'thefuck_firstuse = thefeck.entrypoints.not_configured:main']}
else:
    scripts = [
        'feck_integrations/batfeck.py',
        'feck_integrations/curlfeck.py'
    ]
    entry_points = {'console_scripts': [
                  'thefeck = thefeck.entrypoints.main:main',
                  'feck = thefeck.entrypoints.not_configured:main',
                  'ohfeck = thefeck.entrypoints.not_configured:main',
                  'ohfeckit = thefeck.entrypoints.not_configured:main',
                  'batfeck = feck_integrations.batfeck:main',
                  'curlfeck = feck_integrations.curlfeck:main']}

setup(name='thefeck',
      version=VERSION,
      description="Magnificent app which corrects your previous console command",
      long_description=long_description,
      author='Vladimir Iakovlev',
      
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples',
                                      'tests', 'tests.*', 'release']),
      include_package_data=True,
      zip_safe=False,
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
      install_requires=install_requires,
      extras_require=extras_require,
      scripts=scripts,
      entry_points=entry_points)

#!/usr/bin/env python
from __future__ import absolute_import, division, print_function, with_statement

import os
import sys
from setuptools import setup, find_packages

module_name = '{{cookiecutter.project_name}}'
current_path = os.path.dirname(__file__)


# Common 3rd party package dependencies
install_requires = []
with open(os.path.join(current_path, 'requirements.txt')) as requirements_file:
    for requirement in requirements_file:
        if requirement:
            install_requires.append(requirement)

# Unit test 3rd party package dependencies
test_requires = []
with open(os.path.join(current_path, 'test', 'requirements.txt')) as requirements_file:
    for requirement in requirements_file:
        if requirement:
            test_requires.append(requirement)

# Python 3.x backports to 2.x
if sys.version_info.major < 3:
    install_requires.append('enum34')  # enum.Enum
    test_requires.append('mock')  # unittest.mock

# Set __version__
with open(os.path.join(current_path, module_name, '__version__.py')) as f:
    exec f.read()


def forbid_publish():
    """
    Prevent user from accidentally publishing this private package to PyPI
    See: http://www.tomaz.me/2013/09/03/prevent-accidental-publishing-of-a-private-python-package.html
    """
    argv = sys.argv
    blacklist = ['register', 'upload']

    for command in blacklist:
        if command in argv:
            values = {'command': command}
            print('Command "{}" has been blacklisted, exiting...'.format(values))
            sys.exit(2)


forbid_publish()

setup(name=module_name,
      version=__version__,
      author='{{cookiecutter.author_name}}',
      author_email='{{cookiecutter.author_email}}',
      description='{{cookiecutter.project_description}}',
      url='https://github.com/Flushot/{}'.format(module_name),
      license='Proprietary',

      packages=find_packages('.'),
      package_dir={module_name: module_name},

      # Include package documentation files
      package_data={
          module_name: [
              '*.txt',
              '*.rst',
              '*.md'
          ]
      },

      # Dependencies
      install_requires=install_requires,
      tests_require=test_requires,

      # Tests
      test_suite='test'
      )

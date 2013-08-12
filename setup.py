from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='passphrasegen',
      version=version,
      description="Generate a passphrase consisting of words chosen from word list dictionaries.",
      long_description="""\
Generate a passphrase consisting of words chosen from word list dictionaries.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='password generator passphrase entropy',
      author='Ross Patterson',
      author_email='me@rpatterson.net',
      url='https://github.com/rpatterson/passphrasegen',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

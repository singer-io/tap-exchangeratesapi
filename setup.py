#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-exchangeratesapi',
      version='0.2.0',
      description='Singer.io tap for extracting currency exchange rate data from the exchangeratesapi.io API',
      author='Stitch',
      url='http://github.com/singer-io/tap-exchangeratesapi',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_exchangeratesapi'],
      install_requires=['singer-python==5.8.0',
                        'backoff==1.8.0',
                        'requests==2.22.0'],
      extras_require={
          'dev': [
              'ipdb==0.11'
          ]
      },
      entry_points='''
          [console_scripts]
          tap-exchangeratesapi=tap_exchangeratesapi:main
      ''',
      packages=['tap_exchangeratesapi'],
      package_data={"schemas": ["tap_exchangeratesapi/schemas/*.json"]},
      include_package_data=True
)

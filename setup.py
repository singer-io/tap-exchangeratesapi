#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-exchangeratesapi',
      version='1.0.1',
      description='Singer.io tap for extracting currency exchange rate data from the exchangeratesapi.io API by Adswerve',
      author='Adswerve',
      url='http://github.com/adswerve/tap-exchangeratesapi',
      download_url='https://github.com/adswerve/tap-exchangeratesapi/archive/refs/tags/1.0.1.zip',
      install_requires=['singer-python==5.13.0',
                        'backoff==1.8.0',
                        'requests==2.28.2'],
      entry_points='''
          [console_scripts]
          tap-exchangeratesapi=tap_exchangeratesapi:main
      '''
)

from setuptools import setup, find_packages

setup(name='tap-exchangeratesapi',
      version='1.0.1',
      description='Singer.io tap for extracting currency exchange rate data from the exchangeratesapi.io API',
      author='Stitch',
      url='http://github.com/adswerve/tap-exchangeratesapi',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_exchangeratesapi'],
      install_requires=['singer-python==5.13.0',
                        'backoff==1.8.0',
                        'requests==2.28.2'],
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
      include_package_data=True
)

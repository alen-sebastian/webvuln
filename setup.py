from setuptools import setup, find_packages

setup(
   name='webvuln_scanner',  
   version='1.0',
   packages=find_packages(),
   install_requires=[], # No dependencies
   entry_points={
      'console_scripts': [
         'webvuln_scanner = webvuln_scanner:main'
      ]
   }
)

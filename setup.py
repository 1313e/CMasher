# -*- coding: utf-8 -*-

"""
Setup file for the *CMasher* package.

"""


# %% IMPORTS
# Built-in imports
from codecs import open
import re

# Package imports
from setuptools import find_packages, setup


# %% SETUP DEFINITION
# Get the long description from the README file
with open('README.rst', 'r') as f:
    long_description = f.read()

# Get the requirements list
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

# Read the __version__.py file
with open('cmasher/__version__.py', 'r') as f:
    vf = f.read()

# Obtain version from read-in __version__.py file
version = re.search(r"^_*version_* = ['\"]([^'\"]*)['\"]", vf, re.M).group(1)

# Setup function declaration
setup(name="cmasher",
      version=version,
      author="Ellert van der Velden",
      author_email='ellert_vandervelden@outlook.com',
      description=("Scientific colormaps for making accessible, informative "
                   "and 'cmashing' plots"),
      long_description=long_description,
      url="https://cmasher.readthedocs.io",
      project_urls={
          'Documentation': "https://cmasher.readthedocs.io",
          'Source Code': "https://github.com/1313e/CMasher",
          },
      license='BSD-3',
      platforms=['Windows', 'Mac OS-X', 'Linux', 'Unix'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: MacOS',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Scientific/Engineering :: Visualization',
          'Topic :: Utilities',
          ],
      keywords=("cmasher perceptually uniform sequential colormaps plotting "
                "python visualization"),
      python_requires='>=3.6, <4',
      packages=find_packages(),
      package_dir={'cmasher': "cmasher"},
      entry_points={
             'console_scripts': [
                 "cmr = cmasher.cli_tools:main"]},
      include_package_data=True,
      install_requires=requirements,
      zip_safe=False,
      )

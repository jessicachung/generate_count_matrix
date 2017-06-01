#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = \
'''This program reads in one or more input text files with expression counts
and produces a single combined file. Each input will have a column in the
matrix containing expression values. 

The column containing gene (or feature) names should be identical for all
input count files.
'''

setup(
    name='generate-count-matrix-py',
    version='0.1.0.0',
    author='Jessica Chung',
    author_email='jchung@unimelb.edu.au',
    packages=['generate-count-matrix'],
    package_dir={'generate-count-matrix': 'generate-count-matrix'},
    entry_points={
        'console_scripts': ['generate-count-matrix = generate-count-matrix.generate-count-matrix:main']
    },
    url='https://github.com/jessicachung/generate-count-matrix',
    license='LICENSE',
    description=('Generate a count matrix from separate input files.'),
    long_description=(LONG_DESCRIPTION)
)

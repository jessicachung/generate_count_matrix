# Overview

generate_count_matrix reads in one or more input text files with expression
counts and produces a single combined file. Each input will have a column in
the matrix containing expression values.

The column containing gene (or feature) names should be identical for all
input count files.

# Licence

This program is released as open source software under the terms of the
[MIT License](https://raw.githubusercontent.com/jessicachung/generate_count_matrix/master/LICENSE)

# Installing

generate_count_matrix can be installed using `pip` in a variety of ways
(`%` indicates the command line prompt):

1. Inside a virtual environment:
```
% virtualenv generate_count_matrix_dev
% source generate_count_matrix_dev/bin/activate
% pip install -U /path/to/generate_count_matrix
```
2. Into the global package database for all users:
```
% pip install -U /path/to/generate_count_matrix
```
3. Into the user package database (for the current user only):
```
% pip install -U --user /path/to/generate_count_matrix
```

# General behaviour

generate_count_matrix accepts one or more filenames on the command line
containing counts in plain-text format. One column should contain feature
names (such as gene names) and another column should contain expression values.

The program will print to standard output a count matrix delimited with tabs.
The first line contains the column names which are the filenames of the inputs.

Comments and header lines at the beginning of the file can be skipped by
either removing all lines beginning with `#` using `--skip-comments`, or using
the `--skip-lines` argument to specify the number of lines to skip at the
beginning.

# Usage

In the examples below, `%` indicates the command line prompt.

## Help message

generate_count_matrix can display usage information on the command line via
the `-h` or `--help` argument:
```
% generate_count_matrix -h
usage: generate_count_matrix [-h] [--gene-col N] [--count-col N]
                             [--skip-comments] [--skip-lines N]
                             [--delimiter DELIM] [--round] [--keep-all-genes]
                             [--version] [--log LOG_FILE]
                             COUNT_FILE [COUNT_FILE ...]

Generate count matrix from individual files

positional arguments:
  COUNT_FILE         input plain-text count files

optional arguments:
  -h, --help         show this help message and exit
  --gene-col N       field containing gene IDs (default 1)
  --count-col N      field containing counts (default 2)
  --skip-comments    skip all lines beginning with the '#' character (if used
                     with --skip-lines, comment lines will be removed before
                     removing the specified number of lines)
  --skip-lines N     number of heading lines to skip (default 0)
  --delimiter DELIM  use DELIM instead of TAB for field delimiter
  --round            round count values to the nearest integer
  --keep-all-genes   keep all genes in final matrix instead of removing genes
                     with zero counts
  --version          show program's version number and exit
  --log LOG_FILE     record program progress in LOG_FILE
```

# Testing

```
% cd generate_count_matrix/python/generate_count_matrix
% python -m unittest -v generate_count_matrix_test
```

# Bugs

File at our [Issue Tracker](https://github.com/jessicachung/generate_count_matrix/issues)

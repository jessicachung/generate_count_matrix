# Overview 


# Licence

This program is released as open source software under the terms of [MIT License](https://raw.githubusercontent.com/generate-count-matrix-paper/generate-count-matrix/master/LICENSE)

# Installing

Generate-count-matrix can be installed using `pip` in a variety of ways (`%` indicates the command line prompt):

1. Inside a virtual environment: 
```
% virtualenv generate-count-matrix_dev
% source generate-count-matrix_dev/bin/activate
% pip install -U /path/to/generate-count-matrix-py
```
2. Into the global package database for all users:
```
% pip install -U /path/to/generate-count-matrix-py
```
3. Into the user package database (for the current user only):
```
% pip install -U --user /path/to/generate-count-matrix-py
```

# General behaviour

# Usage 

In the examples below, `%` indicates the command line prompt.

## Help message

Generate-count-matrix can display usage information on the command line via the `-h` or `--help` argument:
```
% generate-count-matrix-py -h
usage: generate-count-matrix-py [-h] [--minlen N] [--version] [--log LOG_FILE]
                  [FASTA_FILE [FASTA_FILE ...]]

Print fasta stats

positional arguments:
  FASTA_FILE      Input FASTA files

optional arguments:
  -h, --help      show this help message and exit
  --minlen N      Minimum length sequence to include in stats (default 0)
  --version       show program's version number and exit
  --log LOG_FILE  record program progress in LOG_FILE
```

# Testing

```
% cd generate-count-matrix/python/generate-count-matrix
% python -m unittest -v generate-count-matrix_test
```

A set of sample test input files is provided in the `test_data` folder.
```
% generate-count-matrix-py two_sequence.fasta 
FILENAME	TOTAL	NUMSEQ	MIN	AVG	MAX
two_sequence.fasta	2	357	120	178	237
```

# Bugs

File at our [Issue Tracker](https://github.com/jessicachung/generate-count-matrix/issues)

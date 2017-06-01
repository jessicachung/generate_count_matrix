'''
Description : Generate a count matrix from multiple individual count files.
Copyright   : (c) Jessica Chung, 2017
License     : MIT 
Maintainer  : jchung@unimelb.edu.au

This program reads in one or more input text files with expression counts
and produces a single combined file. Each input will have a column in the
matrix containing expression values.

The column containing gene (or feature) names should be identical for all
input count files.
'''

from __future__ import print_function
from argparse import ArgumentParser
import sys
import logging

PROGRAM_VERSION = "1.0"
EXIT_FILE_IO_ERROR = 1
EXIT_GENE_ERROR = 1
EXIT_COUNT_ERROR = 1
EXIT_COMMAND_LINE_ERROR = 2
DEFAULT_GENE_COLUMN = 1
DEFAULT_COUNT_COLUMN = 2
DEFAULT_DELIMITER = "\t"
DEFAULT_SKIP_LINES = 0
DEFAULT_ROUNDING = False
DEFAULT_KEEP_ALL = False
PROGRAM_NAME = "generate-count-matrix"


def exit_with_error(message, exit_status):
    '''Print an error message to stderr, prefixed by the program name and 'ERROR'.
    Then exit program with supplied exit status.

    Arguments:
        message: an error message as a string.
        exit_status: a positive integer representing the exit status of the
            program.
    '''
    logging.error(message)
    print("{} ERROR: {}, exiting".format(PROGRAM_NAME, message), file=sys.stderr)
    sys.exit(exit_status)


def parse_args():
    '''Parse command line arguments.
    Returns Options object with command line argument values as attributes.
    Will exit the program on a command line error.
    '''
    parser = ArgumentParser(description='Generate count matrix from ' \
        'individual files')
    parser.add_argument(
        '--gene-col',
        metavar='N',
        type=int,
        default=DEFAULT_GENE_COLUMN,
        help='Field containing gene IDs (default {})'.format(
            DEFAULT_GENE_COLUMN))
    parser.add_argument(
        '--count-col',
        metavar='N',
        type=int,
        default=DEFAULT_COUNT_COLUMN,
        help='Field containing counts (default {})'.format(
            DEFAULT_COUNT_COLUMN))
    parser.add_argument(
        '--skip-lines',
        metavar='N',
        type=int,
        default=DEFAULT_SKIP_LINES,
        help='Number of heading lines to skip (default {})'.format(
            DEFAULT_SKIP_LINES))
    parser.add_argument(
        '--delimiter',
        metavar='DELIM',
        type=str,
        default=DEFAULT_DELIMITER,
        help='Use DELIM instead of TAB for field delimiter')
    parser.add_argument(
        '--round',
        action='store_true',
        default=DEFAULT_ROUNDING,
        help='Round count values to the nearest integer')
    parser.add_argument(
        '--keep-all-genes',
        action='store_true',
        default=DEFAULT_KEEP_ALL,
        help='Keep all genes in final matrix instead of removing genes with ' \
             'zero counts')
    parser.add_argument('--version',
        action='version',
        version='%(prog)s ' + PROGRAM_VERSION)
    parser.add_argument('--log',
        metavar='LOG_FILE',
        type=str,
        help='record program progress in LOG_FILE')
    parser.add_argument('count_files',
        nargs='+',
        metavar='COUNT_FILE',
        type=str,
        help='Input plain-text count files')
    return parser.parse_args()


def process_files(options):
    '''Extract counts from each input file and generate a combined matrix.
    Print count matrix to stdout.

    Arguments:
       options: the command line options of the program
    Result:
       None
    '''
    all_counts = []
    header = ["gene_id"]
    for count_filename in options.count_files:
        logging.info("Processing counts from {}".format(count_filename))
        try:
            counts_file = open(count_filename)
        except IOError as exception:
            exit_with_error(str(exception), EXIT_FILE_IO_ERROR)
        with counts_file:
            header.append(count_filename)
            data = counts_file.read().strip().split("\n")[options.skip_lines:]
            data = [x.split(options.delimiter) for x in data]
            genes, counts = list(zip(*data))
            try:
                # Check if integers or floats
                if any([x.count(".") for x in counts]):
                    counts = [float(x) for x in counts]
                else:
                    counts = [int(x) for x in counts]
            except ValueError:
                exit_with_error("Not all count values are numeric", 
                    EXIT_COUNT_ERROR)
            # Round counts
            if options.round:
                counts = [round(x) for x in counts]
            if not all_counts:
                all_counts.append(genes)
            # Check if gene IDs match
            if all_counts[0] == genes:
                all_counts.append(counts)
            else:
                exit_with_error("Gene IDs are not identical", EXIT_GENE_ERROR)
    output_rows = [list(x) for x in zip(*all_counts)]
    print("\t".join(header))
    for row in output_rows:
        # Only print rows with at least one count
        if options.keep_all_genes or sum(row[1:]) > 0:
            print("\t".join([str(x) for x in row]))


def init_logging(log_filename):
    '''If the log_filename is defined, then
    initialise the logging facility, and write log statement
    indicating the program has started, and also write out the
    command line from sys.argv

    Arguments:
        log_filename: either None, if logging is not required, or the
            string name of the log file to write to
    Result:
        None
    '''
    if log_filename is not None:
        logging.basicConfig(filename=log_filename,
            level=logging.DEBUG,
            filemode='w',
            format='%(asctime)s %(levelname)s - %(message)s',
            datefmt='%m-%d-%Y %H:%M:%S')
        logging.info('program started')
        logging.info('command line: {0}'.format(' '.join(sys.argv)))


def main():
    "Orchestrate the execution of the program"
    options = parse_args()
    init_logging(options.log)
    process_files(options)


# If this script is run from the command line then call the main function.
if __name__ == '__main__':
    main()

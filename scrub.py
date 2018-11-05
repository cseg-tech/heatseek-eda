#!/usr/bin/env python3

"""Data Scrubber

This script scrubs data exported from a Heroku Data Snippet, removing any
personally identifiable information unnecessary for exploratory data
analysis.

Special consideration was taken to avoid directly naming column headers.
"""

import sys, os
import csv

def usage():
	"""Script usage message"""
	print('Usage: python scrub.py raw_input clean_output')
	sys.exit(1)

# main function
if __name__ == '__main__':
	# check script arguments
	if len(sys.argv) != 3:
		usage()

	input_filepath = sys.argv[1]
	output_filepath = sys.argv[2]

	# check if file is csv
	if input_filepath[-4:] != '.csv':
		sys.stderr.write('Error: input file must be a .csv')
		sys.exit(1)
	if output_filepath[-4:] != '.csv':
		sys.stderr.write('Error: output file must be a .csv')
		sys.exit(1)

	# open files and turn them into csv readers/writers
	input_file = open(input_filepath, 'r', newline='')
	input_reader = csv.reader(input_file)

	output_file = open(output_filepath, 'w', newline='')
	output_writer = csv.writer(output_file)

	# for each row in the input file, only write the clean columns to the
	# output file.
	for row in input_reader:
		cols_to_keep = [row[0], row[4], row[6], row[7], row[8], row[9]]
		output_writer.writerow(cols_to_keep)

	# close the opened files
	input_file.close()
	output_file.close()




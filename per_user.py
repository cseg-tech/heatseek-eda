#!/usr/bin/env python3

"""per_user.py

This script separates the dataset into separate datasets per unique user.
This encourages individual-level statistics instead of aggregates.

"""

import sys, os
import csv
import pandas as pd

def usage():
	""" Script message usage """
	sys.stderr.write("""
	Usage: python scrub.py dataset output_dir/\n""")
	sys.exit(1)

def user_import(filepath):
	"""
	Given a filepath to a dataset, return a list of dataframes
	per user.
	"""
	# open the file
	with open(input_filepath, 'r') as inputfile:
		# import csv with pandas
		file_df = pd.read_csv(inputfile, header = 0)
		# determine list of unique users
		userlist = file_df['user_id'].tolist()
		userset = set(userlist)
		print(userset)

		global_list = []
		# iterate through each user and save out data
		for user in userset:
			user_df = file_df.loc[file_df['user_id'] == user]
			global_list.append(user_df)

	return global_list

if __name__ == '__main__':
	if len(sys.argv) != 3:
		usage()

	input_filepath = sys.argv[1]
	output_dirpath = sys.argv[2]

	# if output dir doesn't exist, create it

	if not os.path.exists(output_dirpath):
		os.makedirs(output_dirpath)

	# open the file
	with open(input_filepath, 'r') as inputfile:
		# import csv with pandas
		file_df = pd.read_csv(inputfile, header = 0)
		# determine list of unique users
		userlist = file_df['user_id'].tolist()
		userset = set(userlist)
		print(userset)

		# iterate through each user and save out data
		for user in userset:
			user_df = file_df.loc[file_df['user_id'] == user]
			user_df.to_csv(os.path.join(output_dirpath, str(user)+'.csv'), index=False)
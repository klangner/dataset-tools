#
# Merge dataset exported from Dataset-Recorder into format used by
# image classifiers. 
# In this format images are saved in the subfolders with names taken from labels
# E.g. For Card-Colors dataset we have the following structure
# card-colors
#   train
#     clubs
#	  diamonds
#	  hearts
#	  spades

import os
import sys
import shutil
import pandas as pd


def merge(source_dataset, destination_folder):
	"""
	Create folders based on data labels and put files there
	"""	
	source_folder = os.path.dirname(source_dataset)
	df_source = pd.read_csv(source_dataset)
	for row in df_source.values:
		fname = row[0]
		source_file = os.path.join(source_folder, fname)
		label_folder = os.path.join(destination_folder, row[1])
		if not os.path.exists(label_folder):
			os.makedirs(label_folder)
		destination_file = os.path.join(label_folder, fname)
		if os.path.exists(destination_file):
			print('File {:} already exists'.format(destination_file))
		else:
			shutil.copyfile(os.path.realpath(source_file), os.path.realpath(destination_file))


if len(sys.argv) != 3:
	print("Usage:")
	print("  python merge_classifier_dataset.py <source_dataset> <destination_folder>")
else:
	merge(sys.argv[1], sys.argv[2])
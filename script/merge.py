#
# Merge Pull Request data into the dataset
#
import os
import sys
import shutil
import pandas as pd


def merge(source_dataset, destination_dataset):
	"""
	Merge Pull Request into Dataset
	"""	
	source_folder = os.path.dirname(source_dataset)
	destination_folder = os.path.dirname(destination_dataset)
	df_source = pd.read_csv(source_dataset)
	df_destination = pd.read_csv(destination_dataset)
	for row in df_source.values:
		fname = row[0]
		source_file = os.path.join(source_folder, fname)
		destination_file = os.path.join(destination_folder, fname)
		if os.path.exists(destination_file):
			print('File {:} already exists'.format(destination_file))
			df_source = df_source[df_source.file != fname]
		else:
			shutil.copyfile(os.path.realpath(source_file), os.path.realpath(destination_file))
	df = df_destination.append(df_source)
	df.to_csv(destination_dataset, index=False)


merge(sys.argv[1], sys.argv[2])
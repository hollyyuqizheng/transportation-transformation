import numpy as np
import pandas as pd
import random
import csv
from scipy import stats
import statsmodels.api as sm
from statsmodels.tools import eval_measures
import sys

# TODO: Chicago vs New York
# TODO: pickup v dropoff

def split_data(data, prob):
	"""
	   input:
	data: a list of pairs of x,y values
	prob: the fraction of the dataset that will be testing data, typically prob=0.2
	output: two lists with training data pairs and testing data pairs
	"""
	#TODO: Split data into fractions [prob, 1 - prob]. You can re-use the code from part I.
	train_data = []
	test_data = []
	for x, y in data:
		if random.random() <= prob:
			test_data.append((x, y))
		else:
			train_data.append((x, y))

	return train_data, test_data

def train_test_split(x, y, test_pct):
	"""input:
	x: list of x values, y: list of independent values, test_pct: percentage of the data that is testing data=0.2.

	output: x_train, x_test, y_train, y_test lists
	"""

	#TODO: Split the features X and the labels y into x_train, x_test and y_train, y_test as specified by test_pct.
	#You can re-use code from part I.
	data = zip(x, y)
	train_pairs, test_pairs = split_data(data, test_pct)
	train_lst = list(zip(*train_pairs))
	test_lst = list(zip(*test_pairs))
	return list(train_lst[0]), list(test_lst[0]), list(train_lst[1]), list(test_lst[1])

if __name__=='__main__':

	# DO not change this seed. It guarantees that all students perform the same train and test split
	random.seed(1)
	# Setting p to 0.2 allows for a 80% training and 20% test split
	p = 0.2

	#############################################
	# TODO: open csv and read data into X and y #
	#############################################
	def load_file(file_path):
		"""input: file_path: the path to the data file
		   output: X: array of independent variables values, y: array of the dependent variable values
		"""
		#TODO:
		#1. Use pandas to load data from the file. Here you can also re-use most of the code from part I.
		#2. Select which independent variables best predict the dependent variable count.
		data = pd.read_csv(file_path, delimiter="\t")
		df = pd.DataFrame(data)

		y = df["taxi_records"]
		X = df.drop(["lat", "long", "station_id", "station_name", "year", "zipcode", "taxi_records"], axis=1)

		# create dummy variables from month
		dummy_month = sm.categorical(X["month_beginning"], drop=True)
		dummy_month_df = pd.DataFrame(dummy_month)

		# drop one of the columns to have linear independence
		dummy_month_df = dummy_month_df.drop(dummy_month_df.columns[0], axis=1)
		# rename for human legibility
		dummy_month_df.columns = ["february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

		# drop original categorical columns
		X = X.drop(["month_beginning"], axis=1)
		frames = [X, dummy_month_df]
		# concatenate dummy variables onto X dataframe
		X = pd.concat(frames, axis=1)

		print(X.head)

		print(X.dtypes)

		for i in range(len(X.columns.values)):
			print(i + 1, X.columns.values[i])

		y = y.to_numpy()
		X = X.to_numpy()

		return X, y

	X, y = load_file("chicago_cta_combined_pickup.tsv")

	# try:
	#     opts, args = getopt.getopt(argv, "hc:t:", ["city=", "type="])
	# except getopt.GetoptError:
	#     print "regression.py -c <city_name> -t <pickup_or_dropoff>"
	#     sys.exit(2)


	# if opts[0] == '-h':
	#     print "regression.py -c <city_name> -t <pickup_or_dropoff> \n <city_name> can be 'chicago' or 'new_york'"
	#     sys.exit()
	# elif opts[0] in ["-c", "--city"]:
	#     city_arg = arg
	#     if opts[1] in ["-t", "--type"]:
	#         type_arg = arg
	#
	#     if arg == "chicago":
	#         X, y = load_file("../../data/chicago/", "chicago")
	#     elif arg == "new_york":
	#         X, y = load_file("../../data/new_york/", "new_york")
	#     else:
	#         print

	##################################################################################
	# TODO: use train test split to split data into x_train, x_test, y_train, y_test #
	#################################################################################
	x_train, x_test, y_train, y_test = train_test_split(X, y, p)

	x_train = np.array(x_train)
	x_test = np.array(x_test)
	y_train = np.array(y_train)
	y_test = np.array(y_test)

	##################################################################################
	# TODO: Use StatsModels to create the Linear Model and Output R-squared
	#################################################################################

	# TODO: should we be adding constants?
	# x_train = sm.add_constant(x_train)
	# x_test = sm.add_constant(x_test)

	model = sm.OLS(y_train, x_train)
	results = model.fit()
	predictions = results.predict(x_test)

	# Prints out the Report
	# TODO: print R-squared, test MSE & train MSE
	print("train summary: ", results.summary())
	print("train r-squared: ", results.rsquared)
	print("test mse: ", eval_measures.mse(predictions, y_test))
	print("train mse: ", eval_measures.mse(results.fittedvalues, y_train))

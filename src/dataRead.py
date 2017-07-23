import pandas as pd
from nltk.corpus import brown
import data_clean
import sys
import glob
import errno

def clean(s):
	s = str(s)
	if (len(s) == 0):
		return ""
	s = s.replace('\n','')
	return s

def write(X_train,X_test):
	f_prefix = "../data/sentences/"

	f = open(f_prefix+'train_question1', 'w')
	for i in X_train['question1']:
		i = clean(i)
		f.writelines(i+'\n')
	f.close()

	f = open(f_prefix+'train_question2', 'w')
	for i in X_train['question2']:
		i = clean(i)
		f.writelines(i+'\n')
	f.close()

	f = open(f_prefix+'test_question1', 'w')
	for i in X_test['question1']:
		i = clean(i)
		f.writelines(i+'\n')
	f.close()

	f = open(f_prefix+'test_question2', 'w')
	for i in X_test['question2']:
		i= clean(i)
		f.writelines(i+'\n')
	f.close()

def do():
	# Read data from train
	train = "../data/train.csv"
	test = "../data/test.csv"
	X_train = pd.read_csv( train, header=0,delimiter="," )
	X_test = pd.read_csv( test, header=0,delimiter="," )

	return X_train,X_test
	# X_train = pd.DataFrame(columns=('review','type'))

	# path = '../data/train_data/*'   
	# files = glob.glob(path)
	# train = ''
	# for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
	# 	with open(name) as f:
	# 		for line in f:
	# 			train+=line
				
	# train = train.replace('\n',' ')
	# train = train.split('.')

	# netreview = ''
	# i = 1
	# for review in train:
	# 	netreview += (review+'.')
	# 	if i == 10:
	# 		X_train = X_train.append({'review':netreview, 'type':'indian'}, ignore_index=True)
	# 		i = 1
	# 		netreview = ''
	# 	else:
	# 		i = i + 1
	# if i!=1:
	# 	X_train = X_train.append({'review':netreview, 'type':'indian'}, ignore_index=True)

	# path = '../data/foo/*'   
	# files = glob.glob(path)
	# train = ''
	# for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
	# 	with open(name) as f:
	# 		for line in f:
	# 			train+=line
				
	# train = train.replace('\n',' ')
	# train = train.split('.')

	# netreview = ''
	# i = 1
	# for review in train:
	# 	netreview += (review+'.')
	# 	if i == 10:
	# 		X_train = X_train.append({'review':netreview, 'type':'non-indian'}, ignore_index=True)
	# 		i = 1
	# 		netreview = ''
	# 	else:
	# 		i = i + 1
	# if i!=1:
	# 	X_train = X_train.append({'review':netreview, 'type':'non-indian'}, ignore_index=True)

	# # Read data from test
	# file = '../data/test_data/test.csv'
	# X_test = pd.read_csv( file, header=0,delimiter="," )
	# X_train = X_train.sample(frac=1).reset_index(drop=True)
	#return X_train,X_test
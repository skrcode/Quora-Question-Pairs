import sys, os
import pandas as pd

def writeSentenceVectors():
	os.system('source ./getFeatures.sh')

def getFeatures(X_train,X_test):
	f1 = '../data/sentences/train_question1_wordvecs'
	f2 = '../data/sentences/train_question2_wordvecs'
	f3 = '../data/sentences/test_question1_wordvecs'
	f4 = '../data/sentences/test_question2_wordvecs'
	
	wv1 = pd.read_csv( f1,header=-1,delimiter=" ")
	wv2 = pd.read_csv( f2,header=-1,delimiter=" ")
	wv3 = pd.read_csv( f3,header=-1,delimiter=" ")
	wv4 = pd.read_csv( f4,header=-1,delimiter=" ")

	del wv1[100]
	del wv2[100]
	del wv3[100]
	del wv4[100]

	# concatenate features
	X_train_features = pd.concat([X_train,(wv1-wv2)*(wv1-wv2)], axis=1, join_axes=[X_train.index])
	X_test_features = pd.concat([X_test,(wv3-wv4)*(wv3-wv4)], axis=1, join_axes=[X_test.index])

	return X_train_features,X_test_features

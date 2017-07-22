from nltk.corpus import stopwords
import re
import pandas as pd

def do():

	f1 = '../data/sentences/train_question1_wordvecs'
	f2 = '../data/sentences/train_question2_wordvecs'
	wv1 = pd.read_csv( f1,header=-1,delimiter=" ")
	wv2 = pd.read_csv( f2,header=-1,delimiter=" ")
	del wv1[100]
	del wv2[100]

	f3 = '../data/sentences/test_question1_wordvecs'
	f4 = '../data/sentences/test_question2_wordvecs'
	wv3 = pd.read_csv( f1,header=-1,delimiter=" ")
	wv4 = pd.read_csv( f2,header=-1,delimiter=" ")
	del wv3[100]
	del wv4[100]

	return wv1,wv2,wv3,wv4
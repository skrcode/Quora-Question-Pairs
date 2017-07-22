import pandas as pd
import os
from collections import OrderedDict
from subprocess import check_call
from shutil import copyfile

def do(result,test):
	# count number of files
	path, dirs, files = os.walk("../results").next()
	file_count = len(files)+1

	# Write the test results
	data=OrderedDict()
	data["test_id"]=test["test_id"] 
	data["is_duplicate"]=result["is_duplicate"]
	
	output = pd.DataFrame(data=data)
	filename = "../results/result"+str(file_count)+".csv"
	output.to_csv( filename, index=False )
	check_call(['gzip', filename])

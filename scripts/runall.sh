#!/bin/bash

# Give name of experiment to first input argument
	# if empty, generic names will be written
# Whole svm learning and testing
# Calls on feat-extract.py
# Calls on svm_learn and svm_classify

if [ -z "$1"];	then
	name="exp0"
else
	name=$1
fi

path=$(pwd)
spath=${path%/*}

# 1 Create input in svm_light readable format
"$path"/feat-extract.py > "$spath"/data/"$name"data.svm

# 2 Divide input into training and test set
	# Module under construction

# 3 Run learning and testing. Retrieve logs

#"$path"/svm-light/svm_learn "$spath"/data/"$name"examples.svm "$spath"/outs/"$name"_model > "$spath"/logs/"$name".train.log

#"$path"/svm-light/svm_classify "$spath"/data/"$name"test.svm "$spath"/outs/"$name"_model "$spath"/outs/"$name"_class > "$spath"/logs/"$name".train.log

echo "End of script"
echo $spath
echo $path

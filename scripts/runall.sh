#!/bin/bash

# Give name of experiment to first input argument
	# if empty, generic names will be written
# Whole svm learning and testing
# Calls on feat-extract.py
# Calls on svm_learn and svm_classify


# 0 Check arguments, get paths

	# Check arguments
if [ -z "$1" ];	then
	name="exp0"
else
	name="$1"
fi
	# Get paths
path=$(pwd)
spath=${path%/*}


# 1 Create input in svm_light readable format
"$path"/feat-extract.py "$name"

# 2 Divide input into training and test set
	# Module under construction

# 3 Run learning and testing. Retrieve logs

"$path"/svm_light/svm_learn "$spath"/data/"$name"data.svm \
	"$spath"/outs/"$name"_model > "$spath"/logs/"$name".train.log & pid=$!

spin='-\|/'

i=0
while kill -0 $pid 2>/dev/null
do
  i=$(( (i+1) %4 ))
  printf "\r${spin:$i:1}"
  sleep .1
done

"$path"/svm_light/svm_classify "$spath"/data/"$name"data.svm \
	"$spath"/outs/"$name"_model "$spath"/outs/"$name"_class > "$spath"/logs/"$name".train.log



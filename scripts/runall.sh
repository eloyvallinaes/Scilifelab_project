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

	# Create folder
if [ ! -d "../experiments/$name" ];
then
	mkdir ../experiments/"$name"
else
	echo "Folder ../experiments/$name already exists"
	exit
fi

if [ -z "$2" ]
then
	num=1
else
	num="$2"
fi
# 1 Divide into test, training and independet taking care of homologs
"$path"/set-divide_homologs.py "$name"

# 2 Create input in svm_light readable format
"$path"/feat-extract.py "$name"

# Merge training and rename test set
mv "../experiments/$name/set$num.svm" "../experiments/$name/test.svm"
for i in $( ls ../experiments/* | grep set.\.svm );
do
	cat "../experiments/$name/$i" > "../experiments/$name/training.svm"
	rm "../experiments/$name/$i"
done


# 4 Run learning and testing. Retrieve logs

"$path"/svm_light/svm_learn -t 0 "$spath"/experiments/"$name"/training.svm \
	"$spath"/experiments/"$name"/model $> "$spath"/experiments/"$name"/train.log & pid=$!

########################### Working in progress indicator
#spin='-\|/-|'						#
							#
#i=0							#
#while kill -0 $pid 2>/dev/null				#
#do							#
#  i=$(( (i+1) %6 ))					#
#  printf "\r Training. Be patient... ${spin:$i:1}"	#
#  sleep .5						#
#done							#
#########################################################

sleep 10

"$path"/svm_light/svm_classify -v 3 "$spath"/experiments/"$name"/test.svm \
	"$spath"/experiments/"$name"/model "$spath"/experiments/"$name"/class &> \
	"$spath"/experiments/"$name"/test.log



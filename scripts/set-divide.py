#!/usr/bin/python

# Written by Eloy Vallina
# February 2016

# Divide dataset into test and training
# 5 fold cross validation scheme
# Argument 1: keyname
# Agumentt 2: data set selection
	# 1 2 3 4 5
# Dataset already parsed to svm-light format
import sys

i=int(sys.argv[2])
j=range(1, 6)
j.remove(i)

test = open('../data/'+str(sys.argv[1])+'test.svm', 'w')
train = open('../data/'+str(sys.argv[1])+'train.svm', 'w')
F = open('../data/'+str(sys.argv[1])+'data.svm', 'r').readlines()

length=len(F)/5

f1=F[:length]
f2=F[length+1:2*length]
f3=F[2*length+1:3*length]
f4=F[3*length+1:4*length]
f5=F[4*length+1:5*length]

F=[f1, f2, f3, f4, f5]

print i
print j
test.write(F[i])
test.close()
for inidex in j:
	train.write(F[index])
train.close()

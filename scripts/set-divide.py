#!/usr/bin/python

# Written by Eloy Vallina
# February 2016

# Divide dataset into test and training
# 5 fold cross validation scheme
# Argument 1: keyname
# Agumentt 2: data set selection
	# 0 1 2 3 4
# Dataset already parsed to svm-light format
import sys

i=int(sys.argv[2])
j=range(0, 5)
j.remove(i)

test = open('../data/'+str(sys.argv[1])+'test'+str(i)+'.svm', 'w')
train = open('../data/'+str(sys.argv[1])+'train'+str(i)+'.svm', 'w')
F = open('../data/'+str(sys.argv[1])+'data.svm', 'r').readlines()

length=len(F)/5

f1=F[:length]
f2=F[length:2*length]
f3=F[2*length:3*length]
f4=F[3*length:4*length]
f5=F[4*length:5*length]

F=[f1, f2, f3, f4, f5]

print i
print j

for line in F[i]:
	test.write('{0}'.format(line))
test.close()
for index in j:
	for line in F[index]:
		train.write('{0}'.format(line))
train.close()

#!/usr/bin/python

# Writen by Eloy Vallina
# February 2016

# Extract features for classification in svm-light format
# Data file contains sequences in single lines starting ">"
# Second line contains characters "b" and "e", for "buried" and "exposed"

# Module 1 - extract outcome and first two features: name and P-C

# Residue dictionary
	# Name: 1-20
	# P-C properties: 1 (charged), 2 (polar), 3 (hydrophobic)
import sys

folder=str(sys.argv[1])+'/'
outcome = []
labels = []
seqs = []
groups = []
code = []
PC= []
nametonumb = {'A':[1,3], 'R':[2,1], 'N':[3,2], 'D':[4,1], 'C':[5,2], 'Q':[6,2], 'E':[7,1], 'G':[8,3], 'H':[9,1], 'I':[10,3], 'L':[11,3], 'K':[12,1], 'M':[13,3], 'F':[14,3], 'P':[15,3], 'S':[16,2], 'T':[17,2], 'W':[18,2], 'Y':[19,2], 'V':[20,3]}

for set in ['set1', 'set2', 'set3', 'set4', 'set5', 'set6']:
	f = open('../data/'+folder+set+'.3line').readlines()

	for i in range(0, len(f), 3):
		print i
		labels.append(f[i].strip())
		seqs.append(f[i+1].strip())
		groups.append(f[i+2].strip())

	for seq in seqs:
		for letter in seq:
			code.append(nametonumb[letter][0])
			PC.append(nametonumb[letter][1])
	for group in groups:
		for letter in group:
			if letter.strip() == 'b':
				outcome.append(1)
			else:
				outcome.append(-1)

	f = open('../data/'+folder+set+'.svm', 'w')
	for j in range(len(outcome)):
		f.write ('{0} 1:{1} 2:{2} \n'.format(outcome[j], code[j], PC[j]))

	f.close()

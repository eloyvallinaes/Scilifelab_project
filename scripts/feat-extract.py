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
nametonumb = {'A':[1,3, "10000000000000000000", "001"], 'R':[2,1, "01000000000000000000", "100"], \
	'N':[3,2, "00100000000000000000", "010"], 'D':[4,1, "00010000000000000000", "100"], \
	'C':[5,2, "00001000000000000000", "010"], 'Q':[6,2, "00000100000000000000", "010"], \
	'E':[7,1, "00000010000000000000", "100"], 'G':[8,3, "00000001000000000000", "001"], \
	'H':[9,1, "00000000100000000000", "100"], 'I':[10,3, "00000000010000000000", "001"], \
	'L':[11,3, "00000000001000000000", "001"], 'K':[12,1, "00000000000100000000", "100"], \
	'M':[13,3, "00000000000010000000", "001"], 'F':[14,3, "00000000000001000000", "001"], \
	'P':[15,3, "00000000000000100000", "001"], 'S':[16,2, "00000000000000010000", "010"], \
	'T':[17,2, "00000000000000001000", "010"], 'W':[18,2, "00000000000000000100", "010"], \
	'Y':[19,2, "00000000000000000010", "010"], 'V':[20,3, "00000000000000000001", "001"]}

for set in ['set1', 'set2', 'set3', 'set4', 'set5', 'independent-set']:
	f = open('../experiments/'+folder+set+'.3line').readlines()

	for i in range(0, len(f), 3):
		labels.append(f[i].strip())
		seqs.append(f[i+1].strip())
		groups.append(f[i+2].strip())

	for seq in seqs:
		for letter in seq:
			code.append(nametonumb[letter][2])
			PC.append(nametonumb[letter][3])
	for group in groups:
		for letter in group:
			if letter.strip() == 'b':
				outcome.append(1)
			else:
				outcome.append(-1)

	f = open('../experiments/'+folder+set+'.svm', 'w')
	for j in range(len(outcome)):
		f.write ('{0} 1:{1} 2:{2} \n'.format(outcome[j], code[j], PC[j]))

	f.close()

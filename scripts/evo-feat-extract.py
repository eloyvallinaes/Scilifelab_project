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

headers=[]
sequences=[]
groups=[]
PC= []
nametonumb = {'A':[1,3], 'R':[2,1], 'N':[3,2], 'D':[4,1], \
        'C':[5,2], 'Q':[6,2], 'E':[7,1], 'G':[8,3], \
        'H':[9,1], 'I':[10,3], 'L':[11,3], 'K':[12,1], \
        'M':[13,3], 'F':[14,3], 'P':[15,3], 'S':[16,2], \
        'T':[17,2], 'W':[18,2], 'Y':[19,2], 'V':[20,3]}

for set in ['set1', 'set2', 'set3', 'set4', 'set5', 'independent-set']:
	f=open('../experiments/'+folder+set+'.3line', 'r').readlines()
	for i in range(0, len(f),3):
		headers.append(f[i][1:].strip())
		sequences.append(f[i+1].strip())
		groups.append(f[i+2].strip())
	for header in headers:
		g=open('../data/multi_fasta/'+header+'.psi', 'r').readlines()
		for line in g:
			if re.match(r"^   [0-9 ][0-9] [A-Z]", line):
				score=line.split()[2:22]
	for seq in sequences:
		for letter in seq:
			PC.append(nametonumb[letter][1])
	for group in groups:
		for letter in group:
                       	if letter.strip() == 'b':
                               	outcome.append(1)
                       	else:
                               	outcome.append(-1)
	for j in range(len(outcome)):
		print outcome[j],
		for k in range(len(score)):
			print '{0}:{1}'.format(feature[k], score[k]),
		print '{0}:1'.format(PC[j])

#!/usr/bin/python

# Written by Eloy Vallina
# February 2016

# Generate fasta format sequence-only file for multiple sequence alignment

g = open('../data/sequences.fasta', 'w')
with open('../data/buried-exposed.3line', 'r') as f:
	for line in f:
		if '>' in line:
			g.write(line)
		elif 'b' not in line:
			g.write(line)
g.close()

#!/usr/bin/python

# Divide fasta file with multiple sequences in multiple fasta files

f=open('../data/sequences.fasta').readlines()
for i in range(0, len(f), 2):

	g=open('../data/multi_fasta3/'+f[i][1:].strip()+'.fasta', 'w')
	g.write(f[i])
	g.write(f[i+1])
	g.close()
	i=i+1

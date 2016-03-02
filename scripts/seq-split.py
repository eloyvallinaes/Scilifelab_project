#!/usr/bin/python

# Divide fasta file with multiple sequences in multiple fasta files

f=open('../data/sequences.fasta').readlines()
for i in range(0, len(f), 2):
	istring= '%0.3i' % (i/2+1)
	g=open('../data/multi_fasta/seq'+istring+'.fasta', 'w')
	g.write(f[i])
	g.write(f[i+1])
	g.close()
	i=i+1

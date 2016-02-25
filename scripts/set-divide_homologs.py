#!/usr/bin/python

# Written by Eloy Vallina
# February 2016

# Filter homologs using clustering results from CD hit
import sys

f = open('../data/CDhit.cluster', 'r').readlines()
g = open('../data/buried-exposed.3line', 'r').readlines()

set1 = open('../data/set1.3line', 'w')
set2 = open('../data/set2.3line', 'w')
set3 = open('../data/set3.3line', 'w')
set4 = open('../data/set4.3line', 'w')
set5 = open('../data/set5.3line', 'w')
set6 = open('../data/set6.3line', 'w')
allsets = [set1, set2, set3, set4, set5, set6]
set=[]
setcount=0
counter=1

for line in f:
	if '>Cluster' not in line:
		set.append(line.split()[2])
		counter=counter+1
		nextline=f[counter]
	else:
		if (set and counter >= len(f)/6+1 and setcount <=5 and '>Cluster' in nextline):
			for name in set:
				name = name.replace('...','\n')

				allsets[setcount].write(g[g.index(name)])
				allsets[setcount].write(g[g.index(name)+1])
				allsets[setcount].write(g[g.index(name)+2])
			setcount=setcount+1


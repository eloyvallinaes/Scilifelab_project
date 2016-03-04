#!/bin/bash

# Run psiblast on each single sequence fasta file

for sequence in $( ls ../data/multi_fasta3/* | grep "...\.fasta" )
do
	name=${sequence%\.fasta}
	./blast-2.2.26/bin/blastpgp -j 3 -d ../data/uniref90.fasta -i $sequence \
		-o "$name".blastpgp -Q "$name".psi
done

#!/usr/bin/python

# http://www.rosalind.info/problems/rna/

seqfile = open('/home/tunisia/Projects/rosalind/files/rosalind_dna.txt')
seq = seqfile.read()[:-1]

rnaseq = seq.replace('T','U')

print rnaseq
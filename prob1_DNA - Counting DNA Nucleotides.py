#!/usr/bin/python

# http://www.rosalind.info/problems/dna/

seqfile = open('/home/tunisia/Projects/rosalind/files/rosalind_dna.txt')
seq = seqfile.read()[:-1]

bases = set(list(seq))
counts = {base : 0 for base in bases}

for nt in list(seq):
    counts[nt] += 1

print counts
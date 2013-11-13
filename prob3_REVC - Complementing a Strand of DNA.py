#!/usr/bin/python

# http://www.rosalind.info/problems/revc/

seqfile = open('/home/tunisia/Projects/rosalind/files/rosalind_dna.txt')
seq = seqfile.read()[:-1]

binding = {'A' : 'T', 'C' : 'G', 'T' : 'A', 'G' : 'C'}

compseq = ''.join(binding[nt] for nt in seq)

compseq = compseq[::-1]

print compseq
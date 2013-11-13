#!/usr/bin/python

# http://www.rosalind.info/problems/hamm/

seqfile1 = open(a_file1)
seqfile2 = open(a_file2)
seq1 = seqfile1.read()
seq2 = seqfile2.read()

count = 0

for i in range(len(seq1)):
    if not seq1[i] == seq2[i]:
        count += 1

print 'Hamming distance is', count
#!/usr/bin/python

# http://www.rosalind.info/problems/gc/

def GCcontent(seq):
    GCcount = 0
    noncount = 0
    for nt in seq:
        if nt in ['G', 'C']:
            GCcount += 1
        else:
            noncount += 1
    return GCcount/(GCcount+noncount)

seqfile = open(a_file) # change this
seq = seqfile.read()
seqlist = seq.split('\n')

sequences = {}

for el in seqlist:
    if el[0] == '>':
        key = el[1:]
    else:
        value = el
        sequences[key] = value

contents = {key : GCcontent(sequences[key]) for key in sequences}

print max(contents, key = contents.get)
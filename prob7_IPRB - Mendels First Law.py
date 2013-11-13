#!/usr/bin/python

# http://www.rosalind.info/problems/iprb/

import itertools as it
from collections import Counter

domhetrec = (2,2,2)
popn = []

for i in range(domhetrec[0]):
    popn.append('dom')
for i in range(domhetrec[1]):
    popn.append('het')
for i in range(domhetrec[2]):
    popn.append('rec')

comb = list(it.combinations(popn,2))
totalpairs = len(comb)
#comb = [set(pair) for pair in comb]

counts = Counter(comb)
probs = {geno : 0 for geno in set(popn)}

for pair in counts:
    if pair[0] == pair[1]:
        if 'dom' in pair or 'rec' in pair:
            probs[pair[0]] += counts[pair]/totalpairs
        else:
            probs['dom'] += counts[pair]*0.25/totalpairs
            probs['rec'] += counts[pair]*0.25/totalpairs
            probs['het'] += counts[pair]*0.5/totalpairs
    elif not 'het' in pair:
        probs['het'] += counts[pair]/totalpairs
    elif 'dom' in pair:
        probs['dom'] += counts[pair]*0.5/totalpairs
        probs['het'] += counts[pair]*0.5/totalpairs
    else:
        probs['het'] += counts[pair]*0.5/totalpairs
        probs['rec'] += counts[pair]*0.5/totalpairs

print probs
    
        
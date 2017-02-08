#!/usr/bin/python

import sys
maxKey = None
maxHits = 0
hits = 0
oldKey = None

for line in sys.stdin:
    thisKey = line.strip()


    if oldKey and oldKey != thisKey:
        hits = 0

    oldKey = thisKey
    hits += 1

    if hits > maxHits:
	maxHits = hits
	maxKey = thisKey
print maxKey, '\t', maxHits



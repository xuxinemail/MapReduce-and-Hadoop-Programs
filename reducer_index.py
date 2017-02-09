#!/usr/bin/python
# the reducer file of building an inverted index

import sys
import re


oldword = None
nodes = []
num = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    word, node_id = data_mapped
    try:
	node_id = int(node_id)

        if oldword and oldword != word:
            print oldword, "\t", num, '\t',nodes
            oldword = word;
            nodes = []
	    num = 0

        oldword = word
        num += 1
        nodes.append(node_id)
    except:
	continue

if oldword != None:
    print oldword, "\t", num, '\t', nodes


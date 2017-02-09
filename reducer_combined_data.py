#!/usr/bin/python
# the reducer file of combining two datasets

import sys

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 10 or len(data_mapped) !=6:
        # Something has gone wrong. Skip this line.
        continue
    if len(data_mapped) == 6:
	author_id, marker, reputation, gold, silver, broze = data_mapped
    if len(data_mapped) == 10:
	author_id, marker, node_id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score = data_mapped
	print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(author_id, node_id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score, reputation, gold, silver, broze)




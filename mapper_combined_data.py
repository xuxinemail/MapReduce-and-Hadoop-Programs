#!/usr/bin/python

# the mapper of combining two datasets

import sys
import re

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 19:
    	node_id, title,tagnames, author_id, body, node_type, parent_id,abs_parent_id, added_at, score, state_string,last_edited_id,last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = data
    	author_id = author_id.strip()
    	author_id = re.findall(r'"([^ ]+)"', author_id)
    	author_id = node_id[0]
        try:
	    author_id = int(author_id)
	    print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}".format(author_id, 'B', node_id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score)
        except:
	    continue

    if len(data) == 5:
        author_id, reputation, gold, silver, broze = data
    	author_id = author_id.strip()
        author_id = re.findall(r'"([^ ]+)"', author_id)
    	author_id = node_id[0]
        try:
	    author_id = int(author_id)
	    print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(author_id, 'A', reputation, gold, silver, broze)
        except:
            continue
	



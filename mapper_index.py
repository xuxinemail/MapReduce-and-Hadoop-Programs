#!/usr/bin/python

# the mapper of building an inverted index

import sys
import re

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 19:  
	continue         			
    node_id, title,tagnames, author_id, body, node_type, parent_id,abs_parent_id, added_at, score, state_string,last_edited_id,last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = data

    node_id = node_id.strip()
    node_id = re.findall(r'"([^ ]+)"', node_id)
    node_id = node_id[0]
    body = body.strip()
    body = body.lower()
    words = re.split(r"[.!?,:;\"()<>\[\]#$=\-\/\s]", body)
    for word in words:
	print "{0}\t{1}".format(word, node_id)

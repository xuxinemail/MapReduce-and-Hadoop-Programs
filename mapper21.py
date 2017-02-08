#!/usr/bin/python


import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        IP, ID, user, time, req, method, path, protocol, status, size = data
	newpath = path.replace("http://www.the-associates.co.uk",'')
        print newpath


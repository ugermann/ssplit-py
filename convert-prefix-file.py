#!/usr/bin/env python3

# convert a moses prefix file into a python dictionary

import sys,os,regex,glob,pickle

pat = regex.compile(r"([^#].*)(?:[\s]+(\#NUMERIC_ONLY\#))?",regex.U)
def file2dict(fname):
    D = {}
    for line in open(fname):
        if line.startswith('#'): continue
        m = pat.match(line)
        if m: D[m.group(1)] = 2 if m.group(2) else 1
        pass
    return D

D = {}
for prefix_file in glob.glob("%s/nonbreaking_prefix.*"%sys.argv[1]):
    p = prefix_file.rfind('.')+1
    D[prefix_file[p:]] = file2dict(prefix_file)
    pass

pickle.dump(D,open(sys.argv[2], 'wb'),protocol=pickle.HIGHEST_PROTOCOL)

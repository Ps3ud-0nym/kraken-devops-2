#!/usr/bin/env python

import pandas

file = pandas.read_csv("/etc/hosts",comment='#')

for col in file.columns:
    print(col[1])

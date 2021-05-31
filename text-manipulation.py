#!/usr/bin/env python

import re

pattern = "docker"

file = open("/etc/hosts", "r")

#re.findall(pattern, file)
for word in file:
    if re.search(pattern, word):
        print(word)


#!/usr/bin/env python3
from functools import *

text_file = open("puzzle", "r")
lines = text_file.read().splitlines()
text_file.close()
print(lines)

r = reduce(lambda acc, v: acc + int(v), lines, 0)
print(r)
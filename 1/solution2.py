#!/usr/bin/env python3
from itertools import *

text_file = open("puzzle", "r")
lines = text_file.read().splitlines()
text_file.close()
# print(lines)

# lines = ["+1", "-1"]
# lines = ["+3", "+3", "+4", "-2", "-4"]
# lines = ["-6", "+3", "+8", "+5", "-6"]
# lines = ["+7", "+7", "-2", "-7", "-4"]

acc = 0
values = [0]
for v in cycle(lines):
  acc += int(v)
  if acc in values:
    print(">>>>",acc)
    break
  values.append(acc)

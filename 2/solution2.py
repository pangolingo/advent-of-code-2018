#!/usr/bin/env python3
import numpy as np

text_file = open("puzzle", "r")
lines = text_file.read().splitlines()
text_file.close()
# print(lines)

def find_common(data):
  for i in range(0, len(data)):
    for j in range(i+1, len(data)):
      # print(data[i], data[j])
      mask = np.array(list(data[i])) == np.array(list(data[j]))
      # print(mask)
      if mask.tolist().count(False) == 1:
        # print("found one!", data[i], data[j])
        index = mask.tolist().index(False)
        common = list(data[i])
        common.pop(index)
        common = "".join(common)
        # print("common", common)
        return common

test_lines = [
  "abcde",
  "fghij",
  "klmno",
  "pqrst",
  "fguij",
  "axcye",
  "wvxyz",
]
assert(find_common(test_lines)=="fgij")

print(">>>", find_common(lines))
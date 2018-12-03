#!/usr/bin/env python3
import numpy as np

text_file = open("puzzle", "r")
lines = text_file.read().splitlines()
text_file.close()
# print(lines)

def parse_line(line):
  parts = line.split()
  id = parts[0][1:]
  x, y = parts[2].split(",")
  y = y.strip(":")
  w, h = parts[3].split("x")
  return {
    "id": id,
    "x": int(x),
    "y": int(y),
    "w": int(w),
    "h": int(h)
  }

assert(parse_line("#1360 @ 208,456: 28x10") == { "id": "1360", "x": 208, "y": 456, "w": 28, "h": 10 })

fabric = np.zeros((2000, 2000))

for raw_line in lines:
  line = parse_line(raw_line)
  shape = np.ones((line["w"], line["h"]))
  fabric[line["x"] : line["x"] + line["w"], line["y"] : line["y"] + line["h"]] += shape

overlaps = np.count_nonzero(fabric > 1)
print(">>>", overlaps)

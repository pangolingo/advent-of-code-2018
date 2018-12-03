#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

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

def does_overlap(l1, l2):
  top_left1 = (l1["x"], l1["y"])
  top_left2 = (l2["x"], l2["y"])
  bottom_right1 = (l1["x"] + l1["w"], l1["y"] + l1["h"])
  bottom_right2 = (l2["x"] + l2["w"], l2["y"] + l2["h"])

  # If one rectangle is on left side of other 
  if top_left1[0] > bottom_right2[0] or top_left2[0] > bottom_right1[0]:
    return False; 
 
  # If one rectangle is above other 
  if top_left1[1] > bottom_right2[1] or top_left2[1] > bottom_right1[1]:
    return False

  return True

# a super slow overlap dectector, using numpy's 2d arrays
def does_overlap_numpy(line1, line2):
  fabric = np.zeros((2000, 2000))
  shape_1 = np.ones((line1["w"], line1["h"]))
  shape_2 = np.ones((line2["w"], line2["h"]))
  fabric[line1["x"] : line1["x"] + line1["w"], line1["y"] : line1["y"] + line1["h"]] += shape_1
  fabric[line2["x"] : line2["x"] + line2["w"], line2["y"] : line2["y"] + line2["h"]] += shape_2

  overlaps = np.count_nonzero(fabric > 1)
  return overlaps > 1


def find_overlaps():
  overlaps_set = set()
  for i in range(0, len(parsed_lines)):
    overlap = False
    line1 = parsed_lines[i]

    if line1["id"] in overlaps_set:
        next

    for j in range(i+1, len(parsed_lines)):
      line2 = parsed_lines[j]

      if line2["id"] in overlaps_set:
        next

      if does_overlap(line1, line2):
        overlaps_set.add(line1["id"])
        overlaps_set.add(line2["id"])

  # find the missing shape in the set
  for line in parsed_lines:
    if line["id"] not in overlaps_set:
      return line


parsed_lines = []
for line in lines:
  parsed_lines.append(parse_line(line))

unique_claim = find_overlaps()
print(">>>", unique_claim)

# show a chart
for line in parsed_lines:
  currentAxis = plt.gca()
  currentAxis.add_patch(Rectangle((line["x"], line["y"]), line["w"], line["h"] ,edgecolor='b',fill=False, alpha=0.2))
  
  plt.text(line["x"], line["y"], line["id"], fontsize=4)
  
  if line["id"] == unique_claim["id"]:
    currentAxis.add_patch(Rectangle((line["x"], line["y"]), line["w"], line["h"] ,edgecolor='r',fill=False, alpha=1))

plt.gca().invert_yaxis()
plt.autoscale()
plt.show()

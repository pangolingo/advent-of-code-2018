#!/usr/bin/env python3
import re

text_file = open("puzzle", "r")
lines = text_file.read().splitlines()
text_file.close()
# print(lines)

def taxi_dist(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] -p2[1])

def parse_line(line):
  l = line.split(", ")
  return (int(l[0]), int(l[1]))


assert(parse_line("225, 205") == (225, 205))

p_lines = set(map(parse_line, lines))

x_sort = sorted(p_lines, key=lambda l: l[0])
y_sort = sorted(p_lines, key=lambda l: l[1])

bounds_top_left = (x_sort[0][0], y_sort[0][1])
bounds_bottom_right = (x_sort[-1][0], y_sort[-1][1])
bounds_width = bounds_bottom_right[0] - bounds_top_left[0]
bounds_height = bounds_bottom_right[1] - bounds_top_left[1]

# consider throwing away points on the bounds

points_with_owner = {}

for test_point_x in range(bounds_top_left[0], bounds_bottom_right[0]):
  for test_point_y in range(bounds_top_left[1], bounds_bottom_right[1]):
    test_point = (test_point_x, test_point_y)

    for point in p_lines:
      dist = taxi_dist(point, test_point)

      if test_point in points_with_owner:
        if points_with_owner[test_point] == "overlap":
          continue
        elif points_with_owner[test_point][1] > dist:
          # if the dict number is bigger than our dist, do nothing
          pass
        elif points_with_owner[test_point][1] < dist:
          # if it's less, replace with our dist/point owner
          points_with_owner[test_point] = (point, dist)
        else:
          # if it's the same, add "overlap"
          points_with_owner[test_point] = "overlap"
      else:
        # the tuple is (owning point, distance)
        points_with_owner[test_point] = (point, dist)

owner_totals = {}

for i in points_with_owner:
  p = points_with_owner[i]
  if p[0] in owner_totals:
    owner_totals[p[0]] += 1
  else:
    owner_totals[p[0]] = 1



print(owner_totals)




# print(point_owners)
# first compute the bounds
# MAYBE: throw away the items on the bounds because they'll be infinite
# for each point
  # walk through every point in the bounds ~400x400 = 160,000
  # compute the manhattan distance

  # OR
  # save it in a dict: dict[(x,y)] = (line#, dist)
  # if that dict already exists
    # if that dict key contains "overlap", do nothing
    # if that dict key is empty, add the tuple
    # if that dict key has number
      # if the dict number is bigger than our dist, do nothing
      # if it's less, add our dist
      # if it's the same, add "overlap"


# loop through the dict once again
# create a new table with line# -> # of points that belongs to it
# return the largest
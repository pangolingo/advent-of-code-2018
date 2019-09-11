#!/usr/bin/env python3
from datetime import datetime
import re

text_file = open("puzzle", "r")
lines = text_file.read().splitlines()
text_file.close()
# print(lines)

def parse_line(line):
  parts = line.split()
  d = parts[0].strip("[]")
  t = parts[1].strip("[]")
  raw_dt = " ".join([d, t])
  date = datetime.fromisoformat(raw_dt)
  action = " ".join(parts[2:])
  return (date, action)

parsed_lines = sorted(map(parse_line, lines), key=lambda x: x[0])

guards = {}

guard = None
sleep_start = None
for line in parsed_lines:
  date = line[0]
  action = line[1]
  # print(date, action)
  if action[0:5] == "Guard":
    guard = action.split()[1].strip("#")
  elif action[0:5] == "falls":
    sleep_start = date
  elif action[0:5] == "wakes":
    sleep_end = date
    elapsed_time = sleep_end - sleep_start

    if guard in guards:
      guards[guard]["total_sleep"] += elapsed_time.total_seconds()
      for m in range(sleep_start.minute,sleep_end.minute):
        if m in guards[guard]["mins"]:
          guards[guard]["mins"][m] += 1
        else:
          guards[guard]["mins"][m] = 1
    else:
      guards[guard] = { "total_sleep": elapsed_time.total_seconds(), "mins": {} }
      for m in range(sleep_start.minute,sleep_end.minute):
        guards[guard]["mins"][m] = 1


s = sorted(guards, key=lambda g: guards.get(g)["total_sleep"])
sleepiest_guard = guards[s[-1]]
print("sleepiest guard >>>", sleepiest_guard)
z = sorted(sleepiest_guard["mins"], key=sleepiest_guard["mins"].get)
print("most sleepy minute of that guard >>>", z[-1])
print(">>>", int(s[-1]) * z[-1])

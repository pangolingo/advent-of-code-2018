#!/usr/bin/env python3
from datetime import datetime
import re
from tabulate import tabulate

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

empty_mins = {}
for i in range(0, 61):
  empty_mins[i] = 0

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
      guards[guard] = { "total_sleep": elapsed_time.total_seconds(), "mins": empty_mins.copy() }
      for m in range(sleep_start.minute,sleep_end.minute):
        guards[guard]["mins"][m] += 1

rows = []
sleepy_guard_minutes = []

for g in guards:
  guard = guards[g]
  mins = []
  for i in range(0,61):
    mins.append(guard["mins"][i])
  rows.append([g] + mins)
  sleep_totals_by_minute = sorted(guard["mins"], key=guard["mins"].get)
  sleepy_guard_minutes.append((g, sleep_totals_by_minute[-1], guard["mins"][sleep_totals_by_minute[-1]]))

headers = ["Guard"] + list(range(0,61))
print(tabulate(rows, headers=headers))

ordered_sleepy_guard_minutes = sorted(sleepy_guard_minutes, key=lambda g: g[2])
sleepiest = ordered_sleepy_guard_minutes[-1]
print(">>>", sleepiest, ">>>", int(sleepiest[0]) * sleepiest[1])

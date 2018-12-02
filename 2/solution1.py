#!/usr/bin/env python3
from collections import *

text_file = open("puzzle", "r")
lines = text_file.read().splitlines()
text_file.close()
# print(lines)

def find_with_letters(str):
  two = False
  three = False
  for letter, count in Counter(str).items():
    if count == 2:
      two = True
    if count == 3:
      three = True
    if two and three:
      break
  return (two, three)

assert(find_with_letters("abcdef") == (False, False))
assert(find_with_letters("bababc") == (True, True))
assert(find_with_letters("abbcde") == (True, False))
assert(find_with_letters("abcccd") == (False, True))
assert(find_with_letters("aabcdd") == (True, False))
assert(find_with_letters("abcdee") == (True, False))
assert(find_with_letters("ababab") == (False, True))

two_letters = 0
three_letters = 0

for line in lines:
  counts = find_with_letters(line)
  if counts[0]:
    two_letters += 1
  if counts[1]:
    three_letters += 1

checksum = two_letters * three_letters
print(">>>", checksum)

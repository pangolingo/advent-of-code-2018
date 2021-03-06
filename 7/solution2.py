#!/usr/bin/env python3
import re
import string
import sys

text_file = open("puzzle", "r")
puzzle = text_file.read()
text_file.close()
# print(puzzle)

regex = re.compile(
  "aA|Aa|"
  "bB|Bb|"
  "cC|Cc|"
  "dD|Dd|"
  "eE|Ee|"
  "fF|Ff|"
  "gG|Gg|"
  "hH|Hh|"
  "iI|Ii|"
  "jJ|Jj|"
  "kK|Kk|"
  "lL|Ll|"
  "mM|Mm|"
  "nN|Nn|"
  "oO|Oo|"
  "pP|Pp|"
  "qQ|Qq|"
  "rR|Rr|"
  "sS|Ss|"
  "tT|Tt|"
  "uU|Uu|"
  "vV|Vv|"
  "wW|Ww|"
  "xX|Xx|"
  "yY|Yy|"
  "zZ|Zz|"
)

def react(o_str):
  new_str = regex.sub("", o_str)
  # print(new_str, o_str)
  # print(len(new_str), len(o_str))
  if len(new_str) == len(o_str):
    return o_str
  else:
    return react(new_str)

assert(regex.sub("", "aAqqqBb") == "qqq")
assert(regex.sub("", "aAAabBBbcCCcdDDdeEEefFFfgGGghHHhiIIijJJjkKKklLLlmMMmnNNnoOOopPPpqQQqrRRrsSSstTTtuUUuvVVvwWWwxXXxyYYyzZZz") == "")
assert(react("dabAcCaCBAcCcaDA") == "dabCBAcaDA")

def replace_letter(s, l):
  return re.sub(l, "", s, flags=re.IGNORECASE)

assert(replace_letter("dabAcCaCBAcCcaDA", "a") == "dbcCCBcCcD")
assert(replace_letter("dabAcCaCBAcCcaDA", "b") == "daAcCaCAcCcaDA")
assert(replace_letter("dabAcCaCBAcCcaDA", "c") == "dabAaBAaDA")
assert(replace_letter("dabAcCaCBAcCcaDA", "d") == "abAcCaCBAcCcaA")


letters = {}

sys.setrecursionlimit(5000)

for l in string.ascii_lowercase:
  smaller_puzzle = replace_letter(puzzle, l)
  letters[l] = len(react(smaller_puzzle))
  print("tried", l, "result", letters[l])

print(letters)
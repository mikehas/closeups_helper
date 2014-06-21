#!/usr/bin/env python
import sys
from sets import Set

# Given a set of letters and a word length n, display all possible words of length n you can make with the original set of letters.

# Input
input = 'blabbeougotoum' # set of letters
length = 9               # n

# HELPERS

# Find the number of occurences of each letter in a word
def getCounts(word):
  counts = {}
  for i in word:
    if counts.has_key(i):
      counts[i] = counts[i] + 1
    else:
      counts[i] = 1
  return counts

# MAIN

sup = Set(input)
print sup
print "Searching..."

words = '/usr/share/dict/words'
f = open(words)

results = []

# First pass 
# Python Set comparisons only consider unique elements.
for line in f.readlines():
  line = line.strip()
  if len(line) == length:
    sub = Set(line) 
    if sub.issubset(sup):
      results.append(line)
counts = getCounts(input)
  
results2 = []

# Remove words from 1st pass that have incorrect number of letters
for item in results:
  itemcounts = getCounts(item)
  candidate = True
  for key, val in itemcounts.iteritems():
    if candidate:
      if val > counts[key]:
        candidate = False
  if candidate:
    results2.append(item)

for item in results2:
  print item


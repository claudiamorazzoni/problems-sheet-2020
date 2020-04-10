# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.

import collections

c = collections.Counter()
with open('lorem-ipsum.txt', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

print(c['e'])


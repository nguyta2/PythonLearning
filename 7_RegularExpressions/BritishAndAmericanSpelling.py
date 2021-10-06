import re
import sys

lines = []
words = []
input = '''
7
unfair arrival faint region pride realise paralyse length officially disturbing
call fashionable room take claim capable biscuit cough qualified realze
decoration indeed caramelise gas habit downward salad realize on knee
catalyse blade artistic put careless league final waste catalyse bedroom
door materialize catalyse round point routine celebration paralyse stranger weather
artificially materialise personally elegant lane celebration statement whom tend bone
realise infect coloured planet pet estimate lane infectious destroy exchange
9
materialize
catalyze
realize
hydrolyze
caramelize
recognize
organize
paralyze
colonize
'''
input = input.strip()
lines = input.splitlines()

numLines = int(lines[0])
numWords = int(lines[1+numLines])

for i in range(numLines, numLines + numWords):
  words.append(lines[i+2])

for word in words:
  word = word[:len(word) - 2]
  regex = re.compile(re.escape(word) + r'[zs]e')
  count = 0
  for i in range(1, numLines + 1):
    #print(regex.findall(lines[i]))
    if(bool(regex.findall(lines[i]))):
      count+=len(regex.findall(lines[i]))
  print(count)

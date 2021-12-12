import numpy as np

data = open('input.txt').read().splitlines()

M = dict()
for line in data:
  b, e = line.split("->")

  x1, y1 = b.split(',') 
  x2, y2 = e.split(',')
  x1, x2 = int(x1), int(x2)
  y1, y2 = int(y1), int(y2)
  
  x1, x2 = min(x1, x2), max(x1, x2)
  y1, y2 = min(y1, y2), max(y1, y2)
  #if x1 == x2 or y1 == y2:
  for i in range(x1, x2+1):
    for j in range(y1, y2+1):
      if (i, j) not in M:
        M[(i, j)] = 0
      M[(i, j)] += 1
  
count = 0
for key in M:
  if M[key] > 1:
    count += 1
print(count)

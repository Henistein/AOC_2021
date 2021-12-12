import numpy as np

data = list(map(int, open('input.txt').read().splitlines()[0].split(',')))
data = np.array(data)

def part1():
  m = np.median(data)

  count = 0
  for i in data:
    count += abs(m - i)

  return count

def part2():
  m = data.mean()
  
  count = 0
  for i in data:
    count += (abs(m - i) * (abs(m - i) + 1) / 2)

  return count

print(part1())
print(part2())

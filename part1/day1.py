data = [int(i.strip()) for i in open('input1').readlines()]

def part1():
  prev = -1
  inc = 0
  for row in data:
    if prev != -1:
      if prev < row:
        inc += 1
    prev = row

def part2():
  prev = -1
  inc = 0
  s = []
  for i in range(len(data)-2):
    s.append(data[i] + data[i+1] + data[i+2])
  for row in s:
    if prev != -1:
      if prev < row:
        inc += 1
    prev = row

  print(inc)
      

part2()

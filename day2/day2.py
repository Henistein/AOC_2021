data = [i.strip() for i in open("input.txt").readlines()]

def part1():
  h = 0
  d = 0
  for row in data:
    aux = row.split()
    if aux[0] == 'forward':
      h += int(aux[1])
    if aux[0] == 'down':
      d += int(aux[1])
    if aux[0] == 'up':
      d -= int(aux[1])
  return h * d

def part2():
  aim = 0
  h = 0
  d = 0
  for row in data:
    aux = row.split()
    if aux[0] == 'forward':
      h += int(aux[1])
      d += (aim * int(aux[1]))
    if aux[0] == 'down':
      aim += int(aux[1])
    if aux[0] == 'up':
      aim -= int(aux[1])
  return h * d

print(part1())
print(part2())

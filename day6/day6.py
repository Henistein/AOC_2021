data = list(map(int, open('input.txt').read().splitlines()[0].split(',')))

count8 = 0

for k in range(80):
  for i in range(len(data)):
    if data[i] - 1 == -1:
      data[i] = 6
      count8 += 1
    else:
      data[i] -= 1
  for j in range(count8):
    data.append(8)
  count8 = 0
print(len(data))

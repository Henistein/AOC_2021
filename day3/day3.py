import numpy as np

dataa = [[i for i in j] for j in open('input.txt').read().splitlines()]

def part1():
  data = np.array(dataa).T
  gamma = []
  epsilon = []

  for i in range(data.shape[0]):
    aux = data[i].astype('uint')
    if aux.mean() > 0.50:
      gamma.append(1)
      epsilon.append(0)
    else:
      gamma.append(0)
      epsilon.append(1)

  g = int("".join([str(i) for i in gamma]), 2)
  e = int("".join([str(i) for i in epsilon]), 2)
  return g * e

def part2():
  def solve(criteria):
    X = np.array(dataa)

    filt = X.copy()
    gas = 0
    for i in range(X.shape[1]):
      aux = filt.T[i].astype('uint')
      if criteria == 'o2':
        bit = int(aux.mean() >= 0.50)
      else:
        bit = int(aux.mean() < 0.50)

      idx1 = [i for (i, v) in enumerate(aux) if v==bit]

      if len(idx1) == 1:
        gas = filt[idx1, :]
      filt = filt[idx1, :]
    return gas

  o2 = int("".join([str(i) for i in solve('o2')[0]]), 2)
  co2 = int("".join([str(i) for i in solve('co2')[0]]), 2)
  return o2 * co2

print(part2())

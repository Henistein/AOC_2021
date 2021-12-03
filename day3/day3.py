import numpy as np

data = [[i for i in j] for j in open('input.txt').read().splitlines()]

data = np.array(data).T
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
print(g*e)

import numpy as np

data = [line for line in open('input.txt').read().splitlines()]

header = [int(i) for i in data[0].split(',')]

boards = []
aux = []
for row in data[2:]:
  if len(row) == 0:
    boards.append(aux.copy())
    aux = []
  else:
    aux.append([int(i) for i in row.split()])
boards.append(aux.copy())
boards = np.array(boards)

# mark all the boards with -1
def part1():
  def solve():
    for h in header:
      for board in boards:
        index = np.argwhere(board == h) 
        if len(index) != 0:
          board[index[0, 0], index[0, 1]] = -1
          # check if row is complete
          for row in board:
            if np.sum(row) == -5:
              return (h,board)
          # check if col is complete
          for col in board.T:
            if np.sum(col) == -5:
              return (h,board)

  h, board = solve()
  # count how many -1
  count = np.count_nonzero(board == -1)
  count = np.sum(board) + count
  return count * h

def part2():
  def solve():
    I = set()
    for (hi, h) in enumerate(header):
      for (i, board) in enumerate(boards):
        index = np.argwhere(board == h) 
        if len(index) != 0:
          aux = board
          board[index[0, 0], index[0, 1]] = -1
          # check if row is complete
          for row in board:
            if np.sum(row) == -5:
              I.add(i)
          # check if col is complete
          for col in board.T:
            if np.sum(col) == -5:
              I.add(i)
        if len(I)+1 == len(boards):
          idx = ((len(boards) * (len(boards)-1)) // 2) - sum(I)
          return (header[hi:], boards[idx]) # returns last board

  (hd, board) = solve()

  # check which h will complete the last board
  stop = 0
  f = 0
  for h in hd:
    if not stop:
      index = np.argwhere(board == h) 
      if len(index) != 0:
        board[index[0, 0], index[0, 1]] = -1
        for row in board:
          if np.sum(row) == -5:
            stop = 1
            f = h
        for col in board.T:
          if np.sum(col) == -5:
            stop = 1
            f = h

  count = np.count_nonzero(board == -1)
  count = np.sum(board) + count
  return count * f

print(part1())
print(part2())

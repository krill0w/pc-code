import math
from itertools import combinations

f= open('searchNumbers.txt', 'r')

def solve(length):
  for value in combinations(n, length):
    if sum(value) == 2020:
      return math.prod(value)


n = [int(line.strip()) for line in f]
print(solve(2))
print(solve(3))
import random

MAX = 1<<20
x, delta = 10000, 30

for i in xrange(0, MAX):
  print x
  x += -delta + random.randint(0, 2*delta)

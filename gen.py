import random

MAX = 2000
x, delta = 10000, 2000

for i in xrange(0, MAX):
  print x
  x += -delta + random.randint(0, 2*delta)

#!/usr/bin/env python3

def fibs(low = 0, high = 1):
  while True:
    yield low
    low, high = high, low+high

if __name__ == '__main__':
  print("It said 'add a few lines of code', not what to add, so ...")
  print("Here are the first 20 numbers in the fibonacci sequence, I guess.")
  for i, fib in enumerate(fibs()):
    print(fib)
    if i > 19: break

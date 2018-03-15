# There are exactly 100 prime numbers whose digits are in strictly ascending order
import itertools
import math

def is_prime(n):
  if n == 2:
    return True
  if n % 2 == 0 or n <= 1:
    return False

  sqr = int(math.sqrt(n)) + 1

  for divisor in range(3, sqr, 2):
    if n % divisor == 0:
      return False
  return True

count = 0
arr = range(1, 10)
for i in xrange(10):
  for j in itertools.combinations(arr, i):
    num = int('0' + ''.join(map(str, j)))
    if is_prime(num):
      count += 1
      print num

print
print "Number of primes with digits in strictly ascending order: ", count

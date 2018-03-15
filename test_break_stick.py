# If you break a stick into three parts, what is the probability that the parts can form a triangle?

# Hypothesis: 1/4
# If you want to ensure that you don't form a triangle, at least one part of the stick should be greater than or equal to L/2
# So let's assume you break the stick somewhere. Tou have two parts: x and (L-x). One of these will be greater than or equal to L/2
# Take that piece. Let's assume x >= L/2 for now. So, you will pick up the piece with length x and you want to ensure that you preserve 1/2 of the length.
# This will mean that you can either break the stick somewhere along (0 to x-L/2) or (L/2 to x) which gives you 2 * (x - L/2) space.
# Additionally, you can always break the smaller stick. Thus, the second break has 2 * (x - L/2) + (L-x) possible points = x possible points
# So, the possibility of not forming a triangle will be 2/L * Integral[x = L/2 --> L][x/L] = 2/L^2 * [L^2/2 - (L/2)^2/2] = 2/L^2 * 3L^2/8 = 3/4
# [NOTE: 2/L is multiplied at the start because 1/L probability of breaking the stick, and x can be < L/2 with equal probability]
#
# Hence, the probability of forming a triangle will be 1 - 3/4 = 1/4

import random

L = 100000

triangle = 0
total = 0
for i in range(100000):
  i = random.randrange(L)
  j = random.randrange(L)

  if i > j:
    i, j = j, i

  p1 = i
  p2 = j - i
  p3 = L - j

  # Check if triangle
  if (p1 + p2) > p3 and (p2 + p3) > p1 and (p1 + p3) > p2:
    triangle += 1

  total += 1

print(triangle * 1.0 / total)
print("Should be roughly 0.25")

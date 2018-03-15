import random

fingers = 7
players = 7
times = 100000 * players

picks = [0]*players

for _ in range(times):
  tot_fingers = 0
  for i in range(players):
    tot_fingers += random.randrange(fingers)
  picks[tot_fingers % players] += 1

print (picks)

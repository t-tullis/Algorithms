#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  rps = ['rock', 'paper', 'scissors']
  outcomes = []

  def rps_results(roundsLeft, play):
    if roundsLeft == 0:
      return outcomes.append(play)
    for i in rps:
      rps_results(roundsLeft- 1, play + [i])
  rps_results(n, [])
  return outcomes

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

  print(rock_paper_scissors(2))

# Mike Bland
# Mastermind game
#

import random
import collections

length = 4
guesses = 10
pattern = [random.choice('RBWG') for _ in range(length)]
#print (*pattern) # for debugging
counted = collections.Counter(pattern)

def running():
    guess = input('Please enter your guess(R-Red, B-Blue, G-Green, W-white: ')
    guess_count = collections.Counter(guess)
    close = sum(min(counted[k], guess_count[k]) for k in counted)
    exact = sum(a==b for a,b in zip(pattern, guess))
    close -= exact
    print('Exact Match: {}.Close Match: {}.'.format(exact, close))
    return exact != length

for attempt in range(10):
    if not running():
        print('You won! Game Over')
        break
    else:
        print('Guessing remaining:', guesses - 1 - attempt)
else:
    print('Game Over. The pattern was {}.'.format(''.join(pattern)))
        

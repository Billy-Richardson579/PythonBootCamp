import random

random_int = random.randint(0,1)


players_choice = input('Heads or Tails? ')

if random_int == 0:
    result = 'Heads'
else: result = 'Tails'

if result == players_choice:
    print('You Win It Landed on ' + result)
else: print('You Lose It Landed on ' + result)
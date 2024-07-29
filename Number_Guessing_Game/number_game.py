import random
RANDOM_NUMBER = random.randint(1,100)
print(RANDOM_NUMBER) 
def lives_selector():
    lives = 0
    mode = input('Choose Level (easy) 10 attempts or (hard) 5 attempts')
    if mode == 'easy':
        lives += 10
    else: lives += 5
    return lives

def number_check(user_guess,rand_int):
    if user_guess == RANDOM_NUMBER:
        print(f'You Win The Number Was {RANDOM_NUMBER}')
        return True
    elif user_guess > RANDOM_NUMBER:
        print('Too High')
    else: print('Too Low')
print('Welcome to number guess ')
user_lives = lives_selector()
while user_lives != 0:
    print(f'You have {user_lives} lives remaining')
    user_input = input('Pick a Number: ')
    if number_check(int(user_input),RANDOM_NUMBER) == True:
        break
    user_lives -= 1
    

if user_lives == 0:
    print('YOU RUN OUT OF LIVES')


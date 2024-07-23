import random

cpu_choice = random.randint(0,2)

print(cpu_choice)
choice = ['Rock', 'Paper', 'Scissors']

player_choice = input("rock,paper or scissors ")

if player_choice == 'rock':
    player_choice = 0
elif player_choice == 'paper':
    player_choice = 1
elif player_choice == 'scissors':
    player_choice = 2
else: 
    print("error you gave a wrong value")
    exit()



if cpu_choice == player_choice:
    print('CPU also chose ' + choice[cpu_choice] + ' you Draw')
elif player_choice == cpu_choice + 1 or player_choice == cpu_choice -2:
    print('You Win CPU chose ' + choice[cpu_choice])
else: print('You Lose CPU chose ' + choice[cpu_choice])

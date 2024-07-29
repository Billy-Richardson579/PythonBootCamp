from game_data import data
import random

def print_celeb_data(celebData):
    print(f"{celebData['name']}, a {celebData['description']} from {celebData['country']}")
    return celebData['follower_count']

def random_Celeb():
    rand_number = random.randint(0,len(data)) 
    return rand_number
print(random_Celeb())
correct = True
score = 0

while correct == True:
   rand_num1 = random_Celeb()
   print(f'Curent Score {score}')
   rand_num2 = random_Celeb()
   if score == 0:
       celeb_A = print_celeb_data(data[rand_num1])
   else: celeb_A = winner 
   celeb_B = print_celeb_data(data[rand_num2])
   user_choice = input('Who has has more follwers?  A or B  ')
   if user_choice == 'a':
       if celeb_A > celeb_B:
           print('Correct + 1 Score')
           score += 1
           winner = print_celeb_data(data[rand_num2])
       else: correct = False
       
   elif user_choice == 'b':
       if celeb_A < celeb_B:
           print('Correct + 1 Score')
           score += 1
           winner = print_celeb_data(data[rand_num2])
       else: correct = False
       
    
       
       
    

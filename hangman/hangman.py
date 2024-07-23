import random

# List of sample words
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
guessed_alphabet = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

hangman_stages = [
    """
      
     
     
     
     
     
     
    _|___
    """,
    """
      _______
     |/      
     |      
     |      
     |       
     |      
     |
    _|___
    """,
    """
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
    """,
    """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
    """
]

# Test output by printing each stage
for stage in hangman_stages:
    print(stage)
    print("\n")


# Generate a set of five random words
chosen_word = word_list[1]
lives = 11
i = 0
was_in_word = True
hidden_word = list('_' * len(chosen_word))
print(hidden_word)
return_word = ''
while lives > 0:
    print(hangman_stages[lives])
    
    user_guess = input('Enter a Letter ')
    if user_guess in guessed_alphabet:
        print('You have already guessed this')
         
    elif user_guess not in alphabet:
        print('This isnt a letter')
        
    elif user_guess not in guessed_alphabet and user_guess in alphabet:
        guessed_alphabet.append(user_guess) 
        print(guessed_alphabet)
    was_in_word = False
    for i in range(len(chosen_word)):
        if user_guess == chosen_word[i]:
            was_in_word = True
            hidden_word[i] = user_guess
            return_word = ''.join(hidden_word)
            print(return_word)
    if not was_in_word: 
             lives -= 1
             print('Wrong ' + str(lives) + ' lives remaining!!!')
    else: print('Good Guess')
    if lives == 0:
         print('GAME OVER')
    

    

        
      
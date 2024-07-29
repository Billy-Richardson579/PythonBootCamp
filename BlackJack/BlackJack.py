import random

cards = ['A', 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9, 10 ,'J' , 'Q', 'K']

def twist(whos_cards):
    random_card = random.randint(0,12)
    whos_cards.append(cards[random_card])


def check_score(players_cards):
    score = 0
    for card in players_cards:
        if card == 'A':
            user_choice = input('would you like the Ace to equal 1 or 11  ')
            score += int(user_choice)
        elif card == 'J' or card == 'K' or card == 'Q':
            score += 10
        else: 
            score += card
    if score > 21:
        return 'You Bust'
    else: return score

def dealer_logic(dealers_cards):
    score = 0
    aces = 0
    
    # First pass: Calculate score without Aces
    for card in dealers_cards:
        if card in ['J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            aces += 1
        else:
            score += int(card)
    
    # Second pass: Handle Aces
    for _ in range(aces):
        if score + 11 <= 21:
            score += 11
        else:
            score += 1
    while score < 16:
        twist(dealers_cards)
        new_card = dealers_cards[-1]
        if new_card in ['J', 'Q', 'K']:
            score += 10
        elif new_card == 'A':
            if score + 11 <= 21:
                score += 11
            else:
                score += 1
        else:
            score += int(new_card)
    if score > 21:
        return 'Dealer Bust'
    else:
        return score
    
def winner(user_score,dealer_score):
    if user_score == 'You Bust':
        return 'You Lost'
    elif dealer_score == 'Dealer Bust':
        return 'You Win'
    elif user_score > dealer_score:
        return 'You WON'
    else: return 'You LOST'
    
users_cards = []
dealers_cards = []
start_playing = input('Do you want to play blackjack (y) for yes (n) for no  ')
i = 0
while start_playing == 'y':
    while i < 2:
        twist(users_cards)  
        i += 1
        twist(dealers_cards)    
    print(users_cards) 
    user_score = check_score(users_cards)
    print(f'your current score is {user_score}')
    print(f'dealer first card {dealers_cards}') 
    twist_or_stick = input('Do you want to stick or twist (s) for stick and (t) for twist ')
    if twist_or_stick == 't':
        twist(users_cards)
        print(users_cards)
    elif twist_or_stick == 's':
        print(users_cards)
        print(user_score)
        start_playing = 'n'

dealer_logic(dealers_cards)
print(dealers_cards)
print(dealer_logic(dealers_cards))
print(winner(check_score(users_cards),dealer_logic(dealers_cards)))




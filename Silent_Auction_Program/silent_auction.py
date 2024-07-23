import os 
# os.system('clear') 
print('Welcome to secret Auction')
bidder_and_bids = {}
continue_bidding = True
while continue_bidding == True:
    users_name = input('What is your name? ')
    users_bid = input('How Much Would You Like to Bid? ')
    bidder_and_bids[users_name] = int(users_bid)
    anymore_bidders = input('Anyone Else to bid (yes) or (no)? ')
    if anymore_bidders == 'yes':
        os.system('clear')
    else:
        highest_bidder = ''
        highest_bid = 0
        os.system('clear')
        for key in bidder_and_bids:
            if highest_bid <  bidder_and_bids[key]:
                highest_bid = bidder_and_bids[key]
                highest_bidder = key
        print('The Highest Bidder was '+ highest_bidder + ' with the bid of ' + str(highest_bid))
        continue_bidding = False


            
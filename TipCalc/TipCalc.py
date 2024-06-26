total_bill = float(input('What was the total bill?  $'))
tip_percent = int(input('What tip would you like to give 5, 10 ,15 or custom '))
split_bill = int(input('How many to split the bill?  '))
total_per_split = round(total_bill * (1+(float(tip_percent)/100)) / split_bill, 2)

print('each person should pay $' + str(total_per_split))
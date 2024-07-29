print('welcome to calculator ')
def calculate(number1,number2,operator):
    if operator == '+':
        cal_result = number1 + number2
        return cal_result
    elif operator == '-':
        cal_result = number1 - number2
        return cal_result
    elif operator == '/':
        cal_result = number1 / number2
        return cal_result
    elif operator == '*':
        cal_result = number1 * number2
        return cal_result
         
calculating = True

number_1 = float(input('Enter First Number. '))
operator = input('select operator +,-,/,* ')
number_2 = float(input('Enter Second Number. '))
calc_result = calculate(number_1,number_2,operator)
print(calc_result)

while calculating == True:
    
    continue_calc = input('Do you want to continue type (y) for yes and (n) for no. ')
    if continue_calc == 'n':
        calculating = False
    elif continue_calc == 'y':
        operator = input('select one of these +,-,/,* operators ')
        number_2 = float(input('Enter New Number. '))
        calc_result = calculate(calc_result,number_2,operator)
        print(calc_result)
    else: 
        print('Not a y or n ')
        break



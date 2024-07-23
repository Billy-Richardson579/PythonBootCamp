def encode(userMessage,shiftNumbers):
    encodedmessage= ''
    i = 0
    for letter in userMessage:
        letterIndex= letters.index(userMessage[i])
        cipher = (letterIndex + int(shiftNumbers))
        if cipher > 25:
            cipher -= 26
        elif cipher < 0:
            cipher += 26
        encodedmessage += letters[cipher]
        i += 1
    print(encodedmessage)

def decode(userMessage,shiftNumbers):
    decodedmessage= ''
    i = 0
    for letter in userMessage:
        letterIndex= letters.index(userMessage[i])
        cipher = (letterIndex - int(shiftNumbers))
        if cipher > 25:
            cipher -= 26
        elif cipher < 0:
            cipher += 26
        decodedmessage += letters[cipher]
        i += 1
    print(decodedmessage)

useAgain = 'y'

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while useAgain == 'y':
    encodeOrDecode = input('Welcome to Cipher would you like to (encode) or (decode) please type your answer  ')

    userMessage = input('Input your message  ')

    shiftNumbers = input('What is the shift amount  ')

# logic here
    if encodeOrDecode != 'encode' and encodeOrDecode != 'decode':
        print('not a method')
    elif encodeOrDecode == 'encode':
        encode(userMessage,shiftNumbers)
    else: decode(userMessage,shiftNumbers)
    useAgain = input('Would You Like To Continue type (y) for yes and (n) for no  ')











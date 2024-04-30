#import this

#input for twelve numbers
input1 = {}
i = 0

print('I will need 12 numbers')
while i < 12:
    try:
        input1['number'+str(i+1)] = int(input('Please enter a number: '))
        i += 1
    except ValueError: 
        print("that was not a valid number, please try again.")

#print (input1)

for i in range(0, len(input1), 3):
    try:
        print(input1['number'+str(i)])
    except:
        pass

def printSent(sent):
    punctuation = ['.', ',', '!', '?']
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in sent:
        if i in punctuation:
            print(i, end="")
            print(i, end="")
        elif i.isdigit():
            break
        elif i in vowels:
            continue
        else:
            print(i, end="")

printSent(input('Please enter a sentence: '))
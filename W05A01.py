#try except function (had to follow along and didn't finish)
def tryInput(question):
    output = input(question)

    return output

#take in name and major then output structured sentence
isPass = False

while(not (isPass)):
    try:
        name = input("What's your name: ")
        isPass = True
    except:
        print('That input was not correct, please try again.')
        isPass = False
        continue
    
    try:
        major = input ("\nWhat's your major: ")
        isPass = True
    except:
        print('That input was not correct, please try again.')
        isPass = False
        continue
    

print(f'\nHello, my name is {name} and I am a {major} student.\n')

print('''The major you have chosen
will not be difficult to complete.\n''')

print(f'Hey {name}\nFor the major {major} you must\nremember to pay your tuition.\n')

isPass = False

while(not (isPass)):
    try:
        name01 = input("What's your name: ")
        isPass = True
    except:
        print('That input was not correct, please try again.')
        isPass = False
        continue
    
    try:
        name02 = input("What's your second name: ")
        isPass = True
    except:
        print('That input was not correct, please try again.')
        isPass = False
        continue

    try:
        name03 = input("What's your third name: ")
        isPass = True
    except:
        print('That input was not correct, please try again.')
        isPass = False
        continue
    
List01 = []
List01.append(name01)
List01.append(name02)
List01.append(name03)

print(List01)

print()

list02 = []
dict01 = {}

for i in range(3):
    inUID = input("Please enter the student's UID: ")
    name04 = input("Please enter the student's first name: ")
    name05 = input("please enter the student's last name: ")
    major01 = input("Please enter the student's major: ")
    print()

    list02.append(inUID)
    list02.append(name04)
    list02.append(name05)
    list02.append(major01)

    dict01[list02[i*4]] = list02[(i*4+1):(i*4+4)]

print(dict01)

searchID = input('Enter the UID of the preffered student: ')
print()
print(f'I have found the student {dict01[searchID][0]} {dict01[searchID][1]} with the {searchID} in the major of {dict01[searchID][2]}')



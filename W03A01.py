import random

ints = {}
for i in range(10):
    varName = 'num' + str(i+1)
    ints[varName] = random.randint(-500, 500)

floats = {}
for i in range(10):
    varName = 'f' + str(i+1)
    floats[varName] = random.random() * random.randint(-500, 500)

strings = []
string1 = "Jimmy, is a strange child"
string2 = "Jimangthly, is cooler than Jimmy"
string3 = "Jomoly, is a very jolly fellow"
string4 = "Isaak, is very tired"
string5 = "Greta, is allergic to chocalate"
strings.append(string1)
strings.append(string2)
strings.append(string3)
strings.append(string4)
strings.append(string5)

ints['num10'] = "does this work?"
string1 = 1.0

passed = "Many years have passed"
born = "since I was born."

print (ints)
print (floats)
print (strings)

print(passed+" "+born)

myVar="utah"
myVarUpper = myVar.upper()
print(myVarUpper)

myName = "Jimangtholy"
bankAccount = 46789204

message = ("I am %s and my bank account has $%d in it." % (myName,bankAccount))
print(message)

prof = "Professor"
num = 14.32

print(f'My {prof} has ${num:0.2f} in his pocket.')

pie = 3.1415926

print("Pie has the value %6.5f in it."%(pie))

accountAmount = 845.65
accountNumber = "032410"

print("A bank account with the number %s has $%.2f in it"%(accountNumber,accountAmount))
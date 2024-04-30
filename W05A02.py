#ask for first name
inName = input("please enter a first name: ")

#store names in memory
nameList = ["Mark", "Frank", "Bill", "Tim", "Mary", "Kallie", "Sarah"]

#if name in memory print structured statement
if (inName in nameList):
    print(f"The name {inName} was found in index spot number {nameList.index(inName)}")
#if name not in memory print not found
else:
    print(f"The name {inName} was not found in memory")

#create for loop to go through names
for i in nameList:
    #print first name
    print(i)
    #create for loop to go through characters
    for o in i:
        #print char individually
        print(o)

thisIsDumb = []
for x in range(10):

    for y in range (10):
        thisIsDumb.append([x,y])

    print(thisIsDumb[0], thisIsDumb[1], thisIsDumb[2], thisIsDumb[3], thisIsDumb[4], thisIsDumb[5], thisIsDumb[6], thisIsDumb[7], thisIsDumb[8], thisIsDumb[9])
    thisIsDumb = []

print()

for x in range(10):

    for y in range (10):
        print ([x,y], end=" ")

    print()

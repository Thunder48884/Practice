#excercisesDictionary

diction = {}
diction[1]= 'Tom'
diction[2]= 'Carl'
diction[3]= 'Mark'
diction[5] = 'Tim'

print(diction.get(3))

print(len(diction), diction.keys(), diction.values())

diction.update({0:None})
print(diction)

separateList = [4,5,6,7]

for x in diction:
    diction[x] = separateList

print(diction)

diction[1]= [1,2,3,4]
diction[2]= [2,3,4,5]
diction[3]= [3,4,5,6]
diction[5] = [4,5,6,7]
diction[0]= [5,6,7,8]

print(diction)
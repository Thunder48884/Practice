exercisesList = [1,2,3,4]
exercisesList.append(5)
print(exercisesList)

del exercisesList[4]
print (exercisesList)

exercisesList.insert(2, 2.5)
print(exercisesList)

newList = [8,7,6,1.5]
exercisesList += newList
print(exercisesList)

exercisesList.sort(reverse=True)
print(exercisesList)
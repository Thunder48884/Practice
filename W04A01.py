#print Tuesday, Wednesday, Friday, and Sunday on separate lines
daysofweek=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(daysofweek[1],'\n',daysofweek[2],'\n',daysofweek[4],'\n', daysofweek[6],'\n')

#map 5ids to 5mails
idList = {123456 : 'u123456@utah.edu', 234567 : 'u234567@utah.edu', 345678 : 'u345678@utah.edu', 456789 : 'u456789@utah.edu', 567891 : 'u567891@utah.edu'}
print(idList[123456],idList[567891])

#map 5ids to 5mails now with strings
idList2 = {'u123456' : 'u123456@utah.edu', 'u234567' : 'u234567@utah.edu', 'u345678' : 'u345678@utah.edu', 'u456789' : 'u456789@utah.edu', 'u567891' : 'u567891@utah.edu'}
print (idList2['u123456'],idList2['u234567'], idList2['u345678'], idList2['u456789'], idList2['u567891'])

#get statement with default
getList = {1:'one',
           2:'two',
           3:'three',
           4:'four',
           5:'five',
           6:'six'}
print(getList.get(7, 'This is a default value'))

#get an actual value
print(getList.get(4))

#print stored value
var1 = getList.get(1)
print(var1)

#use update
getList1 = {1:'one',
           2:'two',
           3:'three'}
getList2 = {3:'three',
           4:'four',
           5:'five'}
getList2.update(getList1)
print(getList2)
getList1.update(getList2)
print(getList1)

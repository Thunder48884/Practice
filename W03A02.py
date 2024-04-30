str1="Your bank account balance is $148.68"
str2=str1[30:36]
print(float(str2) + 100)

str3 = "I have $15.12 in my wallet."
splice2 = float(str3[8:13])
print ("%.2f"%(splice2 + 2.23))

studentAges=[18,20,21,19,18,30]
studentAges[3] = 29

print (studentAges)

animals=['dog','cat','shark','fish']
animals[2] = "horse"

splice3 = studentAges[1:4]
print(splice3)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
splice4 = months[8:]

print(splice4)
print(months[1:4])

List1 = []
for i in months:
    List1.append(i)

print(List1)

list2 = [5,6,8,9]
list2.insert(2,7)
print(list2)

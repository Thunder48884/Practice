i=0
while i < 10:
    print("Loop until i is 10, i=", i)
    i+=1


while i >= 0:
    print("Loop until i is 10, i=", i)
    i-=1

emptyL = []
for x in range(5):
    emptyL.append(x+1)
print(emptyL)

x=0
emptyL2 = []
while(x < 5):
    emptyL2.append(x+1)
    x+=1
print(emptyL2)

Pass = False
while(not Pass):
    numbaaa = input("Please enter a number (1-10): ")

    if(numbaaa.isdigit() and int(numbaaa) == 7):
        print("Yay! You guessed correctly, you may pass.")
        Pass = True
    else:
        print("That was not the right number, please try again")

sentence01 = input("Please enter a sentence with 5 words: ")
sentence02 = ""
if (len(sentence01.split(" ")) == 5):
    i = len(sentence01) - 1
    while i >= 0:
        #print(sentence01[i])
        sentence02+=(sentence01[i])
        i-=1
else:
    print ("Your sentence was not 5 words long.")

print(sentence01, '\n', sentence02)
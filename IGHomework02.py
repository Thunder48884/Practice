"""
Phase 1
In the first phase your program will ask a user to enter three credit card numbers to be
validated. You will need to store these three credit card numbers in a list. Each number should
be different so don’t input the same three credit card numbers in a row. You will need to use a
loop which will keep looping in this phase until three credit card numbers have been entered.
"""
def Phase1(pf):
    Pass = False
    Cr1 = None
    Cr2 = None
    Cr3 = None

    Numbers = []
    while(not Pass):
        

        try:
            Cr1 = input("please enter the first credit card Number: ")
        except:
            pass
        try:
            Cr2 = input("please enter the second credit card Number: ")
        except:
            pass
        try:
            Cr3 = input("please enter the third credit card Number: ")
        except:
            pass

        Numbers.append(Cr1)
        Numbers.append(Cr2)
        Numbers.append(Cr3)


        Numbers, Pass = verify(Numbers)
        #Pass = True
        
    if (Numbers and Pass):
        return Phase2(Numbers, pf)
    else:
        return Numbers, False	

#This function put me through my paces
#first check if the list passed in is empty
#instatiate a list for unique values and duplicate values
#iterate through passed list and check if it is a duplicate or matches a prior duplicate
#pass all unique values to be returned (if there are values to return)
def verify(Numbers):

    if(Numbers):
        badList=[]
        goodList=[]
        for x in range(len(Numbers)):
            if (x>=len(Numbers)):
                #print('continue')
                continue
            if ((Numbers[x] in Numbers[x+1:]) or (Numbers[x] in badList)):
                badList.append(Numbers[x])
            else:
                goodList.append(Numbers[x])
                
            # y = x+1
            # if (y>=len(Numbers)):
            #     continue
            # for y in range(len(Numbers)-1):
            #     if (Numbers[x] == Numbers[y]):
            #         print(f'these numbers are equal {Numbers[x]} | {Numbers[y]}')
            #         Numbers.pop(x)
            #         Numbers.pop(y)
            #         print("You've entered a duplicate and both have been removed")
            #         break
    if (badList):
        print("A duplicate has been found and both have been removed")
                
    if (goodList):
        return goodList, True
    else:
        print("No card numbers left!")
        return goodList, False

"""
Phase 2
Then in phase two you will need to use a for loop and go through the list of credit card numbers
you collected from Phase 1 and check if each number is valid.
To check if a credit card number is valid you need to use the following rules:
1. The number will be 16 digits long.
2. The number must all be digits with no characters.
3. The number will start with a 4,5 or 6.
(Hint: Look in Appendix A in your book for functions that will help you to check these rules.
Also, you can look at this website for example code of how to loop through each character of a
string:
https://www.geeksforgeeks.org/iterate-over-characters-of-a-string-in-python/)
If a credit card number is not valid it should be removed from the list. A message should be
printed to the screen that states that a number was not valid and was removed.
When this phase is complete you should have a list of valid credit cards to send to Phase 3
"""
def Phase2(Numbers, pf):
    #print(Numbers)
    toRemove = []
    if((Numbers and (pf == True))):
        for i in Numbers:
            # if(len(i) != 16):
            #     print('16 is cause')
            # if (not i.isdigit()):
            #     print('isdigit is cause')
            #if ((int(i[0]) in [4,5,6])):
                #print((int(i[0]) not in [4,5,6]))

            if ((len(i) == 16) and ((i.isdigit()) and (int(i[0]) in [4,5,6]))):
                continue
            else:
                print(f"{i} is an invalid credit number and has been removed")
                toRemove.append(i)
                continue

    else:
        print("No card numbers left!")
        return Numbers, False
    
    for y in toRemove:
        Numbers.remove(str(y))

    return Phase3(Numbers, True)
"""
Phase 3
In this last phase you will go through the list of credit cards you checked in Phase 2 and print
each of them out in groups of four numbers using dashes.
For an example:
If the credit card input is 4234567890909999 then you should print it to the screen like this
4234-5678-9090-9999. (Notice the dashes)
"""

def Phase3(Numbers,pf):
    if (Numbers and (pf == True)):
        for I in Numbers:
            print(f"Credit number: {I[0:4]}-{I[4:8]}-{I[8:12]}-{I[12:16]} is a valid credit number")
        return Numbers, True
    else:
        print("No card numbers left!")
        return Numbers, False	
    
"""
Additional Requirements
Make sure that you use try except in your code to help catch errors.
Each phase of your program should occur inside its own function. You should name these
functions phase1(), phase2() and phase3(). You will need to figure out how to pass the list of
credit cards from one phase to another.
Your solution should be just one py file. Turn in that py file for grading when finished.
"""
homeworkSucceeded = False
while(not(homeworkSucceeded)):
    Numbers, homeworkSucceeded = Phase1(True)
    exitString = input("Would you like to continue or exit? (ENTR/exit): ")
    if exitString == 'exit':
        break
    if exitString == '':
        homeworkSucceeded = False
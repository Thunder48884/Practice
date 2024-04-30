"""
Exercise 1
Create three variables with the values 10,15 and 20. Print them to the screen so the output
looks like this:
Var1=10
Var2=15
Var3=20
"""

#store values
Var1=10
Var2=15
Var3=20
#print them
print(f"Ex 1\nVar1={Var1}\nVar2={Var2}\nVar3={Var3}")

"""
Exercise 2
Write code that will calculate the average of the following numbers 3,7,8,2,10. Print the
average to the screen.
"""

#store values (doesn't say that you can't store them in a list)
numbers = [3,7,8,2,10]
# make a function for average cause I think I'll need it and I feel like it
def average(x):
    z = 0
    for y in x:
        #add up all given numbers in z
        z += y
    #divide z by the # of #s given
    z = z/len(x)
    #return for print
    return z
#print
print("Ex 2")
print(average(numbers))

"""
Exercise 3
Start with the variable x=3. Then add the following numbers to x: 34,22,65,78,99 using the +=
operator. Then subtract the following numbers from x: 44,33,22,11 using the -= operator.
Finally multiply the following numbers by x: 5,4,3,2,1 using the *= operator.
"""

#store values
x = 3
lista = [34,22,65,78,99]
lists = [44,33,22,11]
listm = [5,4,3,2,1]

#+= the first list
for a in lista:
    x+=a
    #print(x)

#-= the second
for s in lists:
    x-=s
    #print(x)

#*= the third
for m in listm:
    x*=m
    #print(x)

print("Ex 3")
print(x)

"""
Exercise 4
Calculate the remainder of 100/23 and print it to the screen. (Hint: use modulus)
"""
print("Ex 4")
#100 module 23
print(100%23)

"""
Exercise 5
Create the following variables:
name=”Alice Vahn”
investment=10000
interestRate=0.0532.
Then print out the following to the screen using these variables in your print statement:
Alice Vahn has invested $10,000 into a savings account that has a 5.32% interest rate.
"""
#store values
name= "Alice Vahn"
investment=10000
interestRate=0.0532
sign = "%"

print("Ex 5")
#print formatted string
print(f"{name} has invested ${investment:,d} into a savings account that has a %.2f%s interest rate." % (interestRate*100, sign))

"""
Exercise 6
Create a variable retirementAge=”67”. Create another variable x=3. Add the retirementAge
variable to the variable x and print out the answer to the addition (should be 70).
"""

#as retirementAge is a string you will need to cast it as and int in order to add it to x
retirementAge="67"
x=3
print("Ex 6")
print(int(retirementAge)+x)

"""
Exercise 7
Create a variable like this:
grades=[90,89,93,75]
Using this list variable calculate the average of all the grades and print it to the screen.
"""

print("Ex 7")
#use average function from ex 2
grades=[90,89,93,75]
print(average(grades))

"""
Exercise 8
Create an empty dictionary named: starwars={}
Add the following key value pairs to the starwars dictionary:
U123456 Han Solo
U987654 Luke Skywalker
U876543 Darth Vader
U321455 Ben Kenobi
Once the characters have all been added, print the value of each one of them by key name
"""

print("Ex 8")
starwars={}
starwars["U123456"] = "Han Solo"
starwars["U987654"] = "Luke Skywalker"
starwars["U876543"] = "Darth Vader"
starwars["U321455"] = "Ben Kenobi"
print(starwars["U123456"]+'\n'+starwars["U987654"]+'\n'+starwars["U876543"]+'\n'+starwars["U321455"])
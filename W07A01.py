def helloWorld():
    for i in range(10):
        print('helloWorld')

def myFirstFunction(num):
    x = num
    x -= 4
    return x

def functionUno():
    global f
    f = 99

def functionTwo():
    print(f)

def sum(list):
    x = 0
    for i in list:
        x += i
    return x

f = 0
print(myFirstFunction(10))
helloWorld()
functionUno()
functionTwo()

listofnum = [5.00,6.5,7.25,3.15]
print(sum(listofnum))
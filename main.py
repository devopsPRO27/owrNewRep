'''import math


def calcHekef(*radius):

    return radius *2*math.pi

print(calcHekef(8.9))'''
'''def add(x=0,y=0):
    return x+y
def sub(x=0,y=0):
    return x-y
def mul(x=0,y=0):
    return x*y
def div(x=0,y=0):
    if y!=0 :
        return x/y
    return (f'y cant be zero !={y}')

x=float(input('please enter x : '))
y=float(input('please enter the value of y '))
print(add(x,y))
print(sub(x,y))
print(mul(x,y))
print(div(x,y))'''
def getInRange(min,max):
    if max<=min:
        return "wrong input"
    while True:
        in2=int(input('enter a number'))
        if  min<= in2 <=max :
            return in2
x=getInRange(10,100)
print(x)'''
'''def myMin(x,y,z):
    return max(x,y,z)
print(myMin(y,x,z))







#day - 1   

                                                                        
import numbers
from re import A


print("five is greater than two")
if 5>2:
    print("hiiiii")
    x=5
    y=52
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    #who invented python
    
    x=9
    y="shantanu"
    print(type(x))
    print(type(y))
    x=4.5
    print (type(x))
    x=4
    y=5
    print(bool(x+y))
    x=""
    print(bool(x))
    shantanu=50
    print(shantanu)
    my_var=40
    print(my_var)
    x="30","40","50"
    print(x)
    x=y=z="apple"
    print(x)
    fruits=["apple","bnana","cherry"]
    x,y,z=fruits
    x=y=z=fruits
    print(type(x))
    fruits=[2,4,7,8,34,50]
    print(type(fruits))
    print(fruits)
    x="this is python"
    print(x)
    x="python"
    y="is"
    z="good"
    print(x+y+z)
    print(type(x+y+z))
    x="kumar"
    y="shantanu"
    print(x+y)
x="good"

def my_func():
    print("python is "+ x)
my_func()    


def my_func():
    global x
    x="good"
my_func()
print("python is " + x)

x=1j
print(type(x))



#list 

my_list=["apple","banana"]
print(type(my_list)) 

print(my_list)

print(len(my_list))

my_list=["apple","banana","1","3","5"]
print(type(my_list))
my_list=["apple","banana","cherry"]
print(my_list[-1])

my_list=["apple","banana","cherry","dfgd","xdfgxdf","dfg"]
print(my_list[-4:])

my_list=["apple","banana","cherry","blueberry","pomegranate","orange"]
my_list[1]="mango"
print(my_list)




# day - 2




my_list=["apple","banana","cherry","blueberry","pomegranate","orange"]
my_list.append("date")
print(my_list)

my_list.insert(1, "coconut")
print(my_list)


my_list=["apple","banana","cherry","blueberry","pomegranate","orange"]
removed_item = my_list.pop()
my_list.insert(1, "coconut")
my_list.append("date")
print(my_list)

my_list=[1,2,3]
new_items=[4,5,6]

my_list[1:1]=new_items
print(my_list)

initial=[1,3,4]
new_items=2

combined_list=[*initial, new_items, *[5,6], 'number']
print(combined_list)

list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)


#remove 

list1=[1,2,3,"apple",4,5,6]
# list1.remove("apple")
list1.pop()
print(list1)

list1=[1,2,3,4,5,6]
list2=[7,8,9]
list1.append("apple")
list1.insert(3, "banana")
list1.remove("banana")
list1.pop()
print(list1)
print(list1.index(2))


list1=[1,2,3,3,3,3,3,3,4,5,6]
count_of_three=list1.count(3)
print(count_of_three)


list1=[]
list1.append(1)
list1.insert(2, "apple")
list1[0]="eat"
print(list1)


#looplists

list1=[1,2,3,4,4,4,4,5,6]
for x in list1:
    print(x)


#sort

list=[4,9,26,26,6,6,6,6,6,262,6,262,2,821,54,71,50,29,2,614,62]

list.sort(reverse=False)
print(list)

list=[4,9,26,26,6,6,6,6,6,262,6,262,2,821,54,71,50,29,2,614,62]

list.sort(reverse=True)
print(list)

text=" hello python "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("python","world"))
print(text.split())


x=18
y="Shantanu"
print(f"my name is {y} and i am {x} years old".upper())

x=5
x+=3
print(x)



x=10
y=7


print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

x=5
print(x>3 and x<10)
print(x>3 or x<10)
print (not(x<10))

x=8
y=x
z=10
print(y)
print(z is not y)

a=(1,2,3,4,5)
for x in a:
    print(x)


b={54,34,55,55,55}
print(b)

b.add(34)
print(b)

b.remove(55)
print(b)

for b in b:
    print(b)

student={"name":"Alice","age":20,"grade":"A"}
print(student)

student["age"]=20
student["city"]="delhi"
print(student)


print(student['name'])
print(student["city"])

# student.pop("age")
# del student["city"]
# print(student)


for key,value in student.items():
    print(key,":",value)

# if ....else

age=int(input("please enter your age ....".capitalize()))

if age>=18:
    print("you are able to vote")

else:
    print("you are a minor")    


numbers=int(input("enter a number...".capitalize()))

if numbers > 20:
        print("number is Greater than 20")
else:
        print("number is Less than or equal to 20")


# day--3


for i in range(5):
    number = int(input("Enter a number: "))
    
    if number > 0:
        print("Positive number!")
    else:
        print("Negative or zero!")


for i in range(80):
    age = int(input("enter your age"))

    if age>=18:
        print("you are able to vote.".capitalize())

    elif age>100:
        print("please enter your real age ".upper())

    else:
        print("yoou are not able to vote.".capitalize())    


x=int(input("please enter a number"))

if x>10:
    print("x is grater than 10".capitalize())

if x>20:
    print("x is also greater than 20".capitalize())

elif 20>x>10:
    print("x is greater than 10 but not greater than 20.".capitalize())

else:
    print("x is not grater than 10 and 20".capitalize())


for i in range(100000):
    x=int(input("entre a number"))

if x % 2 == 0:
    print("x is a even number")

else:
    print("x is a odd number")



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"Greatest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"Greatest number is: {num2}")
else:
    print(f"Greatest number is: {num3}")

# loop

word="python"

for x in word:
    print(x)

for i in range(100):
    print(i)

# range(start,stop.step)

for i in range(2,30,3):
    print(i)


for i in range(1,4):

    for j in range(1,4):
        
        print(f"i={i},j={j}")

for i in range(1,4):
    print(f"i={i}")


for i in range(1,6):
    if i == 4:
        break
    print(i)

for i in range(1,6):
    if i == 3:
        continue
    print(i)


for i in range(1,4):
    print(i)
else:
    print("loop is finished")



for i in range(1,21):
    print(i)


for i in range(2,31,2):
    print(i)



x=["red","blue","black"]
for i in x:
    print(i)




for i in range(1,10):
    if i == 5:
        continue
    print(i)

def greet():
    print("hello python!")

greet()


def greet(name):
    print(f"hello,{name}, the builder!")

greet("Alice")
greet("bob")


def add(a,b):
    return a+b #add

result=add(121,345)

print(result)

def add(a,b):
    return a-b #substract

result=add(121,345)

print(result)

def add(a,b):
    return a*b #multiply

result=add(121,345)

print(result)

def add(a,b):
    return a/b #divide

result=add(121,345)

print(result)


def greet(name="Student"):
    print(f"Hello,{name}!")

greet("Alice")
greet()



x=10 #global variable

def my_func():
    
    y=5 #local variable

    
    print(x,y)

my_func()

print(x)


def greet(name="hello"):
    print(f"{name}!")

greet()


def add(a,b):
    return a+b

result=add(54,65)
print(result)


def greet(name="person"):
    print(f"Hello,{name}!")

greet("shantanu")



class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

    def drive(self):
        print(f'{self.color} {self.brand} is driving 🚗')


car1=Car("BMW" , "Black")
car2=Car("PORSHE" , "YELLOW")


car1.drive()
car2.drive()


# day-4--------


import array

numbers=array.array('i',[1,2,3,4,5])
print(numbers)

from numpy import random

x=random.randint(10)

print(x)

x=random.rand(5)

print(x)

[54]
[1,2,3,4,5]
[[1,2,3],
 [4,5,6]]

from numpy import random

x=random.randint(100,size=(5))

print(x)

x=random.randint(100,size=(3,5))

print(x)

x=random.randint(100,size=(2,3,4,5))

print(x)

x=random.choice([4,5,6] , size=(10))
print(x)

import pandas as pd


data=[10,20,30,40,50]
shantanu=pd.Series(data)

print(shantanu)

data={
    "Name":["Alice","Bob","charlie","David"],
    "Age":[24,27,22,32],
    "City":["Delhi","Mumbai","Chennai","Kolkata"],
}

df=pd.DataFrame(data)

print(df)

import numpy as np

arr=np.array([1,2,3,4,5])

s=pd.Series(arr)

print(s)




data={"math":90,"science":85,"english":78}

s=pd.Series(data)

print(s)

df = pd.read_csv("Data_Salaries.csv")
print(df.head(30))


#use of nested for loop 
for i in range(1,6):      #outer loop = row
    for j in range(1,6):  #inner loop = column
        print(j, end="  ")
    print()


#Function generation

import time
def msg():   #called function
    time.sleep(2)
    print("Hello World")

msg()  #calling function
print("First time call completed")
msg()  #calling function
print("Second time call completed")
msg()  #calling function
print("Third time call completed")


def arithmetic():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Addition: ", a+b)
    print("Subtraction: ",a-b)
    print("Division: ",a/b)
    print("Multiplication: ",a*b)
    print("Modulus: ",a%b)
arithmetic()


def login():
    username = input("Enter your username")
    password = input("Enter your Password")
    if username == password:
        print("login successfull")
    else:
        print("You have entered wrong credentials")
login()


def info(first_name, last_name):
    print("First Name = ",first_name)
    print("Last Name = ",last_name)
info("Aishwarya","Nandanwar")


def add(num):
    print("Addition of two numbers is", num+num)
add(20)


#positional argument passing in correct order
def add(num1,num2):
    return num1+num2
Sum = add(5,6)
print("Sum:", Sum)


def chk_even_odd():
    num = int(input("Enter a number: "))
    if num%2==0:
         print(num, "is an even number")
    else:
        print(num, "is an odd number")
chk_even_odd()


def func(fname):
    print("Hi",fname)
func(fname="Aishwarya")


def city(city = "Nagpur"):
    print("I live in", city)
city("Goa")
city("Mumbai")
city()


#returning multiple values at a time
def add_product(a,b):
    add = a+b
    product = a*b
    return add, product
sum, mul = add_product(50,2)
print("The addition is", sum)
print("The multiplication is", mul)


def loop(name):
    for i in name:
        print(i)
list = ['kitkat', '5star', 'Cardbury', 'Silk']
loop(list)


def func(name):
    j = 0
    for i in name:
        if i=='h':
            print('The character present at index no.',j,'value is:',name)
            break
        j = j+1
name = input('Enter the name')
func(name)


def fact(n):
    if n==0:
        return  1
    else:
        return n*fact(n-1)
print("Factorial of 0 is:", fact(0))
print("Factorial of 5 is:", fact(5))


s = lambda n:n*n
print("The square of 5 is:", s(5))
print("The square of 6 is:", s(6))


#nested function
def myname():
    print("My name is Aishwarya")
    def myrollno():
        print("My roll no is 02")
    myrollno()
myname()


def welcome(fname,lname):
    print("First Name = ",fname)
    print("Last Name = ",lname)


def square(n):
    print(n*n)
pi = 3.14
def login(username,password):
    if username == password:
        print("You have login successfully")
    else:
        print("You have entered wrong credentials")

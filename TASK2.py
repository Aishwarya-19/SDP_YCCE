#WAP to calculate sum of natural number from 1 to 10
num = 0
sum = 0
for num in range (1,11):
    sum = sum + num

print("The sum of Natural no. form 1 to 10 is ", sum)


#WAP to calculate factorial of any number 
i = 1
fact = 1
n = int(input('Enter a number'))
if n<0:
    print("Factorial doesn't exist for negative number")
elif n==0 or n==1:
    print("Factorial of", n ,'is 1')
else:
    for i in range(1,n+1): 
        fact = fact*i  
    print('Factorial of', n, 'is', fact)


#WAP to calculate fibonacci series 0 1 1 2 3 5 8 13
len = int(input("Enter the length of the series : "))
series = 0
n1 = 0
n2 = 1

print(n1,n2,end=" ")

for len in range (2,len+1):
    series = n1+n2
    print(series,end=" ")
    n1 = n2
    n2 = series



#WAP to calculate LCM, HCF, GCD

 
#WAP to check leap year
year = int(input("Enter the Year : "))

if(year%400 == 0):
    print("Its a Leap Year")
elif(year%100 == 0):
    print("Its not a Leap Year")
elif(year%4 == 0):
    print("Its a Leap Year")
else:
    print("Its not a Leap Year")


#WAP to check armstong number
number = int(input("Enter a Number : "))
num = number
sum = 0
while( num>0 ):
    rem = num%10
    num = num//10
    cube = rem*rem*rem
    sum += cube 
if(sum == number):
    print(number,": it is a Armstrong number ")
else:
    print(number,": it is not an Armstrong number")


#WAP to find palindrome number
number = int(input("Enter a No.: "))
num = number
rev_num=0
while(num>0):
    rem = num%10
    num = num//10
    rev_num = (rev_num * 10) + rem
if(number==rev_num):
    print(number,": it is a Palindrome Number")
else:
    print(number,": it is not a Palindrome Number")


#WAP Enter five integer number and find max number (using simple if)
n1 = int(input("Enter No.1:"))
n2 = int(input("Enter No.2:"))
n3 = int(input("Enter No.3:"))
n4 = int(input("Enter No.4:"))
n5 = int(input("Enter No.5:"))

if ((n1>n2) and (n1>n3) and (n1>n4) and (n1>n5)):
    largest = n1
elif ((n2>n1) and (n2>n3) and (n2>n4) and (n2>n5)):
    largest = n2
elif ((n3>n1) and (n3>n2) and (n3>n4) and (n3>n5)):
    largest = n3
elif ((n4>n1) and (n4>n2) and (n4>n3) and (n4>n5)):
    largest = n4
else:
    largest = n5

print("Maximum number is:", largest)

 
#WAP Enter five integer number and find smallest number (using simple if)
n1 = int(input("Enter No.1:"))
n2 = int(input("Enter No.2:"))
n3 = int(input("Enter No.3:"))
n4 = int(input("Enter No.4:"))
n5 = int(input("Enter No.5:"))

if ((n1<n2) and (n1<n3) and (n1<n4) and (n1<n5)):
    Smallest = n1
elif ((n2<n1) and (n2<n3) and (n2<n4) and (n2<n5)):
    Smallest = n2
elif ((n3<n1) and (n3<n2) and (n3<n4) and (n3<n5)):
    Smallest = n3
elif ((n4<n1) and (n4<n2) and (n4<n3) and (n4<n5)):
    Smallest = n4
else:
    Smallest = n5

print("Minimum number is:", Smallest)


#WAP to display exact pattern as below using zip() 
'''
1   5
2   4
3   3
4   2
5   1
'''
num = [ "1", "2", "3", "4", "5" ]
reverse_num = ["5","4","3","2","1"]
for n, r_n in zip(num,reverse_num):
    print ( "%s   %s" %(n, r_n))


#WAP  to convert a alphabet into its ASCII equivalent
char = (input("Enter a character: "))
print("The ASCII value of", char ,"is", ord(char))
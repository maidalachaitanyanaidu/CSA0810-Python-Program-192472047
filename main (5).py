 # 1)Write a program to find the sum of digits of a number.
n=1234
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
print('1)',s)  
# 2) Write a program to check if a given string is a palindrome.
s='madam'
if s==s[::-1]:
    print('2)',s,'is a palindrome')
else:
        print('2)',s,'is not a palindrome')
# 3) Write a program to generate Fibonacci series up to n terms.
f,s=0,1
p=10
print('3)')
for i in range(p):
    print(f,end=' ')
    n=f+s
    f=s 
    s=n 
print()    
# 4)    Write a program to count the occurrences of a character in a string.
s='madam'
a=s.count('m')
print('4)',a)
# 5) Write a program to convert Celsius to Fahrenheit.
c=25
f=(9/5)*c+32
print('5)',f)
# 5)Write a program to calculate the simple interest given principal, rate, and time.
p,r,t=10000,2,2
f=(p*r*t)/100
print('5)',f)
# 6)Write a program to find the maximum of three numbers using if-else.
a,b,c=2,3,4
if a>b and a>c:
    print('5)',a,'is greatest')
elif b>c:
    print('5)',b,'is greatest')
else:
    print('5)',c,'is greatest')
# 7) Write a program to print all even numbers between 1 and 50 using a loop.
print('7)')
for i in range(0,50,2):
    print(i,end=' ')
print()    
# 8)Write a program to check whether a given year is a leap year.
n=2024
if n%4==0:
    print('8)',n,'is leap year')
else:
     print('8)',n,'is not leap year')
# 9)     Write a program to print the multiplication table of a given number.
n=6
print('9)')
for i in range(1,11):
    c=n*i 
    print(n,'*',i,'=',c)
# 10) Write a program to calculate the sum of all numbers in a list.
a=[1,2,3,4,5,6,7,8,9,10]
print('10)',sum(a))
    


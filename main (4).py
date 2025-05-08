# 1) Write a program to add two numbers.
a,b=2,3
print('1)',a+b)
# 2) Write a program to swap two variables without using a third variable.
a,b=4,9
a,b=b,a
print('2)',a,b)
# 3) Write a program to calculate the area of a circle given its radius.
r=5
a=3.14*r*r
print('3)',a)
# 4) Write a program to find the largest of three numbers.
a,b,c=2,3,4
if a>b and a>c:
    print('4)',a,'is greatest')
elif b>c:
    print('4)',b,'is greatest')
else:
    print('4)',c,'is greatest')
# 5) Write a program to check if a number is even or odd.
n=5
if n%2==0:
    print('5)',n,'is even')
else:
    print('5)',n,'is odd')
# 6) Write a program to find the factorial of a given number.
n=5
f=1
for i in range(1,n+1):
    f*=i 
print('6)',f) 
# 7) Write a program to reverse a given number.
n=1234
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
print('7)',s)  
# 8) Write a program to check if a given number is prime.
n=7
c=0
for i in range(2,n):
    if n%i==0:
        c+=1
        break 
if c==0:
    print('8)',n,'is prime')
else:
     print('8)',n,'is not prime')
# 9) Write a program to find the sum of digits of a number.
n=1234
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
print('9)',s)  
# 10) Write a program to check if a given string is a palindrome.
s='madam'
if s==s[::-1]:
    print('10)',s,'is a palindrome')
else:
        print('10)',s,'is not a palindrome')
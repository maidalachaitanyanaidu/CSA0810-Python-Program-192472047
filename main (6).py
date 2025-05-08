 # 1)Write a program to check if a number is an Armstrong number.
n=153
t=n
s=0
while n>0:
    r=n%10
    s=s+r*r*r
    n=n//10
if t==s:
    print('1)',t,'is a armstrong number')
else:
        print('1)',t,'is not a armstrong number')
# 2)Write a program to find the greatest common divisor (GCD) of two numbers.
a,b=12,18
while b!=0:
    a,b=b,a%b
print('2)',a)    
# 3) Write a program to check if a number is a perfect number.
n,s=6,0
for i in range(1,n):
    if n%i==0:
        s+=i
if n==s:
    print('3)',n,'is a perfect number')
else:
    print('3)',n,'is not a perfect number')
# 4)    Write a program to find the sum of the first n natural numbers.
n,s=5,0
for i in range(1,n+1):
    s+=i
print('4)',s)   
# 5) Write a program to generate prime numbers between 1 and 100.
a,b=1,100
print('5)')
for i in range(a,b):
    c=0
    for j in range(2,i):
     if i%j==0:
        c+=1
        break 
    if c==0:
         print(i,end=' ')
print()        
#6)Write a program to print a right-angled triangle pattern using stars (*).
n=5
print('6)')
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()
# 7)Write a program to reverse a string without using built-in functions.
s='headshot'
l=len(s)-1
i=l
r=''
while i>=0:
    r+=s[i]
    i-=1
print('7)',r)  
# 8) Write a program to check if a number is a palindrome.
n=153
t=n
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if t==s:
    print('1)',t,'is a palindrome number')
else:
        print('1)',t,'is not a palindrome number')
# 9)Write a program to print numbers in ascending and descending order using a loop.
print('9)')
for i in range(1,10):
    print(i,end=' ')
print()    
for j in range(10,0):
    print(j,end-' ')
print()
# 10) Write a program to calculate the sum of squares of the first n natural numbers.
n=3
p=0
for i in range(1,n+1):
    p=p+i*i 
print('10)',p)     
   










    
        
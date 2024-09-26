"""
print('Hello world')
"""
from cProfile import label
from enum import nonmember, pickle_by_enum_name
from ftplib import error_temp
from idlelib.outwin import file_line_progs
from idlelib.pyparse import trans
from idlelib.pyshell import restart_line, use_subprocess
from itertools import count
from logging import exception, lastResort
from operator import index
from os.path import split
from sys import audit
from time import process_time
from tkinter.font import names
from tokenize import endpats
from turtledemo.sorting_animate import enable_keys
from types import new_class
from xmlrpc.client import boolean
from zoneinfo import reset_tzpath

'''
x=10
y=20
sum=x+y
mul=x*y
div=x/y
sub=x-y
mod=x%y
dis=sum-sum*div
print(sum)
print(mod)
print(div)
print(sub)
print(mod)
print(dis)
'''
'''
def multisum(num1,num2):
    product= num1*num2
    if product<=1000:
        return product
    else:
        return num1+num2;
res=multisum(30,40)
print(res)
res2=multisum(20,30)
print(res2)
'''
'''
prev_num=0
for i in range(1,10):
    sum=prev_num+i
    print(f'Current Number {i} + previous number {prev_num} = {sum}')
    prev_num=i
'''
'''
user_string=input('Please tell me the any word then i will print even number:')
print(user_string)
size=len(user_string)
print(size)
for i in range(0,size-1,2):
    print(i,user_string[i])

'''
""""
def remove_char(word,n):
    print(word)
    x= word[n:]
    return x

res1=remove_char('tanmoy',4)
print(res1)
"""
"""
def first_last_list(numberlist):

    firstnum=numberlist[0]
    lastnum=numberlist[-1]
    if firstnum==lastnum:
        return True
    else:
        return False

res1=first_last_list([10,20,30,10])
print(res1)
res2=first_last_list([20,30,40])
print(res2)
"""
"""
num_list = [10, 20, 33, 46, 55]
print("Given list:", num_list)
print('Divisible by 5:')
for num in num_list:
    if num % 5 == 0:
        print(num)
"""
"""
sentence='tanu Loves bijo.Bijo loves tanu.'
res=sentence.count('tanu')
print(res)
"""
"""
def count_emma(statement):
    print(statement)
    count=0;
    for i in range(len(statement)-1):
        count+=statement[i:i+4]=='Emma'
    return count

count=count_emma("Emma is good developer. Emma is a writer")
print(count)

"""
"""
for i in range(5):
    for j in range(i):
        print(i ,end=" ")

    print("\n")
"""
"""
def paindrme_num(number):
    orginal_num=number
    reverse_num=0
    while number>0:
        reminder=number%10
        reverse_num=(reverse_num*10)+reminder
        number=number//10

    if orginal_num==reverse_num:
       return 'Palindrm'
    else:
        return 'Not Palindrm'
res=paindrme_num(151)
print(res)
"""
"""
number=151;
res=number%10
print(res)
res2=res//10
print(res2)
"""
"""
def marge_list(list1,list2):
    new_list=[]
    for num in list1:
        if num%2!=0:
             new_list.append(num)

    for num in list2:
        if num%2==0:
            new_list.append(num)
    return new_list

list1=[10,11,12,14,13,17,17]
list2=[21,22,23,34,32,31,23,43]
res=marge_list(list1,list2)
print(res)
"""
"""
number=54638
print(number)
while number>0:
    digit=number%10

    number=number//10

    print(digit ,end="")
"""
"""
x=10
y=10
z=15
print(x is y)
print(id(x))
print(id(y))
print(id(10))
print(id(z))
print(id(15))
print(id(x)==id(10))
"""
"""
income=45000
tax_payble=0
print('Given Income',income)
if income<=10000:
    tax_payble=0
elif income<=20000:
    x=income-10000
    tax_payble=x*10/100
else:
    tax_payble=0
    tax_payble=10000*10/100
    tax_payble=tax_payble+(income-20000)*20/100
print('Total tax payble',tax_payble)
"""
"""
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print('\t \t')
"""

"""
for i in range(6,0,-1):

    for j in range(0,i-1):
        print('*',end='')
    print('')
"""
"""
def exponent(base,exp):
    num=exp
    result=1
    while num>0:
        result=result*base
        num=num-1
    print(result)
exponent(5,4)
"""
"""
a=int(input('Enter a number please'))
b=int(input('Enter a second number please'))
c=a*b
print(c)
"""
"""
print('My','Name','is','Tanu',sep='**')
"""
"""
num=8
print('%o' %num)
"""
"""
num=1234.395942957927
print('%.2f' %num)
"""
"""
numbers=[]
for i in range(0,5):
    print('please add float number',i)
    item=float(input())
    numbers.append(item)
print(numbers)
"""


"""
# read test.txt
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()

# open new file in write mode
with open("new_file.txt", "w") as fp:
    count = 0
    # iterate each lines from a test.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # in each iteration reduce the count
        count += 1
    print(lines)
"""
"""
str1,str2,str3=input('Enter three string:').split()
print('Name1:',str1)
print('name2:',str2)
print('name3:',str3)
"""
"""
money=1000
quantity=3
price=350
print(f"I have {money} for {3} quantity and price is each product{price}")
"""
"""
import os
size=os.stat('test.txt').st_size
print(size)
if size==0:
    print('No file here')
else:
    print('yes!file existed')
"""
"""
with open('test.txt','r')as fp:
    line=fp.readlines()
    print(line[2])
"""
"""
i=1
while i<=10:
    print(i)
    i=i+1
"""
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print('\t \t')
"""
"""
#Mutable List
fruits = ['apple', 'banana', 'cherry']
# It may have diff types of data
fruits = [1, 3.4, True ,'cherry']
# May have duplicate data
fruits = ['apple', 'apple', 'apple']
# List has index
print(fruits[1])
"""
#Immutable touple
"""
info=('Asif',20,'2.9','Teacher')
x=info[1]
print(x)
"""
"""
name=['Asif','Tanmoy','Nobel','Piyash','Pritom','Abrar']
for i in name:
   print(i)
"""
"""
numbers=range(1,10)
for i in numbers:
    print(i)
lists=list(numbers)
print(lists)
print(*numbers)
"""
"""
stdents={'name':'Tanmoy','age':25,"cgpa":'3.15'}
for i in stdents:
    print(i,stdents[i])
    """
"""
numbers={1,2,3,2,3,2,3,1,4,5,5,5}
print(numbers)
list=[1,2,3,4,5,5,3,4,2,1]
print(list)
new_numbers=frozenset([1,2,3,4,5,1,2,4,5])
print(new_numbers)
"""
"""
is_active=True
if is_active==True:
    print('She is in online')
else:
    print('Offline')
    """
"""
def greet(strings):
    print('Hello',strings)
res=greet('I am Tanmoy')
print(res)
"""
"""
def calc(a,b):
    sum=a+b
    sub = b - a
    return sum,sub
res=calc(5,10)
print(res)
"""
"""
a=5
initial_id=id(a)
print(initial_id)
a=5
new_id=id(a)
print(new_id)
"""
"""
a=[1,2,3,4]
initial_id=id(a)
print(initial_id)
a=[1,2,3,4]
new_id=id(a)
print(new_id)

"""
"""
fs=frozenset([1,2,3])
initial_id=id(fs)
print(initial_id)
fs=frozenset([1,2,3])
new_id=id(fs)
print(new_id)
"""

"""
b='Hello'
initial_id=id(b)
print(initial_id)
b='Hellos'
new_id=id(b)
print(new_id)
"""
"""
t=(1,2,3)
initial_id=id(t)
print(initial_id)
t=(1,2,3)
new_id=id(t)
print(new_id)
"""
"""
num=[1,2,3]
initial_id=id(num)
print(initial_id)
num[0]=4
new_id=id(num)
print(new_id)
print(num)
"""
"""
students={"name":'Tanmoy','age':30,'cgpa':'3.15'}
initial_id=id(students)
print(initial_id)
students['sec']=3
new_id=id(students)
print(new_id)
print(students)
"""
"""
s={1,2,3}
initial_id=id(s)
print(initial_id)
s.add(4)
new_id=id(s)
print(new_id)
print(s)
"""
"""
x=123
y=str(x)
print(type(y))
"""
"""
try:
    x='Tanmoy'
    y=int(x)
except Exception as err:
    print(f'this is the biggest error...{err}')

"""
"""
principal=float(input('Enter your amount:'))
rate=float(input('Enter your rate:'))
time=int(input('Enter your time'))

interest=(principal*rate*time)/100
print(interest)
"""
"""
def number(n):
    if n%2==0:
        print('even')
    elif n%2!=0:
        print('odd')
    else:
        print('Invalid action.Please try again!')
user_input=int(input('Please enter a number:'))
number(user_input)
"""
"""
n=0
while n<=20 and n<=30:
    print(n)
    n=n+2
    """
"""
age = 25
is_student = False

if age >= 18 and is_student:
    print("You are eligible for a student discount.")
elif age >= 18 or is_student:
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")
    """
"""
def multiplication_table(num):
   for i in range(1,11):
       print(f"{num}x{i}={num*i}")
while True:
       num=int(input("Enter a number [0 to exit]:"))
       if num==0:
           break
       multiplication_table(num)
"""
"""
def leap_year(year):
    if year%4==0 and (year%400==0 or year%100!=0):
       return True
    else:
        return False
while True:
    year=int(input('Enter a year:'))
    if year==0:
        break
    elif leap_year(year):
        print('leap year')
    else:
        print('not leap year')
        """
"""
def largest_number(n1,n2,n3):
    if n1>n2 and n1>n3:
        print('n1 is largest number')
    elif n2>n1 and n2>n3:
        print('n2 is large')
    else:
        print('n3 is large')
n1=int(input("enter first number"))
n2=int(input("enter second number"))
n3=int(input("enter third number"))
largest_number(n1,n2,n3)
"""
"""
import random
random_number=random.randint(1,5)
print(random_number)
"""
"""
import math
import datetime
res=math.sqrt(100)
print(res)
today=datetime.datetime.today()
print(today)
res2=math.pi
print(res2)
"""
"""
fruits=['apple','banana','orange','lemon']
res='orange' in fruits
print(res)
#res2=fruits.pop()
#print(res2)
for fruit in fruits:
    print(fruit)
for i in range(4):
    print(i,fruits[i])
    """
"""
for i in range(5):
    for j in range(i):
        print("*",end='')
    print('')
    """
"""
s='abcd'
res2=len(s)
print(res2)
res=s*5
print(res)
a=10*'10'
print(a)
s=s[-2:]
print(s)

"""
"""
name='taNmoy'
res=name.upper()
res2=name.lower()
res3=name.capitalize()
print(res,res2,res3)
print(name[0])
"""
"""
country='Bangladesh'
res=country.find('Bang')
print(res)
res2=country.startswith('Bang')
print(res2)
res3=country.endswith('desh')
print(res3)
string='a,b,c,d,e,f,g,h,j'
res4=string.split(',')
print(type(res4))
list=['a','b','c']
res=','.join(list)
print(res)

"""
#calculate the sum using loop
"""
sum=0
n=int(input('Enter your number'))
for i in range(1,n+1,1):
    sum=sum+i
print(sum)
"""
"""
def addition(num):
    sum=0
    for i in range(1,num+1,1):
        sum=sum+i
    return sum
while True:
    num = int(input('Enter a number'))
    if num==0:
        break
    else:
        res=addition(num)
        print(res)
"""
"""
def multi_table(num):
    for i in range(1,11):
        print(f'{num} x {i} = {num*i}')
while True:
    num = int(input('Enter a number:'))
    if num==0:
        break
    else:
        multi_table(num)
        """
"""
def lists_number(list):
    for lists in list:
        print(lists)

list=[10,2,3,4,11,22,43]
lists_number(list)
"""
"""
string4 = "Hello,World!" 
print(string4)

# Using single quotes inside the string with escaping
escaped_quote_in_str = 'He said, \'Hello, World!\''
print(escaped_quote_in_str)

print('Hello,"world!"')

escaped_quote_in_str = "He said, 'Hello, World!'"
print(escaped_quote_in_str)
length=len(s)-1
print(s[length])

"""
"""
s='I am Tanmoy Saha'
res=s[::-1]
res2=s[:-1]
print(res)
print(res2)
"""
"""
user_inpt=input('Enter your name:')
print(f'Hello,{user_inpt}!')
"""
"""
fruits='appele,banana,orange,mango,guava,jackfruit'
data=fruits.split(',')
print(data)
"""
"""
import re
string="I am tanmoy saha.I am a software engineer"
words=re.findall(r"\w+",string)
print(words)
"""
"""
import re
if re.match(r"^\d{4}-\d{2}-\d{2}$","2024-08-26"):
    print('True')
else:
    print('False')
    """
"""
sentence="Hello,World!"
res=sentence[::-1]
print(res)
clean_str=sentence.replace(",", " ")
print(clean_str)
"""
"""
str1="hello"
str2="world"
combines=str1+","+str2+"!"
print(combines)
joined=", ".join([str1,str2])+"!"
print(joined)
formated="{},{}!".format(str1,str2)
print(formated)

format2="%s,%s!"%(str1,str2)
print(format2)
"""
"""
str = 'tanmoy is,my-name,i am ,29-years-old.'
words = str.split('-')
print(words)

str='I am Tanmoy Saha'
res=str.replace('Tanmoy Saha','Bijori Saha')
print(res)
"""
"""
str=['Hello','World']
res=' '.join(str)
print(res)
"""
"""
str='         Hello world                          '
res=str.strip()
print(res)
"""
"""
str='Hello world'
res=str.endswith('world')
print(res)
"""
"""
str='orlddddddddddd'
res=str.find('world')
res2=str.count('d')
res3=str.isalnum()
res4=str.isalpha()
res5=str.isdigit()
print(res)
print(res2)
print(res3)
print(res4)
print(res5)
"""
"""
test=" "
print(test.isspace())
text="Hello World    "
print(text.istitle())
print(text.strip().upper())

immutable_set = frozenset([1,2, 2, 3])

print(immutable_set)

sets={1,2,23,4,4,3,4,2,5,6,7,6}
print(sets)
"""
"""
l1=[1,2,3]
print(id(l1))
l1[0]=4
print(id(l1))
print(l1)
"""
"""
text='Hello world'
print(text[:-1])
print(f"{text} ok")
print(text.swapcase())
"""

"""
def list_numbers(numbers):
    for i in numbers:
        if i > 500:
            break
        elif i > 150:
            continue
        elif i%5==0:
            print(i)

numbers = [12, 75, 150, 180, 145, 525, 50]
numbers2 = [12, 75, 150, 180, 145, 525, 51,43,678]
list_numbers(numbers)
list_numbers(numbers2)
"""
"""
text='   Hello   '
print(text)
print(text.strip())
"""
"""fruits=input('enter a fruit name:')
items=[i.strip() for i in fruits.split() ]
print(items)"""
"""
num=2345355
count=0
while num!=0:
    num=num//10
    print(num)
    count=count+1
print(count)

"""
"""
for i in range(5):
    for j in range(5-i,0,-1):
        print(j,end=" ")
    print(" ")

"""
"""
numbers=[10,20,30,40,50]
x=numbers[::-1]
y=list(reversed(numbers))
print(x)
print(y)
"""
"""
lists=[1,2,3,4,5,6,7,8]
x=len(lists)
print(x)
"""
"""
lists=[11,22,33,43,5,6,7,8]
for i in range(len(lists)-1,-1,-1):
    print(lists[i])
    """
"""
lists="I am Tanmoy Saha"

for i in range(len(lists)-1,-1,-1):
    print(lists[i])
    """
"""
num=int(input('Enter a nuumber:'))
for i in range(0,num):
        if i==5:
            print('done')
        print(i)
"""
"""
start=25
end=50
for num in range(start,end+1):
    if num>1:
        for i in range (2,num):
            if num%i==0:
                break
        else:
            print(num)

"""
"""
num1=0
num2=1
for i in range(10):
    print(num1)
    res=num1+num2
    num1=num2
    num2=res
"""
"""
n=int(input('Enter a number:'))
fact=1

if n<0:
    print('This is not execute')
elif n==0:
    print("The factorial is 1")
else:
    for i in range(1, n + 1):
        fact = fact * i
        print(fact)
"""
"""
n=int(input("Enter a digit:"))
for i in range(n):
    print(i)
    """
"""
n=1234
print(n)
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print(rev)
"""
"""
number=345262
rev=0
while number>0:
    rem=number%10
    rev=(rev*10)+rem
    number=number//10
print(rev)
"""
"""
my_list = [10, 20, 30, 40, 50, 65, 70, 81, 90, 100]
for i in range(len(my_list)):
     if my_list[i]%2==0:
         print(my_list[i])
         """
"""
my_list = [10, 20, 30, 40, 50, 65, 70, 81, 90, 100]
for i in my_list[1::2]:
    print(i,end=" ")
    """
"""
n=int(input("Enter a number:"))
c=0
for i in range(1,n+1):
    c=i*i*i
    print(c)
    """
"""
sum=0
n=int(input('Enter a digit'))
for i in range(1,n+1):
    sum=sum+i
    print(sum)
    """
"""
n=int(input('Enter a number:'))
start=2
sum_seq=0
for i in range(0,n):

    print(start, end="+")
    sum_seq=sum_seq+start
    start=start*10+2
print(sum_seq)
"""
"""
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print(" ")
for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    print(" ")

"""
"""
def num(n):
    return n
x=num(11)
print(x)
"""
"""
def fun1(*args):
   for i in args:
       print(i)
fun1(1,22,4,5,6,78)

"""
"""
def cal(num1,num2):
    sum=num1+num2
    sub = num1 - num2
    return sum,sub
num1=int(input('Enter a nmber:'))
num2=int(input('Enter a second number:'))
x=cal(num1,num2)
print(x)
"""
"""
def show_employee(name,salary=9000):
    print(f"Name:{name} Salary:{salary}")
show_employee('Tanmoy',)
show_employee('Bijo',)
"""
"""
def outer_fun(a,b):
    def inner_fun():
        return a+b
    return inner_fun()+5
x=outer_fun(5,6)
print(x)
"""
"""
def outer_fun(a,b):
    squ= a**2
    print(squ)
    def inner_fun(a,b):
        return a+b
    add=inner_fun(a,b)
    return add+5
x=outer_fun(6,7)
print(x)
"""
"""
def r_fun(n):
    sum=0
    for i in range(0,n+1):
        sum=sum+i
        print(sum)
n = int(input('number:'))
r_fun(n)
"""
"""
def addition(num):
    if num:
        return num+addition(num-1)
    else:
        return 0
x=addition(10)
print(x)
"""
"""
def info(name,age):
    return name,age
info('tanu',28)
information=info
x=information('Tanu',29)
print(x)
"""
"""
def even_num(even_list):
    lists=[]
    for i in range(4,even_list+1):
        if i%2==0:
            lists.append(i)
    return lists

even_list=int(input('Enter a number:'))
res=even_num(even_list)
print(res)
"""
"""
def largest_num(num):
    if not num:
        print(None)
    largest=num[0]
    for i in num[1:]:
        if i>largest:
            largest=i
    return largest
numbers=[1,23,1,234,54,678,65,43]
x=largest_num(numbers)
print(x)
"""
"""
try:
    x='tanu'
    y=int(x)
except Exception as e:
    print(e)
    """
"""
str='tanoy'
x=str.capitalize()
y=str.swapcase()
print(y)
print(x)
z=str.replace('tanoy','bijo')
print(z)
a=str.split()
print(a)
"""
"""
a='hello world'
b=''.join(a)+'!'
print(b)
"""
"""
my_dict={'Bangla':68,"English":59,"Math":78}
keys=list(my_dict.keys())
index=0
while index<len(keys):
    each_keys=keys[index]
    print(f"Subject:{each_keys}={my_dict[each_keys]}")
    index+=1
    """
"""
my_dict={'Bangla':68,"English":59,"Math":78}
for key,values in my_dict.items():
    print(key,values)
    """
"""
list=[1,2,3,4,5,'joho']
for each_item in list:
    print(each_item)
    """
"""
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.


cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True
"""
"""
def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars>=40
    else:
        return 40<=cigars or 60<=cigars
cigar_party(30, False)
cigar_party(50, False)
cigar_party(70, True)
"""
def cigar_party(cigars, is_weekend):
  """Determines if a squirrel party is successful based on the number of cigars and whether it's the weekend.

  Args:
    cigars: The number of cigars at the party.
    is_weekend: True if it's the weekend, False otherwise.

  Returns:
    True if the party is successful, False otherwise.
  """
"""
  if is_weekend:
    return cigars >= 40
  else:
    return 40<=cigars<=60

# Example usage:
a=cigar_party(30, False)  # Output: False
b=cigar_party(50, False)  # Output: True
c=cigar_party(70, True)  # Output: True
x=cigar_party(61, False)
print(a,b,c,x)

"""
"""
def date_fashion(you, date):
     if you<=2 or date<=2:
         return 0
     if you>=8 or date>=8:
         return 2
     else:
         return 1
x=date_fashion(5, 10)
y=date_fashion(5, 2)
z=date_fashion(5, 5)

print(x,y,z)
"""
"""
def squirrel_play(temp, is_summer):
    if is_summer:
        return (temp<=100) and (temp>=60)
    else:
        return (temp>=60) and (temp<=90)

x=squirrel_play(70, False)
y=squirrel_play(95, False)
z=squirrel_play(95, True)
a=squirrel_play(50, True)
print(x,y,z,a)
"""
"""
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed=speed-5
    if speed<=60:
        return 0
    elif  speed<=80:
        return 1
    else:
        return 2

a=caught_speeding(60, False)
b=caught_speeding(65, False)
c=caught_speeding(85, False)
print(a,b,c)

"""
"""
def sorta_sum(a, b):
    sum=a+b
    if sum>=10 and sum<=19:
        return 20
    else:
        return sum

a=sorta_sum(3, 4)
b=sorta_sum(9, 4)
c=sorta_sum(10, 11)
print(a,b,c)
"""

"""
def alarm_clock(day, vacation):
    if vacation:
        if day>=1 and day<=5:
            return '10:00'
        else:
            return 'Off'
    else:
        if day>=1 and day<=5:
            return '7:00'
        else:
            return '10:00'

"""
"""
def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars>=40
    else:
        return cigars>=40 and cigars<=60
"""
"""
def date_fashion(you, date):
    if you<=2 or date<=2:
        return 0
    elif you>=8 or date>=8:
        return 2
    else:
        return 1
x=date_fashion(5, 10)
y=date_fashion(5, 2)
z=date_fashion(5, 5)
print(x,y,z)
"""
"""
def squirrel_play(temp, is_summer):
    if is_summer:
        return temp>=60 and temp<=100
    else:
        return temp>=60 and temp<=90

"""
"""
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed-=5
    if speed<=60:
        return 0
    elif speed>=61 and speed<=80:
        return 1
    else:
        return 2
"""
"""
def sorta_sum(a, b):
    sum=a+b
    if sum>=10 and sum<=19:
        return 20
    elif sum >= 0 and sum <= 9:
        return sum
    else:
        return sum
x=sorta_sum(3, 4)
y=sorta_sum(9, 4)
z=sorta_sum(10, 11)
print(x,y,z)
"""

"""
def love6(a, b):
    sum=a+b
    sub=a-b

    if a==6 or b==6 or sum==6 or sub==6 or sub==-6:
        return True
    else:
        return False

x=love6(6, 4)
y=love6(4, 5)
z=love6(1, 5)
a=love6(1, 7)
print(x,y,z,a)
"""
"""
def in1to10(n, outside_mode):
  if outside_mode:
    return n<=1 or n>=10
  else:
    return n>=1 and n<=10
a=in1to10(5, False)
b=in1to10(11, False)
c=in1to10(12, True)
print(a,b,c)

"""
"""
def near_ten(num):
  if num%10<=2 or num%10>=8
    return True
  else:
    return False
"""
"""
age=20
has_permission=False
if age>=18:
  if has_permission:
    print('You Enter the club')
  else:
    print('You need to permission')
else:
  print('You are not enter the club')
"""
"""
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
"""
"""
words='Hello'
for word in range(len(words)):
  print(words[word])
"""
"""
student_scores = {'Alice': 90, 'Bob': 85, 'Charlie': 92}
for i,j in student_scores.items():
  print(i,j)
  """
"""
lists=['Appele','Banana','Orange','mango']
index=0;
while index<len(lists):
  print(lists[index])
  index+=1
  """
"""
start=0
end=10;
while start<=end:
  print(start)
  start=start+1
  """
"""
students_score={'Bangla':90,'English':92,"Math":88,"Religion":78}
keys=list(students_score.keys())
index=0
while index<len(keys):
  key=keys[index]
  print(f"{key}:{students_score[key]}")
  index+=1
  """
"""
num_set = {1, 2, 3, 4, 5, 6, 'khfu'}
lists=list(num_set)
index = 0
while index < len(lists):
    print(lists[index])
    index += 1

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "kiwi")
print(fruits)
"""



"""
student = {
 "name": "Alice",
 "major": "Computer Science"
}
age = student.get("age","not")
print(age)
"""

"""
def make_bricks(small, big, goal):
 if goal>=big*5:
   big_use=big
   print(big_use)
 else:
   big_use=goal//5
 remain=goal-big_use*5

 if small>=remain:
     return True
 else:
     return False

make_bricks(3, 2, 9)

    """


"""
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
"""
"""
def lone_sum(a, b, c):
    if a==b==c:
        return 0
    if a==b:
        return c
    elif a==c:
        return b
    elif b==c:
        return a
    else:
        return a+b+c

x=lone_sum(3,6,4)
print(x)
"""
"""
lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
"""
"""
def lucky_sum(a, b, c):
  if a==13:
    return 0
  if b==13:
    return a
  if c==13:
    return a+b
  else:
    return a+b+c


lucky_sum(1, 2, 3)
lucky_sum(1, 2, 13)
lucky_sum(1, 13, 3)
"""
"""
no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3

"""
"""
def no_teen_sum(a, b, c):
  if (a==15 or a==16) or (b==15 or b==16) or (c==15 or c==16):
    return a+b+c
  elif a>=b>=c>= 13:
    return 0
  if a>=13:
    return b+c
  elif b>=13:
    return a+c
  elif c>=13:
    return a+b
  else:
    return a+b+c

x=no_teen_sum(16, 17, 18)
print(x)

"""
"""
def fix_teen(n):
  if (n>=13 and n<=14) or (n>=17 and n<=19):
    return 0
  return n

  def no_teen_sum(a, b, c):
    return fix_teen(a)+fix_teen(b)+fix_teen(c)
"""
"""
def round_num(num):
  last_digit=num%10
  if last_digit<5:
    return num-last_digit
  else:
    return num+(10-last_digit)
def sum(a,b,c):
  return round_num(a)+round_num(b)+round_num(c)
"""
"""
def close_far(a, b, c):
  if abs(a-b)<=1 and abs(a-c)>=2 and abs(b-c)>=2:
    return True
  elif abs(a-c)<=1 and abs(a-b)>=2 and abs(b-c)>=2:
    return True
  else:
    return False

x=close_far(1,2,10)
print(x)
"""

"""
def make_chocolate(small, big, goal):
  max_big=goal//5
  if big>=max_big:
     use_big=max_big
  else:
    use_big=big
  remain=goal-(use_big*5)
  if small>=remain:
    return remain
  else:
    return -1

x=make_chocolate(4, 1, 9)
y=make_chocolate(4, 1, 10)
z=make_chocolate(4, 1, 7)
print(x,y,z)
"""
"""
def first_last6(nums):
  first=nums[0]
  last=nums[len(nums)-1]
  if first==6 or last==6:
    return True
  else:
    return False
    """

"""
def same_first_last(nums):
  if len(nums)>=1:
    return nums[0]==nums[-1]
  else:
    return False


x=same_first_last([1, 2, 3, 1])
y=same_first_last([1, 2,  1])
z=same_first_last([1, 2, 3])
print(x,y,z)

"""
"""
def make_pi():
  return [3,1,4]
x=make_pi()
print(x)
"""
"""
a=[1,2,3,4]
print(a[-1])

def common_end(a, b):
    first1=a[0]
    first2=b[0]
    last1=a[-1]
    last12=b[-1]
    if first1==first2 or last1==last12:
      return True
    else:
      return False
"""
"""
def sum3(nums):
  sum=0
  for i in nums:
    sum=sum+i
  return sum
x=sum3([1,2,3,56,8])
print(x)
"""
"""
def rotate_left3(nums):
  return nums[1:]+[nums[0]]

x=rotate_left3([1, 2, 3])
print(x)
"""
"""
def reverse3(nums):
  return nums[::-1]
  """
"""
def max_end3(nums):
  for i in range(0,3):
    if nums[0]>=nums[2]:
       return [nums[0],nums[0],nums[0]]
    else:
       return [nums[2],nums[2],nums[2]]

"""
"""
def sum2(nums):

  if len(nums)>=2:
    return nums[0]+nums[1]
  elif len(nums)==1:
    return nums[0]
  else:
    return 0
    """
"""
mydict={
  'name':'Tanmoy',
  'gpa':3.15,
  'goal':'Full stact developer',
  "age":28
}
cpy_dict=mydict.copy()
mydict['name']='Bijo'
print(mydict)
print(cpy_dict)
"""
"""
class Student:
  roll=''
  gpa=''
  dream=''
  def value_pass(self,roll,gpa,dream):
    self.roll=roll
    self.gpa=gpa
    self.dream=dream

  def pprint(self):
    print(f'Roll:{self.roll},Gpa:{self.gpa},Dream:{self.dream}')

rahim=Student()
rahim.value_pass(123,3.15,'Full stack software developer')
rahim.pprint()
"""
"""
for i in range(5):

    normal_day=input('Enter the day')
    normal_day=normal_day.lower()
    public_holiday=input('Today is public holiday?..yes/no:')
    public_holiday=public_holiday.lower()
    is_sick_today=input('sick today?')
    breaks = input("Do you want to exit?yes or no")
    breaks=breaks.lower()
    if normal_day=='Friday' or normal_day=='Saturday' or public_holiday=='yes' or is_sick_today==True:
      print('Today is Holiday')
    else:
      print('not holiday')

    if breaks == 'yes':
      break
      """
"""
def bye_car(price,color,brand,milege):
  budget=20000
  my_color=['red','silver','black']
  my_brand=['Toyota','BMW','Marcedeze']
  kilmeter=30000

  if (price<=budget and color in my_color and brand in my_brand) or (milege<=kilmeter or milege<=kilmeter//2 and 25000<=budget<=35000):
    return True
  else:
    return False
price=int(input('Enter your price:'))
color=input('Please tell me your color')
brand=input('Please tell me the brand:')
milege=int(input('Enter the mileage'))

if bye_car(price,color, brand, milege):
  print('I select it')
else:
  print('No! I dont select it.')

"""
"""
def middle_way(a, b):
  if a[1] and b[1]:
    return  [a[1],b[1]]
    """
"""
def make_ends(nums):
  first=nums[0]
  last=nums[len(nums)-1]

  return [first,last]

x=make_ends([7, 4, 6, 2])
print(x)
"""
"""
def has23(nums):
  if 2 in nums or 3 in nums:
    return True
  else:
    return False
"""
"""
class Student:
  Roll=''
  Gpa=''
  Dream=''
  def __init__(self,Roll,Gpa,Dream):
    self.Roll=Roll
    self.Gpa=Gpa
    self.Dream=Dream
  def display(self):
    print(f'Roll={self.Roll},Gpa={self.Gpa},Dream={self.Dream}')

tanmoy=Student (125,3.15,'Full stact web developer')
tanmoy.display()
"""
"""
class Vehicle:
  name=''
  wheal=''
  cc=int
  price=int
  def __init__(self,name,wheal,cc,price):
    self.name=name
    self.wheal=wheal
    self.cc=cc
    self.price=price
  def display(self):
    print(f'Name:{self.name},Wheal:{self.wheal},CC={self.cc},Price:{self.price}')
car=Vehicle('Toyota',4,1500,2800000)
car.display()
"""
"""
class Triangle:
  base=int
  height=int
  def __init__(self,base,height):
    self.base=base
    self.height=height
  def display(self):
        return self.base*self.height

obj=Triangle(10,20)
x=obj.display()
print(x)
"""
"""
name={'name':'Tanu','age':25,'Roll':25}
key=list(name.keys())
index=0
while index<=len(key)-1:
  keys=key[index]
  print(f"{keys},{name[keys]}")
  index+=1
  """
"""
age=18
if age!=18:
  print('not adult')
else:
  print('adult')
  
"""
"""
x = 3
y = 5
print(x < y) # True
"""
"""
numbers = [3, 1, 4, 1, 5, 9, 2]
max=float('-inf')
for number in numbers:
  if number>max:
    max=number
print(max)
"""
"""
numbers=[]
for i in range(5):
 number=int(input("Enter 5 number:"))
 numbers.append(number)
max=float('-inf')
for number in numbers:
  if number>max:
    max=number
print('Max:',max)
"""
"""
class Phone:
  def __init__(self,call,message):
    self.call=call
    self.message=message
    return None
  def display(self):
    print(f'{self.call},{self.message}')

class Samsung(Phone):
  def __init__(self,ai,call,message):
    super().__init__(call,message)
    self.ai=ai

  def display2(self):
    print(f"{self.ai}")

obj1=Phone(10,20)
obj1.display()
obj2=Samsung(20,30,40)
obj2.display()
obj2.display2()
"""
"""
res=lambda x,y : x if x>y else y
print(res(2,3))
"""
""""

import os
x=os.mkdir('new')
print(x)
"""
"""
def min_max(numbers):
  return min(numbers),max(numbers)
x,y=min_max([11,22,34,32,1,35,-9])
print(x)
print(y)



def greet(name):
 print(f"Hello, {name}!")
 return None
result = greet("Alice")
print(result) 
"""
"""

def even_list(n):
  new_list=[]
  for i in range(n):
    if i%2==0:
      new_list.append(i)
  return new_list

res=even_list(10)
print(res)
"""
"""
def find_first_even(numbers):
   for number in numbers:
     if number % 2 == 0:
       return number

result = find_first_even([1, 3, 5, 6, 7,8])
print(result) 
"""
"""
numbers=[1,2,3,4,5,6]
res=map(lambda x:x**2,numbers)

print(list(res))
"""
"""
numbers=[1,2,3,4,5,6]
res=filter(lambda x:x%2==0,numbers)
print(list(res))
"""
"""
points=[(9,6  ),(1,2),(2,1)]
sorted_point=sorted(points,key=lambda x:x[1])
print(sorted_point)
"""
"""
global_var = 20
def my_function():
 global global_var
 global_var = 30
 print("Inside the function, global_var:", global_var)
my_function()
print("Outside the function, global_var:", global_var)

"""
"""
with open('Demo.text','r') as f:
  content=f.read()
print(content)
"""
"""
my_lists=[2,3,44,56,76,54,21,34,68,76]
new_list=[]
for my_list in my_lists:
  if my_list%2==0:
    new_list.append(my_list)
print(new_list)
"""
"""
my_lists=[2,3,44,56,76,54,21,34,68,76]
big_num=my_lists[0]
for my_list in my_lists:
  if my_list>big_num:
    big_num=my_list
print(big_num)
"""
"""
def multiplication(num):
  for i in range(1,11):
     res=num*i
     print(res)
x=multiplication(10)
print(x)
"""
"""
with open("example.txt", "w") as file:
 file.write("This is a new file.")
with open("example.txt", "r") as file:
 content = file.read()
 print(content)
 
"""
"""
import os
r=os.listdir('.')
print(r)
"""
"""
with open('Folder/example.text','w') as file:
  file.write('I am new')
  """

"""
import os
os.rename('Folder','New_folder')
"""
"""
os.remove('New_folder/example.text')
os.rmdir('New_folder')
"""
"""
import os
path='demo'
res=os.listdir(path)
print(res)
for i in res:
    print(i)

"""
"""
with zipfile.ZipFile('c.zip','w') as zfile:
  zfile.write('d.txt')
  """
"""
import zipfile
path_zip='b.zip'
with zipfile.ZipFile(path_zip,'r') as zfile:
  zfile.extractall()
  extracted_files=zfile.namelist()
  print(extracted_files)
"""
"""
import shutil
which_file='demo'
which_name='demo_archive'
shutil.make_archive(which_name,'zip',which_file)
print(f'{which_name},{which_file}')
"""
"""
import csv
data=[
  ['name','age','profession','income','life style'],
  ['Tanmoy','27','surviver','not fixed','nimno moddhobitto'],
  ['name','age','profession','income','life style'],
  ['name','age','profession','income','life style'],
  ['name','age','profession','income','life style'],
  ['Tanmoy','30','Software enginear','50000$','Milonear'],

]

path_csv='example.csv'
with open(path_csv,'w',newline='')as f_csv:
  csv_writer=csv.writer(f_csv)
  csv_writer.writerows((data))
print(path_csv)
"""
"""
import csv
path_csv='example.csv'
data_list=[]
with open(path_csv,'r')as file:
  csv_reader=csv.reader(file)
  for row in csv_reader:
    data_list.append(row)
print(data_list)
"""
"""
import random
numbers=[]
for _ in range(10):
    numbers.append(random.randint(1,100))
print(numbers)
max=float('-inf')
for number in numbers:
    if number>max:
        max=number
print(max)
"""
"""
def f_1(a,b,c):
    global d
    d=d*2
    a=a*2
    b=b*2
    c=c*2
    return a+b+c
def f_2():
    print(d)

d=100

x=f_1(1,2,3)
print(x)

x=f_1(1,2,3)
print(x)
f_2()
f_2()
x=f_1(1,2,3)
print(x)
print(d)

"""
"""
nums=[1,2,34,4,5,66]
res=[x*y for x in nums for y in nums]
print(res)
"""
"""
n=int(input().strip())
if n%2!=0:
    print('Weired')
elif 2<=n<=5:
    print('Not Weired')
elif 6<=n<=20:
    print('Weired')
elif n>20:
    print('Not Weired')

"""
"""
import json
person={
    "name":'Tanmoy',
    'age':27,
    'gap_study':'2 years',
    'profession':'Nothing'
}

json_data=json.dumps(person)
print(json_data)
with open('new.json','w') as file:
    json.dump(person,file,indent=4)
    print('complete')

"""
"""
import json
with open('new.json','r') as file:
    x=json.load(file)
    print(x['name'])
"""
"""
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

"""
"""
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return
    else:
        return False
"""
"""
def sum_double(a, b):
    if a==b:
        return (a+b)*2
    else:
        return a+b
"""
"""
def diff21(n):
    if n<=21:
        return 21-n
    else:
        return (n-21)*2
        """
"""
import random
def number_guesing_game():
    target_number=random.randint(1,100)
    attempts=0
    guess_number=False
    print('Welcome to the Number Guessing Game!')
    print('Try to guess the number between 1 and 100.')
    while not guess_number:
      try:
        guess=int(input('Enter your Number:'))
        attempts=attempts+1

        if guess<target_number:
          print('Too low!')
        elif guess>target_number:
          print('Too High')
        else:
          guess_number=True
          print(f'It is matched and you have {attempts} attempts')
      except Exception as e:
        print(e,'Enter a number only.')


number_guesing_game()

"""

"""
def addition(x,y):
  return x+y
def subtraction(x,y):
  return x-y
def multiplication(x,y):
  return x*y
def division(x,y):
  res=x/y
  return f'{res:.2f}'
def modulus(x,y):
  res=x%y
  return f'{res:.2f}'

def main():
  print('select an operation:')
  print('1.Add')
  print('2.Sub')
  print('3.Mul')
  print('4.Division')
  print('5.Modulus')
  try:
    choice=input('Enter choice 1/2/3/4/5:')
    num1=int(input('Enter your first number:'))
    num2 = int(input('Enter your second number:'))
    if choice=='1':
      print(f'{num1}+{num2}={addition(num1,num2)}')

    if choice=='2':
      print(f'{num1}-{num2}={subtraction(num1,num2)}')

    if choice=='3':
      print(f'{num1}x{num2}={multiplication(num1,num2)}')

    if choice=='4':
      print(f'{num1}/{num2}={division(num1,num2)}')

    if choice=='5':
      print(f'{num1}%{num2}={modulus(num1,num2)}')
  except Exception as e:
    print(e,'Please enter a number...............')

main()
"""
"""
words = ['hello', 'world']
print("Join:", ' '.join(words))
"""
"""
def is_weird(n):
  if n%2!=0:
    print('weird')
  elif n%2==0 and 2<=n<=5:
    print('not weird')
  elif n%2==0 and 6<=n<=20:
    print('weird')
  elif n%2==0 and n>20:
    print('not weird')
n=int(input('Enter a number:'))
is_weird(n)
"""
"""
def stdin(a,b):
  summation=a+b
  sub=a-b
  mul=a*b
  print(summation)
  print(sub)
  print(mul)
a=int(input('Enter a first number:'))
b=int(input('Enter a second number:'))
stdin(a,b)
"""
"""
a=int(input())
b=int(input())

int_div=a//b
div=a/b

print(int_div)
print(div)

"""

"""
def is_leap(year):
  leap = False

  if (year%4==0 and year%100!=0) or (year%400==0):
    return True

  return leap


year = int(input())
print(is_leap(year))
"""
"""
x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if [i + j + k] !=n]
coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
print(coordinates)
"""
"""
def even_numbers(n):
  return [x for x in range(n) if x%2==0]
res=even_numbers(10)
print(res)

"""
"""
def dic(name,age):
  return {'name':name,'age':age}
res=dic('alice',28)
print(res)

"""
"""
def e_exit(numbers):
  for number in numbers:
    if number%2==0:
      return number
  return None
res=e_exit([1,3,5,3,3,3,3,3])
print(res)
"""
"""
add=lambda x,y:2+3
print(add(3,3))

grater=lambda a,b:a if a>b else b
res=grater(10,20)
print(res)

"""
"""
numbers=[1,2,3,4,5]
res=map(lambda number:number**2 ,numbers)
print(list(res))

numbers=[11,22,33,44,55,66]
res=filter(lambda x: x%2==0,numbers)
print(list(res))

"""
"""
points=[(1,7),(4,2),(3,5)]
res=sorted(points ,key=lambda point:point[0])
print(res)

"""
"""
global_var = 20
def my_function():
 global_var = 10 # This is a local variable
 print("Inside the function, global_var:", global_var)
my_function()
print("Outside the function, global_var:", global_var)
"""
"""
import os
demo_path='demo'
file_lists=os.listdir(demo_path)
print(file_lists)
for file_list in file_lists:
  print(file_list)

"""
"""
import shutil
# Specify the directory to be zipped
directory_to_zip = "demo"
# The name of the output zip file (without extension)
output_zip_name = "kemo_archive"
# Create a zip archive
res=shutil.make_archive(output_zip_name, 'zip', directory_to_zip)

print(res)

"""
"""
import csv

data=[
  ['name','age'],
  ['n',28],
  ['t','27']
]
with open('e.csv','w',newline='') as file:
  csv_writer=csv.writer(file)
  csv_writer.writerows(data)

"""

import csv
path='e.csv'
csv_list=[]
with open(path,'r') as file:
  csv_reader=csv.reader(file)
  for row in csv_reader:
    csv_list.append(row)
for row in csv_list:
  print(row)




























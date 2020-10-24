# Arithmetic Operators

a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)

# Hello World!

print("Hello, World!")

#Loops

i=0
n=int(input())
if n>20 and n<1:
    print("Choose another positive integer not greater than 20")
else:
    for i in range(n):
        print(i*i)

# Print Function

i=1
n=int(input())
if n>=1 and n<=150:
    while i<=n:
        print(i, end="")
        i=i+1

# Python Division

a=int(input())
b=int(input())
if b==0:
    print("Division impossible for b=0, try another integer")
else: 
    print(a//b)
    print(a/b)

# Python If-Else

n=int(input())
if n>=1 and n<=100:
    if n%2!=0:
        print("Weird")
    if n%2==0 and n>=2 and n<=5:
        print("Not Weird")
    if n%2==0 and n>=6 and n<=20:
        print("Weird")
    if n%2==0 and n>20:
        print("Not Weird")
else:
    print("Choose another positive integer")

# Write a Function

def is_leap(year):
    if year%4!=0:
        return False
    elif year%4==0:
     if year%100==0:
      if year%400==0:
         return True   
      else:
          return False
    return True 

year=int(input())
if year>=1900 and year<=10**5:
    if is_leap(year):
     print("True")
    else:
     print("False")

# Find the Runner-up

if __name__=='__main__':
 n=int(input())
 arr=(input().split(" "))
 A=set(arr)
 list=[]
 for i in A:
     list.append(int(i))
 list.sort()
 print(list[-2])

 # Finding the Percentage

 if __name__ == '__main__':
    n=int(input())
    student_marks={}
    for _ in range(n):
        name,*line=input().split()
        scores=list(map(float, line))
        student_marks[name]=scores
    query_name=input()
    for key in student_marks:
        if query_name==key:
         sums=0
         c=0
         for i in student_marks[key]:
             sums=sums+i
             c=c+1 
         average=float(sums/c)
         print("%.2f" % average)

# List Comprehensions

x=int(input())
y=int(input())
z=int(input())
n=int(input())
list=[]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if(i+j+k)!=n:
                list.append([i,j,k])

print(list)

# Lists

if __name__=='__main__':
    N=int(input())
    list=[]
    while N>0:
        command=input()
        command=command.split()
        if command[0]=="insert":
            pos=int(command[1])
            el=int(command[2])
            list.insert(pos,el)
            N-=1
        elif command[0]=="print":
            print(list)
            N-=1
        elif command[0]=="remove":
            el=int(command[1])
            list.remove(el)
            N-=1
        elif command[0]=="append":
            el=int(command[1])
            list.append(el)
            N-=1
        elif command[0]=="sort":
            list.sort()
            N-=1
        elif command[0]=="pop":
            list.pop()
            N-=1
        elif command[0]=="reverse":
            list.reverse()
            N-=1

# Nested Lists

if __name__ == '__main__':
    records=[]
    scores=[]
    for _ in range(int(input())):
        name=input()
        score=float(input())
        records=records+[[name,score]]
        scores.append(score)
    scores=set(scores)
    ndlowest=sorted(scores)[1] 
    for n,s in sorted(records):
        if s==ndlowest:
            print(n)

# Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))

# Alphabet Rangoli

def print_rangoli(size):
    alph="a b c d e f g h i j k l m n o p q r s t u v w x y z"
    l=alph.split(" ")
    dim1=size*2-1
    dim2=2*dim1-1
    for i in range(1,size):
        print(("-".join(l[size-1:size-i:-1]+l[size-i:size])).center(dim2,"-"))
    for i in range(size,0,-1):
        print(("-".join(l[size-1:size-i:-1]+l[size-i:size])).center(dim2,"-"))


    return

# Capitalize!

def solve(s):
    l1=s.split(" ")
    l2=[]
    for p in l1:
        l2.append(p[0:1].upper()+p[1:])
    name=" ".join(l2)
    return name

# Designer Door Mat

s=input()
s=s.split()
N=int(s[0])
M=int(s[1])
for i in range(1,N,2):
    print((i*".|.").center(M,"-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,0,-2):
    print((i*".|.").center(M,"-"))
 
# Without method center()

s=input()
s=s.split()
N=int(s[0])
M=int(s[1])
c="WELCOME"
j=0
for i in range(1,N,2):
    print((((M//2)-(i+j))*"-"), end="")
    print((i*".|."),end="")
    print((((M//2)-(i+j))*"-"))
    j+=1
print((((M//2)-(7//2))*"-"), end="")
print(c, end="")
print((((M//2)-(7//2))*"-"))
j-=1
for i in range(N-2,0,-2):
    print((((M//2)-(i+j))*"-"), end="")
    print((i*".|."),end="")
    print((((M//2)-(i+j))*"-"))
    j-=1

# Find a string

def count_substring(string, sub_string):
    c=0
    i=0
    l1=len(string)
    l2=len(sub_string)
    while i<l1:
        if(string[i:i+l2]==sub_string):
            c+=1
        i+=1
    return c

# Merge the Tools!

def merge_the_tools(string, k):
    n=len(string)
    l=[]
    l2=[]
    s=""
    for i in range(0,n,k):
        l.append(string[i:i+k])
    for el in l:
        for c in el:
            if (c not in l2):
                l2.append(c)
        print("".join(l2))
        l2=[]        
    return

# Mutations

def mutate_string(string, position, character):
    string=string[:position]+character+string[position+1:]

    return string

# String Formatting

# I had to consult the formatting bibliograpy of Python and the Discussions section

def print_formatted(number):
    w=len(str(bin(number)).replace("0b",""))
    
    for i in range(1,number+1):
        l=[]
        d=str(i).rjust(w," ")
        o=str(oct(i)[2:]).replace("0o","  ").rjust(w," ")
        h=str(hex(i)[2:]).replace("0x","  ").upper().rjust(w," ")
        b=str(bin(i)[2:]).replace("0b","  ").rjust(w," ")
        l.append(d)
        l.append(o)
        l.append(h)
        l.append(b)
        s=" ".join(l)
        print(s)
    
    return

# String Split and Join

def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    return line

# String Validators

if __name__=='__main__':
    s=input()
    n=0
    for char in s:
        if char.isalnum():
            n+=1
    if n>0:
        print("True")
    else:
        print("False")
    n=0
    for char in s:
        if char.isalpha():
            n+=1
    if n>0:
        print("True")
    else:
        print("False")
    n=0
    for char in s:
        if char.isdigit():
            n+=1
    if n>0:
        print("True")
    else:
        print("False")
    n=0
    for char in s:
        if char.islower():
            n+=1
    if n>0:
        print("True")
    else:
        print("False")
    n=0
    for char in s:
        if char.isupper():
            n+=1
    if n>0:
        print("True")
    else:
        print("False")

# sWAP cASE

def swap_case(s):
    S1=list(s)
    S2=[]
    for l in s:
        if(l.isupper()):
         l=l.lower()
         S2.append(l)
        else:
         l=l.upper()
         S2.append(l)
 
    return("".join(S2))

# Text Alignment

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Text Wrap

import textwrap

def wrap(string, max_width):
    l=len(string)
    list=[]
    for i in range(0,len(string),max_width):
        list.append(string[i:i+max_width])
    s="\n".join(list)


    return s

# The Minion Game

# My first attempt with function Find a String, I could not find a way to ignore substrings already counted with this procedure

def count_substring(string, sub_string):
    c=0
    i=0
    l1=len(string)
    l2=len(sub_string)
    while i<l1:
        if(string[i:i+l2]==sub_string):
            c+=1
        i+=1
    return c


def minion_game(string):
    sc=0
    kc=0
    for i in range(0,len(string)):
        if(not(string[i]=="A"or"E"or"I"or"O"or"U")):
            for j in range(i+1,len(string)-i):
              sc+=count_substring(string,string[i:j])
        else:
            continue
    for i in range(0,len(string)):
        if(string[i]=="A"or"E"or"I"or"O"or"U"):
            for j in range(i+1,len(string)-i):
              kc+=count_substring(string,string[i:j])
        else:
            continue
    if(sc==kc):
        print("Draw")
    elif(sc>kc):
        print("Stuart {}".format(sc))
    else:
        print("Kevin {}".format(kc))
    return

# What's Your Name

def print_full_name(a, b):

    print("Hello {} {}! You just delved into python.".format(first_name,last_name))

# Check Strict Superset

A=set(map(int,input().split()))
N=int(input())
truth=0
for i in range(N):
    s=set(map(int,input().split()))
    if(len(set(s).difference(set(A).intersection(s)))!=0):
        truth+=1
if(truth==0):
    print(True)
else:
    print(False)

# Check Subsets

T=int(input())
for i in range(T):
    nA=int(input())
    A=list(map(int,input().split()))
    nB=int(input())
    B=list(map(int,input().split()))
    O=set(A).difference(set(A).intersection(B))
    if(len(O)==0):
        print(True)
    else:
        print(False)

# Introduction to Sets

def average(array):
    avg=0
    avg=sum(set(array))/len(set(array))
    return avg

# No Idea!

l=list(input().split())
arr=list(map(int,input().split()))
hap=0
A=set(map(int,input().split()))
B=set(map(int,input().split()))
for i in arr:
    if(i in A):
        hap+=1
    elif(i in B):
        hap-=1
    else:
        continue
print(hap)

# Set Mutations

n=int(input())
s=set(map(int,input().split()))
N=int(input())
for i in range(N):
    command=input().split()
    l=list(map(int,input().split()))
    if command[0]=="intersection_update":
        s.intersection_update(set(l))
    elif command[0]=="update":
        s.update(set(l))
    elif command[0]=="symmetric_difference_update":
        s.symmetric_difference_update(set(l))
    elif command[0]=="difference_update":
        s.difference_update(set(l))
print(sum(s))

# Set.add()

N=int(input())
stamps=set()
for i in range(N):
    stamps.add(input())
print(len(stamps))

# Set.difference()

n=int(input())
s1=set(map(int,input().split()))
b=int(input())
s2=set(map(int,input().split()))
print(len(s1.difference(s2)))

# Set.discard(), .remove() & .pop()

n=int(input())
s=set(map(int,input().split()))
N=int(input())
for i in range(N):
    command=input().split()
    if command[0]=="pop":
        s.pop()
    elif command[0]=="remove":
        s.remove(int(command[1]))
    elif command[0]=="discard":
        s.discard(int(command[1]))
print(sum(s))

# Set.intersection()

n=int(input())
s1=set(map(int,input().split()))
b=int(input())
s2=set(map(int,input().split()))
print(len(s1.intersection(s2)))

# Set.symmetric_difference()

n=int(input())
s1=set(map(int,input().split()))
b=int(input())
s2=set(map(int,input().split()))
print(len((s1.union(s2)).difference(s1.intersection(s2))))

# Set.union()

n=int(input())
s1=set(map(int,input().split()))
b=int(input())
s2=set(map(int,input().split()))
print(len(s1.union(s2)))

# Symmetric Difference

M=int(input())
set1=set(map(int,((input().split()))))
N=int(input())
set2=set(map(int,((input().split()))))
set3 = sorted((set1.union(set2)).difference(set1.intersection(set2)))
for i in set3:
    print(i)

# The Captain's Room

# My first correct solution, though not optimised

K=int(input())
l=list(map(int,input().split()))
s=set(l)
count=0
for i in s:
    count=0
    for j in l:
        if(i==j):
            count+=1
    if(count==1):
        print(i)
        
# Other solution with Set operations

K=int(input())
l=list(map(int,input().split()))
s1=set()
s2=set()
for i in l:
    if(i not in s1):
        s1.add(i)
    else:
        s2.add(i)
l2=list(s1.difference(s2))
print(l2[0])

# collections.Counter()

from collections import Counter

X=int(input())
S=list(map(int,input().split()))
N=int(input())
C=Counter(S)
n=0
for i in range(N):
    l=list(map(int,input().split()))
    if C[l[0]]>0:
        n+=l[1]
        C[l[0]]-=1
print(n)

# DefaultDict Tutorial

from collections import defaultdict
d=defaultdict(list)
l=list(map(int,input().split()))
for i in range(l[0]):
    d[input()].append(i+1)
for i in range(l[1]):
    a=input()
    if(a in d.keys()):
        print(" ".join(map(str,d[a])))
    else:
        print(-1)

# Collections.namedtuple()

from collections import namedtuple

N=int(input())
sum=0
avg=0
attributes=input()
S=namedtuple("S",attributes)
for i in range(N):
    a,b,c,d=(input().split())
    i=S(a,b,c,d)
    sum+=int(i.MARKS)
avg=sum/N
print("{:.2f}".format(avg))

# Collections.OrderedDict()

from collections import OrderedDict

N=int(input())
d=OrderedDict()
for i in range(N):
    items=[]
    items=list(input().split())
    item=" ".join(items[:-1])
    price=items[-1]
    if(item in d.keys()):
        d[item]+=int(price)
    else:
        d[item]=int(price)
for key in d:
    print(key,d[key])

# Collections.deque()

from collections import deque

d=deque()
N=int(input())
for i in range(N):
    comm=input().split()
    if comm[0]=="append":
        d.append(comm[1])
    elif comm[0]=="appendleft":
        d.appendleft(comm[1])
    elif comm[0]=="pop":
        d.pop()
    elif comm[0]=="popleft":
        d.popleft()
print(" ".join(map(str,d)))

# Word Order

from collections import Counter

n=int(input())
words=[]
for i in range(n):
    words.append(input())
C=Counter(words)
print(len(C))
print(" ".join(map(str,C.values())))

# Company Logo

# I had to consult Python collections library for most_common method

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    s=input()
    C=Counter(sorted(s))
    C1=C.most_common(3)
    print(C1[0][0],C1[0][1])
    print(C1[1][0],C1[1][1])
    print(C1[2][0],C1[2][1])

# Piling Up!

from collections import deque

T=int(input())
for i in range(T):
    n=int(input())
    cubes=deque((map(int,input().split())))
    truth=1
    for j in range(len(cubes)-1):
        if(cubes[0]>=cubes[1]):
            cubes.popleft()
        elif(cubes[len(cubes)-1]>=cubes[len(cubes)-2]):
            cubes.pop()
        else:
            truth=truth-1
            break
    if(truth==1):
        print("Yes")
    else:
        print("No")

# Calendar Module

import calendar

m,d,y=map(int,input().split())
day=(calendar.day_name[calendar.weekday(y,m,d)])
print(day.upper())

# Time Delta

# I had to look up the definitions and methods of datetime library online

def time_delta(t1, t2):
    time1=datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
    time2=datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")

    return(str(int((abs(time1-time2).total_seconds()))))

# Exceptions

T=int(input())
for i in range(T):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)

# Zipped!

N,X=map(int,input().split())
l=[]
A=[]
for i in range(X):
    l=((map(float,input().split())))
    A+=[l]
for i in zip(*A):
    print(sum(i)/len(i))

# Athlete Sort

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nm=input().split()
    n=int(nm[0])
    m=int(nm[1])
    arr=[]
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k=int(input())
    for i in sorted(list(zip(*arr))[k]):
        for row in arr:
            if i==row[k]:
                print(*row)
                arr.remove(row)
                break

# ginortS

S=input()
up=[]
low=[]
odd=[]
even=[]
for char in S:
    if(char.isupper()):
        up.append(char)
    elif(char.islower()):
        low.append(char)
    elif(char.isalnum()):
        if(int(char)%2!=0):
            odd.append(char)
        else:
            even.append(char)
print("".join(sorted(low)+sorted(up)+sorted(odd)+sorted(even)))

# Map and Lambda Function

cube=lambda x: x*x*x
fib=[]

def fibonacci(n):
    for i in range(n):
        if(i==0):
            fib.append(0)
        elif(i==1):
            fib.append(1)
        else:
            fib.append(fib[i-1]+fib[i-2])
    return fib

# Re.split()

# I had to consult the re library in Python documentation

regex_pattern = r"[,.]"	

import re
print("\n".join(re.split(regex_pattern, input())))

# Detect Floating Point Number

# I had to check re library on the Web

import re

T=int(input())
for i in range(T):
    N=input()
    if(re.search(r"^[+-]?[0-9]*\.[0-9]+$",N)):
        print(True)
    else:
        print (False)

# Group(), Groups() & Groupdict()
 
import re

S=input()
el=re.search(r"([a-z0-9])\1+",S)
if(el):
    print(el.group(1))
else:
    print(-1)

# Re.findall() & Re.finditer()

# I had some difficulties with the correct expression of r"", library re document does not mention char "^" as not operator for expressions, despite using it

import re

S=input()
matches=re.findall(r"(?<=[^AEIOUaeiou])([AEIOUaeiou]{2,})[^AEIOUaeiou]", S)
s="\n".join(matches)
if(matches):
    print(s)
else:
    print(-1)

# Re.start() & Re.end()

import re

S=input()
k=input()
i=0
m=re.search(k,S)
if(m==None):
    print("(-1, -1)")
else:
    while len(k)+i<=len(S):
        m=re.search(k,S[i:i+len(k)])
        if(m):
            print("({}, {})".format(i+m.start(),i+m.end()-1))
        i+=1

# Validating Roman Numerals

# I needed to check re library document

regex_pattern=r"^(?=[MDCLXVI])M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))

# Validating phone numbers

import re

N=int(input())
for i in range(N):
    s=input()
    if(re.match(r"^[789]\d{9}$",s)):
        print("YES")
    else:
        print("NO")

# Validating and Parsing Email Addresses

import re
import email.utils

n=int(input())
for i in range(n):
    addr=[]
    addr=input().split()
    m=re.match(r"<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>",addr[1])
    if(m):
        print(addr[0],addr[1])

# Hex Color Code

import re

N=int(input())
for i in range(N):
    s=input()
    l=[]
    m=re.findall(r"(?<=.)#[0-9A-Fa-f]{3}\b|#[0-9A-Fa-f]{6}\b",s)
    l=list(m)
    for el in l:
        print(el)

# HTLML Parser - Part 1

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :",tag)
        for i in attrs:
            print("->", i[0],">",i[1])
    def handle_endtag(self, tag):
        print("End   :",tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :",tag)
        for i in attrs:
            print("->", i[0],">",i[1])

parser=MyHTMLParser()
n = int(input())
for i in range(n):
    parser.feed(input())

# HTLML Parser - Part 2

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data=="" or data=="\n":
            pass
        else:
            print(">>> Data")
            print(data)

    def handle_comment(self, data):
        lines=data.split("\n")
        if len(lines)==1:
            print(">>> Single-line Comment")
            print(data)
        else:
            print(">>> Multi-line Comment")
            print(data)
  

  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += "\n"
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Detect HTML Tags, Attributes and Attribute Values

# Code derives from modified HTLML Parser - Part 1 

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print("->", i[0],">",i[1])
    

parser=MyHTMLParser()
n = int(input())
for i in range(n):
    parser.feed(input())

# Validating UID

# I needed to check re library document

import re

T=int(input())
for i in range(T):
    s=input()
    m=re.match(r"^(?!.*(.).*\1)(?=(?:(.*[A-Z]){2,}))(?=(?:(.*\d){3,}))[a-zA-Z0-9]{10}$",     s)
    if(m):
        print("Valid")
    else:
        print("Invalid")

# Regex Substitution

import re 

def substitute(match):
    if(match.group(0)=="&&"):
        s="and"
        return s
    else:
        s="or"
        return s

N=int(input())
for i in range(N):
    print(re.sub(r"(?<= )(&&|\|\|)(?= )",substitute,input()))

# Validating Credit Card Numbers

# I had to check the re library document and Discussions for a more correct second r pattern, I could not figure out why my 6th output line for test 0 was "Valid"

import re

N=int(input())
for i in range(N):
    s=input()
    m1=re.match(r"^[5|4|6]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$",s)
    m2=re.search(r"[\d|-]*(\d)-?\1-?\1-?\1-?[\d|-]*",s)
    if(m1 and not m2):
        print("Valid")
    else:
        print("Invalid")

# Validating Postal Codes

regex_integer_in_range=r"^[1-9][\d]{5}$"	
regex_alternating_repetitive_digit_pair=r"(\d)(?=(\d\1))"	


import re
P = input()
print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# Matrix Script

# I don't understand why I cannot get the same output with Matrix_item=input().split()

import math
import os
import random
import re
import sys

first_multiple_input=input().rstrip().split()
n=int(first_multiple_input[0])
m=int(first_multiple_input[1])
matrix = []
for i in range(n):
    matrix_item=input()
    matrix.append(matrix_item)
cols=list(zip(*matrix))
l=[]
for i in cols:
    for el in i:
        l.append(el)
s="".join(l)
line=re.sub(r"(?<=([a-zA-Z0-9]))[\s$#%&]+(?=[a-zA-Z0-9])"," ",s)
print(line)

# XML 1 - Find the Score

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    number=len(node.attrib)
    for i in node:
        number+=get_attr_number(i)
    return(number)

if __name__=='__main__':
    sys.stdin.readline()
    xml=sys.stdin.read()
    tree=etree.ElementTree(etree.fromstring(xml))
    root=tree.getroot()
    print(get_attr_number(root))

# XML2 - Find the Maximum Depth

def depth(elem, level):
    global maxdepth
    level+=1
    if(level>=maxdepth):
        maxdepth=level
    for node in elem:
        depth(node,level)

# Standardize Mobile Number Using Decorators

# I had to consult materials concerning decorators

def wrapper(f):
    def fun(l):
        n=[]
        for i in l:
            
            if len(i)==10:
                n.append("+91 "+str(i[0:5]+" "+i[5:10]))
            elif len(i)==11:
                n.append("+91 "+str(i[1:6]+" "+i[6:11]))
            elif len(i)==12:
                n.append("+91 "+str(i[2:7]+" "+i[7:12]))
            elif len(i)==13:
                i=i[0:3]+" "+str(i[3:8])+" "+str(i[8:13])
                n.append(i)
            
        return f(n)
        
    return fun

# Decorators 2 - Name Directory

# I had to check the correct expression of lambda function on Discussions

import operator

def person_lister(f):
    def inner(p):
        p=sorted(p,key=lambda x: int(x[2]))
        pers=[]
        for i in range(len(p)):
            b=[]
            b=p[i]
            if b[3]=="M":
                s="Mr. "+b[0]+" "+b[1]
            else:
                s="Ms. "+b[0]+" "+b[1]
            pers.append(s)
        return pers
    return inner

# Arrays

def arrays(arr):
    a=[]
    j=-1
    for i in range(0,len(arr)):
        a.append(arr[j])
        j-=1
    a=numpy.array(a,float)
    return a

# Shape and Reshape

import numpy

arr=input()
a=list(map(int,arr.split(" ")))
a=numpy.array(a)
a.shape=(3,3)
print(a)

# Transpose and Flatten

import numpy

N,M=map(int,input().split(" "))
m=[]
for i in range(N):
    m.append(list(map(int,input().split(" "))))
m=numpy.array(m)
m1=numpy.transpose(m)
print(m1)
print(m.flatten())

# Concatenate

import numpy

N,M,P=map(int,input().split(" "))
m1=[]
m2=[]
for i in range(N):
    m1.append(list(map(int,input().split(" "))))
for i in range(M):
    m2.append(list(map(int,input().split(" "))))
m1=numpy.array(m1)
m2=numpy.array(m2)
print(numpy.concatenate((m1,m2),axis=0))

# Zeroes and Ones

import numpy

dimensions=tuple(map(int,input().split(" ")))
print(numpy.zeros((dimensions),dtype=numpy.int))
print(numpy.ones((dimensions),dtype=numpy.int))

# Eye and Identity

# I checked on Discussions about the bug in test cases, where there is a space before unit number in the output

import numpy

n,m=map(int,input().split(" "))
numpy.set_printoptions(sign=" ")
print(numpy.eye(n,m))

# Array Mathematics

import numpy

N,M=map(int,input().split(" "))
m1=[]
m2=[]
for i in range(N):
    m1.append(list(map(int,input().split(" "))))
for i in range(N):
    m2.append(list(map(int,input().split(" "))))
m1=numpy.array(m1)
m2=numpy.array(m2)
print(numpy.add(m1,m2))
print(numpy.subtract(m1,m2))
print(numpy.multiply(m1,m2))
d=numpy.array((numpy.divide(m1,m2)),int)
print(d)
print(numpy.mod(m1,m2))
print(numpy.power(m1,m2))

# Floor, Ceil and Rint

import numpy

A=list(map(float,input().split(" ")))
A=numpy.array(A)
numpy.set_printoptions(sign=" ")
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))

# Sum and Prod

import numpy

N,M=map(int,input().split(" "))
m=[]
for i in range(N):
    m.append(list(map(int,input().split(" "))))
m=numpy.array(m)
res=numpy.sum(m,axis=0)
print(numpy.prod(res,axis=None))

# Min and Max

import numpy

N,M=map(int,input().split(" "))
m=[]
for i in range(N):
    m.append(list(map(int,input().split(" "))))
m=numpy.array(m)
res=numpy.min(m,axis=1)
print(numpy.max(res))

# Mean, Var and Std

# I checked on Discussions for a bug in output format

import numpy


N,M=map(int,input().split(" "))
m=[]
for i in range(N):
    m.append(list(map(int,input().split(" "))))
m=numpy.array(m)
numpy.set_printoptions(sign=" ")
numpy.set_printoptions(legacy="1.13")
print(numpy.mean(m,axis=1))
print(numpy.var(m,axis=0))
print(numpy.std(m))

# Dot and Cross

import numpy

N=int(input())
m1=[]
m2=[]
res=[]
for i in range(N):
    m1.append(list(map(int,input().split(" "))))
for i in range(N):
    m2.append(list(map(int,input().split(" "))))
m1=numpy.array(m1)
m2=numpy.array(m2)
m2=numpy.transpose(m2)
for i in m1:
    l=[]
    for j in m2:
        l.append(numpy.dot(i,j))
    res.append(l)
res=numpy.array(res)
print(res)

# Inner and Outer

import numpy

A=list(map(int,input().split(" ")))
B=list(map(int,input().split(" ")))
A=numpy.array(A)
B=numpy.array(B)
print(numpy.inner(A,B))
print(numpy.outer(A,B))

# Polynomials

import numpy

coef=list(map(float,input().split(" ")))
x=float(input())
print(numpy.polyval(coef,x))

# Linear Algebra

# Originally I used "{:.2f}" in print() as requested, but there is a bug in the indentation of test case outputs, so I checked Discussions for set_printoptions() as in a few exercises above

import numpy

N=(int(input()))
m=[]
for i in range(N):
    m.append(list(map(float,input().split(" "))))
m=numpy.array(m)
numpy.set_printoptions(legacy='1.13')
print(numpy.linalg.det(m))

# Birthday Cake Candles

def birthdayCakeCandles(candles):
    count=1
    candles.sort()
    for i in range(len(candles)-1):
        if candles[i]==candles[-1]:
            count+=1
    return count

# Number Line Jumps

# I made a little modification: kangaroo prints the results instead of returning a string

def kangaroo(x1, v1, x2, v2):
    d0=x2-x1
    d1=(x2+v2)-(x1+v1)
    pace=d0-d1
    if d0>d1:
        if d0%(pace)==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    return

# Viral Advertising

def viralAdvertising(n):
    likes0=math.floor(5/2)
    likes1=likes0+math.floor((likes0*3)/2)
    re=likes1-likes0
    likes0=likes1
    count=likes1
    for i in range(3,n+1):
        likes1=likes0+math.floor((re*3)/2)
        count=likes1
        re=likes1-likes0
        likes0=likes1

    return count

# Recursive Digit Sum

# I had to modify code because first code did not finish in time limits

def superDigit(n, k):
    if len(n)==1:
        return n
    else:
        N=[]
        for i in range(0,k):
            for j in range(len(n)):
                N.append(int(n[j]))
                digits=0
            digits+=sum(N)
        return superDigit((str(digits)),1)

def superDigit(n, k):
    if len(n)==1:
        return n
    else:
        digits=0
        for i in range(len(n)):
            digits+=int(n[i])
    return superDigit(str(digits*k),1)

# Insertion Sort - Part 1

# I got some test cases wrong multiple times while the code was correct on online compiler, I inserted the input of the wrong test as a custom input and I managed to succeed

import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    z=arr[-1]
    arr[-1]=arr[-2]
    print(" ".join(map(str,arr)))
    for i in range(2,len(arr)):
        if(arr[-i-1]<arr[-i] and arr[-i-1]>z):
            arr[-i]=arr[-i-1]
            print(" ".join(map(str,arr)))
            if(i==len(arr)-1):
                arr[0]=z
                print(" ".join(map(str,arr)))
        if(arr[-i-1]<arr[-i] and arr[-i-1]<z):
            arr[-i]=z
            print(" ".join(map(str,arr)))
            break
        
        
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

# Insertion Sort - Part 2

# insertionSort1() is slightly modified from the version above

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    if(n==1):
        return arr
    elif(n==2):
        temp=arr[-2]
        arr[-2]=arr[-1]
        arr[-1]=temp
        return arr
    else:
        z=arr[-1]
        arr[-1]=arr[-2]
        for i in range(2,len(arr)):
            if(arr[-i-1]<arr[-i] and arr[-i-1]>z):
                arr[-i]=arr[-i-1]
                if(i==len(arr)-1):
                    arr[0]=z
            if(arr[-i-1]<arr[-i] and arr[-i-1]<z):
                arr[-i]=z
                break
    
    return arr

def insertionSort2(n, arr):
    if(len(arr)==1):
        print(" ".join(map(str,arr)))
    if(len(arr)==2):
        if(arr[-1]<=arr[-2]):
            temp=arr[-2]
            arr[-2]=arr[-1]
            arr[-1]=temp
            print(" ".join(map(str,arr)))
    if(len(arr)>=3):
        for i in range(1,len(arr)):
            if(arr[i]>arr[i-1]):
                print(" ".join(map(str,arr)))
            else:
                if(i!=len(arr)):
                    arr=insertionSort1(len(arr[:i+1]),arr[:i+1])+arr[i+1:]
                    print(" ".join(map(str,arr)))
                else:
                    arr=insertionSort1(len(arr[:i+1]),arr[:i])+arr[-1]
                    print(" ".join(map(str,arr)))

        



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)






















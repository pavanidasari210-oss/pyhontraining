# The main difference between device drivers and firmware is their purpose and scope
# A device driver is a software program that allows a computers operating system and other programs to access a devices hardware functions
# A firmware is a low level software that provides the core instructions for a devices operation,such as how to startup,communicate with other devices
# and perform basic inputoutput tasks


# A device driver is software that enables an operating system to communicate with a specific hardware component,
# acting as a translator between the hardware and higher-level software.
# Firmware is software embedded directly into hardware,
# providing low-level instructions for how the hardware should operate and perform its basic functions, often including startup routines


# str1="Pavani"           #pAVANI
# str2=str1.swapcase()
# print(str2)


# t=Thread(target=display)
# t.start()
# current_thread().getName()
# current_thread().setName("sunny")
# current_thread().ident
# active_count()
# t1.isAlive()

# multithreading
# executing several tasks simultaneously.
# process based multi tasking and thread based multi tasking
# process based multi tasking: executing several tasks simultaneously,where each task is a separate independent process.it is best suitable at os level

# thread based multitasking:executing each independent program in a single code as thread1 and thread2.each task is an independent process
# we should go for multithreading where ever independent jobs are there,in that case we use. at a time 60 threads can process siultaneously.module name is threading.
# adv is ...performance will be improved ,because the total job will be completed in the less time
# import threading
# print("current executing thread",threading.current_thread().getName())

# 2
# from threading import *
# def display():
#    print("child thread",current_thread().getName())
# t=Thread(target=display)
# t.start()
# print("main thread name",current_thread().getName())


# we can define thread in 3 ways
# creating a thread without using any class
# creating a thread by extending thread class
# creating a thread without extending the thread class.

# 1 without using any class,by using functional way
# from threading import *
# def display():
#    for i in range(10):      #this code executed by child thread
#        print("child thread")
# t=Thread(target=display)      #creating thread object
# t.start()                    #starting the thread
# for i in range(10):        #this code executed by main thread
#    print("main thread")


# 3  this is object oriented style
# from threading import *
# class MyThread(Thread):    #mythread is child class of tread
#    def run(self):      #run method is predefined method.start method will call run method internally.run name is fixed
#        for i in range(10):
#            print("child thread")
# t=MyThread()                        #create an object
# t.start()
# for i in range(10):
#    print("main thread")


# 4 without extending thread class,but still it is object oriented way only
# from threading import *
# class Test:
#    def m1(self):
#        for i in range(10):
#            print("child thread1")
# obj=Test()    # creating object
# t=Thread(target=obj.m1)   #creating thread oject for the target job.keyword aurgment shold be given as target
# t.start()
# for i in range(10):
#    print("main thread1")


# example of with and witout multithreading
# import time
# def doubles(numbers):
#    for n in numbers:
#        time.sleep(1)
#        print("double value is",2*n)

# def squares(numbers):
#    for n in numbers:
#        time.sleep(1)
#        print("square value is",n*n)
# numbers=[1,2,3,4,5,6]
# begintime=time.time()
# doubles(numbers)
# squares(numbers)
# endtime=time.time()
# print("total time taken",endtime-begintime) #total time taken 12.54543662071228


# import time
# from threading import *
# def doubles(numbers):
#    for n in numbers:
#        time.sleep(1)
#        print("double value is",2*n)
# def squares(numbers):
#    for n in numbers:
#        time.sleep(1)
#        print("square value is",n*n)
# numbers=[1,2,3,4,5,6]
# begintime=time.time()
# t1=Thread(target=doubles,args=(numbers,)) #args should be in tuple
# t2=Thread(target=squares,args=(numbers,))
# t1.start()
# t2.start()
# t1.join()   #main thread will wait untill t1 thread completes. if a thread wants to wait until completing some other thread,then we go for join method.
# t2.join()
# from here it is main thread
# endtime=time.time()
# print("total time taken",endtime-begintime) #total time taken 6.261850118637085


# how to get the name of a thread and set the name of a thread.
# from threading import *
# print(current_thread().getName())
# current_thread().setName("sunny")  or use  current_thread().name("sunny")
# print(current_thread().getName())  or use current_thread().name


# for every thread a unique number will be assigned by PVM
# thread identification number
# by using implicit variable: "ident"
# from threading import*
# def test():
#    print("child thread")
# t=Thread(target=test)
# t.start()
# print("main thread id num",current_thread().ident)
# print("child thread id num",t.ident)


# active_count() function :
# from threading import*
# import time
# def display():
#    print(current_thread().name,"...started")
#    time.sleep(3)
#    print(current_thread().name,"...ended")
# print("the nummber of active threads",active_count())
# t1=Thread(target=display,name="child thread1")
# t2=Thread(target=display,name="child thread2")
# t3=Thread(target=display,name="child thread3")
# t1.start()
# t2.start()
# t3.start()
# print("the nummber of active threads",active_count())
# time.sleep(10)
# print("the nummber of active threads",active_count())


# enumerate():  to listout the active current executing threads
# from threading import*
# import time
# def display():
#    print(current_thread().name,"...started")
#    time.sleep(3)
#    print(current_thread().name,"...ended")
# print("the nummber of active threads",active_count())
# t1=Thread(target=display,name="child thread1")
# t2=Thread(target=display,name="child thread2")
# t3=Thread(target=display,name="child thread3")
# t1.start()
# t2.start()
# t3.start()
# l=enumerate()
# for t in l:
#    print("thread name",t.name)
#    print("thread id",t.ident)
#    print()
# time.sleep(10)
# for t in l:
#    print("thread name",t.name)
#    print("thread id",t.ident)
#    print()


# isAlive()

# from threading import*
# import time
# def display():
#    print(current_thread().name,"...started")
#    time.sleep(3)
#    print(current_thread().name,"...ended")
# print("the nummber of active threads",active_count())
# t1=Thread(target=display,name="child thread1")
# t2=Thread(target=display,name="child thread2")
# t1.start()
# t2.start()
# print(t1.name,"is Alive",t1.isAlive()) #true
# print(t2.name,"is Alive",t2.isAlive()) #true
# time.sleep(10)
# print(t1.name,"is Alive",t1.isAlive()) #false
# print(t2.name,"is Alive",t2.isAlive()) #false


# join() method  if a thread wants to wait until completing some other thread then...we use join method.
# from threading import*
# import time
# def display():
#    for i in range(10):
#        print("seetha thread")
#        time.sleep(3)
# t=Thread(target=display)
# t.start()

# t.join(10)  #main thread will wait until  child thread completing.here 10 is in seconds, we will pass it as aurgment ,if required we will pass it.
# for i in range(10):
#    print("rama thread")


# iterators
# An iterator in Python is an object used to traverse through all the elements of a
# collection (like lists, tuples, or dictionaries) one element at a time.
# It follows the iterator protocol, which involves two key methods:
# __iter__(): Returns the iterator object itself.
# __next__(): Returns the next value from the sequence. Raises StopIteration when the sequence ends.


# s="GFG"
# it=iter(s)   #<str_ascii_iterator object at 0x0000016987208B80>
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))


# mytuple=("apple", "banana", "cherry")
# myit=iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))


# decorators
# Decorators act as wrapper for your original function.
# Common usecase of decorators is logging and timing.to measure the performance of function.
# Decorators solve both these issues.
# code duplication and cluttering the main logic of a function with additional functionality.
# It takes the functionas an aurgment
# @ is used as the decorator


# import time
# def time_it(func):
#    def wraper(*args,**kwargs):
#        start=time.time()
#        result=func(*args,**kwargs)
#        end=time.time()
#        print(func.__name__+" took "+str(end-start)*1000+"millisec")
#        return(result)
#    return(wraper)
# @time_it
# def cal_square(numbers):
#    result=[]
#    for number in numbers:
#        result.append(number**2)
#        return(result)
# @time_it
# def cal_cube(numbers):
#    result=[]
#    for number in numbers:
#        result.append(number**3)
#        return(result)
# array=range(1,100000)
# out_square=cal_square(array)
# out_cube=cal_cube(array)


# def greet():
#    print("HelloWorld")
# result=greet()   # Calling the function #HelloWorld
# print(result)


# def greet():
#    return "HelloWorld"
# result=greet()   # Store the return value
# print(result)    #HelloWorld


# print → for humans (shows info to the user).
# return → for programs (gives data back to the code).


# 1. Built-in Functions
# These are already provided by Python.
# Examples:

# print("Hello")        # prints output
# len("Python")         # returns length of string
# max([2, 8, 5])        # maximum value
# sum([1, 2, 3])        # sum of elements


# 2. User-defined Functions
# Functions written by the programmer using def.

# def greet(name):
#    return name
# print(greet("Pavani"))   #Pavani


# 3. Functions with Arguments
# Takes parameters as input.

# def add(a,b):
#    return a+b
# print(add(5,3))   # 8


# 4. Functions with Default Arguments
# Provides a default value if not passed.


# def greet(name="Guest"):
#    return name
# print(greet())       #Guest
# print(greet("Pavani")) #Pavani


# 5. Functions with Variable Arguments
# *args → accepts multiple positional arguments.
# **kwargs → accepts multiple keyword arguments.

# def total(*nums):
#    return sum(nums)
# print(total(1, 2, 3, 4))   # 10
# def info(**data):
#    return data
# print(info(name="Alice", age=25))
# {'name': 'Alice', 'age': 25}


# 6. Lambda (Anonymous) Functions
# One-line functions without def.
# square=lambda x:x*x
# print(square(5))   # 25


# 7. Recursive Functions
# Functions that call themselves.
# def factorial(n):
#    if n == 0:
#        return 1
#    return n * factorial(n-1)
# print(factorial(5))   # 120


# 8. Higher-order Functions
# Functions that take another function as input or return a function.
# def double(x): return x * 2
# nums = [1, 2, 3]
# print(list(map(double, nums)))   # [2, 4, 6]


# 9. Generator Functions
# Uses yield to return values one at a time (lazy evaluation).
# def counter():
#    for i in range(3):
#        yield i
# for num in counter():
#    print(num)   # 0, 1, 2


# 10. Decorators
# Special functions that modify other functions.
# def decorator(func):
#    def wrapper():
#        print("Before function")
#        func()
#        print("After function")
#    return wrapper
# @decorator
# def hello():
#    print("Hello!")
# hello()


# generators
# All generators are iterators,but all iterators are not generators
# generators are used to hold the sequence of values.
# The yield operator is used to define the generator concept
# Generator function is a function which returns the generator iterator with the help of yield keyword.
# yield is a keyword.
# if any function is having this keyword then it is called generator function
# yield keyword is like return in normal function.

# n=int(input("enter a number"))
# def fib(x):
#    a,b=0,1
#    for i in range(x):
#        yield(a)
#        a,b=b,(a+b)
# y=fib(n)
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))


# It is the ability of the object to adopt the code to the type of data precision.
# Polymorphism helps to define a action,regardless the type of object
# polymorphism example
# def add(a,b):
#    return (a+b)

# print(add(3,4))                  # Integer addition
# print(add("Hello," , "World!"))  # String concatenation
# print(add([1, 2], [3, 4]))       # List concatenation


#####operator overloading  Note: magic methods are used here

# when ever we r calling + operator then __add__()method will be called
# when ever we r printing Book object reference then __str__() method willl be called

# class Book:
#    def __init__(self,pages):
#        self.pages=pages
#    def __str__(self):
#        return "the number of pages:"+str(self.pages)
#    def __add__(self,other):
#        total=self.pages+other.pages
#        b=Book(total)
#        return b
#    def __mul__(self,other):
#        total=self.pages*other.pages
#        b=Book(total)
#        return b
# b1=Book(300)
# b2=Book(200)
# b3=Book(100)
# b4=Book(700)
# print(b1+b2*b3+b4)  #book object


# class Book:
#    def __init__(self,pages):
#        self.pages=pages
#    def __str__(self):
#        return "the number of pages:"+str(self.pages)
#    def __add__(self,other):
#        total=self.pages+other.pages
#        b=Book(total)
#        return b
# b1=Book(300)
# b2=Book(200)
# b3=Book(100)
# b4=Book(700)
# print(b1+b2+b3+b4)  #book object


#####methodoverloading :
# two methods are said to be overloaded if both are having same name but different aurgments.
# python wont provide support for methodoverloading and constructor overloading
# if overloading is not there then python will consider the last recent method

# class Test:
#    def m1(self):
#        print("no arg")
#    def m1(self,x):
#        print("one arg")
# t=Test()
# t.m1(10) #one arg


##constructor overloading
##class Test:
##    def __init__(self):
##        print("no arg constructor")
##    def __init__(self,a):
##        print("one arg constructor")
##    def __init__(self,a,b):
##        print("two arg constructor")
##t=Test(10,20)                                ## two arg constructor


# method overriding


# class 14
# default aurgments and variable length aurgments


# a=input("enter a number")
# sum=0
# sum1=0
# for i in range(0,len(a)):
#    if i%2==0:
#        sum=sum+int(a[i])
#    if i%2!=0:
#        sum1=sum1+int(a[i])
#    if (sum-sum1)==0 or (sum-sum1)%11==0:
#        print("given number divides by 11")
# else :
#    print("No")


# a=int(input("enter a number"))
# if a%11==0:
#    print("ok")
# else :
#    print("notok")


# str1="printing hello world is not at all a matter"
# l=str1.split(" ")    #['matter', 'a', 'all', 'at', 'not', 'is', 'world', 'hello', 'printing']
# l.reverse()
# print(l)

# str1="printing hello world is not at all a matter"     #matter a all at not is world hello printing
# l=str1.split(" ")
# for i in range(len(l)-1,-1,-1):
#    print(l[i],end=" ")

# str1="printing hello world is not at all a matter"
# l=str1.split(" ")    #['world', 'printing', 'not', 'matter', 'is', 'hello', 'at', 'all', 'a']
# l.sort(reverse=True)
# print(l)


# l1=[[233,234,235],[466,869,346],[757,123,678]]
# l2=[[233,234,235],[466,869,346],[757,123,678]]
# l4=[]
# for i in range(len(l1)):
#    for j in range(len(l2)):
#        k=l1[i][j]+l2[i][j]
#        l4.append(k)
# print(l4)


# l1=[33,21,34,56,67]
# l2=[11,42,93,16,25]
# d={}
# for i in range(len(l1)):
#        d[l1[i]]=l2[i]
# print(d)


# l1=[33,21,34,56,67]
# l2=[11,42,93,16,25]
# l3=[]
# for i in range(len(l1)):
#    for j in range(len(l2)):
#        if i==j:
#            k=l1[i]+l2[i]
#            l3.append(k)
# print(l3)


# class student :
#    def __init__(self,name,rollno):
#        self.name=name
#        self.rollno=rollno
#    def talk(self):
#        print("Hello my nameis :",self.name)
#        print("my roll no is:",self.rollno)
# s=student("sunney",100)
# s.talk()
# s1=student(200,"bunney")
# s1.talk()
##print(s.name)
##print(s.rollno)


# deleting instance variables

# class test:
#    def __init__(self):
#        self.a=10
#        self.b=20
#        self.c=30
#    def delete(self):
#        del self.b
#        del self.c
# t1=test()
# print(t1.__dict__)  #{'a': 10, 'b': 20, 'c': 30}
# t1.delete()
# print(t1.__dict__)  #{'a': 10}
# del t1.a


# class test:
#    def __init__(self):
#        self.a=10
#        self.b=20
#        self.c=30
# t1=test()
# t2=test()
# del t1.a
# del t2.b
# print(t1.__dict__)  #{'b': 20, 'c': 30}
# print(t2.__dict__)  #{'a': 10, 'c': 30}


# str1="python interview is going on"    #nohtyp weivretni si gniog no
# l=str1.split(" ")
# l1=[]
# for i in l:
#    k=i[::-1]
#    l1.append(k)
# for i in l1:
#    str2=" ".join(l1)
# print(str2)


# import time
# def time_it(func):
#    def wraper(*args,**kwargs):
#        start=time.time()
#        result=func(*args,**kwargs)
#        end=time.time()
#        print(func.__name__+" took "+str(end-start)*1000+"millisec")
#        return(result)
#    return(wraper)
# @time_it
# def cal_square(numbers):
#    result=[]
#    for number in numbers:
#        result.append(number**2)
#        return(result)
# @time_it
# def cal_cube(numbers):
#    result=[]
#    for number in numbers:
#        result.append(number**3)
#        return(result)
# array=range(1,100000)
# out_square=cal_square(array)
# out_cube=cal_cube(array)


# import re
# f=open("file.txt","r")
# f1=f.read()
# print(f1)
# s=list(f1.split("\n"))
# print(s)
# for i in s:
#    result=re.findall('@\w+',i)
# print(result)


# n=int(input("enter a number"))
# def fact(n):
#    if n==1:
#        return(1)
#    else:
#        return(n*fact(n-1))
# print(fact(n))


# n=int(input("enter a number"))
# def fib(x):
#    a,b=0,1
#    for i in range(x):
#        print(a)
#        a,b=b,(a+b)
# y=fib(n)


# n=int(input("enter upper limit"))
# for i in range(2,n+1):
#    for j in range(2,i//2+1):
#        if i%j==0:
#            break;
#    else:
#        print(i)


# n=int(input("Enter a number:"))
# if n>1:
#    for i in range(2,n//2):
#        if(n%i)==0:
#            print(n,"is not a prime number")
#            break
#    else:
#        print(n,"is a prime number")


# n=int(input("enter a number"))
# fact=lambda n:1 if n==0 else n*fact(n-1)
# print(fact(n))


# import math
# n=int(input("enter a number"))
# result=math.factorial(n)
# print(result)


# import time
# print(time.asctime())


# l1=[7,2,10,3,8]
# l1.sort()
# print(l1)
# l=sorted(l1,reverse=True)
# print(l)


# import functools
# num=[1,2,3,4]
# l=functools.reduce(lambda x,y:x+y,num)
# print(l)

# l1=[13,12,25,32,26]
# l=list(filter(lambda x:x%13==0,l1))
# print(l)

# a=[1,2,3,4]
# b=[1,1,1,1]
# k=list(map(lambda x,y :x+y,a,b))
# print(k)


# import re
# p=input("enter password")
# X=True
# while X:
#    if (len(p)<6 or len(p)>12):
#        break
#    elif not re.search("[a-z]",p):
#        break
#    elif not re.search("[0-9]",p):
#        break
#    elif not re.search("[A-Z]",p):
#        break
#    elif not re.search("[$#@]",p):
#        break
#    elif re.search("\s",p):
#        break
#    else:
#        print("valid password")
#        X=False
#        break
# if X:
#    print("not valid password")


# p=input("enter password")
# for i in p:
#    if (i.isdigit() or i.isalpha() or i.isupper() or i.islower() or i=="$" or i=="@" or i=="#" or i=="%") and (len(p)>=12):
#        print("valid password")
#    else:
#        print("invalid password")


# import re
# str1="community in india abc@gmail.com and xyz@hotmail.com date is 25-02-1234 and ip is 10.140.32.80 another date is 23-12-1993 and phone number is has two 7625197646 8008883514 mac is A0:F2:D8:C7:A5"


# words=re.findall("\w+",str1)

# mac=re.search("(([A-F0-9]{2}\:){4}[A-F0-9]{2})",str1)

# phonenum=re.findall("[7-9]{1}[0-9]{9}",str1)

# ip=re.search(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})",str1)

# date=re.findall("\d{2}-\d{2}-\d{4}",str1)

# gmail=re.findall('@\w+',str1)

# gmailcom=re.findall('@\w+.\w+',str1)


# print(ip.group())

# print(mac.group())
# print(phonenum)
# print(date)
# print(gmail)
# print(gmailcom)
# print(words)


##valid and invalid ips

# import re
# str1="community in india abc@gmail.com and xyz@hotmail.com date is 25-02-1234 and ip is 10.140.32.80 and 10.140.32.801  another date is 23-12-1993 and phone number is has two 7625197646 8008883514 mac is A0:F2:D8:C7:A5"
# l=str1.split(" ")
# l1=[]
# for i in l:
#    ip=re.search(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", i)
#    if ip:
#        l1.append(ip)   # store the match object, not just the string
# for i in l1:
#    a,b,c,d=int(i.group(1)),int(i.group(2)),int(i.group(3)),int(i.group(4))
#    if 0<=a<=255 and 0<=b<=255 and 0<=c<=255 and 0<=d<=255:
#        print(i.group(), "is  valid IP")
#    else:
#        print(i.group(), "is invalid IP")


# import re
# text="Order numbers are 123, 456 and 789"
# extract_numbers=lambda s:re.findall(r"\d+",s)
# print(extract_numbers(text))  #Here you are calling the lambda function and passing text


# IMP
# import re
# f=open("file.txt","r")
# f1=f.read()
# s=f1.split("\n")
# k=" ".join(s)
# l=k.split(" ")
# for i in l:
#    result=re.search("(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})",i)
#    if result:
#        print(result.group())


# str1="a2b2c3"
# f=""
# for i in str1:
#    if i.isalpha():
#        k=i
#    else:
#        f=f+k*int(i)
# print(f)


# l=[7,2,3,4,8,1,9,5,6]
# l1=sorted(l)
# l2=sorted(l,reverse=True)
# print(l1)
# print(l2)

# numbers=[5, 2, 9, 1, 7]
# sorted_list=[x for x in sorted(numbers)]


# str1="AXMPT6599E"
# str2=""
# for i in str1:
#    if i.isalpha():
#        str2=str2+i
# print(str2)


# t=((3,8),(2,9),(1,10),(4,7))
# t1=sorted(t)
# t2=sorted(t,reverse=True)
# print(t1)
# print(t2)

# d={3:"e",2:"a",1:"c",7:"b",5:"d"}
# d1=sorted(d)
# d2=sorted(d.keys())
# d3=sorted(d.values())
# print(d1)
# print(d2)
# print(d3)


# l=[7,2,3,4,8,1,9,5,6]
# for i in range(0,len(l)):
#    for j in range(i+1,len(l)):
#        if l[i]>l[j]:
#            l[i],l[j]=l[j],l[i]
# print(l)


# l=[1,2,3,4]
# l1=[]
# for i in range(len(l)-1,-1,-1):
#    l1.append(l[i])
# print(l1)


# all words in file
# import re
# f=open("file.txt","r")
# f1=f.read()
# s=f1.split("\n")
# k=" ".join(s)
# l=k.split(" ")
# print(l)


# l=[1010,1000,1100,1101]
# l1=[]
# for i in l:
#    k=int(str(i),2)
#    l1.append(k)
# print(l1)


# l=[2,3,4,8,10]
# l1=[]
# for i in l:
#    k=bin(i)
#    l1.append(k)
# print(l1)


# l=[(10,5,2),(12,15,1),(18,1,10)]
# l1=[]
# l2=[]
# for i in l:
#    k=list(i)
#    l1.append(k)
# for i in l1:
#    i[0],i[1]=i[1],i[0]
# for i in l1:
#    a=tuple(i)
#    l2.append(a)
# print(l2)


# Packing → many values → one tuple.
# Unpacking → one tuple → many values.

fruits = "apple", "banana", "grapes"
print(fruits)  # ('apple', 'banana', 'grapes')
print(type(fruits))

# students = [("Alice", 21, "Computer Science"),("Bob", 22, "Mathematics"),("Charlie", 20, "Physics")]
# Unpacking inside the loop
# for name,age,major in students:
#    print(f"Name:{name},Age:{age},Major:{major}")

# output:
# Name:Alice,Age:21,Major:Computer Science
# Name:Bob,Age:22,Major:Mathematics
# Name:Charlie,Age:20,Major:Physics


# l2=[(3,7),(1,10),(2,9)]
# def sortbysec(element):
#    return element[1]
# l2.sort(key=sortbysec)
# print(l2)


# str1="pavani learning python in online"
# l=str1.split(" ")
# l1=[]
# for i in range(len(l)-1,-1,-1):
#    l1.append(l[i])
#    str2=" ".join(l1)
# print(str2)


# str1="pavani learning python in online"
# str2=""
# for i in range(len(str1)-1,-1,-1):
#    str2=str2+str1[i]
# print(str2)


# l=[21,34,23,32,89,45]
# if len(l)%2==0:
#    print("middle num cant be find")
# if len(l)%2!=0:
#    print(l[int(len(l)/2)])


# str1="abc"            #output  adbecf
# str2="def"
# l1=[]
# l2=[]
# l3=[]
# for i in str1:
#    l1.append(i)
# for i in str2:
#    l2.append(i)
# for i in range(len(l1)):
#    for j in range(len(l2)):
#        if i==j:
#            k=l1[i]+l2[i]
#            l3.append(k)
# for i in l3:
#    str3="".join(l3)
# print(str3)


# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))


# n=int(input("enter a number"))
# def fib(x):
#    a,b=0,1
#    for i in range(x):
#        yield(a)
#        a,b=b,(a+b)
# y=fib(n)
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))


# d={"pavani":2,"python":3}   #output {'pavani': 2, 'python': 3, 'learning': 4}
# d1={"learning":4}
# d.update(d1)
# print(d)


# d={'pavani':2,'python':3,'learning':4}     #output  {'pavani': 2, 'python': 3, 'learning': 4, 'bhanu': 4}
# print(d.setdefault("bhanu",4))
# print(d)


# l=[1,56,22,34,90,23,1]   #output {1: 1, 56: 1, 22: 1, 34: 1, 90: 1, 23: 1}
# d={}
# d1=d.fromkeys(l,1)
# print(d1)

# find missing number
# l=[23,22,21,25,26]
# list1=[]
# for num in range(min(l),max(l)+1):
#        if num not in list1:
#            list1.append(num)
# print(list1)
# print(set(list1)-set(l))


# missing letter
# l=["a","b","c","e","f"]
# l1=[]
# l2=[]
# for i in l:
#    k=ord(i)
#    l1.append(k)
#    for i in range(min(l1),max(l1)+1):
#        if i not in l2:
#            l2.append(i)
#            k=set(l2)-set(l1)
#            for i in k:
#                k1=chr(i)
# print(k1)


# max sum in sublist
# l=[1,2,3,4,5,6,7,8,9,10,11,12]
# l2=[]
# l1=[]
# for i in range(0,len(l),3):
#    sublists=l[i:i+3]
#    l2.append(sublists)
# print(l2)
# for i in l2:
#    k=sum(i)
#    l1.append(k)
# print(max(l1),i)


# fing max length of the word of ["pavani","basava","karthik","navaneeth"]
#
# l=["pavani","basava","karthik","navaneeth"]
# print(max(l,key=len))
# l1=[]
# for i in l:
#    k=len(i)
#    l1.append(k)
# print(max(l1),i)


# Longest Palindromic Substring
# s="madamkataaaat"
# l=[]
# for i in range(len(s)):
#    for j in range(i+1,len(s)+1):
#        temp=s[i:j]
#        if temp==temp[::-1]:
#            l.append(temp)
# print(max(l,key=len))
# print(l)


# Longest Substring Without Repeating Characters
# s="madamkataaaat"
# l=[]
# l1=[]
# l2=[]
# for i in range(len(s)):
#    for j in range(i+1,len(s)+1):
#        temp=s[i:j]
#        l.append(temp)
# for i in l:
#    k=set(i)
#    l1.append(k)
#    for i in l1:
#        k="".join(i)
#        l2.append(k)
# print(max(l2,key=len))


# l=[1,2,3,4]   #[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# import itertools
# permutations=list(itertools.permutations(l))
# print(permutations)


# import itertools     #[(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]  for step 2
# l=[1,2,3,4,5]           #[(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]  for step 3
# r=int(input("enter step:"))
# combinations=list(itertools.combinations(l,r))
# print(combinations)


# l1=[1,2,3,4,5]
# l2=[4,6]
# print(l1+l2)


# import re            #['1', '2', '3', '4']
# str1="123khf#$%&43"
# l=re.findall("\d",str1)
# print(l)

# \d = "just one digit"
# \d+ = "a complete number"

# match = “does the string START with this?”
# search = “does the string CONTAIN this anywhere?”

# str1="123khf#$%&"      #['1', '2', '3']
# l=[]
# for i in str1:
#    if i.isdigit():
#        l.append(i)
# print(l)


# str1="PavaniLearningPythonu"        #P1v1n9L51rn9ngPyth15n21
# str2=""
# for i in range(0,len(str1)):
#    if str1[i]=="a" or  str1[i]=="e" or str1[i]=="i" or str1[i]=="o" or str1[i]=="u":
#        print(ord(str1[i])-96,end="")
#    else:
#        print(str1[i],end="")

# print(ord("a"))  #97

# str1="PavaniLearningPython"   #pAVANIlEARNINGpYTHON
# str2=""
# for i in str1:
#    if i.isupper():
#        str2=str2+i.lower()
#    if i.islower():
#        str2=str2+i.upper()
# print(str2)


# str1="pavanilearningpython"   #pAvAnIlEArnIngpythOn
# str2=" "
# for i in str1:
#    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#        str2=str2+i.upper()
#    else:
#        str2=str2+i
# print(str2)


# l1=["eat", "sleep", "repeat"]   #[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
# obj1=enumerate(l1)
# print(list(obj1))


# s1="geek"           #[(0, 'g'), (1, 'e'), (2, 'e'), (3, 'k')]
# print(list(enumerate(s1)))


# s1="geek"           #[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]
# print(list(enumerate(s1,2)))


# single inheritance:
# ====================
# class P:
#    def m1(self):
#        print("parentmethod")
# class c(P):
#    def m2(self):
#        print("child methid")
# C=c()
# C.m1()      #parentmethod
# C.m2()      #child methid

# multilevel inheritance:
# =======================
# class P:
#    def m1(self):
#        print("parentmethod")
# class c(P):
#    def m2(self):
#        print("child methid")
# class cc(c):
#    def m3(self):
#        print("subchild methid")
# C=cc()
# C.m1()      #parentmethod
# C.m2()      #child methid
# C.m3()      #subchild methid

# hirerchical inheritance:
# =========================
# class P:
#    def m1(self):
#        print("parentmethod")
# class c1(P):
#    def m2(self):
#        print("child1 methid")
# class c2(P):
#    def m3(self):
#        print("child2 methid")
# C=c1()
# C.m1()    #parentmethod
# C.m2()    #child1 methid
# C1=c2()
# C1.m1()   #parentmethod
# C1.m3()   #child2 methid

# multiple inheritance:
# ======================             #parent1 method
# class P1:
#    def m1(self):
#        print("parent1 method")
# class P2:
#    def m1(self):
#        print("parent2 method")
# class c(P1,P2):pass
# C=c()
# C.m1()


# class p:                            #[<class '__main__.c'>, <class '__main__.p'>, <class 'object'>]
#    def m1(self):
#        print("parent method")
# class c(p):pass
# print(c.mro())


# class p:                            #[<class '__main__.p'>, <class 'object'>]
#    def m1(self):
#        print("parent method")
# class c(p):pass
# print(p.mro())


# class A:pass
# class B(A):pass
# class C(A):pass
# class D(B,C):pass
# print(A.mro())
# print(B.mro())
# print(C.mro())
# print(D.mro())

# output
# [<class '__main__.A'>, <class 'object'>]
# [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
# [<class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


# class A:                            #D class method                                     #A  a is child of object(in python object class is parent class)
#    def m1(self):
#        print("A class method")                                             #B child                #C child
# class B(A):
#    def m1(self):                                                                       #D child
#        print("B class method")
# class C(A):
#    def m1(self):
#        print("C class method")
# class D(B,C):
#    def m1(self):
#        print("D class method")
# d=D()
# d.m1()


# class A:                            #B class method
#    def m1(self):
#        print("A class method")
# class B(A):
#    def m1(self):
#        print("B class method")
# class C(A):
#    def m1(self):
#        print("C class method")
# class D(B,C):pass
# d=D()
# d.m1()


# class A:                            #C class method
#    def m1(self):
#        print("A class method")
# class B(A):pass
# class C(A):
#    def m1(self):
#        print("C class method")
# class D(B,C):pass
# d=D()
# d.m1()


# class A:                            #A class method
#    def m1(self):
#        print("A class method")
# class B(A):pass
# class C(A):pass
# class D(B,C):pass
# d=D()
# d.m1()


# class A:pass                        #AttributeError: 'D' object has no attribute 'm1'
# class B(A):pass
# class C(A):pass
# class D(B,C):pass
# d=D()
# d.m1()


# l=["flower","flow","flight"]
# f=str1[0]
# l=str1[len(str1)-1]
# str1=""
# s=""
# for i in range(len(min(f,l))):
#    if l[i]==f[i]:
#        s+=l[i]
#    else:
#        break
# print(s)


# import sys
# print(sys.ps2)


# l=[2,6,10,14,18,22]  #[14, 18, 22]
# print(l[-3:])

# print('{1} and {0}'.format('test','run'))  #run and test


# x=set("ospsowupsw")     #{'u', 'p', 'w', 's', 'o'}
# print(x)


# import re                               #['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
# line="asdf fjdk;afed,fjek,asdf,foo"
# res=re.split('[;,\s]',line)
# print(res)

# import re                               #asdf fjdk afed fjek asdf foo
# line="asdf fjdk;afed,fjek,asdf,foo"
# res=re.sub('[;,\s]'," ",line)
# print(res)

# from datetime import datetime
# date1=datetime(2024, 11, 30)
# date2=datetime(2023, 11, 30)
# difference=date1-date2
# days_between=difference.days
# print(days_between)
# print(date1.date())
# print(date2.date())
# print(f"The number of days between {date1.date()} and {date2.date()} is {days_between} days.")


# str1="bangalore"
# print(str1[0:6])
# print(str1[2:6])
# print(str1[0:])
# print(str1[:6])
# print(str1[-1:])
# print(str1[::-1])


# bangal
# ngal
# bangalore
# bangal
# e
# erolagnab


# str1="Hi"               #Hihello
# str2="hello"
# print(str1+str2)

# str1="Hi"               #HiHiHiHiHi
# print(str1*5)


# str1="python is a language"
# print(str1.capitalize())     #Python is a language
# print(str1.center(30,"*"))   #*****python is a language*****
# print(str1.title())             #Python Is A Language
# print(str1.find("a"))           #10
# print(str1.find("a",0,5))       #-1
# print(str1.find("a",0,15))      #10


# print(str1.startswith("a",0,15)) #False
# print(str1.startswith("python",0,15)) #True
# print(str1.endswith("a",0,15))
# print(str1.endswith("language",0,15))


# str1="    baba is powerful god  "
# print(str1)
# print(str1.strip())
# print(str1.lstrip())
# print(str1.rstrip())


# str1="python is a language python"
# str2=str1.replace("python","pavani",1)
# print(str2)


# for i in range(0,10,1):
#    print(i,end="")         #0123456789


# for i in range(0,10,2):     #02468
#    print(i,end="")


# for i in range(1,10,2):     #13579
#    print(i,end="")


# for i in range(10,0,-1):  #10987654321
#    print(i,end="")

# for i in range(-4,-1,1):  #-4-3-2
#    print(i,end="")

# for i in range(-4,-7,-1):  #-4-5-6
#    print(i,end="")


# for i in range(-4,-1,-1):  #
#    print(i,end="")


# str1="python is good to learn"  #['python', 'is', 'good', 'to', 'learn']
# l=str1.split(" ")
# print(l)


# str1="PAvaNi"                #paVAnI
# for i in str1:
#    if i.islower():
#        print(i.upper(),end="")
#    if i.isupper():
#        print(i.lower(),end="")


# l=[1,4,5,8,23]
# l.append(3)
# print(l)                #[1, 4, 5, 8, 23, 3]


# l=[1, 4, 5, 8, 23]      #[1, 3, 4, 5, 8, 23]
# l.insert(1,3)
# print(l)


# l1=[1,4,5,8,23]        #[1, 4, 5, 8, 23, 45, 12, 67, 20]
# l2=[45,12,67,20]
# l1.extend(l2)
# print(l1)


# l1=[1, 4, 5, 8, 23, 45, 12, 67, 20]    #[1, 4, 5, 8, 45, 12, 67, 20]
# l1.pop(4)
# print(l1)


# l1=[1, 4, 5, 8, 23, 3]    #[1, 4, 8, 23, 3]
# l1.remove(5)
# print(l1)


# l1=[1, 4, 5, 8, 23, 45, 12, 67, 20]    #[1, 4, 5, 8, 45, 12, 67, 20, 23]
# k=l1.pop(4)
# l1.append(k)
# print(l1)


# l1=[1, 4, 5, 8, 23, 45, 12, 67, 20]     #[1, 4, 5, 8, 12, 20, 23, 45, 67]
# l1.sort()
# print(l1)


# l1=[1, 4, 5, 8, 23, 45, 12, 67, 20]      #[20, 67, 12, 45, 23, 8, 5, 4, 1]
# l1.reverse()
# print(l1)


# l1=[1,3,6,23,4,1,5,10]      #2
# l=l1.count(1)
# print(l)


# l1=[1,3,6,23,4,1,5,10]
# print(len(l1))      #8
# print(max(l1))      #23
# print(min(l1))      #1


# str1="10-20-30-40-50"      #['10', '20', '30', '40', '50']
# l=str1.split("-")
# print(l)


# l=['10', '20', '30', '40', '50']    #10-20-30-40-50
# str2="-".join(l)
# print(str2)


# l1=[1,3,6,23,4,1,5,10]     #[10, 5, 1, 4, 23, 6, 3, 1]
# l2=l1[::-1]
# print(l2)


# l1=[1,3,6,23,4,1,5,10]        #[10, 5, 1, 4, 23, 6, 3, 1]
# l2=[]
# for i in range(len(l1)-1,-1,-1):
#    l2.append(l1[i])
# print(l2)


# l1=[1,3,6,23,4,1,5,10]         #53
# sum=0
# for i in l1:
#    sum=sum+i
# print(sum)


# l1=[1,3,6,23,4,1,5,10]      #16 37
# sum=0
# sum1=0
# for i in range(len(l1)):
#    if i%2==0:
#        sum=sum+l1[i]
#    if i%2!=0:
#        sum1=sum1+l1[i]
# print(sum,sum1)


# l1=[1,3,6,23,4,1,5,10]  #[1, 3, 23, 4, 1, 5, 10]
# del(l1[2])
# print(l1)


# d={"name":"python","id":"3","prio":"1"}      #{'name': 'python', 'id': '3', 'prio': '1', 'lan': 'java'}
# d["lan"]="java"
# print(d)


# d={"name":"python","id":"3","prio":"1"}       #{'name': 'oracle', 'id': '3', 'prio': '1'}
# d["name"]="oracle"
# print(d)


# d={'name': 'python', 'id': '3', 'prio': '1', 'lan': 'java'}      #['name', 'id', 'prio', 'lan']
# l=list(d.keys())
# print(l)


# d={'name': 'python', 'id': '3', 'prio': '1', 'lan': 'java'}      #['python', '3', '1', 'java']
# l=list(d.values())
# print(l)


# d={'name': 'python', 'id': '3', 'prio': '1', 'lan': 'java'}      #[('name', 'python'), ('id', '3'), ('prio', '1'), ('lan', 'java')]
# l=list(d.items())
# print(l)


# d={'name': 'python', 'id': '3', 'prio': '1', 'lan': 'java'}    #{'name': 'python', 'id': '3', 'prio': '1', 'lan': 'java', 'address': 'guntur'}
# d1={"address":"guntur"}
# d.update(d1)
# print(d)


# d={'name': 'python', 'id': '3', 'prio': '1', 'lan': 'java'}    #{}
# d.clear()
# print(d)


# d={'name': 'python', 'id': '3', 'prio': '1', 'lan': 'java'}
# d1=d.copy()
# print(d1)                   #{'name': 'python', 'id': '3', 'prio': '1', 'lan': 'java'}


# l=[1, 3, 23, 4, 1, 5, 10,4]    #{1: 1, 3: 1, 23: 1, 4: 1, 5: 1, 10: 1}
# d={}
# for i in l:
#    if i not in d:
#        d[i]=1
# print(d)


# l=[1, 3, 23, 4, 1, 5, 10,4]    #{1: 2, 3: 1, 23: 1, 4: 2, 5: 1, 10: 1}
# d={}
# for i in l:
#    if i not in d:
#        d[i]=1
#    else:
#        d[i]=d[i]+1
# print(d)


# d={'name': 'python', 'id': '3', 'prio': '1', 'lan': 'java'}       #{'python': 'name', '3': 'id', '1': 'prio', 'java': 'lan'}
# d1={}
# for i in d:
#    d1[d[i]]=i
# print(d1)


# l=[1, 3, 23, 4, 1, 5, 10,4]     #{1: 1, 3: 1, 23: 1, 4: 1, 5: 1, 10: 1}
# d={}
# d1=d.fromkeys(l,1)
# print(d1)


# d={'name': 'python', 'id': '3', 'prio': '1', 'lan': 'java'}     #3
# print(d.get("id"))


# d={'name': 'python', 'id': '3', 'prio': '1', 'lan': 'java'}       #{'name': 'python', 'id': '3', 'prio': '1', 'lan': 'java', 'bhanu': 4}
# d.setdefault("bhanu",4)
# print(d)


# a={"history","maths","physics","computers"}
# b={"history","maths","art","dsign"}
# print(a.intersection(b))                    #{'history', 'maths'}
# print(a.union(b))                           #{'design', 'maths', 'computers', 'physics', 'art', 'history'}
# print(a.difference(b))                      #{'computers', 'physics'}


# frozen sets doubt

# normal_set=set(["a","b","c"])
# normal_set.add("d")
# print(normal_set)


# frozen_set=frozenset(["e","f","g"])
# print(frozen_set)


##expression , forloop
# print([i for i in range(1,11)])
# print([i for i in range(1,11) if i%2==0])
# print([i if i>2 else  i+1 for i in range(1,11)])


# words=["hello","a","amul"]
# print([i.upper() for i in words])

# l=[1,2,3,4]    #[10, 20, 30, 40]
# l1=[i*10 for i in l]
# print(l1)


# a=[1,2,3,4]     #[7, 7, 10, 12]
# c=[6,5,7,8]
# l=[a[i]+c[i] for i in range(0,len(a))]
# print(l)


# a=[1,2,3,4]
# b=[6,5,7,8]        #[7, 7, 10, 12]
# l=[x + y for x, y in zip(a, b)]
# print(l)


# l=[2,3,4,5]                 #[3, 2, 4, 5]
# l[0],l[1]=l[1],l[0]
# print(l)

# import os
# os.mkdir("")
# os.getcwd("")
# os.chdir("")
# os.listdir()
# os.environ.get("HOME")
# os.rename("pav.txt","ganga.txt")
# os.stat("demo.txt")
# os.walk()
# os.rmdir("amul")
# os.remove dirs("dir1/dir2")


# import copy
# l1=[10,20,[30,40],50]
# l2=copy.copy(l1)
# l1[0]=111
# l1[1]=222
# l1[2][0]=888
# l1[2][1]=999
# l1[3]=777
# print(l1)  #[111, 222, [888, 999], 777]
# print(l2)  #[10, 20, [888, 999], 50]


# import copy
# l1=[10,20,[30,40],50]
# l2=copy.deepcopy(l1)
# l1[0]=111
# l1[1]=222
# l1[2][0]=888
# l1[2][1]=999
# l1[3]=777
# print(l1)  #[111, 222, [888, 999], 777]
# print(l2)  #[10, 20, [30, 40], 50]


# import pickle
# class employee:
#    def __init__(self,eno,ename,esal,eaddr):
#        self.eno=eno
#        self.ename=ename
#        self.esal=esal
#        self.eaddr=eaddr
#    def display(self):
#        print(self.eno,self.ename,self.esal,self.eaddr)
# with open("emp.dat","wb") as f:
#    e=employee(100,"durga",1000,"hyd")
#    pickle.dump(e,f)
#    print("pickling of employee object completed")
# with open("emp.dat","rb") as f:
#    obj=pickle.load(f)
#    print("employee info after unpickling")
#    obj.display()
#    print(obj)


# str1="aabbccccdefffggaabbc"   #a4b4c5d1e1f3g2
# d={}
# for i in str1:
#    if i not in  d:
#        d[i]=1
#    else:
#        d[i]=d[i]+1
# for i in d:
#    k=i+str(d[i])
#    print(k,end="")

#############################################################


# * matches 0 or more occurences of character before *

# . matches any single character(except new line)

# a*b  b,ab,aab,aaab,cab,acb,cab,bac  true
#     a false


# a.b  acb,aab,axb,acby  true
#     ab,cb false


# a*b.*y    by,bly,ably,ablmy   true
#          ay,ab             false

###########################################################


# import re
# a=input("enter string to match")
# out=re.search("a*b",a)
# if out:
#    print("pattern matched",a)
# else :
#    print("pattern not matched")


# import re
# a=input("enter string to match")
# out=re.search("a.b",a)
# if out:
#    print("pattern matched",a)
# else :
#    print("pattern not matched")

##########################################################################################################################
# import copy
# L=[1,2,3,4]
# L1=copy.deepcopy(L)
# L.append(5)
# print(L)   #[1, 2, 3, 4, 5]
# print(L1)  #[1, 2, 3, 4]
##############################################################################################################################
##############################################################################################################################
# 7.print the most repeated char count in a string
# str1="pavani"
# d={}
# for i in str1:
#    if i not in d:
#        d[i]=1
#    else:
#        d[i]=d[i]+1
# print(max(d.values()))

# 6.remove repeated elements in a string without using methods
# str1="pavani"
# str2=""
# for i in str1:
#   if i not in str2:
#       str2=str2+i
# print(str2)


# 5.find no of chars without using len in a string
# str1="madams"
# count=0
# for i in str1:
#    count=count+1
# print(count)

# find out the vowels in a string
# str1="madampavani"
# l=[]
# for i in str1:
#    if i=="a" or i=="e" or i=="i"or i=="o"or i=="u":
#        l.append(i)
# print(l)


# import re
# str1="madampavani"
# vowels=re.findall(r"\[aeiouAEIOU]",str1)
# print(vowels)


# 3.commmon characters in 2 strings
# str1="pavani"
# str2="basava"
# str3=set(str1).intersection(set(str2))
# print(str3)


# str1="pavani"
# str2="basava"
# str3=""

# for i in str1:
#    if i in str2 and i not in str3:
#        str3=str3+i
# print(str3)


# 5.Create a Function to return The position of a given element in a List
# l=["a","b","e","q","k"]
# print(tuple(enumerate(l)))


# Find the all the Words in string Starts with vowels
# str1="i am preparing for mock and I am attending interviews"  #['i', 'am', 'and', 'am', 'attending', 'interviews']
# l=str1.split(" ")
# l1=[]
# for i in l:

#    if i.startswith("a") or i.startswith("e") or i.startswith("i") or i.startswith("o") or i.startswith("u"):
#        l1.append(i)
# print(l1)


# import re    #['i', 'am', 'and', 'I', 'am', 'attending', 'interviews']
# str1="i am preparing for mock and I am attending interviews"
# vowels=re.findall(r"\b[aeiouAEIOU]\w*",str1)  #['i', 'am', 'and', 'I', 'am', 'attending', 'interviews']
# vowels=re.findall(r"\b[aeiouAEIOU]\w+",str1)  #['am', 'and', 'am', 'attending', 'interviews']
# print(vowels)


# S='AabBcD'
# print(S[-2:])


###tagnames
# div
# input  (inputboxes,checkboxes,radiobuttons)
# span
# form
# select (dropdownbox)
# img
# a      (link or anchortag)
# button
# li     (list item)
# td     (table data)
# th     (table header)
# tr     (table row)


###attributes
# name
# id
# type
# css
# class
# tag
# src
# href
# style
# placeholder
# value
# autocomplete
# data-testid
# autofocus
# area-label


# from selenim import webdriver
# from selenium.webdriver.chrome.service import service
# from selenium.webdriver.common.by import By
# serv_obj=service("c:\Drivers\chromedriver_win32\chromedriver.exe")
# driver=webdriver.chrome(service=serv_obj)
# driver.get("url")
# driver.maximize_window
# import time
# import os
# import requests as request
# from selenium.webdriver import ActionChains
# from selenium.webdriver import ActionChains.keys
# import openpyxl
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver.find_element("By.ID","").send_keys("")
# driver.find_element("By.NAME","").send_keys("")
# driver.find_element("By.TAG_NAME","")
# driver.find_element("By.CLASS_NAME","")
# driver.find_element("By.LINK_TEXT","").click()
# driver.find_element("By.PARTIAL_LINKTEXT","reg").click()
# driver.find_element("By.CSS_SELECTOR","input#email").send_keys("abc")
# driver.close()
# driver.quit()

# css selector
# tagname#Id
# tagname.class
# tagname[attribute=value]
# tagname.class[attribute=value]

# //tagname[@attribute="value"]
# //*[@id=""]

# selector hub

# full xpath and relative xpath


# Xpath options
# =============
# and
# or
# contains()
# starts_with()
# text()


# application commands
# =====================
# get()
# title
# current_url
# page_source


# find_element
# find_elements
# text
# get_attribute(value/id/name/type)


# conditional commands
# ====================
# is_displayed()
# is_enabled()
# is_selected()


# browsercommands
# ==================
# close()
# quit()

# navigational commands
# =======================
# back()
# forward()
# refresh()


# driver.implicitly_wait(10)


# mywait=webdriver(driver,pole_frequency=2,10,ignored_exceptions=[Nosuch Element Exception,Element Not visible Exception,Element Not Selectable Exception,Exception])
# searchlink=mywait.until(Ec.precence_of_element_located(By.XPATH,"\\h3[text()=selenium]"))

# drpcountry=Select(drpcountry_ele)
# drpcountry.Select_by_visible_text("")
# drpcountry.Select_by_value("")
# drpcountry.Select_by_index()


# myalert=driver.switch_to.alert
# myalert.accept()
# myalert.dismiss()
# myalert.text
# myalert.send_keys("")


# syntax to inject(to bypass url) : http://admin:admin@url

# Switch_to.frame(name of frame)
# Switch_to.frame(id of frame)
# Switch_to.frame(web element)
# Switch_to.frame(0)
# Switch_to.default_content()


# driver.Switch_to.frame(innerframe)
# driver.Switch_to.frame(outerframe)
# driver.Switch_to.parent_frame()

# switch_to.window(window id)
# driver.current_window_handle      ---->return window id of single webbrowser windows
# driver.window_handles           ------->return window ids of multiple browser windows


# options=webdriver.chrome options()
# options.add_aurgment("__disable__notification")   ---->to disable notification at browser level


# act=Actionchains(driver)
# Mousehover      act.move_to_element(admin).perform()
# Rightclick      act.context_click(element).perform()
# Doubleclick     double_click(element).perform()
# Drag and Drop   drag_and_drop(source,target).perform()
# slider          drag_and_drop_by_offset(element,xoffset,yoffset).perform()

# driver.execute_script("windows.scrollby(0,3000)"," ")
# driver.execute_script("return window.page Y offset;")


# act.key_down(keys.CONTROL).send_keys("a").key_up(keys.CONTROL).perform()
# act.key_down(keys.CONTROL).send_keys("c").key_up(keys.CONTROL).perform()
# act.send_keys(keys.TAB).perform()


# ops=webdriver.chromeoptions()
# ops.add_experimental_option("perfs",preferences)
# preferences = {
#    # 📂 Downloads
#    "download.default_directory": r"C:\Downloads",   # Set default download folder
#    "download.prompt_for_download": False,           # Don’t ask where to save
#    "profile.default_content_settings.popups": 0,    # Disable download popups

#    # 🔔 Notifications
#    "profile.default_content_setting_values.notifications": 2,  # 1 = allow, 2 = block

#    # 🖼️ Images
#    "profile.managed_default_content_settings.images": 2,       # 1 = show, 2 = block

#    # 🎥 Videos / Media
#    "profile.default_content_setting_values.media_stream_camera": 2, # Block camera
#    "profile.default_content_setting_values.media_stream_mic": 2,    # Block mic

#    # 🌐 GeoLocation
#    "profile.default_content_setting_values.geolocation": 2,    # Block location requests
# }

# driver.save_screenshot(path.png)
# driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")
# driver.get_screenshot_as_png()
# driver.get_screenshot_as_base64()


# Reglink=keys.CONTROL+keys.RETURN
# driver.switch_to.newwindow("tab")
# driver.switch_to.new_window("window")

# driver.get_cookies
# driver.add_cookie({})
# driver.delete_cookie(" ")
# driver.delete_all_cookies()


# import pytest                                            #py.test -s -v test.py
# @pytest.yield_fixture(scope="module")
# def setUptearDownClass():
#    print("setup class activity")
#    yield
#    print("teardownclass activity")
# @pytest.yield_fixture()
# def setUptearDown():
#    print("setup activity")
#    yield
#    print("teardown activity")

# def test_methodA(setUptearDownClass,setUptearDown):
#    print("test_methodA execution")
# def test_methodB(setUptearDownClass,setUptearDown):
#    print("test_methodB execution")


# output
# setup class activity

# setup activity
# test_methodA execution
# teardown activity

# setup activity
# test_methodB execution
# teardown activity

# teardownclass activity


# It supports fixtures, parameterization, plugins, and is widely used in automation.
# Test discovery is automatic (just prefix with test_).

# Rich plugin ecosystem (pytest-html, pytest-xdist, etc.).

# Supports fixtures and parameterization.

# Run specific file: pytest test_file.py

# Run specific function: pytest test_file.py::test_function

# @pytest.mark.skip(reason="Not implemented")

# @pytest.mark.parametrize("x,y,result", [(2,3,5), (4,5,9)])

# pip install pytest-xdist
# pytest -n 4   # runs tests in 4 parallel workers

# pip install pytest-html
# pytest --html=report.html

# pytest.raises  #handle expected exceptions

# pip install pytest-cov  #measure coverage
# pytest --cov=src/ --cov-report=html

# pytest-ordering module
# pip install pytest-ordering
# @pytest.mark.Run(order=n)

# @pytest.mark.parametrize enables u to build parameterised tests

# pytest.inj file is used to configure settings for things like test discovery,test execution and reporting

# pytest.skip()

# Xfail is used to indicate that a test is ikely to fail, whilw skip is used to indicate thhat
# a test is inapplicable or momentarily unavailable.when test is mark with xfail flag it is anticipates to fail,and pytest will record the failure as xfail
# when test is marked with skip flag,it will not run and will instead be rported as skipped by pytest

# pytest.raises is acontext manager that is used to test for exceptions in pytest

# assert is used to check whether a condition  is true,while assert not is used to check ehether a condition is false

# pytest -v -s test.py --html=results2.html
# py.test -v -s
# py.test -v -s test.py
# py.test -v -s test.py test1.py
# py.test -v -s test.py::test_test_methodB
###############################################################################################

# How do you run tests in parallel with Pytest?
# Install plugin: pip install pytest-xdist
# Run: pytest -n 4 (4 parallel workers).

# pip install pytest-html
# pytest --html=report.html
# pytest -v -s test.py --html=results2.html

# pip install pytest-cov  #measure coverage
# pytest --cov=src/ --cov-report=html

# pytest-ordering module
# pip install pytest-ordering
# @pytest.mark.Run(order=n)

# pytest-rerunfailures
# pytest --reruns 3

# pytest-django
# Special support for testing Django applications.

# pytest-flask

# Helpers for testing Flask web apps.
# pytest-mock
# Provides an easy way to use unittest.mock.
# Example:
# def test_api(mocker):
#    mocker.patch("requests.get", return_value="fake data")


# pytest-faker
# Use fake data generators in tests (names, emails, addresses).

# pytest-randomly
# Randomizes the test order → helps catch hidden test dependencies.

# pytest-selenium
# Provides Selenium fixtures & integration for browser automation.


# cd p4
# ls
# cd Automation_testcase
# p4 edit test.thpl
# p4 sync
# p4 resolve
# rvi test.thpl
# pwd
# p4 change    edit description to tc names, burt status fixed and add reviewers
# p4 change changenumber
# rbt post changenumber # url will generate here
# open url and add logs in notes,resolve error and publish
# incase want to do changes to the existin change number
# resolve the issues in file
# rbt post -r rbnumber changenumber
# p4 sync
# p4 resolve testpath
# p4 submit -c changeno  #checkin
# p4 revert file.txt


# nate framework
# nacl and pynacl are libraries

# import pytest
# import Hostrec
# from pynacl import Hostrec
# import re
# import time
# import sys
# import os
# import pynacl.apiset
# import pprint
# from pynacl import pass,fail
# from pynacl.client import client
# from pynacl import find_clients
# from pynacl.client.cexecute import CExecute
# from pynacl.ontap.node import Node
# from pynacl.transit.transit import Transit
# from pynacl.ontap.cluster importCluster,ClusterHA
# from pynacl.ontap.storage import StorageFailover
# from pynacl.ontap.storage.failover import StorageFailover_Component

# class Test_watchdog():


# re.findall(r"a.c", "abc aac acc adc")
# ['abc', 'aac', 'acc', 'adc']


# re.findall(r"^Hello", "Hello World")
# ['Hello']


# re.findall(r"World$", "Hello World")
# ['World']


# \d → digit


# \D → non-digit


# \w → word character (letters/digits/underscore)


# \W → non-word character


# \s → whitespace


# \S → non-whitespace


# re.findall(r"\d+", "My number is 1234 and code is 56")
# ['1234', '56']

# re.findall(r"\s", "Hello World")
# [' ']   (space found)

# re.findall(r"[aeiou]", "Hello World")
# ['e', 'o', 'o']

# re.findall(r"[^aeiou]", "Hello")
# ['H', 'l', 'l']   (non-vowels)

# * → 0 or more

# + → 1 or more

# ? → 0 or 1

# {n} → exactly n

# {n,} → n or more

# {n,m} → between n and m

# re.findall(r"ab*", "a ab abb abbb")
# ['a', 'ab', 'abb', 'abbb']

# re.findall(r"ab+", "a ab abb abbb")
# ['ab', 'abb', 'abbb']

# re.findall(r"ab?", "a ab abb abbb")
# ['a', 'ab', 'ab', 'ab']

# re.findall(r"(cat|dog)", "I love cat and dog")
# ['cat', 'dog']

# re.findall(r"\bcat\b", "cat scatter category")
# ['cat']

# text = "apple an 123 cat scatter category"
# print(re.findall(r"\b[aeiouAEIOU]\w*", text))
# ['apple', 'an']   (words starting with vowels)


# second highest repeting number
# l=[2,2,3,4,4,3,3,5,5,5,5,5,6,8,4,3,6,6,6,6,6,6]
# d={}
# d1={}
# for i in l:
#    if i not in d:
#        d[i]=1
#    else:
#        d[i]=d[i]+1
#        k=list(d.items())
# print(k)
# def sortbysec(element):
#    return element[1]
# k.sort(key=sortbysec)
# print(k)
# print(k[-2])


l = [2, 2, 3, 4, 4, 3, 3, 5, 5, 5, 5, 5, 6, 8, 4, 3, 6, 6, 6, 6, 6, 6]
s = set(l)
l1 = list(s)
k = l1[-2]
print(k, "repeted", l.count(k), "times")

# import re
# l1=[1,2,3,4,5,6,7,8,9,10,[2,3,[4,5]],"PYTHON"]
# for i in range(0,len(l1)):
#    if i%2==0:
#        print(l1[i],end="")
#    if str(l1[i]).isalpha():
#        print(l1[i])


# l1=[1,2,3,4,5,6,7,8,9,10,[2,3,[4,5]],"PYTHON"]
# for i in range(0,len(l1)):
#    if i%2==0:
#        print(l1[i])
#    if str(l1[i]).isalpha():
#        print(l1[i][::2])


# l1=[1,2,3,4,5,6,7,8,9,10,[2,3,[4,5]],"PYTHON"]
# print(l1[-1][::2])


# l=[1, 2, 3, 2, 4, 2, 5]
# l1=[]
# for i in range(len(l)):
#    if l[i]==2:
#        l1.append(i)
# print(l1)


# try:
#    # Code that might cause an error
#    num = int(input("Enter a number: "))
#    result = 10 / num
#    print("Result:", result)

# except ValueError:
#    # Handles wrong input type (like entering text instead of number)
#    print("Error: Please enter a valid integer.")

# except ZeroDivisionError:
#    # Handles division by zero
#    print("Error: Cannot divide by zero.")

# except Exception as e:
#    # Handles any other unexpected error
#    print("Unexpected error:", e)

# finally:
#    # This block always runs (optional)
#    print("Execution completed.")


try:
    num = int(input("Enter a number:"))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Error: Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print("Unexpected error:", e)
finally:
    print("Execution completed.")

# Exception: An event that occurs during execution that disrupts the normal flow of a program (e.g., division by zero, file not found).
# try block: Contains code that may raise an exception.
# except block: Catches and handles specific exceptions.
# else block (optional): Executes if no exception occurs.
# finally block (optional): Executes always, even if an exception occurs, usually for cleanup.


try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Error: Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Result:", result)  # Runs only if no exception occurs
finally:
    print("Execution completed.")

# l=[4,5,1,2,1,4,5]       #output 2
# d={}
# for i in l:
#    if i not in d:
#        d[i]=1
#    else:
#        d[i]=d[i]+1
# for i in d:
#    if d[i]==1:
#        print(i)


# l=[2,7,11,3,6]
# for i in l:
#    for j in l:
#        if i+j==9:
#            print(i,j)


# 2 7
# 7 2
# 3 6
# 6 3

# l1=[1,2,3,4]
# l2=["a","b","c","d"]
# for i in range(len(l1)):
#    for j in range(len(l2)):
#        if i==j:
#            print(l1[i],l2[j])


# 1 a
# 2 b
# 3 c
# 4 d


# l1=[1,2,3,4]       #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# l2=["a","b","c","d"]
# k=[]
# k=zip(l1,l2)
# print(list(k))


# to print duplicates
l = [1, 2, 3, 2, 4, 1, 5]  # [1, 2]
d = {}
l1 = []
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1
print(d)
for i in d:
    if d[i] > 1:
        l1.append(i)
print(l1)

str1 = "a2b3c2d"  # aabbbccd
f = ""

for i in str1:
    if i.isalpha():
        k = i
    else:
        f = f + k * int(i)
print(f)

str1 = "aabbbccd"  # a 2 b 3 c 2 d 1
l = []
d = {}
for i in str1:
    l.append(i)
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1
for i in d:
    print(i, d[i], end=" ")

str1 = "python interview is going on"  # no gniog si weivretni nohtyp

for i in range(len(str1) - 1, -1, -1):
    print(str1[i], end="")

# isinstance(i, list) means:   #"Check whether i is a list."


# l=[1,2,[3,4],[4,5,6,5],[4],8,9]
# output [1, 2, 3, 4, 4, 5, 6, 5, 4, 8, 9]

# l1=[]
# for i in l:
#    if isinstance(i,list):
#        l1.extend(i)
#    else:
#        l1.append(i)
# print(l1)


# l=[1,2,3,4,5]
# k=int(input("enter number"))
# l1=l[k:len(l):1]+l[0:k]
# print(l1)


# Count vowels, consonants, digits, spaces, and special characters

import re

str1 = "Sai123 @ Python"
vowels = len(re.findall(r'[aeiouAEIOU]', str1))
consonants = len(re.findall(r'[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]', str1))
digits = len(re.findall(r'[0-9]', str1))
spaces = len(re.findall(r'\s', str1))
special = len(re.findall(r'[^a-zA-Z0-9\s]', str1))

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)  # [^a-zA-Z0-9\s] Anything that is not a letter, digit, or space

l = ["sat", "bat", "cat", "mat"]  # [['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]
l1 = list(map(list, l))
print(l1)

l = ["sat", "bat", "cat", "mat"]
l1 = []
for i in l:
    k = list(i)
    l1.append(k)
print(l1)

# longest substring
# str1="abcccbbac"
# l=list(str1)
# print(l)


l = [1, 2, 3, 4, 5]
l1 = l[0:len(l):2]
print(l1)

# l=[1,2,3,4,5,6,7,8,9,10,11,12]
# l2=[]
# l1=[]
# n=int(input("enter size of sublist"))
# for i in range(0,len(l),n):
#    print(i)
#    sublists=l[i:i+n]
#    l2.append(sublists)
# print(l2)


# anagrams
str1 = "listen"
str2 = "silent"
l1 = sorted(list(str1))
l2 = sorted(list(str2))
if l1 == l2:
    print("anagram")
else:
    print("not anagram")

str1 = "madam"
str2 = "damam"
if str1 == str1[::-1] and sorted(list(str1)) == sorted(list(str2)):
    print("it is palendrome and palendromic word")





🎭 Playwright + Python
Cheat
Sheet
1.
Installation
pip
install
playwright
pip
install
pytest - playwright
playwright
install

Run
tests:

pytest
pytest - v
pytest
test_file.py
pytest
test_file.py::test_name

2.
Basic
Test
Structure
from playwright.sync_api import Page, expect


def test_example(page: Page):
    page.goto("https://example.com")

    expect(page).to_have_title("Example Domain")
    expect(page).to_have_url("https://example.com/")


3.
Browser
browser = p.chromium.launch(headless=False)
browser = p.firefox.launch()
browser = p.webkit.launch()

page = browser.new_page()

browser.close()

4.
Navigation
page.goto("https://example.com")

page.go_back()
page.go_forward()
page.reload()

print(page.url)
print(page.title())

5.
Locators ⭐
Locator
Example
ID
page.locator("#username")
Class
page.locator(".login")
CSS
page.locator("input[name='email']")
Text
page.get_by_text("Login")
Role
page.get_by_role("button", name="Login")
Label
page.get_by_label("Username")
Placeholder
page.get_by_placeholder("Enter username")
Test
ID
page.get_by_test_id("login-btn")

6.
Click
page.locator("#login").click()

page.get_by_role("button", name="Login").click()

page.get_by_text("Login").click()

7.
Text
Input
page.locator("#username").fill("admin")

page.locator("#password").fill("12345")

Type
character
by
character:

page.locator("#username").type("admin")

Clear:

page.locator("#username").fill("")

8.
Keyboard
page.locator("#username").press("Enter")

page.keyboard.press("Control+A")
page.keyboard.press("Backspace")

9.
Checkbox
page.locator("#remember").check()

page.locator("#remember").uncheck()

Check
status:

expect(page.locator("#remember")).to_be_checked()

10.
Radio
Button
page.locator("#male").check()

11.
Dropdown
page.locator("#country").select_option("India")

By
label:

page.locator("#country").select_option(label="India")

By
value:

page.locator("#country").select_option(value="IN")

12.
Assertions ⭐

Import:

from playwright.sync_api import expect

URL:

expect(page).to_have_url("https://example.com/")

Title:

expect(page).to_have_title("Example Domain")

Text:

expect(page.locator("h1")).to_have_text("Example Domain")

Contains
text:

expect(page.locator("h1")).to_contain_text("Example")

Visible:

expect(page.locator("#login")).to_be_visible()

Hidden:

expect(page.locator("#login")).to_be_hidden()

Enabled:

expect(page.locator("#login")).to_be_enabled()

Disabled:

expect(page.locator("#login")).to_be_disabled()

13.
Get
Values
print(page.locator("h1").inner_text())

Input
value:

print(page.locator("#username").input_value())

Attribute:

print(page.locator("#username").get_attribute("placeholder"))

Count:

print(page.locator("button").count())

14.
Wait
page.wait_for_timeout(2000)

Wait
for element:

page.locator("#login").wait_for()

Wait
for URL:

page.wait_for_url("https://example.com/home")

Prefer
Playwright
's auto-waiting and web-first assertions instead of unnecessary wait_for_timeout().

15.
Screenshot
page.screenshot(path="screenshot.png")

Full
page:

page.screenshot(path="screenshot.png", full_page=True)

16.
Mouse
page.mouse.click(100, 200)

page.mouse.move(100, 200)

page.mouse.dblclick(100, 200)

Hover:

page.locator("#menu").hover()

17.
Frames
frame = page.frame_locator("#my-frame")

frame.locator("#username").fill("admin")
frame.get_by_role("button", name="Login").click()

18.
Alerts / Dialogs
page.on("dialog", lambda dialog: dialog.accept())

Dismiss:

page.on("dialog", lambda dialog: dialog.dismiss())

19.
Multiple
Elements
items = page.locator(".item")

print(items.count())

items.nth(0).click()
items.nth(1).click()

First:

page.locator(".item").first.click()

Last:

page.locator(".item").last.click()

20.
New
Tab / Popup
with page.expect_popup() as popup_info:
    page.get_by_text("Open").click()

popup = popup_info.value

print(popup.url)


⭐ Interview
Must - Know

Memorize
these
first:

page.goto()
page.locator()
page.get_by_role()
page.get_by_text()
page.get_by_label()

.click()
.fill()
.type()
.check()
.uncheck()
.select_option()
.press()

.inner_text()
.input_value()
.get_attribute()

expect().to_have_url()
expect().to_have_title()
expect().to_have_text()
expect().to_be_visible()
expect().to_be_enabled()

page.screenshot()
page.go_back()
page.go_forward()
page.reload()

Quick
example

from playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto("https://example.com")

    expect(page).to_have_title("Example Domain")

    page.locator("#username").fill("admin")
    page.locator("#password").fill("12345")

    page.get_by_role("button", name="Login").click()

    expect(page.locator("h1")).to_be_visible()


targets = [{"target_iqn": "iqn.cisco.2026-10:storage.target01", "protocol": "iSCSI", "status": "ONLINE"},
           {"target_iqn": "iqn.cisco.2026-10:storage.target02", "protocol": "FC", "status": "ONLINE"},
           {"target_iqn": "iqn.cisco.2026-10:storage.target03", "protocol": "iSCSI", "status": "OFFLINE"},
           {"target_iqn": "iqn.cisco.2026-10:storage.target04", "protocol": "iSCSI", "status": "ONLINE"}]

for i in targets:
    if i["protocol"] == "iSCSI" and i["status"] == "ONLINE":
        print(i["target_iqn"])

nfs_exports = [{"export_path": "/vol/data/share1", "volume_name": "vol_data", "size_gb": 500},
               # {"vol_data": 1250, "vol_logs": 400, "vol_backup": 2000}
               {"export_path": "/vol/logs/app", "volume_name": "vol_logs", "size_gb": 100},
               {"export_path": "/vol/data/share2", "volume_name": "vol_data", "size_gb": 750},
               {"export_path": "/vol/backup/daily", "volume_name": "vol_backup", "size_gb": 2000},
               {"export_path": "/vol/logs/db", "volume_name": "vol_logs", "size_gb": 300}]

result = {}
for i in nfs_exports:
    name = i["volume_name"]
    size = i["size_gb"]
    if name in result:
        result[name] = result[name] + size
    else:
        result[name] = size
print(result)

cluster_vols = [{"node_id": "node_01", "volume_name": "vol_finance"},
                {"node_id": "node_02", "volume_name": "vol_hr"},
                {"node_id": "node_01", "volume_name": "vol_eng"},
                {"node_id": "node_02", "volume_name": "vol_sales"},
                {"node_id": "node_01", "volume_name": "vol_infra"}]

result = {}
for i in cluster_vols:
    node = i["node_id"]
    volume = i["volume_name"]
    if node not in result:
        result[node] = []
        result[node].append(volume)
        print(result)

l = [1, 2, 4, 5]
mid = len(l) // 2
first = l[:mid]
second = l[mid:]
print(first)
print(second)

import re

str1 = "444this5555is6666666Python7interview"
result = re.findall(r'\d+|[^\d]+', str1)
print(result)
for i in result:
    if i.isdigit():
        print(str(len(i)) + i[0], end="")
    else:
        print(i[::-1], end="")


# binary search

def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


numbers = [10, 20, 30, 40, 50, 60, 70]
target = 50

result = binary_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

# swaping
a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)















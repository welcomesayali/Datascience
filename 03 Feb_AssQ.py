#!/usr/bin/env python
# coding: utf-8

# In[15]:


#def is used to create a function
def odd_nums(start,end):
    if start>end:
        return
    print(start,end=" ")
    return odd_nums(start+2,end)
start=1;end=25
odd_nums(start,end)


# We use *args and **kargs as an argument when we are unsure about the number of arguments to pass in the functions.
# For *args --> allows us to pass variable length argument list.Tuple opertion can be performed.
# For **kargs --> it allows us to pass the variable length of "keyword" arguments to the function.Arguments are passed a dictionary

# In[1]:


# *args example :here passed 3 different tuples as argument and prints the results
def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)


# In[3]:


# **kargs example :#return a key and value pair where value is list
def test12(**xyz):
    for i in xyz.keys():
        if type(xyz[i])==list:
            return i ,xyz[i]


# In[6]:


test12(a=1,b="saya",c="data science",d=[1,2,3,4],e=(1,2,3))


# Iterators are methods that iterate collections like lists, tuples, etc.Using an iterator method, we can loop through an object and return its elements.
# Iter() and next() are the methods used to initialise the iterator object.

# In[9]:


#To print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16,18, 20] using Iterator methods:

my_list = [2, 4, 6, 8, 10, 12, 14, 16,18, 20] # define a list
iterator = iter(my_list)# create an iterator from the list
print(next(iterator))# fetch the first element of the iterator
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# #What is a generator function in python? Why yield keyword is used? Give an example of a generator
# A Generator is a function that returns an iterator, that produces a sequence of values when iterated over.
# Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.
# Whenever the generator function is called, it does not execute the function body immediately. Instead, it returns a generator object that can be iterated over to produce the values.
# 
# "Yield" keyword is used to produce a value from the generator.Instead of "Return" statement ,we use "yield" statement in generators

# In[15]:


#example of generator function:
def test_fib(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b ,a+b
        
for i in test_fib(10):
    print(i)


# In[18]:


test_fib(2)


# In[23]:


#Create a generator function for prime numbers less than 1000. Use the next() method to print the
#first 20 prime numbers.

from math import sqrt

def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2
    return True

def prime_generator(limit=1000):
    n = 2
    while True:
        if n<limit:
            if is_prime(n):
                yield n
            n += 1
        else:
            break
generator = prime_generator()

for i in range(20):
    print(next(generator))


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


# create a variable containing string:
str1="Data Science"
print(str1)


# In[2]:


type(str1)


# In[4]:


lst=["s","a","y","a","l","i"]
print(lst)


# In[5]:


type(lst)


# In[7]:


flt1=5.55
print(flt1)


# In[8]:


type(flt1)


# In[9]:


tupl=("mango","banana","orange")
print(tupl)


# In[10]:


type(tupl)


# In[14]:


var2 = '[ DS , ML , Python]'
type(var2)


# In[17]:


var3 = ['DS','ML','Python']
type(var3)


# In[20]:


var1 = ' '
type(var1)


# In[21]:


var4 = 1
type(var4)


# In[24]:


# (i) division operator
a=2
b=5
b/a


# In[25]:


# (ii) modulo operator---> output is the remainder
a%b


# In[27]:


# (iii) modulo operator---> output is the integer quotient
b//a


# In[28]:


# (iv) exponentiation operator---> output is the calculation of 1st number is power of 1st number
a**b


# In[35]:


# list of length 10 
type1=[1,"one",[3,4,5],"data science",1.1,("mango","orange"),{"a","b"},True,1+2j,10]
len(lst)


# In[36]:


for i in type1:
    print(f"The element is:{i} and its datatype is:{type(i)}")


# In[3]:


a=16
b=2
i=0
while ((a%b)==0):
        a=a/b
        i+=1
print(f"The number is divisible {i} times")


# In[17]:


""" list containing 25 int type data. Using for loop and if-else condition print if the element is 
divisible by 3 or not"""

lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for i in range(len(lst)):
    if ((lst[i])%3)==0:
        print(f"The element {lst[i]} is divisible by 3")
    else:
        print(f"The element {lst[i]} is not divisible by 3")


# In[18]:


# mutable and immutable datatypes
"""Mutable datatypes are the ones whose value can be changes while immutable object's value cannot be modified.
List object is mutable whereas string object is immutable"""
#eg. list
lst1=[1,2,3,4,5]
lst[0]


# In[21]:


lst1[0]=2
print(lst1)


# In[22]:


#string
str1="Data"
str1[0]


# In[27]:


str1[0]='N'
print(str1[0])


# In[26]:


print(str1[0])


# In[32]:





# In[33]:





# In[ ]:





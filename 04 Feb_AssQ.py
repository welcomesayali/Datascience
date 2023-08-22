#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Create a python program to sort the given list of tuples based on integer value using a
#lambda function: [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
list_x=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]


# In[19]:


list_x.sort(key = lambda a:a[1])
print(list_x)


# In[33]:


#Write a Python Program to find the squares of all the numbers in the given list of integers using
#lambda and map functions.
list_y=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[32]:


list(map(lambda a: a**2, list_y))


# In[36]:


list(map(lambda a: a**2, list_y))


# In[146]:


# Write a python program to convert the given list of integers into a tuple of strings. Use map and lambda functions

list_z= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[147]:


tuple(map(lambda x:str(x),list_z))


# In[113]:


# Write a python program using reduce function to compute the product of a list containing numbers from 1 to 25
from functools import reduce
list_t=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]


# In[114]:


reduce(lambda x,y:x*y,list_t)


# In[115]:


# Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
#filter function
list_s=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]


# In[116]:


list(filter(lambda x:x%2==0 and x%3==0,list_s))


# In[117]:


#Write a python program to find palindromes in the given list of strings using lambda and filter
#function.
list_p=['python', 'php', 'aba', 'radar', 'level']


# In[125]:


list(filter(lambda x: x==x[::-1],list_p))


# In[ ]:





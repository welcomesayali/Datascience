#!/usr/bin/env python
# coding: utf-8

# # Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.
# Python class contains set of object which shares common characteristics/ behavior and common properties/ attributes.
# An object is simply a collection of data (variables) and methods (functions). 
# A class is a blueprint for that object.An Object is an instance of a Class.

# # Name the four pillars of OOPs.

# The Four Pillars of Object Oriented Programming
# 1. Abstraction.
# 2. Encapsulation.
# 3. Inheritance.
# 4. Polymorphism.

# # Explain why the __init__() function is used. Give a suitable example.

# Constructors are generally used for instantiating an object.
# The __init__ function is called every time an object is created from a class.

# In[7]:


class Person:
  def  __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# #Why self is used in OOPs?

# #The "self" variable is used to represent the instance of the class which is often used in object-oriented programming. 
# #It works as a reference to the object. Python uses the self parameter to refer to instance attributes and methods of the class.

# # What is inheritance? Give an example for each type of inheritance.

# In[10]:


#Inheritance allows us to define a class that inherits all the methods and properties from another class.
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass


# In[11]:


x = Student("Mike", "Olsen")
x.printname()


# In[ ]:





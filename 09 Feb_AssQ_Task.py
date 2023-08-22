#!/usr/bin/env python
# coding: utf-8

# # Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed and average_of_vehicle. 

# In[3]:


class vehicle:
    def __init__(self,name_of_vehicle, max_speed,average_of_vehicle):
        self.name =name_of_vehicle
        self.speed =max_speed
        self.average=average_of_vehicle

    


# In[39]:


x =vehicle("tata",25,20)
x.name


#  # Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
# # Create a method named seating_capacity which takes capacity as an argument and returns the name of the vehicle and its seating capacity.

# In[4]:


class car(vehicle):
    def seating_capacity(self, capacity):
        return f" {self.name}  {capacity}"
    


# In[5]:


x = car("tata","45 mph","15 kmph")
x.seating_capacity(85)


# # What is multiple inheritance? Write a python code to demonstrate multiple inheritance

# A class can be derived from more than one superclass in Python.This is called multiple inheritance

# In[4]:


class A:
    def A_info(self):
        print("This is super class A")
        
class B:
    def B_info(self):
        print("This is super class B")
        
class C(A,B):
    print("This is derived class")
    
info=C()

info.A_info()
info.B_info()


# # What are getter and setter in python? Create a class and create a getter and a setter method in this class.
1.The main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation.
2.We use getters & setters to add validation logic around getting and setting a value.
3.To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.
4. This can be achieved using  property() function.There is one more way to implement property function i.e. by using decorator. Python @property is one of the built-in decorators.Here , the main purpose of any decorator is to change your class methods or attributes in such a way so that the user of the class need not make any changes in the code
# In[17]:


class Geeks:
    def __init__(self):
        self._age = 0
       
     # using property decorator
     # a getter function
    @property
    def age(self):
        print("getter method called")
        return self._age
       
     # a setter function
    @age.setter
    def age(self, a):
        if(a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a

mark = Geeks()
  
mark.age = 19
  
print(mark.age)


# What is method overriding in python? Write a python code to demonstrate method overriding.
When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a method in its super-class, then the method in the subclass is said to override the method in the super-class.
# In[18]:


# Defining parent class
class Parent():
      
    # Constructor
    def __init__(self):
        self.value = "Inside Parent"
          
    # Parent's show method
    def show(self):
        print(self.value)
          
# Defining child class
class Child(Parent):
      
    # Constructor
    def __init__(self):
        self.value = "Inside Child"
          
    # Child's show method
    def show(self):
        print(self.value)
          
          
obj1 = Parent()
obj2 = Child()
  
obj1.show()
obj2.show()


# In[ ]:





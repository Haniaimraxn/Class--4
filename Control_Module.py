# Control Modules & Function in Python

# Types of Modules
#  Built-in Modules

# These are pre-installed with Python and provide standard functionality. 
import math
print(math.sqrt(16)) 

# 2.User-defined Modules
# These are custom Python files created by users, which can contain functions, classes, or variables.

def add(a, b):
    return a * b

# 3.External Modules
# These are developed by others and not included with Python by default.You install them using pip

import numpy as np
arr = np.array([1, 2, 3])
print(arr)

# Function in Python
#  Afunction is a resuable block of code that performs a specific task.

def my_greet(name):
    print(f"Hello, {name}!")
    return
    my_greet("Alice")

# Pass by Reference as Value    
def modify_list(my_list):
    my_list.append(10)
nums = [1, 2, 3]
modify_list(nums)
print(nums)    

def modify_number(num):
    num += 40

x = 20
modify_number(x)
print(x)    

# Function Argument
def greet(name, message= "Hey"):
    print(message + ", " + name)
greet("Noreh")    
greet(" May your spirit run wild like a stallion in flight, Chasing dreams through morning and into the night. With the heart of a Rider and Courage so true, The World is your meadow - waiting for you!")

# Scope of Variable

total = 0
def sum (int1, int2):
    total = int1 + int2
    print("enclosed in the function : ", total)
    return total
sum (60 ,80)
print("Beyond the function : ", total) 
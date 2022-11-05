# This is how you comment

'''
This is how you comment for multiple lines'''

print("Hello World!") # // First Line Of Python Code 

# -----> Variables 

a = "John"
b= 4.1
c= True

# Any kind of alphabet with symobols can be a variable. Although Symobols like - and numbers cannot be used as variable

A = "John"
a = "Loki"

print(A) # Result: John
print(a) # Result: Loki

# Therefore Case_Sensitive

# -------> Assign Multiple Variable

x, y, z = "Orange", "Banana", "Cherry"
print(x) # Result= Orange
print(y) # Result= Banana
print(z) # Result= Cherry

x = y = z = "Orange"
print(x)   # Result= Orange
print(y)  # Result= Orange
print(z) # Result= Orange

# ---------> Private and GLobal Variable

x = "awesome" # // Global Variable

def myfunc():
  print("Python is " + x)

myfunc()

# In the above code x is the global vaiable and if we create any n numbers of function the variable of that will be x

x = "awesome" # // Global Variable


def myfunc():
  x = "fantastic" # // Private Variable
  print("Python is " + x) # Result: Python is fantastic


myfunc()

print("Python is " + x) # Result: Python is awesome

# In the above code even though there is a global variable it will still accept the private variable for the specific def




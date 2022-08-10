# ----> Data Types

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


# x = "Hello World"	                  str
# x = 20	                          int
# x = 20.5	                          float
# x = 1j	                          complex
# x = ["apple", "banana", "cherry"]	  list
# x = ("apple", "banana", "cherry")	  tuple
# x = range(6)	                      range
# x = {"name": "John", "age": 36}	  dict
# x = {"apple", "banana", "cherry"}	  set
# x = frozenset({"apple", "banana", "cherry"}) frozenset
# x = True	                         bool
# x = b"Hello"	                     bytes
# x = bytearray(5)	                 bytearray
# x = memoryview(bytes(5))	         memoryview
# x = None	                         NoneType


# -------> Python Numbers

# There are three numeric types in Python:

x = 1    # int
y = 2.8  # float
z = 1j   # complex


print(type(x))
print(type(y))
print(type(z))

# You can find the the type of datatype using above code

# ------> INT(INTEGER)

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# -------> float(DECIMAL NUMBERS)

x = 1.10
y = 1.0
z = -35.59
a= 35e3
b = 12E4
c = -87.7e100


print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))

# ---------> complex(real_num+imaginary_num)

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# -----------> Conversion 

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

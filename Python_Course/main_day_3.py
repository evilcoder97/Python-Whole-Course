# -----> Strings (str)

a = ("abc") # str= any alphabet

# ------> Slicing (str)

b = "Hello, World!"
print(b[2:5])  # result: llo

c = "Hello, World!"
print(b[:5]) # result: Hello

d = "Hello, World!"
print(b[2:])  # result: llo, World!

e = "Hello, World!"
print(b[-5:-2])  # result: orl where !=0 , d= -1

# --------> Modifying String

"1.Upper Case"

p = "Hello, World!"
print(p.upper())

"2. Lower Case"

q = "Hello, World!"
print(q.lower())

"3. Remove WhiteSPacing"

r = "Hello, World!   "
print(r.strip())  # returns "Hello, World!"

"4. Replace String"

a = "Hello, World!"
print(a.replace("H", "J")) # result : Jello, World!

"5. Split String"

a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']


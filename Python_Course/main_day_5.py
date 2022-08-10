# -----> If Else Statement

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# ---> One line if statement

if a > b: print("a is greater than b")

# -----> Short Hand If ... Else

a = 2
b = 330
print("A") if a > b else print("B")

# ------> AND

# The and keyword is a logical operator, and is used to combine conditional statements

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# ------> OR

# They ir keyword compares two and check 

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# ----> Nested If ELse 


x = float(input("Enter the number"))

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

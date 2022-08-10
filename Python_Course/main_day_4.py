# --------> Formatting Strings

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


# ------> List

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Adds Orange in the list

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Adds Orange as Second Item

# -----> Remove Item

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# Pop removes last item

thislist = ["apple", "banana", "cherry"]
thislist.remove(1)
print(thislist)

# Remove helps in removing the item of specific index

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # Other way to remove

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Removes all list item

# -----> Use Loop to print item

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# --------> Sort List Item

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# Arranges in Ascending Alphabetical order

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# Arranges in Ascending order

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)
# Arranges in Descending Alphabetical order

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)
# Arranges in Descending  order

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# Arrange in Case-Sensitive Order [Capital First then Small]

# ------> Copy List Item

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)





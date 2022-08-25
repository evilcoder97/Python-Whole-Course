# Password Generator
import random

Lower_case = "abcdefghijklmnopqrstuvwxyz"
Upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Symbols = "@  # $&_-()=%*:/!?+."
Numbers = "1234567890"

length = int(input("Enter the length of the password you want...  "))
password_before = Lower_case+Upper_case+Numbers+Symbols


password = random.sample(password_before, length)


print(password)

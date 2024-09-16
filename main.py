import string

password = "password"

upper_case = any([1 if char in string.ascii_uppercase else 0 for char in password])
lower_case = any([1 if char in string.ascii_lowercase else 0 for char in password])
special_char = any([1 if char in string.punctuation else 0 for char in password])
nums = any([1 if char in string.digits else 0 for char in password])

length = len(password)

score = 0

if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 16:
    score += 1
if length > 20:
    score += 1

# checking common passwords
with open('pwlist.txt', 'r', encoding="utf8") as file1, open('comlist.txt', 'r', encoding='utf8') as file2:
    com1 = file1.read().splitlines()
    com2 = file2.read().splitlines()

if password in com1 or com2:
    print("The password is found in a common list")



# print(upper_case)
# print(lower_case)
# print(special_char)
# print(nums)
# print(length)
import string

password = input("Enter your password: ")

upper_case = any([1 if char in string.ascii_uppercase else 0 for char in password])
lower_case = any([1 if char in string.ascii_lowercase else 0 for char in password])
special_char = any([1 if char in string.punctuation else 0 for char in password])
nums = any([1 if char in string.digits else 0 for char in password])

characters = [upper_case, lower_case, special_char, nums]
chars = sum(characters)

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

if password in com1 or password in com2:
    print("The password is found in a common list")

print(f"Your password length is {length}. You get {score} points")

if chars > 1:
    score += 1
if chars > 2:
    score += 1
if chars > 3:
    score += 1
print(f"Your password has {chars} different character type(s). You get {score - 1} points")

if score < 4:
    print(f"Your password is pretty weak. Score: {score}/7")
elif score == 4:
    print(f"Your password is alright but can be better. Score: {score}/7")
elif score > 4 and score < 6:
    print(f"Your password is pretty good. Score: {score}/7")
elif score > 6:
    print(f"Your password is very good. Good job! Score: {score}/7")

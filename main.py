import string

password = "tesTing123"

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

print(upper_case)
print(lower_case)
print(special_char)
print(nums)
print(length)

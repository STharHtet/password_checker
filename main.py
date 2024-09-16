import string

password = "tesTing123"

upper_case = any([1 if char in string.ascii_uppercase else 0 for char in password])

print(upper_case)
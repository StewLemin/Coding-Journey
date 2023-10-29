password = input("Enter new password:")
result = {}

if len(password) >= 8:
    result["length"] = (True)
else:
    result["length"] = (False)

digit = False
for character in password:
    if character.isdigit():
        digit = True

result["digit"] = digit

upper = False
for character in password:
    if character.isupper():
        upper = True

result["upper"] = upper

if (all(result.values())):
    print("Strong Dragon")
    print(result)
else:
    print("Old Dragon")

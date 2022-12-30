
#Program to check if name is at least 3 characters long and no longer than 50 characters

name = "Josh"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")
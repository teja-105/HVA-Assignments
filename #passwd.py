def consecutive(password):
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return True
    return False

def strong(password):
    upper = False
    lower = False
    digit = False
    special = False

    for i in password:
        if i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i.isdigit():
            digit = True
        else:
            special = True
        
        if upper and lower and digit and special:
            return True

    return False

password = input("Enter password: ")
l = len(password)

if l < 8 or l > 16:
    print("Check the length of the password")
else:
    consecutive = consecutive(password)
    strong = strong(password)
    
    if consecutive or not strong:
        print("Weak password")
    else:
        print("Strong password")
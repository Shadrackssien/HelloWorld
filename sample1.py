def validate(num):
    if (num < 1 or num > 9):
        print('Out of range')
    elif (num != int(num)):
        print("Not an integer")
    else:
        print("just right")
        return True
    
    return False

print(validate(-5))
print(validate(15))
print(validate(5.2))
print(validate(5))
#To take the input from the customer
num = int(input("Enter a number: "))

# By definition, prime numbers are greater than 1
if num > 1:
    # Check for factors
    for i in range(2,num):
        # CHeck for remainder in division (mod), if none it's not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            # Find it's corresponding factor using integer division
            print(i,"times", num//i,"is",num)
            break
        else:
            print(num,"is prime")
else:
    print(num,"is not a prime number")
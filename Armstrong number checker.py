# Armstrong Number Checker

def is_armstrong(num):
    # Convert number to string to easily iterate over digits
    digits = str(num)
    power = len(digits)  # Number of digits
    total = sum(int(digit) ** power for digit in digits)
    return total == num

# Take input from user
number = int(input("Enter a number: "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

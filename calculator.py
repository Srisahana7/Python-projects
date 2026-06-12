# Project: Calculator V3
# Author: Sri Sahana
# Description:
# A calculator with reusable results and cleaner code.

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def floor_div(a, b):
    return a // b

def root(a, b):
    return a ** b


# Main calculate function
def calculate(a, ope, b):
    if b == 0 and ope in ['/', '//', '%']:
        print("Division by zero is not allowed")
        return None

    if ope == '+':
        return add(a, b)
    elif ope == '-':
        return sub(a, b)
    elif ope == '*':
        return mul(a, b)
    elif ope == '/':
        return div(a, b)
    elif ope == '%':
        return mod(a, b)
    elif ope == '//':
        return floor_div(a, b)
    elif ope == '**':
        return root(a, b)
    else:
        print("Invalid operator")
        return None


# First input
a = input("Enter number = ")
ope = input("Enter operator = ")
b = input("Enter number = ")

# Validation
if not a.replace('.', '', 1).isdigit() and not b.replace('.', '', 1).isdigit():
    print("Both inputs are invalid")

elif not a.replace('.', '', 1).isdigit():
    print("You typed invalid input:", a)

elif not b.replace('.', '', 1).isdigit():
    print("You typed invalid input:", b)

else:
    a = float(a)
    b = float(b)

    result = calculate(a, ope, b)

    if result is not None:
        print(result)

        # Continue using previous result
        while True:
            user_choice = input("Do you want to continue? (yes/no): ").lower()

            if user_choice == "yes":
                a = result
                ope = input("Enter operator = ")
                b = input("Enter number = ")

                if not b.replace('.', '', 1).isdigit():
                    print("Invalid input")
                    continue

                b = float(b)

                result = calculate(a, ope, b)

                if result is not None:
                    print(result)

            elif user_choice == "no":
                break

            else:
                print("Type only yes or no.")    
    
        
        

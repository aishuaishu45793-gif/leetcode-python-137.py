number = input("Enter an integer: ")

if number.isdigit():
    if number == number[::-1]:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
else:
    print("Please enter a non-negative integer.")
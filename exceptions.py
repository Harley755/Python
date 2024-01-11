try:
    number = int(input("Please enter number : "))
except ValueError:
    print("This number is not an integer")
else:
    print(f"This number is {number}")
# end try
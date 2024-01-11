def getInt():
    while True:
        try:
            number = int(input("Please enter number : "))
        except ValueError:
            print("This number is not an integer")
        else:
            break
        # end try
    return number
# end def

print(f"This number is {getInt()}")

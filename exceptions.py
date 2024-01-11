while True:
    try:
        number = int(input("Please enter number : "))
    except ValueError:
        print("This number is not an integer")
    else:
        break
    # end try
    
print(f"This number is {number}")
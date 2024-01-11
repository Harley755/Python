def main():
    x = getInt()
    print(f"This number is {x}")
    
    
# end def

def getInt():
    while True:
        try:
            number = int(input("Please enter number : "))
        except ValueError:
            print("This number is not an integer")
        else:
            return number
        # end try
# end def

main()


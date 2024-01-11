def main():
    x = getInt()
    print(f"This number is {x}")
    
    
# end def

def getInt():
    while True:
        try:
            return int(input("Please enter number : "))
        except ValueError:
            pass
# end def

main()


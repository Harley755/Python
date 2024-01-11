def main():
    x = getInt()
    print(f"This number is {x}")
    printPyramid(3)
    
    
# end def

def getInt():
    while True:
        try:
            return int(input("Please enter number : "))
        except ValueError:
            pass
# end def


def printPyramid(n):
    for i in range(n):
        print("#" * (i + 1))
    # end for

main()


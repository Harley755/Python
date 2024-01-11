def main():
    printColumn(3)
    printRow(4)
    square(3)

# end def

def printColumn(number):
   print("#\n" * number,)
# end def

def printRow(width):
   print("#" * width) 
# end def

def square(size):
    for i in range(size):
        printRow(size)
   # end for
    
# end def

main()
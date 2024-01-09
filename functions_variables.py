numbers = [1,22,3,4,5, 55]

def main() :
    number = int(input("Enter number : "))
    if isEven(number) == True:
        print(f"{number} is even")
    else:
        print(f"{number} odd")
        
    print(isMoreBig(numbers))
    
    day = input("Enter day number : ")
    
    match day :
        case '1':
            print('Lundi')
        case '2':
            print('Mardi')
        case '3':
            print('Mercredi')
        case '4':
            print('Jeudi')
        case '5':
            print('Vendredi')
        case '6':
            print('Samedi')
        case '7':
            print('Dimanche')
        case _:
            print('Invalid number')
    



def isEven(x):
    return x % 2 == 0
    

def isMoreBig(numbers):
    more_big_number = 0
    for i in numbers:
        if i > more_big_number:
            more_big_number = i
    return more_big_number  

main()
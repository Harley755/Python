def main() :

    #for i in [0,1,2,4,7]:
    #    print("meooow")
        
    #for i in range(3):
    #    print("meow")
        
    numberMaow(getNumber())
    
    students = []
    
    # Initialiser la liste
    getUserList(students)
    # Afficher les élements de la liste
    getListValues(students)
    # Afficher Hermione
    print(students[2])
    
    
def getNumber():    
    while True:
        n = int(input("Combien de fois le chat miaule ? "))
        if (n > 0) :
            return n
            break
# end def

def numberMaow(number) :
    for i in range(number):
        print("meow")
# end def      

def getListValues(arg):
    for x in arg:
        print(x)
# end def

def getUserList(students):
    numberListElement = int(input("Combien de noms ? "))
    for x in range(numberListElement):
        value = input(f"Entrer le nom {x + 1} ").strip()
        students.append(value)
# end def

main()
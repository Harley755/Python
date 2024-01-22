fruits = ['Banane', 'Orange', 'Pomme']
print(f"LES FRUITS : {fruits}")

# fruits.append('Papaye')
# print(f"Avec append : {fruits}")

# fruits.extend(fruits)
# print(f"Avec extend : {fruits}")

fruits.insert(1, 'Mangue')
print(f"Avec insert : {fruits}")

# INDIQUER LA POSITION POUR ENLEVER
fruits.pop(1)
print(f"Avec pop : {fruits}")

print(f"Avec index : {fruits.index('Orange')}")

print(f"Le type des fruits est {type(fruits)}")


# LES TUPLES
constTyple = ("Banane")
constTyple = ("Banane", "lol")
print(f"Le type des constTyple est {type(constTyple)}")

# LES DICTIONNAIRES
myDic = dict() # ou 
#myDic = {}


myDic = {"name" : 'John', "age" : "23", "isGameAddict" : False}
print(f"Mon dictionnaire : {myDic}")
print(f"Mon name : {myDic.get('name')}")


import csv
from collections import defaultdict

def types_of_pokemon():
    with open('Pokemon.csv') as file:
        reader = csv.DictReader(file, fieldnames=['SN','Name','Type 1','Type 2','Total','Hp','Attack','Defense','Sp. Atk','Sp. Def','Speed','Generation','Legendary'])
        type1, type2 = defaultdict(set), defaultdict(set)
        for line in reader:
            
            type1['Type1'].add(line['Type 1'])
            type2['Type2'].add(line['Type 2'])

        return dict(type1), dict(type2)

def total():
    with open('Pokemon.csv') as file:
        reader = csv.DictReader(file, fieldnames=['SN','Name','Type 1','Type 2','Total','Hp','Attack','Defense','Sp. Atk','Sp. Def','Speed','Generation','Legendary'])
        total = defaultdict(list)
        for line in reader:
            total[line['Total']].append(line['Name'])

        return dict(total)

def speed():
    with open('Pokemon.csv') as file:
        reader = csv.DictReader(file, fieldnames=['SN','Name','Type 1','Type 2','Total','Hp','Attack','Defense','Sp. Atk','Sp. Def','Speed','Generation','Legendary'])
        speed = defaultdict(int)
        for line in reader:

            speed[line['Speed']] += 1

        return( dict(speed))

def type():
    with open('Pokemon.csv') as file:
        reader = csv.DictReader(file, fieldnames=['SN','Name','Type 1','Type 2','Total','Hp','Attack','Defense','Sp. Atk','Sp. Def','Speed','Generation','Legendary'])
        poke = defaultdict(lambda: defaultdict(int))
        for line in reader:
            poke[line['Type 1']][line['Name']] = line['Total']

        return str((dict(poke)))

def pokemon_types(choice):

    with open('Pokemon.csv') as file:
        reader = csv.DictReader(file, fieldnames=['SN','Name','Type 1','Type 2','Total','Hp','Attack','Defense','Sp. Atk','Sp. Def','Speed','Generation','Legendary'])
        type = defaultdict(list)
        for line in reader:
            type[line['Type 1']].append(line['Name'])
    return (type)

types = pokemon_types('Grass')

def lookup(type):
    print(types[type])

    

if __name__ == "__main__":
    type()


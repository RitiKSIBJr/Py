import csv
from collections import defaultdict

def no_of_types_in_year():
    types_in_year = defaultdict(lambda :defaultdict(int))
    with open('naruto.csv') as file:
        reader = csv.DictReader(file, fieldnames=['Num_episode','Title', 'Type', 'Year_launch', 'Rate', 'Votes', 'Saga', 'Airdate'])
        for line in reader:
            year = str(line['Year_launch'])
            type = str(line['Type'])
            types_in_year[year][type] += 1
            
        return str((dict(types_in_year)))

def rates():
    result = defaultdict(int)
    with open('naruto.csv') as file:
        reader = csv.DictReader(file, fieldnames=['Num_episode','Title', 'Type', 'Year_launch', 'Rate', 'Votes', 'Saga', 'Airdate'])
        for line in reader:
            rate = float(line['Rate']) 
            
            if rate <= 7 and rate >= 6:
                result['Between 6 and 7'] += 1

            elif rate <= 8 and rate > 7:
                result['Between 7 and 8'] += 1

            else:
                result['Above 8'] += 1

        return (dict(result))

def total_votes_in_year():
    votes = defaultdict(int)
    with open('naruto.csv') as file:
        reader = csv.DictReader(file, fieldnames=['Num_episode','Title', 'Type', 'Year_launch', 'Rate', 'Votes', 'Saga', 'Airdate'])
        for line in reader:

            vote = int(line['Votes'])
            year = str(line['Year_launch'])
            votes[year] += vote
        return (dict(votes))


def saga():
    episodes = defaultdict(int)
    with open('naruto.csv') as file:
        reader = csv.DictReader(file, fieldnames=['Num_episode','Title', 'Type', 'Year_launch', 'Rate', 'Votes', 'Saga', 'Airdate'])
        for line in reader:
            name = str(line['Saga'])
       
            episodes[name] += 1
    return( dict(episodes))


if __name__ == "__main__":
    no_of_types_in_year()
    rates()
    total_votes_in_year()
    saga()


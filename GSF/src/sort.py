import csv
from collections import defaultdict

def most_win_till_1916():
    with open('goalscorers.csv','r', encoding='utf-8') as file:
        reader = csv.DictReader(file, fieldnames=['date','away_team','home_team', 'team', 'scorer', 'minute', 'own_goal', 'penalty'])
        stack = defaultdict(int)

        for line in reader:
            if line['date'].split("-")[0] <= '1916':
                stack[line['team']] += 1

        for x in stack:
            print(x+'-'+str(stack[x]))

            #prints our 'team name' - 'total no match won till 1916'


def goal_scored_in_a_year():
    with open('goalscorers.csv','r', encoding='utf-8') as file:
        reader = csv.DictReader(file, fieldnames=['date','away_team','home_team', 'team', 'scorer', 'minute', 'own_goal', 'penalty'])
        scorer, year = defaultdict(int), defaultdict(int)
        prev_year = '1916'

        for line in reader:
            scorer[line['scorer']] += 1
            curr_year = line['date'].split("-")[0]

            if curr_year != prev_year:
                scorer = defaultdict(int)
                
            else:
                year[curr_year] = scorer
                
            prev_year = curr_year 
            
        for x in year:
            print(x + " - " +str(year[x]))
            #print out 'year' - '{'scorer' : goad_scored, 'scorer' : goad_scored, 'scorer' : goad_scored, ...... }
            
if __name__ == "__main__":
    most_win_till_1916()
    goal_scored_in_a_year()
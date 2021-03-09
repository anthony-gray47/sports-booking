# @todo convert to file to a class

import requests
from bs4 import BeautifulSoup
import glob


files = glob.glob("data/nba/*.htm")
file_contents = ''

for path in files:
    with open(path, 'r') as file:
        file_contents = file_contents + file.read().replace('\n', '')



#with open('nba/2012-2013page-1.htm', 'r') as file:
    #the_data = file.read().replace('\n', '')

#variables
soup = BeautifulSoup(file_contents, 'html.parser')
data = []


def create_data():
    for val in soup.find_all(class_=["table-participant", "table-score", "odds-nowrp", "result-ok"]):
        row = {}
        if(val['class'] == ['name', 'table-participant']):
            row['game'] = val.get_text()
        elif(val['class'] == ['center', 'bold', 'table-odds', 'table-score']):
            row['score'] = val.get_text()
        elif(val['class'] ==  ['odds-nowrp']):
            row['looser_odds'] = val.get_text()
        elif(val['class'] ==  ['result-ok', 'odds-nowrp']):
            row['winner_odds'] = val.get_text()
        data.append(row)

def add_bet_val(all_vals):
    total_bet_val = 0
    for val in all_vals:
        real_number = val[1:len(val)]
        if(real_number != ''):
            total_bet_val = total_bet_val + float(real_number)
    print(total_bet_val)


def grab_val(needle, needle2):
    favorite_won = 0
    favorite_lost = 0
    games_played = 0
    games_won_at_bet_val = 0
    games_lost_at_bet_val = 0
    winner_odd_val = []
    looser_odd_val = []
    for row in data:
        for key in row:
            if(key == needle):
                games_played = games_played + 1
                if(row[key][0] == '-'):
                    favorite_won = favorite_won + 1
                    #if(row[key][1:len(row[key])] > '500' and len(row[key]) == 4):
                        #print('win')
                        #print(row[key][1:len(row[key])])
                    games_won_at_bet_val = games_won_at_bet_val + 1
                    winner_odd_val.append(row[key])
            elif(key == needle2):
                if(row[key][0] == '-'):
                    #if(row[key][1:len(row[key])] > '500' and len(row[key]) == 4):
                        #print('loose')
                        #print(row[key][1:len(row[key])])
                    games_lost_at_bet_val = games_lost_at_bet_val + 1
                    looser_odd_val.append(row[key])


    print('the favorite won: ' + str(favorite_won) + ' games out of ' + str(games_played))
    print('games won at bet value: ' + str(games_won_at_bet_val) + ' games lost at bet value ' + str(games_lost_at_bet_val))
    win_total = games_won_at_bet_val * 100
    print('money gained: ')
    print(win_total)
    print('money lost:')
    add_bet_val(looser_odd_val)



#def grab_looser_odds(needle):


create_data()
grab_val('winner_odds', 'looser_odds')

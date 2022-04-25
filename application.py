import constants
import copy
import time

cleaned_players = copy.deepcopy(constants.PLAYERS)
copied_teams = copy.deepcopy(constants.TEAMS)


def cleaned_data(cleaned_players):
    for players in cleaned_players:
        players['height'] = players['height'].split(' ')
        players['height'] = int(players['height'][0])
        if players['experience'] == 'YES':
            players['experience'] = True
        else:
            players['experience'] = False
        players['guardians'] = players['guardians'].split(' and ')

       
def avg_height(*args):
    avg_sum = []
    for team in args:
        for player in team:
            avg_sum.append(player['height'])
            total_players = len(team)  
    return round((sum(avg_sum)/total_players),1)


def display_players(*team):
    team_players = []
    for players in team:
        for player in players:
            team_players.append(player['name'])  
    print(', '.join(team_players))  


def display_team(team):
    print(f'\n   - {team} - ')
    print('_____________________________________________')
    print(f'\nAmount in team: {int(len(team))}')
    print(f'Total Experienced: {int(len(team)/2)}',f'\nTotal Inexperienced: {int(len(team)/2)}')
    print(f'Average Height: {avg_height(team)}')
    print('_____________________________________________')
    print('\n  Players:'),display_players(team)
    print('\n  Guardians:')
    for players in team:
        player = players['name']
        print(', '.join(players['guardians']), f'({player})')
    print('_____________________________________________')


cleaned_data(cleaned_players)
experienced_players = []
inexperienced_players = []

for player in cleaned_players:
    if player['experience'] == True:
        experienced_players.append(player)
    else:
        inexperienced_players.append(player)

panthers = (experienced_players[::3]+inexperienced_players[::3])
bandits = (experienced_players[1::3]+inexperienced_players[1::3])
warriors = (experienced_players[2::3]+inexperienced_players[2::3])

if __name__ == "__main__":
    print('\n   Basketball Stats Tool')
    print('\n------------ menu ------------')
    print('\nYour options are:')
    print('   A) Display Team stats')
    print('   B) Quit\n')
    answering = True
    while answering == True: 
        if answering == False:
            break     
        
        initial_choice = input('Which would you like to do?  ')
        initial_choice = initial_choice.upper()
        
        while initial_choice not in ('A', 'B'):
            if initial_choice in ('A', 'B'):
                    break
            initial_choice = input('I need an "A" or "B" please \n  ~ ').upper()
        
        if initial_choice == 'B':
            print('\nOk, maybe next time!')
            answering = False
            continue
        
        while initial_choice == 'A' or 'y':
            print('\nAlright, which team would you like to know more about?')
            print(f'  1) {copied_teams[0]}',f'  2) {copied_teams[1]}',f'  3) {copied_teams[2]}')
            team_choice = input('\n  > ')
            valid_ans = ('1','2','3')
            while team_choice not in valid_ans:
                if team_choice in valid_ans:
                    break
                team_choice = input('\nPlease pick from the available teams \n  ~ ')
                
            if team_choice == '1':
                display_team(panthers)
                
            elif team_choice == '2':
                display_team(bandits)
            
            elif team_choice == '3':
                display_team(warriors)
            
            second_choice = input('\nWould you like to learn about another team? [y]es or [n]o? \n  > ')
            valid_second = ('y', 'n')
            while second_choice not in valid_second:
                if second_choice in valid_second:
                    break
                second_choice = input("'y' or 'n' \n  ~ ")
                
            if second_choice == 'y':
                second_choice = initial_choice
                continue
                
            elif second_choice == 'n':
                print('\nThank you for joining me!\n')
                time.sleep(1.5)
                answering = False
                break




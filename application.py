import constants
import copy
import random

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


def parents(*args):
    the_guardians = []
    for team in args:
        for the_players in team:
            if (' and ') in the_players['guardians']:
                guard1, guard2 = the_players['guardians'].split(' and ')
                the_guardians.append(guard1)
                the_guardians.append(guard2)
            else:
                the_guardians.append(the_players['guardians'])
    return the_guardians


cleaned_data(cleaned_players)
random.shuffle(cleaned_players)

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
            print(f'  1) {copied_teams[0]}')
            print(f'  2) {copied_teams[1]}')
            print(f'  3) {copied_teams[2]}')
            team_choice = input('\n  > ')
            valid_ans = ('1','2','3')
            while team_choice not in valid_ans:
                if team_choice in valid_ans:
                    break
                team_choice = input('\nPlease pick from the available teams \n  ~ ')
                
            if team_choice == '1':
                print('\n   - PANTHERS - ')
                print('_____________________________________________')
                print(f'\nAmount in team: {int(len(panthers))}')
                print(f'Total Experienced: {int(len(panthers)/2)}')
                print(f'Total Inexperienced: {int(len(panthers)/2)}')
                print(f'Average Height: {avg_height(panthers)}')
                print('_____________________________________________')
                print('\n  Players:')
                display_players(panthers)   
                print('\n  Guardians:')
                panthers_guardians = parents(panthers)
                print(', '.join(panthers_guardians))
                print('_____________________________________________')
                
            elif team_choice == '2':
                print('\n   - BANDITS - ')
                print('_____________________________________________')
                print(f'\nAmount in team: {int(len(bandits))}')
                print(f'Total Experienced: {int(len(bandits)/2)}')
                print(f'Total Inexperienced: {int(len(bandits)/2)}')
                print(f'Average Height: {avg_height(bandits)}')
                print('_____________________________________________')
                print('\n  Players:')
                display_players(bandits)  
                print('\n  Guardians:')
                bandits_guardians = parents(bandits)
                print(', '.join(bandits_guardians))
                print('_____________________________________________')
            
            elif team_choice == '3':
                print('\n   - WARRIORS - ')
                print('_____________________________________________')
                print(f'\nAmount in team: {int(len(warriors))}')
                print(f'Total Experienced: {int(len(warriors)/2)}')
                print(f'Total Inexperienced: {int(len(warriors)/2)}')
                print(f'Average Height: {avg_height(warriors)}')
                print('_____________________________________________')
                print('\n  Players:')
                display_players(warriors)
                print('\n  Guardians:')
                warriors_guardians = parents(warriors)
                print(', '.join(warriors_guardians))
                print('_____________________________________________')
            
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
                print('\nThank you for joining me!')
                answering = False
                break

import constants

teams = constants.TEAMS[::]
players = constants.PLAYERS[::]
length_of_teams = len(teams)
numb_of_player = len(players)
players_per_team = num_of_players_per_team = num_of_player/ length_of_teams
teams_with_players = {}

for team in teams:
    teams_with_players[team] = []

print('Baseball Team Stats Tool')
print('\n')

while True:
    print('>>>>>>>>> Menu <<<<<<<<< \n')
    print('Please choose one of the following options')
    print('(1) Display Stats')
    print('(2) Exit Application \n')
    user_option_choice = int(input('Enter an option:  '))
    try:
        if (user_option_choice == 1):
            team_index = 0
            for player in players:
                if (team_with_players[teams[teams_index]] == []):
                    print("What the fuck is this guy doing?")
                    print(teams_with_players[teams])
    
        elif (user_option_choice == 2):
            print("Goodbye")
            break
    except ValueError:
        break
    
    if __name__ == '__main__':
        print(player[0])

        print(people[1]['name'])
    print(people[1]['age'])
    print(player[0]['sex'])
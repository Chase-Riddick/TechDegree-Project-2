import constants

teams_list = constants.TEAMS[::]
players_list = constants.PLAYERS[::]

def display_start_menu():
    print('BASKETBALL TEAM STATS TOOL \n')
    print('---- MENU ---- \n')
    print('Here are your choices:')
    print('1) Display Team Stats')
    print('2) Quit')

def get_menu_option():
    menu_option = 0
    while menu_option != "1" and menu_option != "2":
        menu_option = input("Enter an option: ")
    return menu_option

def get_team_option():
    team_option = None
    print(f'1. {teams_list[0]}')
    print(f'2. {teams_list[1]}')
    print(f'3. {teams_list[2]}')
    while team_option != "1" and team_option != "2" and team_option != "3":
        team_option = input("Enter an option: ")
    return team_option




# def create_teams():


# def print_team_statistics():

player1 = players_list[:2:]
for key, value in player1:
    print(f'{key}:  {value}')

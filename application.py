import random
import sys
import constants


playerslista = constants.PLAYERS
teams = constants.TEAMS


def display_start_menu():
    """ \n\n\n Prints a message introducing the function/ purpose of application, as well as the input commands used to proceed with its use or        exit."""
    print(" >>>>>> Baseball Stats Tool <<<<<\n")
    print(" Welcome to the Baseball Stats Tool")
    print("* This application separates a pool of players into three different baseball teams.")
    print("* The user can use the application to view a range of statistics on each of the teams.\n") 
    print("To proceed, please enter one of the following commands:")
    print("Enter 'C' if you would like to continue with using application.")
    print("Enter 'E' if you would like to exit the application. \n")


def  user_input():
    """Collects users input """
    user_input = input(">>> ")
    return user_input


def test_function(func):
    value1 = func
    accepted_value1 = "C" 
    accepted_value2 = "E"
    
    if value1 != accepted_value1 or value1 != accepted_value2:
        while value1 != accepted_value1 and value1 != accepted_value2:
            print(f"Sorry, '{value1}' isn't an accepted option. Please input 'C' or 'E' (Continue/ Exit)")
            value1 = user_input()
    print(f"You entered: {value1}")
    return value1


def proceed_or_exit_app(value):
    command_input = value
    if command_input == "E":
        exit_app()
    if command_input == "C":
        print("Well, let's continue onward shall we? \n")
        

def exit_app():
    print("\n You have opted to 'Exit' this application.")
    print("That's an unfortunate choice! But thanks for giving it a try at least.")
    print("Have a great day, and we'll to see you around here again soon.")
    sys.exit()


def convert_player_height_into_int(list):
    """ """
    for element in list:
        height = element['height'].split(" ")
        element['height'] = int(height[0])
    return list

def convert_experience_into_bool(list):
    for element in list:
        if element['experience'].lower() == "yes":
            element['experience'] = bool(1)
        elif element['experience'].lower()  == "no":
            element['experience'] = bool(0)
    return list


def separate_players_by_experience(list):
    experienced_players_list = []
    inexperienced_players_list = []
    
    for element in list:
        if element['experience'] == True:
            experienced_players_list.append(element)
            
        elif element['experience']  == False:
            inexperienced_players_list.append(element)
    
    return experienced_players_list, inexperienced_players_list


def sort_players_into_team_by_experience(experienced_players_list, inexperienced_players_list, teams_list):
    """ """
    experienced_players = experienced_players_list 
    inexperienced_players = inexperienced_players_list 
    
    experienced_players = random.sample(experienced_players, len(experienced_players))
    inexperienced_players = random.sample(inexperienced_players, len(inexperienced_players))

    experienced_players_per_team = int(len(experienced_players)/ len(teams_list))
    inexperienced_players_per_team = len(inexperienced_players)/ len(teams_list)
    
    teams_and_player_list = [None] * len(teams_list)

    teams_and_player_list[0] = experienced_players[:experienced_players_per_team]
    teams_and_player_list[1] = experienced_players[experienced_players_per_team:int(experienced_players_per_team * 2)]
    teams_and_player_list[2] = experienced_players[int(experienced_players_per_team * 2):]
    
    teams_and_player_list[0].extend(inexperienced_players[:experienced_players_per_team])
    teams_and_player_list[1].extend(inexperienced_players[experienced_players_per_team:int(experienced_players_per_team * 2)])
    teams_and_player_list[2].extend(inexperienced_players[int(experienced_players_per_team * 2):])
    
    
    return teams_and_player_list


def generate_teams(players_list, teams_list):
    teamlista = teams_list
    playerslista = players_list
    playerslista = convert_player_height_into_int(playerslista)
    playerslista = convert_experience_into_bool(playerslista)
    experienced_players, inexperienced_players = separate_players_by_experience(playerslista)
    new_teams = sort_players_into_team_by_experience(experienced_players, inexperienced_players, teams_list)

    return new_teams
    
def user_input_teams():
    """Collects users input """
    while True:
        try:
            user_input = int(input(">>> "))
            break
        except ValueError:
            print(f"Please input an integer value only to proceed.")
    
    return user_input


def display_teamselection_options(teams_list_import):
    teams_list = teams_list_import
    top_of_teams_range = len(teams_list)
    print("\nSo, then which of the baseball teams below would you like to print stats for?")
    print(f"Please input a number correpsonding to the teams below. (1 - {top_of_teams_range})")
    
    for (num, team) in enumerate(teams_list):
        print(num+1, team)
        

def get_valid_input(teams_list_import):
    value = int(user_input_teams())
    team_max_range = len(teams_list_import)
    
    if 1 <= value <= team_max_range:
        print(f"You have selected to display stats for Team {value}: The {teams_list_import[value - 1]}")
    else:
        while value > team_max_range or 1 > value:
            (f"Sorry, '{value}'' isn't an accepted option. Please input an integer between 1 - {team_max_range}.")
            value = user_input_teams()

    return value
    
    
def teams_selection(teams_list_import):
    display_teamselection_options(teams_list_import)
    team_selection = get_valid_input(teams_list_import)
    return team_selection

    
def display_team_statistics(teams_list_import, list_of_teams_and_players, user_select_team_input):
    """  This is the main function of the application. It runs calculations for team states, and prints a diplay of these to the user. """
    
    print(f"\n\nStats for Team {user_select_team_input}: The {teams_list_import[user_select_team_input - 1]}")
    print("------------------------------" )
    
    team_input = int(int(user_select_team_input) - 1)
    
    number_of_players = len(list_of_teams_and_players[team_input])
    print(f"Total Players: {number_of_players}")

    player_names = []
    for player in list_of_teams_and_players[team_input]:
        player_names.append(player['name'])
    player_names = (', ').join(player_names)
    # print((', ').join(player_names))
    print(f"Player Names: {player_names}")
  
    number_of_experienced_players = 0
    for player in list_of_teams_and_players[team_input]:
        if player['experience'] == True:
            number_of_experienced_players += 1
    print(f"Experienced Players: {number_of_experienced_players}")
  
    number_of_inexperienced_players = (number_of_players - number_of_experienced_players)
    print(f"Inexperienced Players: {number_of_inexperienced_players}")
  
    total_team_height = []
    for player in list_of_teams_and_players[team_input]:
        total_team_height.append(player['height'])
    average_height = (sum(total_team_height))/number_of_players
    average_height = round(average_height, 1)
    print(f"Average Height: {average_height}")
    # average_height = sum(total_team_height)/number_of_players
   
    
    guardian_names = []
    print("Name of Guardians: ")
    for player in list_of_teams_and_players[team_input]:
        x = player['guardians'].split("and")
        (', ').join(x)
        guardian_names.extend(x)
    
    print((', ').join(guardian_names))


display_start_menu()
user_command = test_function(user_input())
proceed_or_exit_app(user_command)
new_teams = generate_teams(playerslista, teams)

while True: 
    team_choice = teams_selection(teams)
    display_team_statistics(teams, new_teams, team_choice)
    print("Enter 'C' if you would like to continue using application.")
    print("Enter 'E' if you would like to exit the application.")
    user_command = test_function(user_input())
    proceed_or_exit_app(user_command)
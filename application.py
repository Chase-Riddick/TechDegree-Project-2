import random
import sys
import constants


players_list = constants.PLAYERS
teams_list = constants.TEAMS


def display_start_menu():
    """ Prints a message introducing the function/ purpose of application; stipulates range of user commands."""
    
    print("\n\n>>>>>> Baseball Stats Tool <<<<<")
    print("-----------------------------------\n" )
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


def constrain_user_input(input_function):
    """ Constrains user_input to C (continue) or E (exit)."""

    input_value = input_function
    accepted_values = ["C","E"]
    accepted_values[0]
    accepted_values[1]
    
    if input_value != accepted_values[0] or input_value != accepted_values[1]:
        while input_value != accepted_values[0] and input_value != accepted_values[1]:
            print(f"Sorry, '{input_value}' isn't an accepted option. Please input 'C' or 'E' (Continue/ Exit)")
            input_value = user_input()

    return input_value


def proceed_or_exit_app(user_command_input):
    """ Runs user input, exiting if user inputted corresponding value."""

    user_command = user_command_input
    if user_command == "E":
        exit_app()
    print("You've opted to'continue' - great choice!\n")
        

def exit_app():
    """ Completes exit of application."""

    print("\nYou've opted to 'Exit' this application.\n")
    print("Thanks for taking the time to check out this application. \n Have a great day, and I'll hope to see you around here again soon.")
    sys.exit()


def convert_player_height_into_int(players_list_input):
    """ Runs player list through to change height keyvalue from string into int."""

    for player in players_list_input:
        height = player['height'].split(" ")
        player['height'] = int(height[0])
    return players_list_input


def convert_experience_into_bool(players_list_input):
    """ Runs player list experience through to change experience keyvalue from string to Boolean value."""

    for player in players_list_input:
        if player['experience'].lower() == "yes":
            player['experience'] = bool(1)
        elif player['experience'].lower()  == "no":
            player['experience'] = bool(0)
    return players_list_input


def separate_players_by_experience(players_list_input):
    """ Runs player list through to create two new player list based on whether on not player has experience."""

    experienced_players_list = []
    inexperienced_players_list = []
    
    for player in players_list_input:
        if player['experience'] == True:
            experienced_players_list.append(player)
            
        elif player['experience'] == False:
            inexperienced_players_list.append(player)
    
    return experienced_players_list, inexperienced_players_list


def distribute_equally_players_by_experience(experienced_players_list_input, inexperienced_players_list_input, teams_list_input):
    """Run through player list, creating two new teams based on experience."""
    
    experienced_players = experienced_players_list_input
    inexperienced_players = inexperienced_players_list_input
    
    experienced_players = random.sample(experienced_players, len(experienced_players))
    inexperienced_players = random.sample(inexperienced_players, len(inexperienced_players))

    experienced_players_per_team = int(len(experienced_players)/ len(teams_list_input))
    inexperienced_players_per_team = len(inexperienced_players)/ len(teams_list_input)
    
    teams_and_player_list = [None] * len(teams_list_input)

    teams_and_player_list[0] = experienced_players[:experienced_players_per_team]
    teams_and_player_list[1] = experienced_players[experienced_players_per_team:int(experienced_players_per_team * 2)]
    teams_and_player_list[2] = experienced_players[int(experienced_players_per_team * 2):]
    
    teams_and_player_list[0].extend(inexperienced_players[:experienced_players_per_team])
    teams_and_player_list[1].extend(inexperienced_players[experienced_players_per_team:int(experienced_players_per_team * 2)])
    teams_and_player_list[2].extend(inexperienced_players[int(experienced_players_per_team * 2):])
    
    return teams_and_player_list


def generate_teams(players_list_input, teams_list_input):
    """ This function combines the following functions to process the players list, and generate completed teams lists from it."""

    function_players_list = players_list_input
    function_players_list = convert_player_height_into_int(function_players_list)
    function_players_list = convert_experience_into_bool(function_players_list)
    experienced_players, inexperienced_players = separate_players_by_experience(function_players_list)
    newly_generated_teams = distribute_equally_players_by_experience(experienced_players, inexperienced_players, teams_list)

    return newly_generated_teams
    

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
    """ Takes teams list, and prompts user to choose what team to print stats on."""

    teams_list = teams_list_import
    top_of_teams_range = len(teams_list)
    print("\nSo, then which of the baseball teams below would you like to print stats for?")
    print(f"Please input a number correpsonding to the teams below. (1 - {top_of_teams_range})")
    
    for (num, team) in enumerate(teams_list):
        print(num+1, team)
        

def get_valid_input(teams_list_import):
    """ This constrains user input to choosing a value corresponding to one of the teams."""

    value = int(user_input_teams())
    team_max_range = len(teams_list_import)
    
    if 1 <= value <= team_max_range:
        print(f"You have selected to display stats for Team {value}: The {teams_list_import[value - 1]}")
    else:
        while value > team_max_range or 1 > value:
            (f"Sorry, '{value}'' isn't an accepted option. Please input an integer between 1 - {team_max_range}.")
            value = user_input_teams()

    return value
    
    
def teams_selection_function(teams_list_import):
    """ This function combines the previous few together to bring together process for user choosing a team."""
    display_teamselection_options(teams_list_import)
    team_selection = get_valid_input(teams_list_import)
    return team_selection

    
def display_team_statistics(teams_list_import, list_of_teams_and_players, user_select_team_input):
    """  This is the main function of the application. It runs calculations for team states, and prints a diplay of these to the user. """
    
    print(f"\n\nStats for Team {user_select_team_input}: The {teams_list_import[user_select_team_input - 1]}")
    print("------------------------------" )
    
    team_input = int(int(user_select_team_input) - 1)
    

    number_of_players = len(list_of_teams_and_players[team_input])
    print(f"- Total Players: {number_of_players}")


    player_names = []
    for player in list_of_teams_and_players[team_input]:
        player_names.append(player['name'])
    player_names = (', ').join(player_names)
    # print((', ').join(player_names))
    print(f"- Player Names: {player_names}")
  

    number_of_experienced_players = 0
    for player in list_of_teams_and_players[team_input]:
        if player['experience'] == True:
            number_of_experienced_players += 1
    print(f"- Experienced Players: {number_of_experienced_players}")
  

    number_of_inexperienced_players = (number_of_players - number_of_experienced_players)
    print(f"- Inexperienced Players: {number_of_inexperienced_players}")
  

    total_team_height = []
    for player in list_of_teams_and_players[team_input]:
        total_team_height.append(player['height'])
    average_height = (sum(total_team_height))/number_of_players
    average_height = round(average_height, 1)
    print(f"- Average Height: {average_height}")
    # average_height = sum(total_team_height)/number_of_players
   
    
    guardian_names = []
    print("- Name of Guardians: ")
    for player in list_of_teams_and_players[team_input]:
        x = player['guardians'].split(" and ")
        (', ').join(x)
        guardian_names.extend(x)
    
    print((', ').join(guardian_names))


""" 
    The rundown:
    Display start menu.
    Does the user want to continue to use app or exit?
    Process command accordingly.
    If user wishes to continue...
    First generate the teams by processing player data, and sifting them according to experience.
    Then give the user a menu of options have them choose a team to print stats on.
    Print the stats for the team they selected.
    Take user input to allow them them to exit the app or return to the team selection menu to print stats from another team. 
."""

if __name__ == "__main__":

    display_start_menu()
    user_command = constrain_user_input(user_input())
    proceed_or_exit_app(user_command)
    filled_teams_list = generate_teams(players_list, teams_list)

    while True: 
        team_selection = teams_selection_function(teams_list)
        display_team_statistics(teams_list, filled_teams_list, team_selection)
        print("\n\nEnter 'C' if you would like to continue using application to print the stats of another team.")
        print("Enter 'E' if you would like to exit the application.")
        user_command = constrain_user_input(user_input())
        proceed_or_exit_app(user_command)
import constants.py
import random

teams = constants.TEAMS
number_of_teams = len(teams)
panthers, bandits, warriors = teams

players = constants.PLAYERS
number_of_players = len(players)

experienced_players = ()
number_of_experienced_players = len(experienced_players)
experienced_players_per_team = int(number_of_experienced_players/ number_of_teams)

inexperienced_players = ()
number_of_inexperienced_players = len(inexperienced_players)
inexperienced_players_per_team = int(number_of_inexperienced_players/ number_of_teams)


def display_start_menu():
    print(" >>>>>> Baseball Stats Tool <<<<< ")
    print(" Welcome to the Baseball Stats Tool")
    print("* This application separates a pool of players into three different baseball teams.")
    print("* The user can use the application to view a range of statistics on each of the teams.") 
    print("To proceed, please enter one of the following commands:")
    print("Enter "C" if you would like to continue using application.")
    print("Enter "E" if you would like to exit the application."

    user_input = None

    while user_input != "C" or != "E":
        try: 
            user_input = ("What would you like to do? (C/E) >>> ").lower
        if user_input != "C" or != "E":
            print ("Please enter a valid option.")
            continue
        else:
            return user_input


def convert_player_height():
      for player in teams[team_input]:
        height = player['height'].split(" ")
        player['height'] = int(height[0])


def calculate_team_avgheight(number):
    for player in players:
        sum = sum + player['height']
        average_height = sum / number
    return average_height


def convert_player_experience():
    for player in players:
        if player['experience'] == "Yes":
            player['experience'] == bool("Yes")
        elif player['experience'] == "No":
            player['experience'] == bool("")
            # Change this solution is possilbe.
        

def separate_players_by_experience():
    for player in players:
        if player['experience'] = TRUE
         experienced_players.append(player)
        elif player['experience'] = FALSE
         inexperienced_players.append(player)


def calculate_team_experienced_players(team_input):
    number_of_experienced_players = []
    for player in teams[team_input]:
        if player['experience'] == True
            number_of_experienced_players += 1
    return number_of_experienced_players


def diplay_team_names(team_input):
    team_names = []
    for player in teams[team_input]:
        team_names.append(player['name'])
    return team_names


def generate_teams():
    experienced_players = random.shuffle(experienced_players)
    inexperienced_players = random.shuffle(inexperienced_players)

    experienced_players_per_team = []
    inexperienced_players_per_team = []

    teams[0].extend(experienced_players[:experienced_players_per_team])
    teams[1].extend(experienced_players[experienced_players_per_team:int(experienced_players_per_team * 2)])
    teams[2].extend(experienced_players[int(experienced_players_per_team * 2)])


def display_guardian_list(team_input):
      for player in team[team_input]:
        player_guardians = player['guardians'].split("and")
        team_guardians.append(player_guardians)
        return(team_guardians)


def display_team_options():
    print("Please select of the teams below to print stats.")
    print(f"Team {teams.index[team[0]] + 1}: {teams[0]}")
    print(f"Team {teams.index[team[1]] + 1}: {teams[1]}")
    print(f"Team {teams.index[team[2]] + 1}: {teams[2]}")

    user_select_team_input = ()
    
    while user_select_team_input != 1 and user_select_team_input != 2 and user_select_team_input != 3: 
        try:
        user_select_team_input = input("Which team would you like to select? (1 - 3) >>> ")
        
        if user_select_team_input != 1 and user_select_team_input != 2 and user_select_team_input != 3:
            print("Please input a valid option.")

        else:
            return user_select_team_input


def display_team_statistics():

    team_input = int(int(user_select_team_input) - 1)
    number_of_players = len(team[team_input])
    number_of_experienced_players = calculate_team_experienced_players(team_input)
    number_of_inexperienced_players = (number_of_experienced_players - number_of_players)
    average_height = calculate_team_avgheight(number)

    print(f"Stats for Team {}:" )
    print(f"---------------------" )
    print(f"Total Players: {number_of_players}")
    print(f"Experienced Players: {number_of_experienced_players}")
    print(f"Inexperienced Players: {number_of_inexperienced_players}")
    print(f"Average Height: {average_height}")

    print("Player Names: ")
    print(",".join(team_names))
    print(f"{}")

    print(f"Guardians: ")
    print(",".join(team_guardians))
    print(f"{}")

    #https://stackoverflow.com/questions/983354/how-do-i-make-python-wait-for-a-pressed-key#:~:text=input%20%28%22Press%20Enter%20to%20continue...%22%29%20In%20Python%202,waits%20for%20the%20user%20to%20press%20enter%20though.

    try:
        input("Press enter to continue")
    except SyntaxError:
        pass


def return_start_menu():
    print("Enter "C" if you would like to continue using application.")
    print("Enter "E" if you would like to exit the application."

     user_select_team_input = ()
    
    while user_select_team_input != 1 and user_select_team_input != 2 and user_select_team_input != 3: 
        try:
        user_select_team_input = input("Which team would you like to select? (1 - 3) >>> ")
        
        if user_select_team_input != 1 and user_select_team_input != 2 and user_select_team_input != 3:
            print("Please input a valid option.")

        else:
            return user_select_team_input



display_start_menu()
convert_player_height()
convert_player_experience()
separate_players_by_experience
generate_teams()
display_team_options()
display_team_statistics

diplay_team_names(team_input)
alculate_team_experienced_players(team_input)
display_guardian_list(team_input)
calculate_team_avgheight(number)
display_guardian_list(team_input)

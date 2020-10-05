 
bandits  = []
experienced = ['John', 'Nate', 'Sam', 'Mary', 'Dil', 'Jane', 'Sally', 'Herbert', 'Dorthy']
number_of_players = len(experienced)
trial_number = int(number_of_players / 3)

bandits.extend(experienced[:trial_number])

print(bandits)
print(trial_number)

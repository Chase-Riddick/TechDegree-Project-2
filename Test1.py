import Test
import constants

players  = constants.PLAYERS[::]

for element in players:
    for key, value in element.items():
        if str(key) == 'experience':
            print(f'{key}')
    print("\n")

PLAYERS = {
        'name': 'Karl Saygan',
        'guardians': 'Heather Bledsoe',
        'experience': 'YES',
        'height': '42 inches'
}




for key, value in PLAYERS.items():
    if value == 'NO':
        PLAYERS[value] = True

print(PLAYERS)
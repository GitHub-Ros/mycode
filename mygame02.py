#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory:', inventory)
    if 'items' in rooms[currentRoom]:
        print('You see a ' + ', '.join(rooms[currentRoom]['items']))
    print("---------------------------")

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'items': ['key'],
        'west': 'Garage'
    },
    'Kitchen': {
        'north': 'Hall',
        'items': ['monster'],
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'items': ['potion']
    },
    'Garden': {
        'north': 'Dining Room',
    },
    'Garage': {
        'east': 'Kitchen',
        'items': ['tire iron'],
        'south': 'Basement',
    },
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split(" ", 1)

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way!')

    if move[0] == 'get' and len(move) > 1:
        if 'items' in rooms[currentRoom] and move[1] == rooms[currentRoom]['items'][0]:
            inventory.append(move[1])
            print(move[1] + ' got!')
            #del rooms[currentRoom]['items']
        else:
            print('Can\'t get ' + move[1] + '!')

    if currentRoom == 'Kitchen':
        if 'tire iron' in inventory:
            print('You beat the monster to death with a tire iron.')
            del rooms[currentRoom]['items']
        else:
            print('A monster has got you... Game Over!')
            break
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break


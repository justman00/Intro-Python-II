from room import Room
import textwrap
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# a bunch of items
a = Item("rock", "huge rock smth")
b = Item("scissors", "huge scissors smth")
c = Item("paper", "huge paper smth")
d = Item("water", "huge water smth")
e = Item("ipad", "huge ipad smth")
f = Item("iphone", "huge iphone smth")
g = Item("python", "huge python smth")


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
from player import Player

# Make a new player object that is currently in the 'outside' room.
player = Player('Andy', room['outside'])

player.addItem(a)
player.addItem(b)
player.addItem(c)

room['foyer'].addItem(d)
room['foyer'].addItem(e)
room['foyer'].addItem(f)
room['foyer'].addItem(g)

# player.get_items()
# room['foyer'].get_items()
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
cards = ['n', 's', 'e', 'w']
commands = ['add', 'drop', 'get']


def check_for_direction(val):
    if not val:
        print("You can not go there")
    else:
        player.room = val


def check_cardinal(direction):
    check_for_direction(getattr(player.room, f"{direction}_to"))


def perform_command(com, itemName):
    getattr(player, f'{com}Item')


def check_command(com, room):
    command = com[0]
    itemName = com[1]

    print(command, itemName)

    if command not in commands or not itemName:
        print("Oups, command not found, you can either get or drop")
    elif command == 'get':
        item = room.getItem(itemName)
        player.addItem(item)
        room.dropItem(itemName)
    elif command == 'drop':
        item = player.getItem(itemName)
        room.addItem(item)
        player.dropItem(itemName)


while True:
    print(player.room.__str__())
    print(textwrap.wrap(player.room.description))
    print("Room items:")
    player.room.get_items()
    print("Your items:")
    player.get_items()

    answer = input()

    if answer == 'q':
        break

    if answer in cards:
        check_cardinal(answer)
    else:
        answer = answer.split(' ')
        check_command(answer, player.room)

    print("\n\n")

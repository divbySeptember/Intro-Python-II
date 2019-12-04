from room import Room
from player import Player
# nimport time

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Declare a Item

item = {"fork", "Just in case."}
current_room = room['foyer']




# Main
#
#
# Create a player object


quit = False

player = Player("", room['foyer'])




while quit is False:
    # intro()
    print("you are in a", player.current_room)
    time.sleep(2)
    print("where will you go?")
    time.sleep(2)
    command = input(f"\n(N)orth\n(E)ast\n(S)outh\n(W)est\n(I)nspect area\n(Q)uit while I'm healthy\n\nCommand: ")
    command = command.lower().strip()    #normalize inputs - lowercase and strip removes any extra leading or tailing spaces
    # if command == '':
    #     continue
    # command = command[0]      #no matter how long the input, just take the first letter - not perfect "eat" can head east
    if command == 'q':
        quit: True
        print("so long!")
    elif command == 'n':    # head north
        print("heading north")
        time.sleep(2)
        if player.current_room.n_to:
            player.switch_room(player.current_room.n_to)
        else:
            print("Can't go north.")
    elif command == 'e':    # head east
        print("heading east")
        time.sleep(2)
        if player.current_room.e_to:
            player.switch_room(player.current_room.e_to)
        else:
            print("Can't go east.")
    elif command == 's':    # head south
        print("heading south")
        time.sleep(2)
        if player.current_room.s_to:
            player.switch_room(player.current_room.s_to)
        else:
            print("Can't go south.")
    elif command == 'w':    # head west
        print("heading west")
        time.sleep(2)
        if player.current_room.w_to:
            player.switch_room(player.current_room.w_to)
        else:
            print("Can't go west.")
        
        
    # elif command == 'i':    # investigate the area
    #     pass
    else:
        print("not a valid command\ntry again")
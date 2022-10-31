# Sebastian Jimenez

rooms = {
    'Main Hallway': {'South': 'Main Bridge', 'North': 'Engineering Room', 'West': 'Residential Area', 'East': 'Recreational Area'},
    'Residential Area': {'North': 'Cafeteria', 'East': 'Main Hallway', 'item': 'Pants'},
    'Cafeteria': {'South': 'Residential Area', 'item': 'Pod Escape Key'},
    'Main Bridge': {'North': 'Main Hallway', 'East': 'Escape Pod Room', 'item': 'Helmet'},
    'Engineering Room': {'South': 'Main Hallway', 'East': 'Armory', 'item': 'Oxygen Tank'},
    'Armory': {'West': 'Engineering Room', 'item': 'Laser Gun'},
    'Clinic Wing': {'South': 'Recreational Area', 'item': 'Gloves'},
    'Recreational Area': {'West': 'Main Hallway', 'North': 'Clinic Wing', 'item': 'Torso Part'},
    'Escape Pod Room': {'West': 'Main Bridge', 'item': 'Bad Alien'}
    }



print('Space Adventure Game')
print('Collect 7 items to win the game, or be eaten by the alien')
print('\nYou awaken in the Main Hallway of the derelict ship')

def show_instructions():
    print('Move commands: go South, go North, go East, go West')
    print('Add to Inventory: get "item name"')

def show_status():
    print()
    print(current_room)
    print('Inventory: {}'.format(items_obtained))
    print()


items_obtained = []
directions = ['North', 'South', 'West', 'East']
items_list = ['Pants', 'Pod Escape Key', 'Oxygen Tank', 'Laser Gun', 'Gloves', 'Torso Part', 'Helmet']

def grab_item():
    while True:
        global items_obtained
        if current_room != 'Main Hallway' and current_room != 'Escape Pod Room':
            if rooms[current_room]['item'] not in items_obtained:
                print('You see a {}'.format(rooms[current_room]['item']))
                item_input = str(input())
                item_input = item_input.split()
                item_input.pop(0)
                item_input = ' '.join(item_input)
                if current_room != 'Escape Pod Room' and current_room != 'Main Hallway':
                    if item_input not in items_obtained:
                        if item_input in items_list:
                            if item_input in rooms[current_room]['item']:
                                items_obtained.append(rooms[current_room]['item'])
                                print("\n*** You've obtained", rooms[current_room]['item'],"***")
                                print('Inventory: {}'.format(items_obtained))
                                print()
                                break
                            else:
                                print('That Item is not in this room')
                        else:
                            print('Please type in a valid command')

                    else:
                        break
            else:
                break
        else:
            break




def move_rooms():
    global current_room
    move_input = input()
    move_input = move_input.title().split()
    move_input[1].title()
    if move_input[1] in directions:
        if move_input[1] in rooms[current_room]:
            current_room = rooms[current_room][move_input[1]]
            print('You are now in {}'.format(current_room))
        else:
            print("XXX You can't go that way. Try another direction. XXX")


current_room = 'Main Hallway'
while True:
    show_instructions()
    if current_room == 'Escape Pod Room':
        if len(items_obtained) == 7:
            print()
            print('*' * 30)
            print('Congrats on beating the bad alien')
            print('*' * 30)
            exit()
        else:
            print('You lose. try again')
            exit()
    if current_room != 'Escape Pod Room':
        show_status()
        move_rooms()
        if current_room != 'Main Hallway' or current_room != 'Escape Pod Room':
            grab_item()
            continue

# Debugging.






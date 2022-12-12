import webbrowser
import time
import getpass
import os
#!/bin/python3

respawn_room = 'Hall'

# Replace RPG starter project with this code when new instructions are live
play = True
while play == True:
  play=False
  def showInstructions():
    #print a main menu and the commands
     print('''
      manerium
      ========
      Commands:
        go [direction]
        get [item]
      -----------------
      Remember to use the _ in some necessary items''')

  def showStatus():
      #print the player's current status
      print('---------------------------')
      print('You are in the ' + currentRoom)
      #print the current inventory
      print('Inventory : ' + str(inventory))
      #print an item if there is one
      if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
        print("---------------------------")

    #an inventory, which is initially empty
  inventory = []

    #a dictionary linking a room to other rooms
  rooms = {

                'Hall' : { 
                      'south' : 'Kitchen',
                      'east' : 'Dining Room',
                      'north' : 'Front Garden',
                      'west' : 'Hallway',
                      '27a38b' : 'Cheat Room'
                        
                    },
                'Armory' : {
                      'south' : 'Dining Room',
                      'item' : 'sword'
                    },

                'Kitchen' : {
                      'north' : 'Hall',
                      'item' : 'dying monster',
                      'south' : 'Broom Cupboard'
                        
                    },
                      
                'Dining Room' :{
                      'west' : "Hall",
                      'south' : 'Garden',   
                      'north' : 'Armory'
                        
                    },
                'Broom Cupboard' :{
                      'north' : 'Kitchen',
                      'item' : 'potion'
                    },
                        
                'Garden' : {
                      'north' : 'Dining Room'
                        
                    },
                'Front Garden' : {
                      'south' : 'Hall',
                      'item' : 'key'

                    },
                'Hallway' : {
                      'east' : 'Hall',
                      'north' : 'Stairs'

                    },

                'Stairs' : {
                      'south' : 'Hallway',
                      'north' : 'Landing'

                    },

                'Landing' : {
                      'south' : 'Stairs',
                      'west' : 'Bathroom',
                      'east' : 'Corridor',
                      'north' : 'Nursery'

                    },

              'Bathroom' : {
                    'east' : 'Landing',
                    'item' : 'ladder'

                  },

              'Corridor' : {
                    'west' : 'Landing',
                    'item' : 'picture',
                    'north' : 'Guest Bedroom',
                    'south' : 'Games Room'

                  },

              'Guest Bedroom' : {
                    'south' : 'Corridor',
                    'item' : 'blue_key'

                  },

              'Nursery' : {
                    'south' : 'Landing',
                    'item' : 'gun',
                    'west' : 'Morgue'

                  },

              'Games Room' : {
                    'north' : 'Corridor',
                    'south' : 'Secret Stairs'

                  },

              'Secret Stairs' : {
                    'north' : 'Games Room',
                    'south' : 'Secret Room'

                  },

              'Secret Room' : {
                    'south' : 'Hole in the floor',
                    'item' : 'Dying Flying Monster'

                  },

              'Hole in the floor' : {
                    'north' : 'Secret Room',
                    'south' : 'Dungeon Entrance'

                  },

              'Dungeon Entrance' : {
                    'north' : 'Hole in the floor',
                    'west' : 'Broken Hallway',
                    'east' : 'Dungeon Hallway'

                  },

              'Broken Hallway' : {
                    'east' : 'Dungeon Entrance',
                    'item' : 'Gaping Gorge',
                    'west' : 'Throne Room'

                  },

              'Dungeon Hallway' : {
                    'west' : 'Dungeon Entrance',
                    'north' : 'Witches Layer'

                   },

              'Witches Layer' : {
                    'south' : 'Dungeon Hallway',
                    'item' : 'broom'

                  },

              'Throne Room' : {
                    'east' : 'Broken Hallway',
                    'item' : 'dead_baby',
                    'north' : 'Treasure Room',
                    'south' : 'Teleport Room'

                  },

              'Treasure Room' : {
                    'south' : 'Throne Room',
                    'item' : 'red_key'

                  },

              'Teleport Room' : {
                    'north' : 'Throne Room',
                    'item' : 'teleporter',
                    'west' : 'Roof',
                    'south' : 'Hall'

                  },

              'Cheat Room' : {
                    'item' : 'potion',
                    'north' : 'Cheat Room 2'

                  },

              'Cheat Room 2' : {
                    'item' : 'red_key',
                    'north' : 'Hall',
                    'south' : 'Throne Room'

                  },

              'Morgue' : {
                    'east' : 'Nursery',
                    'item' : 'poking_stick'

                  },

              'Roof' : {
                    'north' : 'Your Grave'

                  },

              'Your Grave' : {
                    'item' : 'Grim Reaper'
                      

                  }
                      
              }


    #start the player in the Hall


  currentRoom = respawn_room

  showInstructions()
  a=getpass.getuser()


  #loop forever
  while True:

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':  
      move = input('>')
        
    move = move.lower().split()

    #if they type 'go' first
    if move[0] == 'go':
      #check that they are allowed wherever they want to go
      if move[1] in rooms[currentRoom]:
        #set the current room to the new room
          currentRoom = rooms[currentRoom][move[1]]
      #there is no door (link) to the new room
      else:
          print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
      #if the room contains an item, and the item is the one they want to get
      if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        #add the item to their inventory
        inventory += [move[1]]
        #display a helpful message
        print('Got ' + move[1])
        #delete the item from the room
        del rooms[currentRoom]['item']
      #otherwise, if the item isn't there to get
      else:
        #tell them they can't get it
        print('Can\'t get ' + move[1] + '!')
          
    if 'item' in rooms[currentRoom] and 'dying monster' in rooms[currentRoom]['item'] and 'sword' in inventory:
      print('You see a monster and slay it like the fine warrior you are')
      del rooms[currentRoom]['item']
    elif 'item' in rooms[currentRoom] and 'dying monster' in rooms[currentRoom]['item']:
      print('The monster has captured you and forced you to do some terrible things making your life a misery forcing you to go out in style by using a magic broom and a dictonary')
      like=input("Did you like the game?(y/n)")
      if like == "y":
          print("Thanks")
      else:
          os.system('shutdown -s')
      play_again=input("Do you want to play again you terrible player?(y/n)")
      if play_again == 'y':
          play=True
      break


    if 'item' in rooms[currentRoom] and 'Dying Flying Monster' in rooms[currentRoom]['item'] and 'gun' in inventory:
      print('You see a monster and kill it with one shot')
      del rooms[currentRoom]['item']
    elif 'item' in rooms[currentRoom] and 'Dying Flying Monster' in rooms[currentRoom]['item']:
      print('The monster has sliced your head in two spilling your brains on the floor')
      like=input("Did you like the game?(y/n)")
      if like == "y":
          print("Thanks")
      else:
          os.system('shutdown -s')
      play_again=input("Do you want to play again you terrible player?(y/n)")
      if play_again == 'y':
          play=True
      break

    if  currentRoom == 'Armory' and 'key' not in inventory:
      print('The door is locked...')
      move[1] = 'south'
      currentRoom = 'Dining Room'

    if  currentRoom == 'Teleport Room':
      print("Be Careful, You can be teleported ANY where")

    if  currentRoom == 'Secret Stairs' and 'blue_key' not in inventory:
      print('The door is locked...')
      move[1] = 'north'
      currentRoom = 'Games Room'

    if  currentRoom == 'Hole in the floor' and 'ladder' not in inventory:
      print('You could get stuck in there...')
      move[1] = 'west'
      currentRoom = 'Secret Room'

    if 'item' in rooms[currentRoom] and 'Gorge' in rooms[currentRoom]['item'] and 'broom' in inventory:
      print('You fly across in one movement')
    elif 'item' in rooms[currentRoom] and 'Gorge' in rooms[currentRoom]['item']:
      print('Damn this gorge. You have been falling down this for over a year when you land, breaking your pinkie in two and a spike gouges out one of your eyes when a piano falls on top of you...')
      like=input("Did you like the game?(y/n)")
      if like == "y":
          print("Thanks")
      else:
          os.system('shutdown -s')
      play_again=input("Do you want to play again you terrible player?(y/n)")
      if play_again == 'y':
          play=True
      break
        
      
    if currentRoom == 'Garden' and 'red_key' in inventory and 'potion' in inventory:
      print("You escaped the house!! you.... you....you WIN!!!(A Rubber duck) Well done " + str(a) + "                    bene factum")
      time.sleep(2)
      webbrowser.open_new("https://amsterdamduckstore.com/wp-content/uploads/2017/07/Trump-rubber-duck-Amsterdam-Duck-Store.jpg")
      like=input("Did you like the game?(y/n)")
      if like == "y":
          print("Thanks")
      else:
          os.system('shutdown -s')
      play_again=input("Do you want to play again you terrible player?(y/n)")
      if play_again == 'y':
          play=True
      break

    if currentRoom =='Corridor' and 'picture' in inventory:
      print('If you want to live get to the garden with the red key and potion, and remeber go south to survive')

    if currentRoom == 'Your Grave':
      print("Well that life was fun.....")
      like=input("Did you like the game?(y/n)")
      if like == "y":
          print("Thanks")
      else:
          os.system('shutdown -s')
      play_again=input("Do you want to play again you terrible player?(y/n)")
      if play_again == 'y':
          play=True
      break


        
    ######del rooms[currentRoom]['item']######


print("Would you like to play Minicraft?y/n")
answer = input()
if answer == 'y':
    print("Your hardcore experience will start soon")
    print("DAY ONE.")
    print("You spawn into Minicraft and there is a zombie in front of you. You have only your fists. Do you run or fight?")
    answer = input()
    if answer == 'run':
        print("Good idea. LEG IT!!!!!")
        print("You need to gather materials for a hut. Do you dig up some dirt [dirt] or use your fist to chop down trees to collect wood [wood]")
        answer = input()
        if answer == 'dirt':
            print("Usefull but not ideal. A creeper blows up your dirt hut and you get caught in the explosion. Your day in Minicraft has ended. GAME OVER!!!!!!")
            quit()
        if answer == 'wood':
            print("Wood is more durable than dirt. Good job. You have completed a day in Minicraft.")
            print("DAY TWO.")
            print("As you wake up, you realise there is no food. Do you risk going back to sleep [sleep] or go to the nearest village [village] ?")
            answer = input()
            if answer == 'sleep':
                print("You sleep but you eventually die of hunger. GAME OVER!!!!!!")
                quit()
            if answer == 'village':
                print("You trudge to the village, after destroying your hut. You raid the bakers and collect some bread and apples. You eat them at once. Your hunger is full.")
                print("You have some options of shelter. Do you set-up in the village[here], or do you go else where to build a hut with the materials you've got[there]?")
                answer = input()
                if answer == 'here':
                    print("You set up your crafting table, chests and bed in a big house, still inhabited by villagers. As you go to sleep, a zombie enters the house and turns the villagers into zombie villagers. They eat your brain and you die. GAME OVER!!!!!")
                    quit()
                if answer == 'there':
                    print("You enter a forest and build a hut with your bed, crafting table and chests. You go to bed and get a good night sleep.")
                    print("DAY THREE.")
                    print("You have 3 choises here. You can go monster hunting to get loot [hunting], you can go mining [mining], or you can set about collecting resources from the village and the woods surounding your hut [resources].")
                    answer = input()
                    if answer == 'hunting':
                        print("You own minicraft story will begin soon. But now you need to choose which quiz path to take. The [Terraria] path, the [Minecraft] path, the [Pokemon] path or the [Mario] path.")
                    if answer == 'mining':
                        print("You own minicraft story will begin soon. But now you need to choose which quiz path to take. The [Terraria] path, the [Minecraft] path, the [Pokemon] path or the [Mario] path.")
                    if answer == 'resources':
                        print("You own minicraft story will begin soon. But now you need to choose which quiz path to take. The [Terraria] path, the [Minecraft] path, the [Pokemon] path or the [Mario] path.")
                else:
                    print("You have refused to make a hut or take residence in a villagers house. You are in the wild and a skeleton starts shooting at you with it's bow. Unfortunally, all of it's arrows hit and you are dead. GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    quit()
            else:
                ("Instead of doing any of the things suggested, you go out to explore. Because you are low on hunger, you end up dying of hunger. GAME OVER!!!!")
                quit()
        else:
            print("You have desided to not create a hut. A creeper sneaks up behind you. You get killed in it's blast. To read about the creeper, open 'The Secret Life of a Creeper'. GAME OVER!!!!!")
            quit()
    if answer == 'fight':
        print("You smash the zombie with you fists but to no avail. The zombie eats your brain. For the zombie story, open 'The City of Zombies'. GAME OVER!!!!")
        quit()
else:
    print("Too bad. Bye.")
    quit()

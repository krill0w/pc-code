#log in system with a password
#the game assuming the username and password is correct

correct = True
while correct:
    name = input("What is your username?  ")
    if name == "thedragon":
        pw = input("Please enter your password  ")
        if pw == "smallfry":
            print("Please enter your password again for maximum safety")
            break  #implementing the files.
        
    if name !="thedragon":
        name = input("Access denied, would you like to try the username again?  y/n: ")
        if name == "y":
            correct = True
        else:
            print("The program you are running will now shut down.")
            quit()
                       
    if pw !="smallfry":
        pw = input("Access denied, would you like to try the password again?  y/n: ")
        if pw == "y":
            correct = False
        else:
            print("The program you are running will now shut down.")
            quit()     
                
correct2 = True
while correct2:
    pw2 = input("Please enter your password  ")
    if pw2 == "smallfry":
         print("Welcome to the files. You will now proceed to view protected documents. Please go to https://www.youtube.com/watch?v=pnmstIodYKI&annotation_id=annotation_1917709741&src_vid=bloVlkCLaXo&feature=iv for your full brefing.")
         break  #implementing the files.
                       
    if pw2 !="smallfry":
        pw2 = input("Access denied, would you like to try the password again?  y/n: ")
        if pw2 == "y":
         correct2 = True
        else:
            print("The program you are running will now shut down.")
            quit() 


           
            
        
    

gun = False
car_key = False



def mainhall_scene():
    print("\n")
    directions = ["left", "right", "forward"]
    print(" You entered the main hall of the mansion, there are doors and a stairs if you move forward, where would you like to go? ")
    userInput = ""
    while userInput not in directions:
        print(" You can only choose: left/right/forward")
        userInput = input()
        if userInput == "left":
            diningroom_scene()
        elif userInput == "right":
            galleryroom_scene()
        elif userInput == "forward":
            stairs_scene()
        else: 
            print("Please enter a valid option. ")
            mainhall_scene()



 #  diningroom scene
def diningroom_scene():
    print("\n")
    directions = ["right", "forward",]
    print(" You entered a spacious dining hall, you see a door on the right and in front, where would you like to go? ")
    userInput = ""
    while userInput not in directions:
        print(" You can only choose: right/forward/back")
        userInput = input()
        if userInput == "right":
            traproom_scene()
        elif userInput == "forward":
            print("The door is locked. You go back to the dining hall.")
            diningroom_scene()
        elif userInput =="back":
            mainhall_scene()
        else: 
            print("Please enter a valid option. ") 
            diningroom_scene() 



# gallery room
def galleryroom_scene():
    print("\n")
    directions = ["left", "right", "back"]
    global gun
    print(" You entered a room with  grotesque paintings and sculptures, you may choose to where to go down, where would you like to go? ")
    userInput = ""
    while userInput not in directions:
        print(" You can only choose: left/right/back")
        userInput = input()
        if userInput == "left":
            print( " You came inside a big closet and you found a gun, you came back to the gallery room.")
            gun = True
            galleryroom_scene()
        elif userInput == "right":
            showZombie()
        elif userInput == "back":
            mainhall_scene()
        else: 
            print("Please enter a valid option. ")
            galleryroom_scene()



# Stairs
def stairs_scene():
    print("\n")
    print("The stairs broke, and you fall to your death, game over!")
    quit()


#TrapRoom
def traproom_scene():
    print("\n")
    print(" You fall into a trap, you tried your best to get out, but you cannot. You died")
    quit()



# zombie
def showZombie():
    print("\n")
    actions = ["fight", "flee"]
    print(" You walk into hallway and there is a zombie in front of you, what will you do?")
    userInput = ""
    while userInput not in actions:
        print(" You can only choose: fight or flee")
        userInput = input()
        if userInput == "fight":
            if gun:
                print( " You fought and killed the zombie.")
                print(" You moved to the next area.")
                corridor1f()
            else:
                print(" You fought the zombie, but you were not able to defeat it. And it ate your body and brain. You died. Game Over")    
        elif userInput == "flee":
                print("Got away safely and moved to the corridor")
                corridor1f()
        else: 
            print("Please enter a valid option. ")
            showZombie()
    
    
    
#corridor right wing 1st floor
def corridor1f():
    print("\n")
    directions = ["left", "right", "forward"]
    print(" You walk into a corridor and there are two direction you may go, you may open the right door or the left door.")
    print( " Choose right or left")
    userInput = input()
    if userInput == "right":
        zombie_room()
    elif userInput == "left":
        print("A big snake immediately pounced on you. You were unable to do anything about it. It squeezed the life out of you. You died.")
        quit()
    elif userInput == "forward":
        print("You entered a garage")
        garage()
    else: 
        print("Please enter a valid option. ")
        corridor1f()



def garage():
    print("\n")
    actions = ["car", "door"]
    global car_key
    print(" You entered a garage,there is a car and a door. Where will you go?")
    userInput = ""
    while userInput not in actions:
        print(" You can only choose: car/door/back")
        userInput = input()
        if userInput == "car":
            if car_key:
                print( " You start the car with the car key and got away safely. End of game.")
            else:
                print(" The car needed a key and you try to hotwire it. While hot wiring an aggressive zombie appeared and killed you. Game over.")
                quit()
                
        elif userInput == "door":
                print("Zombie dogs suddenly appeared in front of you and killed you. Game over.")
                quit()
        else: 
            print("Please enter a valid option. ")
            garage()



def zombie_room():
    print("\n")
    actions = ["fight", "flee"]
    global gun
    global car_key
    print(" You entered a room with a zombie, what will you do?")
    userInput = ""
    while userInput not in actions:
        print(" You can only choose: fight or flee")
        userInput = input()
        if userInput == "fight":
            if gun:
                print( " You fought and killed the zombie, you found a car key in his clothes.")
                print(" You get back to the corridor")
                car_key = True
                corridor1f()
            else:
                print(" You fought the zombie, but it killed you.")
                quit()
                
        elif userInput == "flee":
                print("Got away safely back to the corridor")
                corridor1f()
        else: 
            print("Please enter a valid option. ")
            zombie_room()
    
    
    

if __name__ == "__main__":
        print("Welcome to the Mansion Game!")
        print("You are a truck driver, your truck broke down in the middle of nowhere.")
        print("You need some tools to be able to fix your truck. You see a light coming from somewhere. You walk to it")
        print("You see a mansion, and you try knocking on the door, but there was no response. You came in")
        print("Lets start with your character's name: ")
        character_name = input()
        print(" Good luck," +character_name+ "." )
        mainhall_scene()
        
                
                

           










       
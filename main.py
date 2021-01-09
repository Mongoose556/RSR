
#BASED ON :http://www.miielz.com/WWIII/Media/Red%20Storm%20Rising%20Board%20Game%20Basic%20Rules.pdf

# class factory example http://code.activestate.com/recipes/86900/

# generate random integer values
import random
from unit import Unit

############################################################################

#Dice roll function
def dice_roll():
    roll = random.randint(1, 10)# generate some integers
    print("Dice roll: ", roll) #dice roll
    return roll

#get number of turns
def get_number_of_turns():
    while True:
        try:
            turns = int(input("Number of turns (max 10): "))
        except ValueError:
            print ("Please enter a valid number between 1 and 10")
        else:
            if turns > 10:
                turns = 10
            elif turns <= 0:
                turns = 1
        return turns


def game_loop(t): #(turns)

    ''' this loop puts one unit against another until destroyed or out of turns. '''
    
    # turn 1, player attacks, 
    # if enemy alive then
    # enemy attack else win = true
    # if player alive then 
    # turn 2

    num_turns = t
    win = False
    player_unit = Unit("BLUE") # name
    enemy_unit = Unit("RED") # enemy

    while player_unit.is_alive and num_turns > 0:
        print(player_unit.name, " turn:")
        player_unit.attack(dice_roll(), enemy_unit)
        print("Status: ", player_unit.unit_status())
        
        num_turns -= 1

        print("Turns remaining: ", num_turns)
        input("Press a key.")

        if enemy_unit.is_alive:
            # win = False
            print(enemy_unit.name, " turn:")
            enemy_unit.attack(dice_roll(), player_unit)
            
            print("Status: ", enemy_unit.unit_status())
        else:
            win = True

        
    else:
        print("Game Over")
        
if __name__ == "__main__":
    num_turns=(get_number_of_turns())
    game_loop(num_turns) #call game loop function, number of turns

#Add an attribute to unit called hits_remaining.  And set it to the number of hits that each unit type can survive

#Then you can simplify the game loop to just impose a hit on a unit, then do:
#If not unit.is_alive(): print(“unit dead”) or whatever
#The other thing to think about maybe is writing tests to verify that the code does what you want
#So you’d write another method that would do something like, create a unit, call hit, and then test that it’s dead
#And then maybe have a different one for rank 3 units where you call hit once, check that it’s not dead, call it twice more, then check that it is

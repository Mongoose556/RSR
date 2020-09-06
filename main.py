
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
            print ("Please enter a valid number")
        else:
            if turns > 10:
                turns = 10
            elif turns <= 0:
                turns = 1
        return turns


def game_loop(t): #(turns)
    
#this loop puts one unit against another until destroyed or out of turns. 
#need to change it so unit take turns to attack each other

    num_turns = t

    while num_turns > 0:

        player = Unit("") # name
        enemy = Unit("") # enemy

        print("Number of turns:", num_turns)
        
        player.name=input("Unit 1 name: ")
        enemy.name=input("Unit 2 name: ")
    
        while enemy.is_alive(): # ==True
           
            player.unit_status()
            enemy.unit_status()

            dice = dice_roll() #10 side die
            result = player.attack(dice, enemy)
          
            num_turns -=1

            f= open("results.txt", "a+")
            f.write(f"attack result {result} \r\n")
            f.close()
        else:
            print(enemy.name, "Destroyed!")
        
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

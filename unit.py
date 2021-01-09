import random

#from random import randint

#def Unit class

class Unit:

    #add Class Decorators

    def __init__(self, name):
        self.name = name
        self.hits_remaining = 2 # track number of hits, set it to the number of hits that each unit type can survive
        self.attack_rating = random.randint(1,5)
    
    def hit(self, hit_val=1): # just subtract 1 from self.hits_remaining each time it’s called
        self.hits_remaining -= hit_val

    def is_alive(self): #return true or false
        ''' Check if unit is alive, return bool '''
        return self.hits_remaining > 0
    
    def unit_status(self):
        ''' print unit name, rating, hits '''
        print(self.name, " rating: ", self.attack_rating, " Hits remaining: ", self.hits_remaining)
    
    def retreat(self): #make unit move back 
        pass

    def attack(self, roll, target_unit):
        ''' check results of a dice roll, -1 Destroy, 0 = retreat, 1 = hit, 2 = hit and retreat '''

        DESTROYED = -1
        RETREAT = 0
        HIT = 1
        HIT_RETREAT = 2
        MISS = None

        attack_result = None # init result as empty/null
        # -1 Destroy, 0 = retreat, 1 = hit, 2 = hit and retreat
    
        if roll == self.attack_rating: #roll == attack
            print(f"{target_unit.name} must take hit or retreat.")
            num = random.randint(1,10) #rand to decide hit or retreat, even to retreat, odd to hit
            if (num % 2) == 0:
                attack_result = RETREAT #retreat
                target_unit.retreat()
            else:
                attack_result = HIT # hit
                target_unit.hit()
                
        if roll < self.attack_rating and self.attack_rating > 1:
            attack_result = HIT_RETREAT #hit and retreat
            target_unit.hit()
            target_unit.retreat()

        if roll == 1 and self.attack_rating >= target_unit.attack_rating: #destroy
            attack_result = DESTROYED #target_unit.hits_remaining = 0

        if attack_result is None: #attack has no effect
            
            print("Shot miss!")
        else:
            print(f"Attack result: {attack_result}")

        if attack_result == 1 or 2: #"Hit!" or "Hit and retreat!":
            target_unit.hit()
            print(target_unit.name, f"has been HIT! {target_unit.name} Hit count: {target_unit.hits_remaining} ")

        if target_unit.is_alive == False: #e.status = -1
            print(f"{target_unit.name} Destroyed!")
        

        return attack_result
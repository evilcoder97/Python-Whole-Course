# Python [Class]

# Declare a Class

class myclass:
    x= 5

# Declare a object
# Let the object be Pradyot the Great

pradyot1 = myclass()

print(pradyot1.x)

# Init Function


class Enemy:
    def __init__(self, attack, defense, weakness):
        self.attack = attack
        self.defense = defense
        self.weakness = weakness

    def displaystats(self):
        return self.attack, self.defense, self.weakness


Dinosaur = Enemy('50', '20', 'melee')

print(Dinosaur.displaystats())


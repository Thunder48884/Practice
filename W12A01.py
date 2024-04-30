'''
Make a class to reperesnt a video game character. 
They should have a name, class, how much health points they 
have, and there list of inventory.
Make a function to add items to their inventory. 
Make a function to remove items from their inventory. 
If an item cannot be found, do nothing. 
Lastly make a function to print out their stats 
(their name, class, HP, and their current inventory).
'''

class playerCharacter():
    def __init__(self, name, cls, mhp):
        self.name = name
        self.cls = cls
        self.maxHP = mhp
        self.HP = mhp
        self.inventory = []

    def pickUp(self, item):
        self.inventory.extend(item)
        for i in item:
            print(f'picked up {i}')
    
    def remove(self, item):
        try:
            self.inventory.remove(item)
            print(f'{item}, was removed.')
        except:
            print(f"{item} not found")

    def getStats(self):
        print(f"the {self.cls}, has {self.HP}/{self.maxHP}hp and has the items: ", end='')
        if(self.inventory):
            if (len(self.inventory)==1):
                print(f"{self.inventory[0]}", end='')
            else:
                for i in range(len(self.inventory)-1):
                    print(f"{self.inventory[i]}, ", end='')
                print(f"and {self.inventory[-1]}", end='')
        else:
            print("none",end='')
        print(".")



sean = playerCharacter('sean', 'barbarian', 97)

sean.getStats()
sean.remove("box")
sean.pickUp(["box"])
sean.getStats()
sean.remove("box")
sean.getStats()
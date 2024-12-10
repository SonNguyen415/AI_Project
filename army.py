"""
This file will contain logic for the army system. This includes movement  
"""

import map

MAX_ARMY_SUPPLY = 100000
ATTRITION_DEATHS = 100

class Army:
    def __init__(self, troops, position, supply):
        self.troops = troops
        self.position = position
        self.supply = supply

    #Supplies Methods

    def consume_supplies(self):
        """
        Reduces the number of supplies based on the number of troops
        """
        self.supply = max(0, self.supply - self.troops)

    def attrition(self):
        """
        Reduces the number of troops if there is no supplies
        """
        if self.supply == 0:
            self.troops = max(0, self.troops - ATTRITION_DEATHS)

    #Combat Methods

    def combat(self, damage):
        """
        Reduces the number of troops based on the inputted damage
        """
        self.troops = max(0, self.troops - damage)

    def routed(self):
        """
        Returns true if there exists no more troops in the army
        """
        if self.troops == 0:
            return True
        else:
            return False
        
    #Movement Methods

    def get_legal_moves(self, map: map.GameMap):
        """
        Return all the possible legal moves the army can go from this position
        """
        
        move_list = list()

        for x in range(-1, 1):
            for y in range(-1, 1):
                new_position = self.position[0] + y, self.position[1] + x
                if (x < 0 or y < 0 or x >= map.width or y >= map.height):
                    continue
                if (map.map[new_position[0]][new_position[1]]):
                    move_list.append(new_position)
        
        return move_list
    
    def generate_successor(self, new_position):
        """
        Generate successor given action
        """

        return Army(self.troops, new_position, self.supply)

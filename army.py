"""
This file will contain logic for the army system. This includes movement  
"""

import game
import map
import locations

MAX_ARMY_SUPPLY = 100000

class Army:
    def __init__(self, troops, position, supply):
        self.troops = troops
        self.position = position
        self.supply = supply

    #Supplies Methods

    def attrition(self):
        """
        Reduces the number of supplies based on the number of troops
        """
        self.supply = max(0, self.supply - self.troops)

        if self.supply == 0:
            self.troops = 0

    
    def consume_cache(self, cache_size):
        """
        Consume the cache. For now we will consume the cache in its entirely, the remaining will be wasted
        """
        self.supply = min(MAX_ARMY_SUPPLY, self.supply + cache_size) 

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
        return self.troops == 0
        
    #Movement Methods

    def get_army_legal_moves(self, map: map.GameMap):
        """
        Returns all the possible legal moves the army can go from this position
        :Returns a list of tuples y, x
        """

        y, x = self.position
        
        directions = {
            (y, x - 1),
            (y, x + 1),
            (y - 1, x),
            (y + 1, x),
        }

        legal_moves = list()

        for direction, (nx, ny) in directions.items():
            #make sure position in bounds
            if (nx < 0 or nx >= map.width) or (ny < 0 or ny >= map.height):
                continue

            #get candidate position
            new_position = map.map[nx][ny]

            #check to see if location is passible and no army is already at the position
            if new_position.location_type != locations.LocationType.IMPASSABLE:
                legal_moves.append(direction)

        return legal_moves
        
    
    def generate_army_successor(self, map: map.GameMap, new_position: tuple):
        """
        Returns the successor state of army based on action
        :Returns Army class
        """
        new_supply = max(0, self.supply - 50*(map.get_path_cost(self.position, new_position)))

        new_troops = self.troops
        if new_supply == 0:
            new_troops = 0

        return Army(new_troops, new_position, new_supply)


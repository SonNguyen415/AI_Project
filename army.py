"""
This file will contain logic for the army system. This includes movement  
"""

import game
import map
import locations

MAX_ARMY_SUPPLY = 100000

class Army:
    def __init__(self, troops, position):
        self.troops = troops
        self.position = position
        
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
            # In-Bounds Legality Check
            if (nx < 0 or nx >= map.width) or (ny < 0 or ny >= map.height):
                continue

            # Get Map Location
            new_position = map.map[nx][ny]

            # Passability Check
            if new_position.location_type != locations.LocationType.IMPASSABLE:
                legal_moves.append(direction)

        return legal_moves
        
    
    def generate_army_successor(self, map: map.GameMap, new_position: tuple):
        """
        Returns the successor state of army based on action
        :Returns Army class
        """

        # Attrition
        new_troops = max(0, self.supply - 50*(map.get_path_cost(self.position, new_position)))

        if new_troops == 0:
            return None

        return Army(new_troops, new_position)
    


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

    # Combat Methods
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
        
    # Movement Methods
    def get_legal_moves(self, map: map.GameMap):
        """
        Returns all legal moves for the army from its current position.
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
    
    
    
    # This is in the wrong place and should be at states
    def generate_successor(self, new_position):
        x, y = self.position
        directions = {
            Directions.UP: (x, y - 1),
            Directions.DOWN: (x, y + 1),
            Directions.LEFT: (x - 1, y),
            Directions.RIGHT: (x + 1, y)
        }

        legal_moves = []
        for direction, (nx, ny) in directions.items():
            #make sure position in bounds
            if (nx < 0 or nx > self.state.width) or (ny < 0 or ny > self.state.height)
                continue

            #get candidate position
            location = self.state.get_location(nx, ny)

            #check to see if location is passible and no army is already at the position
            if location.LocationType != LocationType.IMPASSABLE and location.army == 0:
                legal_moves.append(direction)

        return legal_moves


    def move(self):
        """
        Generate successor given action
        """
        return Army(self.troops, new_position, self.supply)

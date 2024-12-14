"""
This file will contain logic for the army system. This includes movement  
"""
import game_map
import locations

class Army:
    def __init__(self, agent, troops, position):
        self.agent = agent
        self.troops = troops
        self.position = position
        
    #Movement Methods

    def get_army_legal_moves(self, game_map: game_map.GameMap):
        """
        Returns all the possible legal moves the army can go from this position
        :Returns a list of tuples y, x
        """

        y, x = self.position
        
        directions = [(y, x - 1), 
                      (y, x + 1),
                      (y - 1, x),
                      (y + 1, x),]

        legal_moves = list()

        for (ny, nx) in directions:
            # In-Bounds Legality Check
            if (nx < 0 or nx >= game_map.width) or (ny < 0 or ny >= game_map.height):
                continue

            # Get Map Location
            new_position = game_map.map[ny][nx]

            # Passability Check
            if new_position.location_type != locations.LocationType.IMPASSABLE:
                legal_moves.append((ny, nx))

        return legal_moves
        
    
    def generate_army_successor(self, game_map: game_map.GameMap, new_position: tuple):
        """
        Returns the successor state of army based on action
        :Returns Army class
        """
        # Attrition
        new_troops = max(0, self.troops - game_map.get_path_cost(self.position, new_position))

        if new_troops == 0:
            return None

        return Army(self.agent, new_troops, new_position)
    


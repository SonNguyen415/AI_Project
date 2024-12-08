"""
This file will contain logic for the army system. This includes movement  
"""

class Army:
     def __init__(self, size, position, state):
        self.size = size
        self.position = position  # (x, y) tuple
        self.state = state        # Reference to the game state/grid
        self.owner = 0
        self.power = 0

    def get_legal_moves(self):
        """
        Returns all legal moves for the army from its current position.
        """
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
        Move the army
        """
        raise NotImplementedError

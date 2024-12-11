"""
This file will contain the main logic for the game flow
"""
import map , manager



class Directions:
    NORTH = 'North'
    SOUTH = 'South'
    EAST = 'East'
    WEST = 'West'
    STOP = 'Stop'

    LEFT =       {NORTH: WEST,
                SOUTH: EAST,
                EAST:  NORTH,
                WEST:  SOUTH,
                STOP:  STOP}

    RIGHT =      dict([(y,x) for x, y in LEFT.items()])

    REVERSE = {NORTH: SOUTH,
            SOUTH: NORTH,
            EAST: WEST,
            WEST: EAST,
            STOP: STOP}


        
class Game:
    def __init__(self, width, height) -> None:
        self.game_map = map.GameMap(width, height)
        self.width = width
        self.height = height
        # supplies: by default, and odd amount of supplies (approx width) are scattered randomly on the map. may break on map size 1, fix later.
        if self.width % 2 == 0:
            self.n_supply = width+1
        else:
            self.n_supply = width
        self.game_map.generate_map_info(self.n_supply)

        # Initialize agents and train them

        # Initialize armies for agents
        self.manager = manager.Manager(self.game_map, [], [])

    def play(self):
        print("Game started")
        self.game_map.display_map()

        while not self.manager.is_goal():
            # Agent A: Pop from list of state, action pair

            # Agent B: Pop from list of state, action pair

            # Calculate combat if there's collision
            self.manager.combat()

            # Calculate resupply via cache. Delete cache on consumption
            self.manager.resupply()
        
        print("Game ended")
    
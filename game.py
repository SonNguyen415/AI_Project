"""
This file will contain the main logic for the game flow
"""
import map 
import supply as sp


        
class Game:
    def __init__(self, width, height, n_hubs, n_generators) -> None:
        self.game_map = map.GameMap(width, height)
        self.width = width
        self.height = height
        self.hub_graph = sp.SupplyTracker()
        self.game_map.generate_map_info(n_hubs, n_generators, self.hub_graph)
    
    def play(self):
        print("Game started")
        self.game_map.display_map()
        self.hub_graph.visualize_graph()
        print("Game ended")
    
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

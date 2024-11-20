"""
This file will contain the main logic for the game flow
"""
import map 
import supply as sp


        
class Game:
    def __init__(self, width, height, n_hubs, n_generators) -> None:
        self.game_map = map.GameMap(width, height)
        self.hub_graph = sp.SupplyTracker()
        self.game_map.generate_map_info(n_hubs, n_generators, self.hub_graph)
    
    def play(self):
        print("Game started")
        self.game_map.display_map()
        self.hub_graph.visualize_graph()
        print("Game ended")
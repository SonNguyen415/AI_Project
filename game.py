"""
This file will contain the main logic for the game flow
"""
import map


        
class Game:
    def __init__(self, width, height, n_hubs, n_generators) -> None:
        self.game_map = map.GameMap(width, height, n_hubs, n_generators)
    

    def play(self):
        print("Game started")
        self.game_map.display_map()
        print("Game ended")
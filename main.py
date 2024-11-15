from game import Game


scenario = {
    "width": 100,
    "height": 100,
    "n_hubs": 9, # Must be a perfect square for now
    "n_generators": 1
}

if __name__ == '__main__':
    game = Game(scenario["width"], scenario["height"], scenario["n_hubs"], scenario["n_generators"])
    game.play()
from game import Game


scenario = {
    "width": 10,
    "height": 9,
}

if __name__ == '__main__':
    game = Game(scenario["width"], scenario["height"])
    game.play()
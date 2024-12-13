from game import Game

scenario = {
    "width": 10,
    "height": 10,
    "iterations": 1000,
    "start_army_sz": 20000
}

if __name__ == '__main__':
    game = Game(scenario["width"], scenario["height"], scenario["iterations"], scenario["start_army_sz"])
    game.play()
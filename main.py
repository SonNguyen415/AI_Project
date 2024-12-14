from game import Game

TRIALS = 10
#set verbose to true to print map
VERBOSE = False
#third scenario. Takes a very long time, even with threading. Set to true at your own discretion
THIRD = False
scenario = {
    "width": 10,
    "height": 10,
    "iterations": 10,
    "start_army": [1000, 3000],
    
}
scenario2 = {
    "width": 10,
    "height": 10,
    "iterations": 100,
    "start_army": [1000, 3000],
}
scenario3 = {
    "width": 10,
    "height": 10,
    "iterations": 1000,
    "start_army": [1000, 3000],
}



def win_count(results: list):
    """
    Count the number of wins per team
    """
    win_counts = {}
    for (winner, troops_left) in results:
        if winner not in win_counts:
            win_counts[winner] = 0
        win_counts[winner] += 1
    return win_counts


if __name__ == '__main__':
    results1 = []
    print("First scenario: Agent 1 and Agent 0 both use MCTS with 20 iterations across 10 trials -- effectively random movement")
    for i in range(TRIALS):
        game = Game(scenario["width"], scenario["height"], scenario["iterations"], scenario["start_army"],VERBOSE)
        results1.append(game.play())

    print(results1)
    print("Scenario 1 Win counts:", win_count(results1))    


    results2 = []
    print("Second scenario: Agent 0 uses 200 iterations while Agent 1 only does 20. 10 Trials")
    for i in range(TRIALS):
        game = Game(scenario2["width"], scenario2["height"], scenario2["iterations"], scenario2["start_army"],VERBOSE)
        results2.append(game.play())
    print("Scenario 2 Win counts:", win_count(results2))
    if THIRD:
        results3 = []
        print("Second scenario: Agent 0 uses 200 iterations while Agent 1 only does 20. 10 Trials")
        for i in range(TRIALS):
            game = Game(scenario3["width"], scenario3["height"], scenario3["iterations"], scenario3["start_army"],VERBOSE)
            results3.append(game.play())
        print("Scenario 3 Win counts:", win_count(results3))

    print("Final Results")
    print("Scenario 1 Win counts:", win_count(results1))    
    print("Scenario 2 Win counts:", win_count(results2))
    if THIRD:
        print("Scenario 3 Win counts:", win_count(results3))
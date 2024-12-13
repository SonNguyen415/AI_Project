from game import Game

scenario = {
    "width": 10,
    "height": 10,
    "iterations": 20,
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

if __name__ == '__main__':
    results = []
    print("first scenario: Agent 1 and Agent 0 both use MCTS with 20 iterations ten times -- effectively random movement")
    for i in range(10):
        game = Game(scenario["width"], scenario["height"], scenario["iterations"], scenario["start_army"])
        results.append(game.play())
    # Count the number of wins per team
    win_counts1 = {}
    for (winner, troops_left) in results:
        if winner not in win_counts1:
            win_counts1[winner] = 0
        win_counts1[winner] += 1



    results = []
    print("second scenario: Agent 0 uses 100 iterations while Agent 1 only does 20. Runs ten times")
    for i in range(10):
        game = Game(scenario2["width"], scenario2["height"], scenario2["iterations"], scenario2["start_army"])
        results.append(game.play())
    # Count the number of wins per team
    win_counts2 = {}
    for (winner, troops_left) in results:
        if winner not in win_counts2:
            win_counts2[winner] = 0
        win_counts2[winner] += 1



    # results = []
    # print("third scenario: Agent 0 uses 1000 iterations while Agent 1 only does 20. Runs ten times")
    # for i in range(10):
    #     game = Game(scenario3["width"], scenario3["height"], scenario3["iterations"], scenario3["start_army"])
    #     results.append(game.play())
    # # Count the number of wins per team
    # win_counts3 = {}
    # for (winner, troops_left) in results:
    #     if winner not in win_counts3:
    #         win_counts3[winner] = 0
    #     win_counts3[winner] += 1

    print("Scenario 1: Agent 1 and Agent 0 both use MCTS with 20 iterations ten times -- effectively random movement.")
    print("we expect agent 1 to win most if not all of the time as has the advantage of going second")
    print("Scenario 1 Win counts:", win_counts1)

    print("Scenario 2: Agent 0 uses 100 iterations while Agent 1 only does 20. Runs ten times")
    print("Scenario 2: Win counts:", win_counts2)

    #third scenario is incredibly slow. but it's important to see how agent zero improves. u

    # print("third scenario: Agent 0 uses 1000 iterations while Agent 1 only does 20. Runs ten times")
    # print("Scenario 3 Win counts:", win_counts3)
    
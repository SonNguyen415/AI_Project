from concurrent.futures import ThreadPoolExecutor, as_completed
from game import Game

TRIALS = 25
# Set verbose to true to print map
VERBOSE = False
# Set to true to run tests. This will run the game with different scenarios and print the win counts. Otherwise we will run a single game
TEST = True
# Third scenario. Takes a very long time, even with threading. Set to true at your own discretion
THIRD = False

default_scenario = {
    "width": 10,
    "height": 10,
    "iterations": 1,
    "start_army": [1000, 3000],
}

scenario1 = {
    "width": 10,
    "height": 10,
    "iterations": 1,
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
            win_counts[winner] = (1, troops_left)
        else:
            win_counts[winner] = (win_counts[winner][0] + 1, win_counts[winner][1] + troops_left)
        
    # Average troops left
    for key, value in win_counts.items():
        win_counts[key] = (value[0], value[1] / value[0])
       
    return win_counts

def print_win_counts(win_counts: list):
    """
    Print the win counts
    """
    total_wins = 0
    for key, value in win_counts.items():
        print(f"Agent {key} won {value[0]} times with an average of {value[1]} troops left")
        total_wins += value[0]
    print(f"Total Draws: {TRIALS-total_wins}")
    

def run_scenario(scenario, num_trials, verbose):
    """Run a series of game trials concurrently and return the results."""
    results = []
    for i in range(num_trials):
        print("-------------------------------------------------------------------------------------")
        print("\tTrial", i+1)
        game = Game(scenario["width"], scenario["height"], scenario["iterations"], scenario["start_army"], verbose)
        game_result = game.play()
        if game_result != None:
            results.append(game_result)
    print("-------------------------------------------------------------------------------------")
    return results


if __name__ == '__main__':
    if not TEST:
        print(f"Default scenario: Agent 1 and Agent 0 both use MCTS. Agent 0 with {default_scenario['iterations']} iterations. Agent 1 with 1 iteration")
        result = run_scenario(default_scenario, 1, VERBOSE)
        print(f"Winner: {result[0][0]}. With {result[0][1]} troops left")
    else:
        results = list()
        print(f"First scenario: Agent 1 and Agent 0 both use MCTS with {scenario1['iterations']} iterations across {TRIALS} trials -- effectively random movement")
        results1 = run_scenario(scenario1, TRIALS, VERBOSE)
        results.append(results1)
        print_win_counts(win_count(results1))

        print(f"Second scenario: Agent 0 with {scenario2['iterations']} iterations across {TRIALS} trials. Agent 1 remains at 1 iteration")
        results2 = run_scenario(scenario2, TRIALS, VERBOSE)
        results.append(results2)
        print_win_counts(win_count(results2))

        if THIRD:
            print(f"Third scenario: Agent 0 with {scenario3['iterations']} iterations across {TRIALS} trials. Agent 1 remains at 1 iteration")
            results3 = run_scenario(scenario3, TRIALS, VERBOSE)
            results.append(results3)
            print_win_counts(win_count(results3))

        print("\nFinal Results:")
        for i in range(len(results)):
            print(f"Scenario {i+1}: ", end="")
            print_win_counts(win_count(results[i]))
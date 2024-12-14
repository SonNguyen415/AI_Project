from concurrent.futures import ThreadPoolExecutor, as_completed
from game import Game

TRIALS = 10
# Set verbose to true to print map
VERBOSE = False
# Third scenario. Takes a very long time, even with threading. Set to true at your own discretion
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


def run_scenario(scenario, num_trials, verbose):
    """Run a series of game trials concurrently and return the results."""
    results = []
    with ThreadPoolExecutor() as executor:
        # Submit tasks to the executor
        futures = [executor.submit(Game(scenario["width"], scenario["height"], scenario["iterations"], scenario["start_army"], verbose).play) for _ in range(num_trials)]
        
        # Collect results as they complete
        for future in as_completed(futures):
            results.append(future.result())
    return results


if __name__ == '__main__':
    print("First scenario: Agent 1 and Agent 0 both use MCTS with 10 iterations across 10 trials -- effectively random movement")
    results1 = run_scenario(scenario, TRIALS, VERBOSE)
    print("Scenario 1 Win counts:", win_count(results1))

    print("\nSecond scenario: Agent 0 uses 100 iterations while Agent 1 only does 10. 10 Trials")
    results2 = run_scenario(scenario2, TRIALS, VERBOSE)
    print("Scenario 2 Win counts:", win_count(results2))

    if THIRD:
        print("\nThird scenario: Agent 0 uses 1000 iterations while Agent 1 only does 10. 10 Trials")
        results3 = run_scenario(scenario3, TRIALS, VERBOSE)
        print("Scenario 3 Win counts:", win_count(results3))

    print("\nFinal Results")
    print("Scenario 1 Win counts:", win_count(results1))
    print("Scenario 2 Win counts:", win_count(results2))
    if THIRD:
        print("Scenario 3 Win counts:", win_count(results3))
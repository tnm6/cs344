from search import Problem

class TSP(Problem):
    """
    State: sequence of visited cities
    Actions: swap two cities in sequence of index i and j
    Result: new sequence of sequences after action
    Value: distance between two cities i and j
    """

    def __init__(self, initial, distances):
        self.initial = initial
        self.distances = distances

    def actions(self, state):
        """From a given state, return possible actions (swaps).
        Actions include swapping any cities in the sequence between the
        first and the last.
        """
        actions = []

        for i in range(1, len(state)-1):
            for j in range(1, len(state)-1):
                if i != j:
                    actions.append((i, j))

        return actions
    
    def result(self, state, action):
        """With given action, swap the cities and return resulting state"""
        new_state = state[:]

        # Gather cities from state at indeces given by action
        swap1 = state[action[0]]
        swap2 = state[action[1]]
        # Swap those in new_state
        new_state[action[0]] = swap2
        new_state[action[1]] = swap1

        return new_state

    def value(self, state):
        """Computes and returns total distance travelled
        as negative value, to function properly with algorithms"""
        value = 0
        for i in range(len(state)-1):
            city1 = state[i]
            city2 = state[i+1]
            # Frozenset to evaluate distance regardless of order
            value -= self.distances[frozenset((city1, city2))]

        return value

from search import hill_climbing, simulated_annealing, exp_schedule
from random import randrange, shuffle
import time

if __name__ == '__main__':
    cities = 10
    max_distance = 20

    # Generate initial sequence of cities
    initial = []
    for city in range(1, cities):
        initial.append(city)
    shuffle(initial)
    # Make the initial state a loop by adding first city to last
    initial.append(initial[0])

    # Generate random distances between each city
    distances = {}

    for city1 in initial:
        for city2 in initial:
            if city1 != city2:  # frozensets to ensure no duplicates
                distances[frozenset((city1, city2))] = randrange(1, max_distance)

    problem = TSP(initial, distances)

    time1 = time.time()
    hill_solution = hill_climbing(problem)
    time2 = time.time()
    print('Hill-climbing solution       x: ' + str(hill_solution)
        + '\tvalue: ' + str(-problem.value(hill_solution))
        + "\t\ttime: %0.3f seconds" % (time2 - time1)
        )

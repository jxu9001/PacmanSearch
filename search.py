# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # states returned by getStartState() and expected by isGoalState() and getSuccessors() are (x, y) position tuples
    # states returned by getSuccessors are a list of (position, action, step cost) tuples

    # initializing data structures
    data_structure = util.Stack()
    path_to_goal = []  # list of strings where the strings are "North", "South", "East", and "West"
    expanded_states = set()  # set of expanded states (x, y)

    # add the start state to the stack
    start_state = (problem.getStartState(), path_to_goal)
    data_structure.push(start_state)

    # using the generic search algorithm in the lecture slides
    while not data_structure.isEmpty():
        # pop the queue
        curr_state, path_to_goal = data_structure.pop()

        # goal test
        if problem.isGoalState(curr_state):
            return path_to_goal

        # check if the current state has been expanded as this is a graph algorithm
        if curr_state not in expanded_states:
            # add current state to the expanded states set
            expanded_states.add(curr_state)
            # add previously unexpanded successor states to the stack
            for state, action, _ in problem.getSuccessors(curr_state):
                if state not in expanded_states:
                    successor_state = (state, path_to_goal + [action])
                    data_structure.push(successor_state)

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # states returned by getStartState() and expected by isGoalState() and getSuccessors() are (x, y) position tuples
    # states returned by getSuccessors are a list of (position, action, step cost) tuples

    # initializing data structures
    data_structure = util.Queue()
    path_to_goal = []  # list of strings where the strings are "North", "South", "East", and "West"
    expanded_states = set()  # set of expanded states (x, y)

    # add the start state to the queue
    start_state = (problem.getStartState(), path_to_goal)
    data_structure.push(start_state)

    # using the generic search algorithm in the lecture slides
    while not data_structure.isEmpty():
        # pop the queue
        curr_state, path_to_goal = data_structure.pop()

        # goal test
        if problem.isGoalState(curr_state):
            return path_to_goal

        # check if the current state has been expanded as this is a graph algorithm
        if curr_state not in expanded_states:
            # add current state to the expanded states list
            expanded_states.add(curr_state)
            # add previously unexpanded successor states to the queue
            for state, action, _ in problem.getSuccessors(curr_state):
                if state not in expanded_states:
                    successor_state = (state, path_to_goal + [action])
                    data_structure.push(successor_state)

    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # states returned by getStartState() and expected by isGoalState() and getSuccessors() are (x, y) position tuples
    # states returned by getSuccessors are a list of (position, action, step cost) tuples

    # initializing data structures
    data_structure = util.PriorityQueue()
    path_to_goal = []  # list of strings where the strings are "North", "South", "East", and "West"
    expanded_states = set()  # set of expanded states (x, y)

    # add the start state to the priority queue
    start_state = (problem.getStartState(), path_to_goal, 0)
    data_structure.push(start_state, 0)

    # using the generic search algorithm in the lecture slides
    while not data_structure.isEmpty():
        # pop the priority queue
        curr_state, path_to_goal, curr_cost = data_structure.pop()

        # goal test
        if problem.isGoalState(curr_state):
            return path_to_goal

        # check if the current state has been expanded as this is a graph algorithm
        if curr_state not in expanded_states:
            # add current state to the expanded states list
            expanded_states.add(curr_state)
            # add previously unexpanded successor states to the priority queue
            for state, action, step_cost in problem.getSuccessors(curr_state):
                if state not in expanded_states:
                    total_cost = curr_cost + step_cost
                    successor_state = (state, path_to_goal + [action], total_cost)
                    data_structure.push(successor_state, total_cost)

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # states returned by getStartState() and expected by isGoalState() and getSuccessors() are (x, y) position tuples
    # states returned by getSuccessors are a list of (position, action, step cost) tuples

    # initializing data structures
    data_structure = util.PriorityQueue()
    path_to_goal = []  # list of strings where the strings are "North", "South", "East", and "West"
    expanded_states = set()  # set of expanded states (x, y)

    # add the start state to the priority queue
    start_state = (problem.getStartState(), path_to_goal, 0)
    data_structure.push(start_state, 0)

    # using the generic search algorithm in the lecture slides
    while not data_structure.isEmpty():
        # pop the priority queue
        curr_state, path_to_goal, curr_cost = data_structure.pop()

        # goal test
        if problem.isGoalState(curr_state):
            return path_to_goal

        # check if the current state has been expanded as this is a graph algorithm
        if curr_state not in expanded_states:
            # add current state to the expanded states list
            expanded_states.add(curr_state)
            # add previously unexpanded successor states to the priority queue
            for state, action, step_cost in problem.getSuccessors(curr_state):
                if state not in expanded_states:
                    cost = curr_cost + step_cost
                    total_cost = cost + heuristic(state, problem)
                    successor_state = (state, path_to_goal + [action], cost)
                    data_structure.push(successor_state, total_cost)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

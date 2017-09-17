# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  #util.raiseNotDefined()
  def is_goal(x):
        return problem.isGoalState(x)
        
  init_state = problem.getStartState()

  stack = util.Stack()
  stack.push((init_state, []))
  visited = set()

  while not stack.isEmpty():
      (node, path) = stack.pop()
      if is_goal(node): # <-- move to here
          return path
      visited.add(node)
      successors = problem.getSuccessors(node)
      for state, action, cost in successors:
          if state not in visited:
                #if is_goal(state): # <-- remove this
                #    return path + [action] # <-- remove this
            stack.push((state, path + [action]))

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  #util.raiseNotDefined()
  def is_goal(x):
        return problem.isGoalState(x)
        
  init_state = problem.getStartState()

  frontier = util.Queue()
  frontier.push((init_state, []))
  visited = set()
  visited.add(init_state)
  while not frontier.isEmpty():
      (node, path) = frontier.pop()
      
      if is_goal(node): # <-- move to here
          return path
      
      
      successors = problem.getSuccessors(node)
      for state, action, cost in successors:
          
          if state not in visited:
                #if is_goal(state): # <-- remove this
                #    return path + [action] # <-- remove this
              #different from the lecture: "There is one slight tweak on the general graph-search algorithm, 
            #which is that the goal test is applied to each node 
            #when it is generated rather than when it is selected for expansion." 
            frontier.push((state, path + [action]))
          visited.add(state) 
      
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    "we use PriorityQueue data structure, 'smart queue' "
    "struture and help us to find the lower cost of action"
    "use PriorityQueue to detect which route is shortest, and pop the shortest route"
   
    nodePriorityQueue = util.PriorityQueue()
    visited = []
    path = []
    totalCost = 0
    startNode =(problem.getStartState(),path)
    nodePriorityQueue.push((startNode),totalCost)
    
    "start while loop to find the correct path"
    
    while  nodePriorityQueue.isEmpty() is False:
        node,path = nodePriorityQueue.pop()
        
        visited.append(node)
        
        if problem.isGoalState(node):
            return path
        
        for successor, direction, cost in problem.getSuccessors(node) :
            if successor not in visited:
                visited.append(successor)
                newNode =(successor,path + [direction])
                nodePriorityQueue.push(newNode,problem.getCostOfActions(path + [direction]))
            if problem.isGoalState(successor):
                newNode =(successor,path + [direction])
                nodePriorityQueue.push(newNode,problem.getCostOfActions(path + [direction]))

    return None

    
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
    "it is very similar to UCS, just change the totalcost to the heuristic + cost  "
    nodePriorityQueue = util.PriorityQueue()
    visited = []
    path = []
    totalCost = heuristic(problem.getStartState(),problem)
    startNode =(problem.getStartState(),path)
    nodePriorityQueue.push((startNode),totalCost)
    
    "start while loop to find the correct path"
    
    while  nodePriorityQueue.isEmpty() is False:
        node,path = nodePriorityQueue.pop()
        
        visited.append(node)
        
        if problem.isGoalState(node):
            return path
        for successor, direction, cost in problem.getSuccessors(node) :
            if successor not in visited:
                visited.append(successor)
                newNode =(successor,path+[direction])
                totalCost = problem.getCostOfActions(path + [direction]) + heuristic(successor,problem)
                nodePriorityQueue.push(newNode,totalCost)
            if problem.isGoalState(successor):
                newNode =(successor,path + [direction])
                totalCost = problem.getCostOfActions(path + [direction]) + heuristic(successor,problem)
                nodePriorityQueue.push(newNode,totalCost)


    return None

    
    util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

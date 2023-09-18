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
    return  [s, s, w, s, w, w, s, w]

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
    #utilizamos una pila para implementar la frontera o fringe
    frontera = util.Stack()
    #creamos una lista para ir poniendo los nodos visitados
    visitados = []
    # creamos  una lista para ir almacenando las acciones posibles
    listaAcciones = []
    # metemos a la pila el estado inicial y la lista de acciones vacias 
    frontera.push((problem.getStartState(), listaAcciones))
    
    #mientras haya algun elemento en la frontera
    while frontera:
        """sacamos las coordenadas del nodo que este mas arriba del stack y lista que contiene las acciones 
   |       para llegar a el  """
        nodo, acciones = frontera.pop() 
        if not nodo in visitados:    
            visitados.append(nodo)          #si el nodo no habia sido visitado entonces lo metemos a la lista de visitados
            if problem.isGoalState(nodo): 
                return acciones             #si el nodo es el  nodo objetivo entonces devolvemos su lista de acciones
            
            for siguiente in problem.getSuccessors(nodo):       #obtenemos los sucesores del nodo actual
                coordenada, direccion, costo = siguiente        #de cada sucesor almacenamos su coordenada, direccion y costo
                siguientesAcciones = acciones + [direccion]     #creamos una nueva variable que actualice la lista de acciones 
                                                                #con la  última direccion del nodo sucesor 
                frontera.push((coordenada, siguientesAcciones)) #metemos a la frontera la coordenada y lista de acciones del sucesor
    
    return [] #si no  se encuentra  el nodo objetivo entonces solo se devueve una lista vacia de acciones


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #Usamos una cola , para que la búsqueda explore todos los nodos que estén en un mismo nivel antes de avanzar al 
    #siguiente nivel
    frontera = util.Queue()
    
    visitados = []
    
    listaAcciones = []
    
    frontera.push((problem.getStartState(), listaAcciones))
    while frontera:
        nodo, acciones = frontera.pop()
        if not nodo in visitados:
            visitados.append(nodo)
            if problem.isGoalState(nodo):
                return acciones
            for siguiente in problem.getSuccessors(nodo):
                coordenada, direccion, costo = siguiente
                siguientesAcciones = acciones + [direccion]
                frontera.push((coordenada, siguientesAcciones))
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    frontera = util.PriorityQueue()

    visitados = []
    listaAcciones = []
    frontera .push((problem.getStartState(), listaAcciones), problem)
    while frontera:
        nodo, acciones = frontera.pop()
        if not nodo in visitados:
            visitados.append(nodo)
            if problem.isGoalState(nodo):
                return acciones
            for siguiente in problem.getSuccessors(nodo):
                coordenada, direccion, costo = siguiente
                siguientesAcciones = acciones + [direccion]
                siguienteCosto = problem.getCostOfActions(siguientesAcciones)
                #print(siguienteCosto)
                frontera.push((coordenada, siguientesAcciones), siguienteCosto)
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
     # Utilizamos la cola de prioridad dada
    franja = util.PriorityQueue()
    # Creamos un lista donde se almacenaran los nodos ya visitados
    visitados = []
    # Lista para las Acciones
    listaAcciones = []
    # Iniciamilamos la franja en su estado inicial con la lista de acciones y con las heurisitcas
    franja.push((problem.getStartState(), listaAcciones), heuristic(problem.getStartState(), problem))
    while franja:
        nodo, acciones = franja.pop()
        if not nodo in visitados:  # Si el nodo actual no se encuentra la lista visitada lo añadimso a la lista
            visitados.append(nodo)
            if problem.isGoalState(nodo): # Si el nodo actual es el nodo Meta retornamos las acciones
                return acciones
            for siguiente in problem.getSuccessors(nodo):
                cordenada, direccion, costo = siguiente
                siguientesAcciones = acciones + [direccion]  # Generamos la nueva lista  de acciones con la direccion actual
                siguienteCosto = problem.getCostOfActions(siguientesAcciones) + \
                               heuristic(cordenada, problem)  # Calculamos el nueov costo acumulado mas la H
                franja.push((cordenada, siguientesAcciones), siguienteCosto) # Agregamso el nuevo estado y las acciones
    return [] 

# Abbreviations
bfs = breadthFirstSearch 
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

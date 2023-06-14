""" Instancias de  clases """
class Node:
    """ Declaración función constructora """
    def __init__ (self, _state, _father, _action, _cost ) :
        self.state = _state
        self.father = _father
        self.action = _action
        self.cost = _cost


class Maze:
    def __init__(self, _path ):
        self.initialState = self.readMaze(_path)
        self.currentState = self.readMaze(_path)

    def readMaze(self, _path):
        with open(_path, "r") as file:
            maze = file.readlines()
            
            for i in range(len(maze)):
                maze[i] = maze[i].replace("\n", "")

            for line in maze:
                print(line)


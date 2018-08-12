from graphics import *

class World:




    def __init__(self, max_x, max_y):
        self.window = GraphWin('Świat', max_x, max_y)
        line = Line(Point(100,4),Point(100,200))
        line.draw(self.window)


        circle = Circle(Point(100, 200),20)
        circle.draw(self.window)

    def drawWorld(self):
        pass

    def makeTurn(self):
        pass






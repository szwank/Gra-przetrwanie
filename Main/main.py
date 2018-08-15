from graphics import *
import time
from world import World
from init_window import WindowInitializer


def main():
    init_window = WindowInitializer()
    width = init_window.ask_about_number('Podaj ilość pól szerokości gry:')
    height = init_window.ask_about_number('Podaj ilość pól wysokość gry:')
    del init_window

    print('szerokość: ' + width + ', wysokość: ' + height)

    # input_window.getMouse()
    # input_max_x.close()

    # window = World(1000,500)
    # while 1:
    #     window.window.update()
    # window.window.getMouse()
    # window.window.close()
    print('kot')


main()

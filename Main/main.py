from graphics import *
from organism import Organism

from world import World
from init_window import WindowInitializer


def main():
    init_window = WindowInitializer()
    width = init_window.ask_about_number('Podaj ilość pól szerokości gry:')
    height = init_window.ask_about_number('Podaj ilość pól wysokość gry:')
    init_window.close_window()

    print('szerokość: ' + width + ', wysokość: ' + height)

    world = World(int(width), int(height))
    world.display_board()

    organism = world.create_organism()
    organism.draw()



    world.wait_to_press_key('Return')
    # input_window.getMouse()
    # input_max_x.close()

    # window = World(1000,500)
    # while 1:
    #     window.window.update()
    # window.window.getMouse()
    # window.window.close()
    print('kot')


main()

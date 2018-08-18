from graphics import *
from organism import Organism
import time

from world import World
from init_window import WindowInitializer


def main():
    '''  #debugoawnie kodu
    init_window = WindowInitializer()
    width = init_window.ask_about_number('Podaj ilość pól szerokości gry:')
    height = init_window.ask_about_number('Podaj ilość pól wysokość gry:')
    init_window.close_window()

    print('szerokość: ' + width + ', wysokość: ' + height)

    world = World(int(width), int(height))
    '''
    world = World(10, 10)
    world.display_board()

    animal = world.create_animal()
    center_point = animal.draw()

    print('położenie środkowe obiektu x: ', center_point.getX(), ',y: ', center_point.getY())

    for i in range(100):
        animal.make_action()
        time.sleep(0.5)

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

from graphics import *
import time
from world import World
from init_window import InitWindow

def main():
    init_window = InitWindow()

    display_message_point = Point(init_window.get_wight() / 2, init_window.get_height() / 2)
    message = Text(display_message_point, 'Podaj ilość pól szerokości gry:')
    init_window.display_message(message)
    input_message = init_window.get_input_massage(Point(display_message_point.getX() + len(message.getText()) * 4.5,
                                                  display_message_point.getY()))
    init_window.hide_message(message)


    while str.isdigit(input_message) is False: #odpalenie pętli jeżeli string nie zawierał tylko cyfr

        message.setText('Wiadomość zawierała znaki nie będące cyframi! Wciśnij enter by kontynuować')
        init_window.wait_to_press_key('Return')

        init_window.display_message(message)
        input_message = init_window.get_input_massage(Point(display_message_point.getX() + len(message.getText()) * 4.5,
                                                            display_message_point.getY()))
        message.undraw()


    print(input)

    # input_window.getMouse()
    # input_max_x.close()

    # window = World(1000,500)
    # while 1:
    #     window.window.update()
    # window.window.getMouse()
    # window.window.close()
    print('kot')


main()






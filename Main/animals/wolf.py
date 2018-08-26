from animal import Animal


class Wolf(Animal):

    def __init__(self, world_handle):
        super(Animal, self).__init__(world_handle)

        self._strength = 9
        self._initiative = 5

        self._representation.setFill('red')  # kolor klasy wilk


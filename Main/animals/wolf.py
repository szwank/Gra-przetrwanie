from animal import Animal


class Wolf(Animal):



    def __init__(self, world_handle, board_height_in_fields, board_width_in_fields):
        super(Wolf, self).__init__(world_handle, board_height_in_fields, board_width_in_fields)
        self._strength = 9
        self._initiative = 5

    def get_initiative(self):
        return self._initiative

    def get_strength(self):
        return self._strength



from animals.wolf import Wolf


class OrganismCreator:


    def create_the_organism(self, organism_name, world_handle, position_x_in_fields, position_y_in_fields):
        """metoda towrzy organizm o podanym indentyfikatorze(organism_name)"""

        if organism_name is 'wolf':
            return Wolf(world_handle, position_x_in_fields, position_y_in_fields)


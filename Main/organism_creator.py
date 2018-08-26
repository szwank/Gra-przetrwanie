from animals.wolf import Wolf


class OrganismCreator:


    def create_the_organism(self, organism_name, world_handle):
        """metoda towrzy organizm o podanym indentyfikatorze(organism_name)"""

        if organism_name is 'wolf':
            return Wolf(world_handle)


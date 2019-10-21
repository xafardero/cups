import string
from CupsGenerator import CupsGenerator

class EnergyCupsGenerator(CupsGenerator):

    def _start_with(self) -> string:
        return '00'

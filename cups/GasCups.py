import string
from CupsGenerator import CupsGenerator

class GasCupsGenerator(CupsGenerator):

    def _start_with(self) -> string:
        return '02'

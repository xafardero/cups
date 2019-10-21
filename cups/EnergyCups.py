import string
from CupsGenerator import CupsGenerator

class EnergyCupsGenerator(CupsGenerator):

    def __init__(self):
        super().__init__()

    def _start_with(self) -> string:
        return '00'

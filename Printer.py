from Filament_types_loader import Filament_types_loader
from Firmware import Firmware

class Printer:

    def __init__(self, model, nozzle, firmware=None, filament_types = "filaments/printer_supported_filaments.csv"):
        self._model = model
        self.nozzle = nozzle
        self.firmware = firmware
        if(self.firmware == None):
            self.firmware = "nenalezena"
        self.filament_types = filament_types
        self.loader = Filament_types_loader(self.filament_types)

    def change_filament_types_file(self, new_path):
        self.filament_types = new_path

    def __str__(self):
        return(f"Tiskárna, model {self._model}, průměr trysky {self.nozzle} mm, verze firmware {self.firmware}. Podporované filamenty: {self.loader.filaments}")
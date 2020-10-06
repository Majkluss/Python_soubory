from Printer import Printer
from Filament_types_loader import Filament_types_loader

class Mini(Printer):

    def __init__(self, model, nozzle, connect, firmware=None, filament_types="filaments/mini_supported_filaments.csv"):
        super().__init__(model, nozzle, firmware)
        self.connect = connect
        self.filament_types = filament_types
        self.loader = Filament_types_loader(self.filament_types)

    def __str__(self):
        return(f"Tiskárna, model {self._model}, průměr trysky {self.nozzle} mm, připojena pomocí {self.connect}, verze firmware {self.firmware}. Podporované filamenty: {self.loader.filaments}")
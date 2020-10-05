class Printer:
    firmware = None
    if (firmware == None):
        firmware = "nenalezena"
    def __init__(self, model, nozzle):
        self._model = model
        self._nozzle = nozzle
        self.filament = ""
        self.supported_filaments = {
        "PLA":215,
        "ABS":220,
        "PP":254
    }

    def list_filaments(self):
        filament_list = []
        for i in self.supported_filaments:
            filament_list.append(i)
        self.filament = ", ".join(filament_list)

    def __str__(self):
        self.list_filaments()
        return(f"Tiskárna standard, model {self._model}, průměr trysky {self._nozzle}mm. Verze firmware {self.firmware}. Podporované filamenty: {self.filament}")
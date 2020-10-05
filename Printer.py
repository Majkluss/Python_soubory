class Printer:
    firmware = None
    if (firmware == None):
        firmware = "nenalezena"
    def __init__(self, model, nozzle):
        self._model = model
        self._nozzle = nozzle

        self.supported_filaments = {
        "PLA":215,
        "ABS":220,
        "PP":254
    }

    def __str__(self):
        filament = ", ".join(self.supported_filaments)
        return(f"Tiskárna standard, model {self._model}, průměr trysky {self._nozzle}mm. Verze firmware {self.firmware}. Podporované filamenty: {filament}")
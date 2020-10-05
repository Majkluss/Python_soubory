from Printer import Printer

class PrinterMini(Printer):
    def __init__(self, model, nozzle, connect):
        super().__init__(model, nozzle)
        self._connect = connect

        self.supported_filaments = {
            "PLA": 215,
            "ABS": 220
        }

    def __str__(self):
        filament = ", ".join(self.supported_filaments)
        return(f"Tiskárna mini, model {self._model}, průměr trysky {self._nozzle}mm. Připojena pomocí {self._connect}. Verze firmware {self.firmware}. Podporované filamenty: {filament}")
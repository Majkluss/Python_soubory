from Printer import Printer

class PrinterMini(Printer):
    def __init__(self, model, nozzle, connect):
        super().__init__(model, nozzle)
        self._connect = connect

    def __str__(self):
        return(f"Tiskárna mini, model {self._model}, průměr trysky {self._nozzle}mm. Připojena pomocí {self._connect}. Verze firmware {self.firmware}")
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

class PrinterMini(Printer):
    def __init__(self, model, nozzle, connect):
        super().__init__(model, nozzle)
        self._connect = connect

    def __str__(self):
        return(f"Tiskárna mini, model {self._model}, průměr trysky {self._nozzle}mm. Připojena pomocí {self._connect}. Verze firmware {self.firmware}")

class Firmware:
    def __init__(self,version):
        self._version = version

    def __str__(self):
        return(f"{self._version}")

    def upgrade(self, new_version):
        self._version = new_version


mk2 = Printer("MK2", 0.4)
mini = PrinterMini("MINI", 0.4, "Wi-Fi")
fw0_1 = Firmware(0.1)
fw0_2 = Firmware(0.2)

mk2.firmware = fw0_1
mini.firmware = fw0_2

print(mk2)
print(mini)



# print(mk2)
# print(mini)
# mini.firmware.upgrade(0.5)
# print(mini)
# mk2.firmware = fw0_2
# print(mk2)
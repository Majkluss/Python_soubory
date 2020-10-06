import csv

class Filament_types_loader:
    filaments = ""
    def __init__(self, path):
        try:
            with open(path, "r", encoding="utf-8") as csv_file:
                csv_reader = csv.reader(csv_file)

                for line in csv_reader:
                    self.filaments += line[0] + ', '
                self.filaments = self.filaments[:-2]
        except:
            print("Při načítání souboru došlo k chybě")

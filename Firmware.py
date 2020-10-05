class Firmware:
    def __init__(self,version):
        self._version = version

    def __str__(self):
        return(f"{self._version}")

    def upgrade(self, new_version):
        self._version = new_version
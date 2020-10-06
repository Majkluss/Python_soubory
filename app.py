from Printer import Printer
from Mini import Mini
from Firmware import Firmware

fw0_1 = Firmware(0.1)
fw0_2 = Firmware(0.2)

mk2 = Printer("MK2", 0.4, fw0_1)
mini = Mini("MINI", 0.4, "Wi-Fi")


# mk2.firmware = fw0_1
# mini.firmware = fw0_2

print(mk2)
print(mini)

# print(mk2)
# print(mini)
# mini.firmware.upgrade(0.5)
# print(mini)
# mk2.firmware = fw0_2
# print(mk2)
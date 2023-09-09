import board
import digitalio

tmp = digitalio.DigitalInOut(board.GP25)
tmp.direction = digitalio.Direction.OUTPUT
tmp.value = True

RP2040GPO = {
    "GP7": board.GP7,
    "GP9": board.GP9,
    "GP10": board.GP10,
    "GP12": board.GP12,
    "GP14": board.GP14,
    "GP15": board.GP15,
    "GP16": board.GP16,
    "GP17": board.GP17,
    "GP20": board.GP20,
    "GP21": board.GP21,
    "GP22": board.GP22,
    "GP26": board.GP26,
    "GP27": board.GP27,
    "GP28": board.GP28,
}
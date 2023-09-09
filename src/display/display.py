import lib.ssd1306 as ssd1306
import busio

from src.board import SDA, SCL


class Display:
    text = 'hello'
    i2c = busio.I2C(SCL, SDA)
    display = ssd1306.SSD1306_I2C(128, 32, i2c)

    # def __init__(self):
    #     self.render()

    def render(self):
        try:
            self.display.fill(0)

            self.display.text(self.text, 0, 0, 1, font_name='lib/font5x8.bin', size=2)
            self.display.show()

            self.display.show()
        except:
            pass

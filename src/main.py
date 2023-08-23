import time

from src.buttons import Buttons
from src.command import command
from lib.adafruit_hid.keyboard import Keyboard
import usb_hid

def main():
    keyboard = Keyboard(usb_hid.devices)
    btn = Buttons()

    while True:
        command.send_command(keyboard, btn.get_buttons())
        time.sleep(0.25)




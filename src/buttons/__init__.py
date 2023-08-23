import json
import time

import digitalio

from src.board.rp2040_gpo import RP2040GPO


class Btn:
    name: str
    gpo: digitalio.DigitalInOut

    def __init__(self, name, gpo_pin):
        try:
            temp = digitalio.DigitalInOut(RP2040GPO[gpo_pin])

            temp.direction = digitalio.Direction.INPUT
            temp.pull = digitalio.Pull.DOWN

            self.name = name
            self.gpo = temp
        except:
            self.__del__()

    def __del__(self):
        print('del')


class Buttons:
    path_to_buttons = 'src/buttons.json'
    btn: [Btn] = []

    def __init__(self):
        self._init_buttons()

    def _get_buttons_key(self):
        temp_file = open(self.path_to_buttons)
        temp_data = temp_file.read()
        temp_file.close()
        try:
            return json.loads(temp_data)['buttons']
        except:
            return None

    def _init_buttons(self):
        self.btn = []
        for btn_elem in self._get_buttons_key():
            try:
                if RP2040GPO[btn_elem['gpo']]:
                    self.btn.append(Btn(btn_elem['name'], btn_elem['gpo']))
            except:
                pass
        return self.btn

    def get_buttons(self):
        while True:
            for elem in self.btn:
                if elem.gpo.value:
                    return elem.name
            time.sleep(0.25)

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
            if name == 'key1' or name =='key2':
                temp.pull = digitalio.Pull.DOWN
            else:
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
        res = []
        while True:
            temp = []
            for elem in self.btn:
                # if not elem.gpo.value and elem.name in res:
                #     print(elem.name)
                #     return list(set(res))
                if elem.gpo.value:
                    try:
                        if elem.name not in temp:
                            temp.append(elem.name)
                    except:
                        temp = []
                    try:
                        if elem.name not in res:
                            res.append(elem.name)
                    except:
                        res = []
                if len(res) > 0:
                    pass
            if len(temp) == 0:
                return list(set(res))

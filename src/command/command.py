import json

import usb_hid

from lib.adafruit_hid.consumer_control import ConsumerControl
from lib.adafruit_hid.consumer_control_code import ConsumerControlCodeDict
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keycode import KeycodeDict

from src.display import oled

class Command:
    name: str
    command: dict

    path_to_macros_folder: str = 'src/command_json'
    last_macros_file = 'last_macros.json'
    last_macros: str

    def __init__(self):
        self.init_macros(self._get_last_macros())
        self.keyboard = Keyboard(usb_hid.devices)
        self.cc = ConsumerControl(usb_hid.devices)

    def _get_last_macros(self) -> str | None:
        file = open(f'{self.path_to_macros_folder}/{self.last_macros_file}')
        temp = file.read()
        file.close()
        try:
            return json.loads(temp)['macros']
        except:
            return None

    def _change_last_macros(self, macros_name):
        file = open(f'{self.path_to_macros_folder}/{macros_name}', 'r+')
        print(macros_name)
        file.write(f'{"macros": "{macros_name}"}')
        file.close()
        print(f'{macros_name}')
        try:
            pass
        except:
            return None

    def init_macros(self, macros_name):
        self.last_macros = macros_name
        file = open(f'{self.path_to_macros_folder}/{macros_name}')
        try:
            temp = json.loads(file.read())
        except:
            return None
        self.name = temp['name']
        self.command = temp['command']

    def next_macros(self):
        try:
            last_macros = self.last_macros
            iter_macros = int(last_macros.split('_')[1].split('.')[0]) + 1
            tmp_name = f'macros_{iter_macros}.json'
            file = open(f'{self.path_to_macros_folder}/{tmp_name}')
            self.init_macros(tmp_name)
            self.last_macros = tmp_name
            file.close()
        except:
            iter_macros = 1
            tmp_name = f'macros_{iter_macros}.json'
            file = open(f'{self.path_to_macros_folder}/{tmp_name}')
            self.init_macros(tmp_name)
            self.last_macros = tmp_name
            file.close()


    def prev_macros(self):
        try:
            last_macros = self.last_macros
            iter_macros = int(last_macros.split('_')[1].split('.')[0]) - 1
            tmp_name = f'macros_{iter_macros}.json'
            file = open(f'{self.path_to_macros_folder}/{tmp_name}')
            self.init_macros(tmp_name)
            self.last_macros = tmp_name
            file.close()
        except:
            pass


    def send_command(self, btn):
        temp = ''
        for i in btn:
            temp += f'{i}'
        btn = temp
        if btn == 'key2':
            self.next_macros()
            oled.text = self.name
            oled.render()
            return
        if btn == 'key1':
            self.prev_macros()
            oled.text = self.name
            oled.render()
            return
        try:
            tmp = []
            cc_temp = self.get_command_by_key(btn)[0]
            if cc_temp in ConsumerControlCodeDict:
                self.cc.send(ConsumerControlCodeDict[cc_temp])
            else:
                for i in self.command[btn]:
                    tmp.append(KeycodeDict[i])
                self.keyboard.send(*tmp)
        except:
            pass

    def get_command_by_key(self, btn):
        try:
            return self.command[btn]
        except:
            return None

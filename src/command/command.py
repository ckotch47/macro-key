import json

from lib.adafruit_hid.keycode import KeycodeDict


class Command:
    name: str
    command: dict

    path_to_macros_folder: str = 'src/command_json'
    last_macros_file = 'last_macros.json'
    last_macros: str

    def __init__(self):
        self.init_macros(self._get_last_macros())

    def _get_last_macros(self) -> dict | None:
        file = open(f'{self.path_to_macros_folder}/{self.last_macros_file}')
        temp = file.read()
        file.close()
        try:
            return json.loads(temp)['macros']
        except:
            return None

    def init_macros(self, macros_name):
        file = open(f'{self.path_to_macros_folder}/{macros_name}')
        try:
            temp = json.loads(file.read())
        except:
            return None
        self.name = temp['name']
        self.command = temp['command']

    def send_command(self, keyboard, btn):
        try:
            tmp = []
            for i in self.command[btn]:
                tmp.append(KeycodeDict[i])
            keyboard.send(*tmp)
        except:
            pass

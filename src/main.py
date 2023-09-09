import time



from src.board.rp2040_gpo import RP2040GPO
from src.buttons import Buttons
from src.command import command



btn = Buttons()


class PrevValue:
    btn = None
    macros = None
    time = None


def current_milli_time():
    return round(time.time() * 1000)



prev_value = PrevValue()
def main():
    while True:
        btn_tmp = btn.get_buttons()
        if len(btn_tmp) == 0:
            continue

        if btn_tmp != prev_value.btn:
            command.send_command(btn_tmp)
            prev_value.btn = btn_tmp
        else:
            command.send_command(btn_tmp)
            prev_value.btn = None
        time.sleep(0.015)
        # try:
        #     oled.text = command.name
        #     oled.render()
        # except:
        #    pass

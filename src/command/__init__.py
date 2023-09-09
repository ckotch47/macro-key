from .command import Command
from src.display import oled
command = Command()
oled.text = command.name
oled.render()
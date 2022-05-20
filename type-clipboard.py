import pyperclip
from pynput.keyboard import Key, Controller

keyboard = Controller()

clipboardItem = pyperclip.paste()

keyboard.type(clipboardItem)

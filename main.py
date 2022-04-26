import pyotp
import pyperclip
from pynput import keyboard
import pyautogui

def on_press(key):
  skey = pyperclip.paste()
  totp = pyotp.TOTP(skey)
  if key == keyboard.Key.right:
    pyautogui.typewrite(totp.now())
    print(skey, totp.now())

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
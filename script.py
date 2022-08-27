from time import sleep
import pyautogui
import keyboard

keys = []


def main():
    initKeys()
    for key in keys:
        keyboard.release(key[1])
    while True:
        loop()


def initKeys():
    keys.append([1061, 'a'])  # 244, 244, 244
    keys.append([1206, 's'])  # 33, 214, 230
    keys.append([1361, 'k'])  # 33, 214, 230
    keys.append([1450, 'l'])  # 244, 244, 244


def loop():
    image = capture()
    press = []
    for key in keys:
        for y in range(1120, 1160, 5):
            if key[1] in press:
                break
            color = image.getpixel((key[0], y))
            if color != (20, 20, 20):
                press.append(key[1])
    for k in ('a', 's', 'k', 'l'):
        if k in press:
            keyboard.press(k)
        else:
            keyboard.release(k)


def capture():
    return pyautogui.screenshot()


if __name__ == '__main__':
    main()

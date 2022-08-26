from time import sleep
import pyautogui
import keyboard

keys = []


def main():
    initKeys()
    for key in keys:
        keyboard.release(key[2])
    while True:
        loop()
        # pos = pyautogui.position()
        # image = capture()
        # try:
        #     print(pos, image.getpixel((pos[0], pos[1])))
        # except:
        #     pass
        # sleep(1)


def initKeys():
    for y in range(1120, 1200, 5):
        keys.append([1061, y, 'a'])  # 244, 244, 244
        keys.append([1206, y, 's'])  # 33, 214, 230
        keys.append([1361, y, 'k'])  # 33, 214, 230
        keys.append([1450, y, 'l'])  # 244, 244, 244


def loop():
    image = capture()
    press = []
    for key in keys:
        if key[2] in press:
            continue
        color = image.getpixel((key[0], key[1]))
        if color != (20, 20, 20):
            press.append(key[2])
    for k in ('a', 's', 'k', 'l'):
        if k in press:
            keyboard.press(k)
        else:
            keyboard.release(k)


def capture():
    return pyautogui.screenshot()


if __name__ == '__main__':
    main()

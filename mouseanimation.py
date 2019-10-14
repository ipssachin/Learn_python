import pyautogui
pyautogui.FAILSAFE = False
for i in range(10):
       pyautogui.moveTo(2451, 995, duration=0.25)
       pyautogui.moveTo(3451, 995, duration=0.25)
       pyautogui.moveTo(3451, 3451, duration=0.25)
       pyautogui.moveTo(2451, 2451, duration=0.25)
print('Press Ctrl-C to quit.')
x, y = pyautogui.position()
positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
print(positionStr, end='')
# print('\b' * len(positionStr), end='', flush=True)

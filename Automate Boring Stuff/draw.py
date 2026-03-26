import pyautogui

pyautogui.click() # click to put drawing program in focus
distance = 200
while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration=0.2) # move right
    distance -= 25
    print(distance, 0)
    pyautogui.dragRel(0, distance, duration=0.2) # move down
    print(distance, 0)
    pyautogui.dragRel(-distance, 0, duration=0.2) # move left
    distance -= 25
    print(distance, 0)
    pyautogui.dragRel(0, -distance, duration=0.2) # move up
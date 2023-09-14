import keyboard
import time
import json

with open('settings.json', 'r') as file:
    data = json.load(file)

try:
    activate_button = data.get('activation_button')
    second_button = data.get('button_for_second_voicelines')
    if activate_button is not None and second_button is not None:
        print(f'Activation button successfully binded as "{activate_button}"')
        print(f'Second voiceline menu successfully binded as: "{second_button}"')
        print('\nScript activated successfully!\n\nTo stop it from activation just close this window')
        while True:
            keyboard.wait(activate_button)
            keyboard.press_and_release('g')
            time.sleep(0.01)
            keyboard.press_and_release('g')
            time.sleep(3)
            keyboard.press_and_release(second_button)
            time.sleep(0.01)
            keyboard.press_and_release('4')
    else:
        print('Error with loading strings from settings.json')
        time.sleep(10)
except:
    print('Error with loading strings from settings.json')
    time.sleep(10)
import keyboard
import time
import pyautogui
import csv
import os
from threading import Thread




def read_codes_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            return row  # Assuming all codes are in a single row




codes = read_codes_from_csv('codes.csv')
position_file = 'position.txt'
typing_active = False
typing_thread = None
stop_typing = False




# Mapping keypad digit positions (assuming the center of the screen)
screen_width, screen_height = pyautogui.size()
center_x = screen_width // 2
center_y = screen_height // 2




digit_positions = {
    '1': (center_x - 50, center_y + 50),
    '2': (center_x, center_y + 50),
    '3': (center_x + 50, center_y + 50),
    '4': (center_x - 50, center_y),
    '5': (center_x, center_y),
    '6': (center_x + 50, center_y),
    '7': (center_x - 50, center_y - 50),
    '8': (center_x, center_y - 50),
    '9': (center_x + 50, center_y - 50),
    '0': (center_x - 50, center_y + 125),
}




def save_position(position):
    with open(position_file, 'w') as f:
        f.write(str(position))




def load_position():
    if os.path.exists(position_file):
        with open(position_file, 'r') as f:
            return int(f.read())
    return 0




def type_codes(start_position):
    global typing_active, stop_typing
    position = start_position
    stop_typing = False
    while typing_active and not stop_typing:
        for i in range(position, len(codes)):
            if not typing_active or stop_typing:
                save_position(i)
                print("Stopping...")
                return


            # Print the current code
            print(f"Typing code: {codes[i]}")


            # Hold down 'e' key
            keyboard.press('e')
            # Add delay before moving the mouse and clicking
            time.sleep(0.25)
            # Move mouse to the position and click
            screen_width, screen_height = pyautogui.size()
            target_x = screen_width * 3 / 4
            target_y = screen_height * 3 / 4
            pyautogui.moveTo(target_x, target_y)
            pyautogui.click()
            # Release 'e' key
            keyboard.release('e')


            # Click each digit in the code
            for digit in codes[i]:
                if digit in digit_positions:
                    pyautogui.click(digit_positions[digit])


        position = 0  # Reset position to start from the beginning if we reach the end




def toggle_typing():
    global typing_active, typing_thread, stop_typing
    typing_active = not typing_active
    stop_typing = False
    if typing_active:
        print("Starting typing...")
        start_position = load_position()
        typing_thread = Thread(target=type_codes, args=(start_position,))
        typing_thread.start()
    else:
        print("Typing paused.")




def stop_typing_function():
    global stop_typing
    stop_typing = True




# Bind the toggle function to 'F9'
keyboard.add_hotkey('f9', toggle_typing)


# Bind the "End" key to stop typing
keyboard.add_hotkey('end', stop_typing_function)




# Keep the script running
print("Press 'F9' to start/stop typing codes.")
print("Press 'End' to stop typing codes.")
print("Press 'Esc' to exit the program.")
keyboard.wait('esc')
print("Program terminated.")

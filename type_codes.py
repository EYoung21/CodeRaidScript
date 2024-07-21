import keyboard
import time
import pyautogui
import csv
import os
import random
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
current_position = 0

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
    global typing_active, stop_typing, current_position
    position = start_position - 1  # Adjust for 1-based indexing
    stop_typing = False
    while typing_active and not stop_typing:
        for i in range(position, len(codes)):
            if not typing_active or stop_typing:
                current_position = i + 1  # Adjust for 1-based indexing
                save_position(current_position)
                print("Stopping...")
                return

            # Hold down 'e' key
            keyboard.press('e')
            # Add delay before moving the mouse and clicking
            time.sleep(0.245)
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

            # Print the current code with position
            print(f"Typed code at position {i + 1}: {codes[i]}")  # Adjust for 1-based indexing

            time.sleep(0.86)

        position = 0  # Reset position to start from the beginning if we reach the end

def toggle_typing(start_position):
    global typing_active, typing_thread, stop_typing, current_position
    typing_active = not typing_active
    stop_typing = False
    if typing_active:
        current_position = start_position if current_position == 0 else current_position
        print("Starting typing...")
        typing_thread = Thread(target=type_codes, args=(current_position,))
        typing_thread.start()
    else:
        print("Typing paused.")
        save_position(current_position)

def stop_typing_function():
    global stop_typing
    stop_typing = True

# Prompt user for starting position
last_position = load_position()
start_position_input = input(f"Enter the starting position (1-based index, or press Enter to resume from {last_position}): ")
start_position = int(start_position_input) if start_position_input.strip() else last_position

# Bind the start typing function to 'F2' with the starting position
keyboard.add_hotkey('f2', toggle_typing, args=(start_position,))

# Bind the "End" key to stop typing
keyboard.add_hotkey('end', stop_typing_function)

# Keep the script running
print("Press 'F2' to start/stop typing codes.")
print("Press 'End' to stop typing codes.")
print("Press 'Esc' to exit the program.")
keyboard.wait('esc')
print("Program terminated.")

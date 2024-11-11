# CodeRaidScript

## Description

CodeRaidScript is a Python script designed to automate typing codes from a CSV file into a specified application or game. The script allows for starting and stopping the typing process using hotkeys and provides an easy way to manage and automate repetitive typing tasks.

## Features

- Read codes from a CSV file.
- Automate typing of codes into a specified application.
- Start and stop the typing process with hotkeys.
- Save the last position of the typed code and resume from that position.

## Prerequisites

- Python 3.x
- Required Python libraries: `keyboard`, `pyautogui`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/EYoung21/CodeRaidScript.git
    ```

2. Change to the project directory:
    ```bash
    cd CodeRaidScript
    ```

3. Install the required libraries:
    ```bash
    pip install keyboard pyautogui
    ```

## Usage

1. Prepare the `codes.csv` file with the codes to be typed. Each code should be in a single row.

2. Run the script:
    ```bash
    python type_codes.py
    ```

3. Control the typing process:
    - When prompted, enter the position of the code you want to start on (1-based index).
    - Press `F2` to start or stop typing the codes (F3 for gates).
    - Press `End` to immediately stop typing the codes.
    - Press `Esc` to exit the program.
    - Change these two lines
      target_x = screen_width * 3 / 4
      target_y = screen_height * 3 / 4
    - To this for compound gates:
      target_x = screen_width * 1 / 4
      target_y = screen_height * 1 / 4
      

## Files

- `type_codes.py`: Main script to automate typing of codes.
- `codes.csv`: CSV file containing the codes to be typed.

## License

This project is licensed under the GNU License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

## Contact

For any inquiries, please contact [Eli Young](mailto:eliyoung4now@swarthmore.edu).

## Future Updates

- Implement automated recorded paths from bags to base for code raiding.

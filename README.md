# CodeRaidScript

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
    - Press `F9` to start or stop typing the codes.
    - Press `End` to immediately stop typing the codes.
    - Press `Esc` to exit the program.

## Files

- `type_codes.py`: Main script to automate typing of codes.
- `codes.csv`: CSV file containing the codes to be typed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

## Contact

For any inquiries, please contact [Eli Young](mailto:eliyoung4now@swarthmore.edu).

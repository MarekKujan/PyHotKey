# PyHotKey

**PyHotKey** is a tool that integrates AutoHotkey (AHK) with Python, allowing users to assign keyboard shortcuts to Python scripts. It includes a setup script that prepares a Python virtual environment for the scripts, and creates a shortcut in the startup folder to ensure the AHK script with the keyboard shortcuts starts automatically at system startup.

## Features

- **Assign Keyboard Shortcuts**: Easily assign custom keyboard shortcuts to Python scripts.
- **Auto Setup**: Automatically set up a Python virtual environment for the scripts.
- **Startup Integration**: Creates a shortcut in the startup folder to ensure the AHK script starts with the system.

## Requirements

- [Python 3.7 or higher](https://www.python.org/downloads/)
- [AutoHotkey v2](https://www.autohotkey.com/)

## Installation

1. **Clone the Repository**:
    ```cmd
    git clone https://github.com/MarekKujan/PyHotKey.git
    cd PyHotKey
    ```

2. **Setup the Environment**:
    Run the setup script to create a Python virtual environment, install necessary packages and create a shortcut in the startup folder to ensure that the AHK script starts automatically at system startup.
    ```cmd
    python setup.py
    ```
    - **Note:** You may need to run this script with admin privileges.

3. **Configure Keyboard Shortcuts**:
    Edit the `shortcuts.ahk` file to assign keyboard shortcuts to your Python scripts.

## Usage

1. **Add Your Scripts**:
    Place your Python scripts anywhere in the project directory, for example, in the `public_scripts` folder.


2. **Assign Keyboard Shortcuts**:
    Open the `shortcuts.ahk` file and add your desired keyboard shortcuts and corresponding Python scripts. For example:
    ```ahk
    ^j::Run ".\run_python.bat .\path\to\your_script.py"
    ```

3. **Run the Setup Script**:
    ```cmd
    python setup.py
    ```


## Example

Here is an example of how to add a keyboard shortcut to run a Python script:

1. **Create `example_script.py`** in the `public_scripts` directory:
    ```python
    print("Hello, World!")
    ```

2. **Edit `shortcuts.ahk`**:
    ```ahk
    ^j::Run ".\run_python.bat .\public_scripts\example_script.py"
    ```

3. **Run the setup script**:
    ```cmd
    python setup.py
    ```

4. **Press `Ctrl + J`** to run `example_script.py`.

## Public Scripts

### `create_tmp_email.py`
This script is used to create a temporary email address.

- **Asigned shortcut**: ctr + alt + E

- **Requirements**: 
    - [Firefox](https://www.mozilla.org/en-US/firefox/new/)
    - [geckodriver](https://github.com/mozilla/geckodriver/releases) must be in the Windows PATH.
- **Setup Instructions**: 
    - Replace `profile_path` on line 15 with the path to a Firefox profile that has an ad blocker and handles data collection pop-ups.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bugs or features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

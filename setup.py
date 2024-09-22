import os
import subprocess
import sys
from pathlib import Path

def run_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(result.returncode)
    return result.stdout

def check_and_install_package(package_name):
    try:
        __import__(package_name)
        print(f"{package_name} is already installed.")
    except ImportError:
        print(f"{package_name} is not installed. Installing...")
        run_command(f"python -m pip install {package_name}")

def generate_requirements():
    # Generate requirements.txt using pipreqs
    print("Generating requirements.txt...")
    run_command("pipreqs . --force")

def create_virtual_environment(env_name='venv'):
    # Create a virtual environment using virtualenv
    print(f"Creating virtual environment '{env_name}'...")
    run_command(f"virtualenv {env_name}")

def install_requirements(env_name='venv'):
    # Install requirements in the virtual environment
    print("Installing requirements in the virtual environment...")
    activate_script = os.path.join(env_name, 'Scripts', 'activate')
    run_command(f"{activate_script} && {env_name}\\Scripts\\pip install -r requirements.txt")

def remove_requirements_file():
    # Remove the requirements.txt file
    print("Removing requirements.txt...")
    os.remove('requirements.txt')

def create_shortcut(target_path, shortcut_path):
    # Create a Windows shortcut (.lnk file) at the specified location.
    import win32com.client
    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(str(shortcut_path))
    shortcut.TargetPath = str(target_path)
    shortcut.save()

def main():
    # Ensure win32com, pipreqs and virtualenv are installed
    check_and_install_package('pipreqs')
    check_and_install_package('virtualenv')
    check_and_install_package('pywin32')
    
    # Create a python venv
    generate_requirements()
    create_virtual_environment()
    install_requirements()
    remove_requirements_file()

    # Create ahk shortcut in startup folder
    ahk_script = Path(__file__).parent.resolve() / "shortcuts.ahk"
    shortcut_location = Path.home() / "AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/autohotkey.lnk"
    print("Creating a ahk shortcut in startup folder...")
    create_shortcut(ahk_script, shortcut_location)

    # run ahk script
    print("starting ahk script...")
    os.startfile(".\\shortcuts.ahk")

    print("Setup complete.")

if __name__ == '__main__':
    main()

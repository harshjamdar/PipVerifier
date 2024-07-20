import subprocess
import time
import logging
import json
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from rich.progress import track

console = Console()

# Configure logging
logging.basicConfig(filename='package_installation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_package_existence(package):
    result = subprocess.run(['pip', 'show', package], capture_output=True, text=True)
    return bool(result.stdout)

def get_installed_version(package):
    result = subprocess.run(['pip', 'show', package], capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if line.startswith('Version:'):
            return line.split(':')[1].strip()
    return None

def install_with_retry(command, retries=3):
    for _ in range(retries):
        result = subprocess.run(command, shell=True)
        if result.returncode == 0:
            return True
        time.sleep(2)
    return False

def load_preferences():
    try:
        with open('preferences.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def create_virtual_environment(env_name):
    subprocess.run(f"python -m venv {env_name}", shell=True)
    subprocess.run(f"source {env_name}/bin/activate", shell=True)  # For Linux/Mac

def verify_package_compatibility(package):
    # Simplified compatibility checks
    return True

def generate_pip_commands(filename, platform, verify_packages):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        commands = []
        status_comments = []
        
        for line in track(lines, description="Generating commands..."):
            library = line.split('==')[0].strip() if '==' in line else line.strip()
            if library:
                command_prefix = "!" if platform in [1, 2] else ""
                command = f"{command_prefix}pip install {library}"
                commands.append(command)
                
                if verify_packages:
                    valid = check_package_existence(library)
                    installed_version = get_installed_version(library)
                    compatibility = verify_package_compatibility(library)
                    status = "valid" if valid and compatibility else "not-valid"
                    version_info = f" (Installed: {installed_version})" if installed_version else ""
                    status_comments.append((library, f"{status}{version_info}"))
                    
                    if not valid and install_with_retry(command):
                        status_comments[-1] = (library, f"valid{version_info}")
                    elif not valid:
                        status_comments[-1] = (library, f"not-valid{version_info}")
        
        return commands, status_comments
    except FileNotFoundError:
        return ["Error: The file does not exist."], []
    except Exception as e:
        return [f"Error: {str(e)}"], []

def display_output(commands, status_comments):
    console.print(Panel("Pip Installation Commands", title="Commands", title_align="left", style="bold green"), style="bold")
    for command in commands:
        console.print(f"[cyan]{command}[/cyan]", style="bold")

    if status_comments:
        console.print(Panel("Package Verification Status", title="Status", title_align="left", style="bold blue"), style="bold")
        table = Table(title="Package Verification Status")
        table.add_column("Package", style="bold magenta", justify="left")
        table.add_column("Status", style="bold green", justify="left")
        for library, status in status_comments:
            color = "green" if "valid" in status else "red"
            table.add_row(library, Text(status, style=color))
        console.print(table)
    
    console.print("\nCreated by: [bold blue]Harsh Jamdar[/bold blue]", style="bold")
    console.print("[link=https://github.com/harshjamdar]GitHub Profile[/link]", style="underline blue")

def main():
    console.print("[bold yellow]Enter the location of your requirements file:[/bold yellow]")
    filename = input("File location: ").strip()
    
    console.print("[bold yellow]Do you want to verify the packages?[/bold yellow]")
    console.print("[1] Yes")
    console.print("[2] No")
    verify_choice = int(input("Enter your choice (1 or 2): "))
    verify_packages = (verify_choice == 1)

    console.print("[bold yellow]Select the platform for which you are going to import packages:[/bold yellow]")
    console.print("[1] Google Colab")
    console.print("[2] Kaggle")
    console.print("[3] Local")
    platform_choice = int(input("Enter your choice (1, 2, or 3): "))

    preferences = load_preferences()
    if platform_choice != 3:  # Local platform does not need virtual env
        env_name = preferences.get('env_name', 'venv')
        create_virtual_environment(env_name)
    
    pip_commands, status_comments = generate_pip_commands(filename, platform_choice, verify_packages)
    display_output(pip_commands, status_comments)

if __name__ == "__main__":
    main()

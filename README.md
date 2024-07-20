# PipVerifier - Pip Command Generator and Installer

## Introduction

The **Pip Command Generator and Installer** is a Python tool designed to streamline the process of generating and managing `pip` installation commands for Python packages. It includes features for verifying package existence, installing packages with retries, and managing virtual environments. It also offers options to visualize package dependencies and verify package compatibility.

## Features

- **Generate Pip Commands**: Automatically generate `pip` commands from a requirements file.
- **Verify Packages**: Check if packages exist and verify their compatibility with your system.
- **Retry Installation**: Retry installation of packages if the initial attempt fails.
- **Virtual Environment Creation**: Create and activate a virtual environment for package management.
- **Rich Output**: Display commands and status in a rich, formatted output in the console.
- **Custom Preferences**: Load and save custom preferences for environment setup and package verification.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/harshjamdar/PipVerifier/edit/main.git
   cd PipCommandGenerator
   ```
2. **Install Dependencies**
 
   Ensure you have pip installed, then install the required Python packages:

   ```bash
   pip install rich
   ```

## Usage

   1. **Run the Program**

   ```bash
   python main.py
   ```
   
   2. **Follow the Prompts**

      a).Enter the location of your requirements file.
      
      b).Choose whether to verify packages.
      
      c).Select the platform for which you are going to import packages (Google Colab, Kaggle, or Local).
     
   4. **Review the Output**
      
     The program will display the generated pip commands and the status of package verification.
## Example

```bash
Enter the location of your requirements file:[/bold yellow]
File location: requirements.txt

Do you want to verify the packages?[/bold yellow]
[1] Yes
[2] No
Enter your choice (1 or 2): 1

Select the platform for which you are going to import packages:[/bold yellow]
[1] Google Colab
[2] Kaggle
[3] Local
Enter your choice (1, 2, or 3): 3
Generating commands... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Pip Installation Commands                                                                                       │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
pip install accelerate
pip install diffusers
pip install numpy
Created by: Harsh Jamdar
```

## Contributing

Contributions are welcome! To contribute:

1. **Fork the Repository:** Create your own fork of the repository on GitHub.
2. **Create a Branch:** Create a new branch for your feature or bug fix.
3. **Make Changes:** Implement your changes.
4. **Submit a Pull Request:** Open a pull request from your branch to the main branch of the original repository.

Please ensure your code adheres to the existing style and includes appropriate tests and documentation.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or issues, please open an issue on GitHub or contact harsh7744jamdar@gmail.com

# Brute Force Password Cracker

This project is a multi-threaded brute force password cracker written in Python. It attempts to crack passwords by trying all possible combinations from a specified character set.

## Features

- **Password Cracking**: Attempt to crack given passwords by generating all possible combinations.
- **Multi-threading**: Utilize multi-threading to speed up the cracking process.
- **Command-line Arguments**: Flexible and customizable via command-line arguments.
- **Password File Input**: Read passwords from a file and attempt to crack each one.

## Prerequisites

- Python 3.x
- Libraries: `itertools`, `string`, `threading`, `time`, `argparse`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/brute-force-password-cracker.git
    cd brute-force-password-cracker
    ```

2. (Optional) Create and activate a virtual environment:
    ```sh
    python -m venv brute_force_env
    # On Windows
    brute_force_env\Scripts\activate
    # On Unix or MacOS
    source brute_force_env/bin/activate
    ```

## Usage

1. Create a text file (e.g., `passwords.txt`) with each password to be cracked on a new line.

2. Run the script with the password file as an argument:
    ```sh
    python brute_force_cracker.py passwords.txt --max_length 4 --num_threads 4
    ```

### Command-line Arguments

- `password_file`: Path to the file containing passwords to crack (required).
- `--charset`: Character set to use for cracking (default: `ascii_letters + digits`).
- `--max_length`: Maximum length of passwords to attempt (default: 8).
- `--num_threads`: Number of threads to use (default: 4).

## Example

1. Create a file `passwords.txt` with the following content:
    ```
    pass
    1234
    ```

2. Run the script:
    ```sh
    python brute_force_cracker.py passwords.txt --max_length 4 --num_threads 4
    ```

3. The script will output:
    ```
    Attempting to crack password: pass
    Password found: pass in 0.12 seconds
    Attempting to crack password: 1234
    Password found: 1234 in 0.05 seconds
    ```

## Notes

- Use this tool responsibly and ethically. It should only be used for educational purposes, penetration testing with explicit permission, or in controlled environments.
- Adjust the `charset`, `max_length`, and `num_threads` arguments as needed for different scenarios.


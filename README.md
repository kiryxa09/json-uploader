# JSONUploader

## Purpose
The purpose of this code is to perform a series of tasks including starting an executable file, waiting for a specified duration, updating FTP servers with JSON files, and converting JSON data to MySQL database entries.

## File Structure
The main script is located in a file named `main_script.py`. The `files` directory contains the JSON files to be uploaded and the `logs.txt` file is used for logging.

## Dependencies
The script uses the following libraries:
- `subprocess` for starting the executable file
- `time` for time-related operations
- `os` for interacting with the operating system
- `json` for JSON handling
- `mysql.connector` for MySQL database interaction
- `ftplib.FTP` for FTP operations
- `dotenv` for loading environment variables

## Steps
1. Start the `Brainstable.Gsk.Centura.Site` executable file using `subprocess.Popen`.
2. Wait for 5 minutes using `time.sleep`.
3. Update FTP servers with JSON files located in the `files` directory.
4. Convert JSON data from `nopatents.json` to MySQL database entries.

## Improvements
- Use a more descriptive variable name instead of `ftp` for better readability.
- Add error handling for FTP and MySQL operations.
- Separate the code into functions for better modularity and readability.
- Add comments to explain the purpose of each section of the code.

## Running the Script
To run the script, ensure that the necessary environment variables are set for FTP and MySQL connections, and the `Brainstable.Gsk.Centura.Site` file is located at the specified path.
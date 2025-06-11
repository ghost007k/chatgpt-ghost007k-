# Badge Request Program

This repository contains a simple Python script `badge_request.py` for collecting information needed to issue company ID cards. The script runs in a terminal and saves the collected data to `badge_requests.csv` which can be opened in Excel.

## Usage

Run the script with Python 3:

```bash
python3 badge_request.py
```

The program will prompt you to choose the area to access, select a main floor if needed, specify whether 14th floor access is required, and provide employee details such as department, position, employee number, and name. After completing the prompts, the data is appended to `badge_requests.csv` in the same directory.

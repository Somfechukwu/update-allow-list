# Update a File Through a Python Algorithm

## Project Overview
This project demonstrates how Python can be used to automate an access-control task. 

It is one of the portfolio projects in the Google Cybersecurity course (Automate Cybersecurity Tasks With Python).

I documented it here as part of my Python learning journey. 

The organization uses an **allow list** containing IP addresses that are permitted to access restricted content. A separate **remove list** identifies IP addresses that should no longer have access.

The Python algorithm *reads* the allow list, **removes the specified IP addresses, and *updates* the original file with the revised list.

## Objective
The objective of this project is to *automate the process of removing unauthorized or no-longer-approved IP addresses from an allow list.*

## How It Works
1. Opens the allow list file.
2. Reads the contents of the file.
3. Converts the contents from a string into a list.
4. Iterates through the remove list.
5. Checks whether each IP address exists in the allow list.
6. Removes matching IP addresses.
7. Converts the updated list back into a string.
8. Writes the updated list back to the allow list file.

## Technologies Used
- Python
- Visual Studio Code
- Git
- GitHub

## Python Concepts Demonstrated
- Variables
- File handling
- `with` statements
- `open()`
- `.read()`
- `.split()`
- `for` loops
- Conditional statements
- `.remove()`
- `.join()`
- `.write()`

## Cybersecurity Relevance
This project demonstrates basic security automation and access-control concepts.

## Project Files
- `update_allow_list.py`: This is the Python script that updates the allow list.
- `allow_list.txt`: This is the file containing the IP addresses allowed to access
restricted content.

## What I Learned
I learned how Python can interact with files and automate a simple security-related task. I also learned how to manipulate strings and lists and use loops and conditional statements to process security data.

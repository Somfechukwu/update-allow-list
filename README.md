# Update a File Through a Python Algorithm

## Project Overview
This project demonstrates how Python can be used to automate an access-control task. 

It is one of the portfolio projects in the Google Cybersecurity course (Automate Cybersecurity Tasks With Python).

I documented it here as part of my Python learning journey. 

The organization uses an **allow list** containing IP addresses that are permitted to access restricted content. A separate **remove list** identifies IP addresses that should no longer have access.

The Python algorithm *reads* the allow list, *removes the specified IP addresses*, and *updates* the original file with the revised list.

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
This project demonstrates **basic security automation** and **access-control** concepts. An allow list represents a security policy describing who or what is permitted to access a resource.

In real environments, similar automation concepts can be applied to firewall rules, network access, user permissions, cloud access controls, security policies, and incident-response processes.

## Project Files
- `update_allow_list.py`: This is the Python script that updates the allow list.
- `allow_list.txt`: This is the file containing the IP addresses allowed to access
restricted content.

## The Steps I Took
**Step 1 - Create The Allow List**
I *created a file* named **allow_list.txt** and entered the following five IP addresses:
192.168.1.10
192.168.1.15
192.168.1.20
192.168.1.25
192.168.1.30

**Step 2 - Create The Python File**
I *created a second file* named **update_allow_list.py** This is the python file which will contain the algorithm.

**Step 3 - Identify The File** 
`import_file = "allow_list.txt"`. 
This creates a variable named **import_file** containing the name of the file I wanted to work with.

**Step 4 - Open The File For Reading**
`(import_file, "r") as file:`. 
The **open()** function opens the file. The **"r"** represents *read*. The **with** statement helps Python manage the file resource and close it properly after the block finishes.

**Step 5 - Read The File Contents**
`ip_addresses = file.read()`
The **.read()** method reads the file and returns its contents as a string. At this point, all of the Ip addresses are together as text.

**Step 6 - Convert The String In A List**
`ip_addresses = ip_addresses.split()`
The **.split()** method separates the text into individual items. This produces a Python list that is much easier to modify.
`["192.168.1.10", "192.168.1.15", "192.168.1.20", "192.168.1.25", "192.168.1.30"]`

**Step 7 - Create The Remove List**
`remove_list = ["192.168.1.15", "192.168.1.25"]`
This list identifies the IP addresses which should no longer be allowed to access the restricted content.

**Step 8 - Iterate Through The Remove List**
`for element in remove_list:`
A **for** loop processes each item in a sequence one at a time. The variable **element** represents the current IP address being checked.

**Step 9 - Check Whether The Address Exists**
if element in ip_addresses:
The **if** statement prevents the program from trying to remove an IP address that is not present in the allow list.

**Step 10 - Remove The Address**
ip_addresses.remove(element)
The **.remove()** method removes the matching item from the list.

**Step 11 - Convert The List Back Into Text**
`ip_addresses = "\n".join(ip_addresses)`
The **.join()** method combines the list items into one string. **\n** means a new line. This means that every IP address remains on its own line.

**Step 12 - Write The Updated List To The File**
`with open(import_file, "w") as file:
file.write(ip_addresses)`
The **"w"** mode opens the file for writing. The **write()** method replaces the old file contents with the updated string.

## The Complete Python Program
`import_file = "allow_list.txt"`

# 1. Read allowlist
`with open(import_file, "r") as file:
    ip_addresses = file.read()`

# 2. Convert to list
`ip_addresses = ip_addresses.split()`

# 3. Define and remove IPs
`remove_list = ["192.168.1.15", "192.168.1.25"]`

`for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)`

# 4. Convert back to string and write out once
`ip_addresses = "\n".join(ip_addresses)`

`with open(import_file, "w") as file:
    file.write(ip_addresses)`

## How I Tested The Program
I saved both files. Next, I opened VS Code terminal and ran:
`python update_allow_list.py`

## How I Checked The Output
I opened the **allow_list.txt** file. I got the following result:
`192.168.1.10
192.168.1.20
192.168.1.30`

The IP addresses remaining are now three instead of the initial five. The two IP addresses in the **remove list** have gone.

## What I Learned
I learned the following:
* **Security Automation:** Learned how scripting reduces human error and enforces the *Principle of Least Privilege* by rapidly updating network and access-control lists.
* **Safe File Handling (I/O):** Used Python's `with open()` context manager to ensure files close automatically and securely, preventing resource leaks.
* **Data Parsing & Type Conversion:** Applied `.split()` to transform raw string data into lists that can be iterated, and `"\n".join()` to reconstruct clean text data before writing.
* **Defensive Programming:** Implemented conditional checks (`if element in ...`) prior to calling `.remove()` to prevent runtime `ValueError` crashes.
* **Resource Optimization:** Structured the script to perform file I/O operations only once at the beginning and end, rather than opening and writing to disk inside a loop.

# Update a File Through a Python Algorithm

## Project Overview
This project demonstrates how Python can be used to automate an access-control task. It is part of the **Google Cybersecurity Certificate** (*Automate Cybersecurity Tasks with Python*).

The organization uses an **allow list** containing IP addresses permitted to access restricted content. A separate **remove list** identifies IP addresses that should no longer have access.

The Python algorithm reads the allow list, removes specified IP addresses, and updates the original file with the revised list.

---

## Objective
Automate the process of removing unauthorized or revoked IP addresses from an access-control allow list using Python file handling and string manipulation.

---

## How It Works
1. Opens the allow list file.
2. Reads the contents of the file.
3. Converts the contents from a string into a list.
4. Iterates through the remove list.
5. Checks whether each IP address exists in the allow list.
6. Removes matching IP addresses.
7. Converts the updated list back into a string.
8. Writes the updated list back to the allow list file.

---

## Technologies Used
- **Language:** Python
- **IDE:** Visual Studio Code
- **Version Control:** Git & GitHub

---

## Python Concepts Demonstrated
- Variables & Data Types
- File handling (`open()`, `with` statement)
- String & list methods (`.read()`, `.split()`, `.remove()`, `.join()`, `.write()`)
- Iteration (`for` loops)
- Conditional statements (`if` checks)

---

## Cybersecurity Relevance
This project demonstrates **basic security automation** and **access control** concepts. An allow list represents a security policy describing who or what is permitted to access a protected resource.

In enterprise environments, similar automation logic applies to:
- Firewall rules
- Network access control (NAC)
- IAM & user permissions
- Cloud security groups
- Incident response playbooks

---

## Project Files
- `update_allow_list.py` — The Python script that updates the access list.
- `allow_list.txt` — The text file containing authorized IP addresses.

---

## Implementation Steps

### Step 1: Create the Allow List
Created `allow_list.txt` containing the initial authorized IP addresses:
```text
192.168.1.10
192.168.1.15
192.168.1.20
192.168.1.25
192.168.1.30
```
### Step 2: Create the Python Script
I created a python file called `update_allow_list.py` which would contain the algorithm.

### Step 3: Identify the File
`import_file = "allow_list.txt"`
Assigned the target file name to the `import_file` variable for easy reuse.

### Step 4: Open and Read the File
`with open(import_file, "r") as file:`
    `ip_addresses = file.read()`
The `open()` function with `"r"` mode opens the file for reading. The `with` statement acts as a context manager, automatically closing the file when execution exits the block. The `.read()` method imports the file contents as a single string.

### Step 5: Convert the String to a List
`ip_addresses = ip_addresses.split()`

The `split()` method splits the string at whitespace (including newlines) to individual elements:
`["192.168.1.10", "192.168.1.15", "192.168.1.20", "192.168.1.25", "192.168.1.30"]`

### Step 6: Define the Remove List
`remove_list = ["192.168.1.15", "192.168.1.25"]`
Defines the list of revoked IP addresses that need to be removed from the allow list.

### Step 7: Iterate and Remove Targeted IPs
`for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)`
- A `for` loop iterates through each address in `remove_list`.
- The `if element in ip_addresses` check prevents runtime errors (`ValueError`) in case an IP is already absent.
- The `.remove()` method removes the matching entry from `ip_addresses`.

### Step 8: Convert the List back into a String
`ip_addresses = "\n".join(ip_addresses)
The `.join()` method combines the elements in a list into a single string separated by newlines (`\n`), matching the original file structure.

### Step 9: Write the Updated Data to the File
`with open(import_file, "w") as file:
    file.write(ip_addresses)`
The `"w"` write mode overwrites `allow_list.txt` with the cleaned string using `.write()`.

### Complete Python Script
# Define the target file
import_file = "allow_list.txt"

# 1. Read allow list contents
with open(import_file, "r") as file:
    ip_addresses = file.read()

# 2. Convert raw string into a list of IPs
ip_addresses = ip_addresses.split()

# 3. Define revoked IPs and remove them
remove_list = ["192.168.1.15", "192.168.1.25"]

for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# 4. Convert list back to formatted string and overwrite file
`ip_addresses = "\n".join(ip_addresses)`

`with open(import_file, "w") as file:`
    `file.write(ip_addresses)`

### Testing & Output Verification
## Execution
Run the script from the VS Code Terminal:
`python update_allow_list.py`

## Output (`allow_list.txt`)
```text
192.168.1.10
192.168.1.20
192.168.1.30
```
**Result:** The two target IP addresses (`192.168.1.15` and `192.168.1.25`) were successfully removed, leaving only the three authorized addresses intact.

### Key Takeaways
In this project, I was able to do the following:
- **Security Automation:** I demonstrated how scripting enforces the Principle of Least Privilege through rapid, repeatable access list maintenance.
- **Safe File Handling:** Used with `open()` to ensure the file closes automatically and safely after reading or writing.
- **Data Parsing & Formatting:** I used `.split()` to turn the text into a list for easy editing, and `"\n".join()` to put it back into clean lines before saving.
- **Error Prevention:** I added an `if` check (`if element in ...`) to make sure an IP address exists before trying to remove it, preventing program crashes.
**Efficient Code:** I kept file reading and writing to single steps at the start and end, avoiding unnecessary file operations inside the loop.

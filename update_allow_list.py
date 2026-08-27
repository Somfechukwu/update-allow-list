import_file = "allow_list.txt"

# 1. Read allowlist
with open(import_file, "r") as file:
    ip_addresses = file.read()

# 2. Convert to list
ip_addresses = ip_addresses.split()

# 3. Define and remove IPs
remove_list = ["192.168.1.15", "192.168.1.25"]

for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# 4. Convert back to string and write out once
ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w") as file:
    file.write(ip_addresses)
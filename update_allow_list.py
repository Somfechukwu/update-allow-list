import_file = "allow_list.txt"
with open(import_file, "r") as file:
    ip_addresses = file.read()
    ip_addresses = ip_addresses.split()
    remove_list = ["192.168.1.15", "192.168.1.25"]
    for element in remove_list:
        if element in ip_addresses:
            ip_addresses.remove(element)
            ip_addresses = "\n".join(ip_addresses)
            with open(import_file, "w") as file:
                file.write(ip_addresses)
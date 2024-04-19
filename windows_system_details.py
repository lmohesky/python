import os
import subprocess
import re
import socket
import psutil
import datetime

def get_logged_in_users():
    output = subprocess.check_output(['query', 'user']).decode('utf-8')
    users = re.findall(r'>\s+(.*?)\s+', output)
    return users

def get_windows_update_history():
    output = subprocess.check_output(['wmic', 'qfe', 'list', 'brief']).decode('utf-8')
    updates = output.strip().split('\n')[1:]
    return updates

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_uptime():
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    return str(uptime)

def get_resource_sizes():
    total_ram = psutil.virtual_memory().total / (1024 * 1024)
    available_ram = psutil.virtual_memory().available / (1024 * 1024)
    total_disk = psutil.disk_usage('/').total / (1024 * 1024 * 1024)
    free_disk = psutil.disk_usage('/').free / (1024 * 1024 * 1024)
    return total_ram, available_ram, total_disk, free_disk

def main():
    print("Logged-in Users:")
    users = get_logged_in_users()
    for user in users:
        print(user)

    print("\nWindows Update History:")
    updates = get_windows_update_history()
    for update in updates:
        print(update)

    print("\nIP Address:")
    ip_address = get_ip_address()
    print(ip_address)

    print("\nUptime:")
    uptime = get_uptime()
    print(uptime)

    print("\nResource Sizes:")
    total_ram, available_ram, total_disk, free_disk = get_resource_sizes()
    print(f"Total RAM: {total_ram:.2f} MB")
    print(f"Available RAM: {available_ram:.2f} MB")
    print(f"Total Disk Space: {total_disk:.2f} GB")
    print(f"Free Disk Space: {free_disk:.2f} GB")

if __name__ == '__main__':
    main()

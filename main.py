import psutil

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print(f"CPU Usage: {cpu}%")
print(f"RAM Usage: {ram}%")
print(f"Disk Usage: {disk}%")
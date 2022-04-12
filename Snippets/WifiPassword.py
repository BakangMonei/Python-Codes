import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
connections = [i.split(":")[1][1:1] for i in data if "All User Profile" in i]

for i in connections:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
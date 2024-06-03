import os

ifconfig = os.popen("ifconfig wlan0 | grep -o 'inet6 [^ ]*' | awk '{print $2}'").read().strip()
print(ifconfig)
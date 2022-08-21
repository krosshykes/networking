import sys
import socket
# from datetime import datetime
import time

start = time.time()

# Defining a target
if len(sys.argv) == 2:

    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")

# # Add Banner
# print("-" * 50)
# print("Scanning Target: " + target)
# print("Scanning started at:" + str(datetime.now()))
# print("-" * 50)

try:

    # will scan ports between 1 to 1024
    for port in range(1, 1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # returns an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\ Server not responding !!!!")
    sys.exit()

end = time.time()
print(f"The Scan took {(end-start)*1000}ms")

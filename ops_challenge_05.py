#!/usr/bin/env python3

# Author: Jamie Giannini

# Objectives: Create a Python script that executes a hardware spec-fetching bash script successfully. Indicate in comments how you achieved this
# [X] The Python library “os” must be utilized
# [X] At least three variables must be declared in Python that contain bash operations
# [X] The Python function print() must be used at least three times
# [X] Extra: Use the subprocess module



#import os # Import the os library
import subprocess # Import subprocess module

print()
print("############################### - Who are you? - ##############################################")
show_user = subprocess.run("whoami", capture_output=True, text=True).stdout.strip("\n") #calls bash command to display user name + strips completed process output message line from displaying
print(show_user)

print()
print("################################ - Hardware Info - #######################################")
show_hardware = subprocess.run(["sudo", "lshw", "-short"], capture_output=True, text=True).stdout.strip("\n") #display hardware paths
print(show_hardware)

print()
print("############################### - IP Info - ##############################################")
show_ip = subprocess.run(["sudo", "ip", "a"], capture_output=True, text=True).stdout.strip("\n") #display ip address
print(show_ip)
print()

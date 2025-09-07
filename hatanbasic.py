#!/usr/bin/python3
import os
import time
import sys

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

def slowprint(s, delay=0.05):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

clear_screen()

print('\033[91mHATANBASIC\033[0m\n')

print(''' \033[95m
+--------------------------------------+
| This Tool Installs Basic Packages    |
+--------------------------------------+
| Coded By hatanhack | version : 2.0  |
+--------------------------------------+''')

slowprint(''' \033[93m
[01] python
[02] python2
[03] python-dev
[04] python3
[05] php
[06] java
[07] git
[08] perl
[09] bash
[10] nano
[11] curl
[12] openssl
[13] openssh
[14] wget
[15] clang
[16] nmap
[17] w3m
[18] hydra
[19] ruby
[20] macchanger
[21] host
[22] dnsutils
[23] coreutils
''')

slowprint('''\033[96m
[00] termux-setup-storage (for storage access)
''')

choice = input("\033[93mDo You Want to Install All Packages [y/n] : ").strip().lower()
if choice == 'n':
    sys.exit("\n\033[91mExiting...")

if choice == 'y':
    # تحديث الحزم
    os.system("pkg update -y && pkg upgrade -y")

    # تثبيت الحزم
    packages = [
        "python", "python2", "python-dev", "python3", "php", "java", "git",
        "perl", "bash", "nano", "curl", "openssl", "openssh", "wget", "clang",
        "nmap", "w3m", "hydra", "ruby", "macchanger", "host", "dnsutils", "coreutils"
    ]
    os.system("pkg install " + " ".join(packages) + " -y")

    print("\n\033[92mAll packages installed successfully!\n")
    input("Press Enter to set up Termux storage (if needed)...")
    os.system("termux-setup-storage")

    print("\033[95m+-------------------------------------------------+")
    slowprint('''\033[95m|             Welcome To Hackers World            |
|                   hatanhack                      |
|         Watch Our Tutorials To Learn Ethical     |
|                     Hacking                      |''')
    print("+-------------------------------------------------+")

input("\n\033[93mPress Enter to exit : ")

print ("""
Subscribe VPP Hacker
""")

print("Allow the Button For Access the Storage in Termux")
os.system("termux-setup-storage")

print("\033[95m+-------------------------------------------------+")
slowprint('''\033[95m|             Welcome To Hackers World            |
|           Subscribe Our YouTube Channel          |
|   Watch Our Tutorials To Learn Ethical Hacking   |''')
print("+-------------------------------------------------+")

input("\n\nPress the enter key to exit : ")    input("Press Enter to set up Termux storage (if needed)...")
    os.system("termux-setup-storage")

    print("\033[95m+-------------------------------------------------+")
    slowprint('''\033[95m|             Welcome To Hackers World            |
|                   hatanhack                      |
|         Watch Our Tutorials To Learn Ethical     |
|                     Hacking                      |''')
    print("+-------------------------------------------------+")

input("\n\033[93mPress Enter to exit : ") nmap -y")
os.system ("apt install w3m -y")
os.system ("apt install hydra -y")


print ("""
subscribe VPP Hacker """)

os.system ("apt install ruby -y")
os.system ("apt install macchanger -y")
os.system ("apt install host -y")
os.system ("apt install dnsutils -y")
os.system ("apt install coreutils -y")

print ("Allow the Button For Access the Storage in Termux")


os.system ("termux-setup-storage")

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[95m+-------------------------------------------------+")
slowprint('''\033[95m|             Welcome To Hackers World            |
|           Subscribe Our YouTube Channel         |
| Watch Ours Tutorials For Learn Ethical Hacking  |''')
print("+-------------------------------------------------+")

input("\n\nPress the enter key to exit : ")

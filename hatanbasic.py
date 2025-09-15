#!/usr/bin/python3
import os
import time
import sys

def slowprint(s, delay=0.04):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def install_package(pkg):
    result = os.system(f"apt install -y {pkg}")
    if result != 0:
        print(f"⚠️ Failed to install {pkg}, skipping...")

def main():
    os.system("clear")
    print("\033[91mHATAN BASIC - Auto Installer\033[0m\n")

    slowprint("\033[93m[+] Updating and upgrading system...\033[0m")
    if os.system("apt update -y && apt upgrade -y") != 0:
        print("⚠️ Warning: System update failed, continuing...")

    slowprint("\033[93m[+] Installing basic packages...\033[0m")

    packages = [
        "git",
        "python",
        "python2",
        "php",
        "ruby",
        "perl",
        "nano",
        "bash",
        "curl",
        "wget",
        "openssl",
        "openssh",
        "clang",
        "nmap",
        "w3m",
        "dnsutils",
        "net-tools",
        "coreutils",
        "openjdk-17",
        "proot",
        "termux-api"
    ]

    for pkg in packages:
        install_package(pkg)

    print("\n\033[92m[✔] All available packages have been installed successfully!\033[0m\n")
    slowprint("\033[95mYour Termux Ubuntu environment is now ready ✔️\033[0m")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()

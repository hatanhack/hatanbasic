#!/usr/bin/python3
import os
import time
import sys

def slowprint(s, delay=0.04):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    os.system("clear")
    print("\033[91mHATAN BASIC - Auto Installer\033[0m\n")

    slowprint("\033[93m[+] Updating and upgrading system...\033[0m")
    os.system("apt update -y && apt upgrade -y")

    slowprint("\033[93m[+] Installing basic packages...\033[0m")

    packages = [
        "git",          # Repository management
        "python",       # Python 3
        "python2",      # Legacy Python 2
        "php",          # PHP scripts
        "ruby",         # Ruby language
        "perl",         # Perl language
        "nano",         # Text editor
        "bash",         # Bash shell
        "curl",         # Data transfer tool
        "wget",         # File downloader
        "openssl",      # SSL/TLS tools
        "openssh",      # SSH client/server
        "clang",        # C/C++ compiler
        "nmap",         # Network scanner
        "w3m",          # Text-based web browser
        "dnsutils",     # host, dig, nslookup
        "net-tools",    # ifconfig, arp, netstat
        "coreutils",    # Basic GNU utilities
        "openjdk-17"    # Java (OpenJDK 17)
    ]

    for pkg in packages:
        os.system(f"pkg install -y {pkg} || echo '⚠️ {pkg} not available'")

    print("\n\033[92m[✔] All available packages have been installed successfully!\033[0m\n")
    slowprint("\033[95mYour Termux environment is now ready ✔️\033[0m")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()

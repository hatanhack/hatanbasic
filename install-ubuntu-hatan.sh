#!/bin/bash
# Script to install or update the Ubuntu environment and run HATAN BASIC

# Download or update the Neo-Oli repository
if [ -d "$HOME/termux-ubuntu" ]; then
    cd "$HOME/termux-ubuntu"
    git pull origin master
else
    git clone https://github.com/Neo-Oli/termux-ubuntu.git
fi

# Install or update Ubuntu
cd "$HOME/termux-ubuntu"
bash ubuntu.sh

# Launch Ubuntu and run HATAN BASIC
./start-ubuntu.sh <<EOF
cd /root/hatanbasic
python3 hatanbasic.py
EOF

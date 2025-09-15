#!/bin/bash
# Script to install or update Ubuntu in Termux

# Update Termux packages
pkg update -y && pkg upgrade -y
pkg install wget proot tar git python -y

# Clone or update Neo-Oli Ubuntu repository inside your project folder
if [ -d "$HOME/hatanbasic/termux-ubuntu" ]; then
    cd "$HOME/hatanbasic/termux-ubuntu"
    git pull origin master
else
    git clone https://github.com/Neo-Oli/termux-ubuntu.git "$HOME/hatanbasic/termux-ubuntu"
    cd "$HOME/hatanbasic/termux-ubuntu"
fi

# Run ubuntu.sh to install and start Ubuntu
bash ubuntu.sh

echo "Ubuntu installation complete! You are now inside Ubuntu environment."

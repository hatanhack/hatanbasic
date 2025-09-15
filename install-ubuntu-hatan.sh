#!/bin/bash
# Script to install or update Ubuntu (Focal 20.04 ARM64) in Termux

# Update Termux packages
pkg update -y && pkg upgrade -y
pkg install wget proot tar git python -y

# Clone or update Neo-Oli Ubuntu repository inside project folder
if [ -d "$HOME/hatanbasic/termux-ubuntu" ]; then
    cd "$HOME/hatanbasic/termux-ubuntu"
    git pull origin master
else
    git clone https://github.com/Neo-Oli/termux-ubuntu.git "$HOME/hatanbasic/termux-ubuntu"
    cd "$HOME/hatanbasic/termux-ubuntu"
fi

# Download Ubuntu Focal image
UBUNTU_IMAGE_URL="https://partner-images.canonical.com/core/focal/current/ubuntu-focal-core-cloudimg-arm64-root.tar.gz"
wget -O ubuntu-rootfs.tar.gz $UBUNTU_IMAGE_URL

# Extract Ubuntu image
proot --link2symlink tar -xzf ubuntu-rootfs.tar.gz -C "$HOME/hatanbasic/termux-ubuntu"

# Fix DNS to connect to the internet
echo "nameserver 8.8.8.8" > "$HOME/hatanbasic/termux-ubuntu/etc/resolv.conf"

# Make launch script executable
chmod +x start-ubuntu.sh

echo "Ubuntu (Focal 20.04) installation complete!"
echo "You can now start Ubuntu with: ./start-ubuntu.sh"

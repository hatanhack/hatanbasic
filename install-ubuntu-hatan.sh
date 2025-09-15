#!/bin/bash
# HATAN BASIC Auto Installer + Ubuntu Focal ARM64 for Termux

# Step 1: Update Termux
pkg update -y && pkg upgrade -y

# Step 2: Install essential packages
pkg install -y git python python2 php ruby perl nano bash curl wget openssl openssh clang nmap w3m dnsutils net-tools coreutils openjdk-17 proot termux-api

# Step 3: Clone termux-ubuntu if not exists
UBUNTU_DIR="$HOME/hatanbasic/termux-ubuntu"
if [ -d "$UBUNTU_DIR" ]; then
    echo "[*] termux-ubuntu exists, skipping clone."
else
    git clone https://github.com/Neo-Oli/termux-ubuntu.git "$UBUNTU_DIR"
fi

cd "$UBUNTU_DIR"

# Step 4: Download updated Ubuntu Focal ARM64 if not exists
TARBALL="ubuntu-focal-root.tar.gz"
if [ ! -f "$TARBALL" ]; then
    echo "[*] Downloading Ubuntu Focal ARM64..."
    wget -O "$TARBALL" "https://cloud-images.ubuntu.com/focal/current/ubuntu-20.04-server-cloudimg-arm64-root.tar.gz"
fi

# Step 5: Extract Ubuntu if folder not exists
FOLDER="ubuntu-fs"
if [ ! -d "$FOLDER" ]; then
    mkdir -p "$FOLDER"
    echo "[*] Extracting Ubuntu image..."
    proot --link2symlink tar -xf "$TARBALL" -C "$FOLDER" --exclude='dev'
    echo "nameserver 1.1.1.1" > "$FOLDER/etc/resolv.conf"
fi

# Step 6: Write start script
BIN="start-ubuntu.sh"
cat > "$BIN" <<- EOM
#!/bin/bash
cd \$(dirname \$0)
unset LD_PRELOAD
command="proot"
command+=" --link2symlink -0 -r $FOLDER"
command+=" -b /dev -b /proc"
command+=" -w /root"
command+=" /usr/bin/env -i HOME=/root PATH=/usr/local/sbin:/usr/local/bin:/bin:/usr/bin:/sbin:/usr/sbin TERM=\$TERM LANG=C.UTF-8 /bin/bash --login"
if [ -n "\$1" ]; then
    \$command -c "\$@"
else
    exec \$command
fi
EOM

# Step 7: Make start script executable
chmod +x "$BIN"
echo "[✔] Ubuntu installation complete! Launch with ./$BIN"

# Step 8: Run HATAN BASIC inside Ubuntu
echo "[*] Launching Ubuntu and HATAN BASIC..."
./start-ubuntu.sh <<'EOF'
cd /root/hatanbasic
python3 hatanbasic
EOF

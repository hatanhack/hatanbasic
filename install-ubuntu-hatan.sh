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

# Step 4: Remove old Ubuntu if exists
rm -rf ubuntu-fs ubuntu.tar.gz

# Step 5: Download updated Ubuntu Focal ARM64
TARBALL="ubuntu.tar.gz"
wget -O "$TARBALL" "https://cloud-images.ubuntu.com/focal/current/ubuntu-20.04-server-cloudimg-arm64-root.tar.gz"

# Step 6: Extract Ubuntu
mkdir -p ubuntu-fs
proot --link2symlink tar -xf "$TARBALL" -C ubuntu-fs --exclude='dev'
echo "nameserver 1.1.1.1" > ubuntu-fs/etc/resolv.conf

# Step 7: Write start script
BIN="start-ubuntu.sh"
cat > "$BIN" <<- EOM
#!/bin/bash
cd \$(dirname \$0)
unset LD_PRELOAD
command="proot"
command+=" --link2symlink -0 -r ubuntu-fs"
command+=" -b /dev -b /proc"
command+=" -w /root"
command+=" /usr/bin/env -i HOME=/root PATH=/usr/local/sbin:/usr/local/bin:/bin:/usr/bin:/sbin:/usr/sbin TERM=\$TERM LANG=C.UTF-8 /bin/bash --login"
if [ -n "\$1" ]; then
    \$command -c "\$@"
else
    exec \$command
fi
EOM

# Step 8: Make start script executable
chmod +x "$BIN"
echo "[✔] Ubuntu installation complete! Launch with ./$BIN"

# Step 9: Run HATAN BASIC inside Ubuntu
echo "[*] Launching Ubuntu and HATAN BASIC..."
./start-ubuntu.sh <<'EOF'
cd /root/hatanbasic
python3 hatanbasic
EOF

#!/bin/bash

echo "Installing CSNova..."

# 1. Check and install system dependencies
echo "Checking system dependencies..."
sudo apt update
sudo apt install -y libxcb-cursor0

# 2. Create installation directory
INSTALL_DIR="$HOME/CSNova 1.0"
mkdir -p "$INSTALL_DIR"

# 3. Copy csnova in executable
cp ./dist/csnova "$INSTALL_DIR/"

# 4. Copy all necessary folders and files
for folder in assets config core data docs gui ai export; do
    if [ -d "$folder" ]; then
        cp -r "$folder" "$INSTALL_DIR/"
    fi
done

# 5. Set executable permissions
chmod +x "$INSTALL_DIR/csnova"

echo "Installation complete!"
echo "You can start CSNova with:"
echo "$INSTALL_DIR/csnova"
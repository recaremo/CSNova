#!/bin/bash

echo "Installing CSNova..."

# 1. Check and install system dependencies
echo "Checking system dependencies..."
sudo apt update
sudo apt install -y libxcb-cursor0

# 2. Create installation directory
INSTALL_DIR="$HOME/CSNova"
mkdir -p "$INSTALL_DIR"

# 3. Copy Executable and Desktop File
cp ./dist/csNova "$INSTALL_DIR/"
cp ./csnova.desktop "$INSTALL_DIR/"
chmod +x "$INSTALL_DIR/csnova.desktop"

# 4. Copy all necessary folders and files
for folder in assets config core data docs gui ai export; do
    if [ -d "$folder" ]; then
        cp -r "$folder" "$INSTALL_DIR/"
    fi
done

# 5. Set executable permissions
chmod +x "$INSTALL_DIR/csNova"

# 6. Desktop Integration
DESKTOP_FILE="$INSTALL_DIR/csnova.desktop"
MENU_FILE="$HOME/.local/share/applications/csnova.desktop"

# Passe Pfade in der .desktop-Datei an (ohne Backslash!)
sed "s|Exec=.*|Exec=$INSTALL_DIR/csNova|g; s|Icon=.*|Icon=$INSTALL_DIR/assets/media/csnova.png|g" "$DESKTOP_FILE" > "$MENU_FILE"
chmod +x "$MENU_FILE"

echo "Installation complete!"
echo "Du kannst CSNova starten mit:"
echo "$INSTALL_DIR/csNova"
echo "Oder über das Anwendungsmenü (Suchbegriff: CSNova)."
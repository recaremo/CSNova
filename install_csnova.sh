#!/bin/bash

echo "Installing CSNova..."

INSTALL_DIR="$HOME/CSNova"
mkdir -p "$INSTALL_DIR"

cp ./dist/csNova "$INSTALL_DIR/"
chmod +x "$INSTALL_DIR/csNova"

for folder in assets config core data docs gui ai export; do
    [ -d "$folder" ] && cp -r "$folder" "$INSTALL_DIR/"
done

MENU_FILE="$HOME/.local/share/applications/csnova.desktop"
cat > "$MENU_FILE" <<EOF
[Desktop Entry]
Type=Application
Name=CSNova
Comment=Creative Writing Tool
Exec=$INSTALL_DIR/csNova
Icon=$INSTALL_DIR/assets/media/csnova.png
Terminal=false
Categories=Office;Utility;
StartupNotify=true
EOF

chmod 644 "$MENU_FILE"
chmod 644 "$INSTALL_DIR/assets/media/csnova.png"

update-desktop-database ~/.local/share/applications/

echo "Installation complete!"
echo "Du kannst CSNova starten über das Anwendungsmenü (Suchbegriff: CSNova) oder mit:"
echo "$INSTALL_DIR/csNova"
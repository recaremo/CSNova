#!/bin/bash

echo "Installing CSNova..."

INSTALL_DIR="$HOME/CSNova"
mkdir -p "$INSTALL_DIR"

# Kopiere Binary und Ressourcen
cp ./dist/csNova "$INSTALL_DIR/"
for folder in assets config core data docs gui ai export; do
    [ -d "$folder" ] && cp -r "$folder" "$INSTALL_DIR/"
done

# Desktop-Datei anpassen und ins Menü kopieren
DESKTOP_FILE="$INSTALL_DIR/csnova.desktop"
MENU_FILE="$HOME/.local/share/applications/csnova.desktop"
sed "s|{INSTALL_DIR}|$INSTALL_DIR|g" ./csnova.desktop > "$MENU_FILE"

# Icon-Rechte setzen
chmod 644 "$INSTALL_DIR/assets/media/csnova.png"

# Desktop-Datei Rechte setzen
chmod 644 "$MENU_FILE"

# Desktop-Datenbank aktualisieren
update-desktop-database ~/.local/share/applications/

echo "Installation complete!"
echo "Du kannst CSNova starten über das Anwendungsmenü (Suchbegriff: CSNova) oder mit:"
echo "$INSTALL_DIR/csNova"
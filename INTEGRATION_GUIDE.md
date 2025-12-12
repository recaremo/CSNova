# Integration der Manager in csNova_main.py

## Überblick
Die Manager müssen in `csNova_main.py` initialisiert und der `app_state` zur Verfügung gestellt werden.

## Schritt 1: Import hinzufügen (oben in der Datei)

```python
from csNova_start import initialize_all_managers
```

## Schritt 2: Initialisierung in der main()-Funktion

```python
def main():
    """Startet die CSNova Hauptanwendung."""
    
    # Initialisiere alle Manager
    managers = initialize_all_managers()
    if managers is None:
        log_error("Konnte Manager nicht initialisieren!")
        return
    
    # Erstelle die Qt-Anwendung
    app = QApplication.instance() or QApplication(sys.argv)
    
    # Weitere Initialisierung...
    
    # App-State mit Managern speichern
    app_state = {
        "managers": managers,
        "references": managers.get("references"),
        "citations": managers.get("citations"),
        "projects": managers.get("projects"),
        "characters": managers.get("characters"),
        "locations": managers.get("locations"),
        "objects": managers.get("objects"),
        "storylines": managers.get("storylines"),
        "ideas": managers.get("ideas"),
        "chapters": managers.get("chapters"),
        # ... weitere State-Variablen
    }
```

## Schritt 3: Zugriff auf Manager aus UI-Funktionen

### Beispiel 1: Referenzen anzeigen
```python
def show_references_window(app_state):
    """Zeigt das Referenzen-Fenster."""
    ref_manager = app_state["references"]
    all_refs = ref_manager.get_all()
    
    for ref_id, reference in all_refs.items():
        print(f"{ref_id}: {reference.get('title', 'Untitled')}")
```

### Beispiel 2: Neue Referenz hinzufügen
```python
def add_reference(app_state, reference_data):
    """Fügt eine neue Referenz hinzu."""
    ref_manager = app_state["references"]
    new_id = ref_manager.add(reference_data)
    return new_id
```

### Beispiel 3: Charaktere filtern
```python
def get_main_characters(app_state):
    """Ruft nur Hauptcharaktere ab."""
    char_manager = app_state["characters"]
    return char_manager.get_main_characters()
```

### Beispiel 4: Zitat generieren
```python
def generate_citation(app_state, reference_id, format_style="APA"):
    """Generiert ein Zitat für eine Referenz."""
    ref_manager = app_state["references"]
    cite_manager = app_state["citations"]
    
    reference = ref_manager.get(reference_id)
    if reference:
        return cite_manager.get_citation(reference, format_style)
    return None
```

## Schritt 4: Änderungen speichern

Alle Manager speichern Änderungen automatisch:

```python
# Daten werden automatisch gespeichert beim:
ref_manager.add(new_reference)
ref_manager.delete(reference_id)
```

Manuelles Speichern ist selten nötig:
```python
# Nur wenn direkt mit self.data manipuliert
manager.save()
```

## Vollständiger Integration-Template

```python
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from csNova_start import initialize_all_managers
from core.logger import log_info, log_error, log_header

class CSNovaApp:
    """Hauptanwendungsklasse für CSNova."""
    
    def __init__(self):
        """Initialisiert die Anwendung."""
        self.managers = initialize_all_managers()
        if self.managers is None:
            log_error("Manager-Initialisierung fehlgeschlagen!")
            sys.exit(1)
        
        self.app_state = {
            "managers": self.managers,
            "references": self.managers.get("references"),
            "citations": self.managers.get("citations"),
            "projects": self.managers.get("projects"),
            "characters": self.managers.get("characters"),
            "locations": self.managers.get("locations"),
            "objects": self.managers.get("objects"),
            "storylines": self.managers.get("storylines"),
            "ideas": self.managers.get("ideas"),
            "chapters": self.managers.get("chapters"),
        }
    
    def get_references(self):
        """Gibt alle Referenzen zurück."""
        return self.app_state["references"].get_all()
    
    def get_characters(self):
        """Gibt alle Charaktere zurück."""
        return self.app_state["characters"].get_all()
    
    def get_projects(self):
        """Gibt alle Projekte zurück."""
        return self.app_state["projects"].get_all()
    
    def run(self):
        """Startet die GUI."""
        qt_app = QApplication.instance() or QApplication(sys.argv)
        # ... weitere GUI-Initialisierung
        qt_app.exec()

if __name__ == "__main__":
    app = CSNovaApp()
    app.run()
```

## Testing der Integration

```bash
# Test: Alle Manager laden
python3 -c "from csNova_start import initialize_all_managers; m = initialize_all_managers(); print('✓ OK' if m else '✗ FAILED')"

# Test: Spezifischen Manager testen
python3 -c "from csNova_start import initialize_all_managers; m = initialize_all_managers(); print(f'Charaktere: {len(m[\"characters\"].get_all())}')"
```

# Phase 6 - Quick Reference Card

## 🎯 Die 5 UI-Fenster auf einen Blick

| Funktion | Zeile | UI-Datei | Manager | Komplexität | Zeit |
|----------|-------|----------|---------|-------------|------|
| **show_locations_window()** | 2300 | csNova_Locations.ui | locations | ⭐ EINFACH | 20m |
| **show_storylines_window()** | 2432 | csNova_Storylines.ui | storylines | ⭐ EINFACH | 20m |
| **show_references_window()** | 3221 | csNova.ui | references + citations | 🔸 MITTEL | 45m |
| **show_projects_window()** | 1775 | csNova_Projects.ui | projects | 🔴 KOMPLEX | 35m |
| **show_characters_window()** | 1958 | csNova_Characters.ui | characters | 🔴 SEHR KOMPLEX | 40m |

---

## 📋 Standard-Implementierungs-Checkliste

Für JEDES Fenster diese Punkte abhaken:

```python
# 1. Import
from csNova_main import app_state

# 2. Manager abrufen
manager = app_state.references  # oder other manager

# 3. Daten laden
all_data = manager.get_all()  # Dict[str, Dict]

# 4. Tabelle füllen
for item_id, item in all_data.items():
    row = table.rowCount()
    table.insertRow(row)
    table.setItem(row, 0, QTableWidgetItem(item_id))
    table.setItem(row, 1, QTableWidgetItem(item.get("title", "")))
    # ... weitere Spalten

# 5. Add-Button
def add_item():
    new_id = manager.add({
        "title": form.titleField.text(),
        "description": form.descField.toPlainText(),
        # ... weitere Felder
    })
    refresh_table()

# 6. Delete-Button
def delete_item():
    if confirm("Wirklich löschen?"):
        manager.delete(selected_id)
        refresh_table()

# 7. Refresh-Funktion
def refresh_table():
    table.setRowCount(0)
    all_data = manager.get_all()
    # ... wieder füllen (Punkt 4)

# 8. Error Handling
try:
    # ... Code
except Exception as e:
    log_error(f"Fehler: {e}")
    show_error_dialog(str(e))
```

---

## 🔥 Manager-API Quick Reference

### ReferenceManager (Zeile 3221)
```python
ref_manager = app_state.references
all_refs = ref_manager.get_all()           # Dict[str, Dict]
new_id = ref_manager.add(data_dict)        # str
ref_manager.delete(ref_id)                 # bool
errors = ref_manager.validate_all()        # List[str]
dups = ref_manager.check_duplicates()      # Dict[str, List[str]]
```

**Spezial: CitationManager**
```python
cite_manager = app_state.citations
formats = cite_manager.list_supported_formats()  # List[str]
citation = cite_manager.get_citation(ref_id, format)  # str
```

### CharacterManager (Zeile 1958)
```python
char_manager = app_state.characters
all_chars = char_manager.get_all()          # Dict[str, Dict]
new_id = char_manager.add(data_dict)        # str
char_manager.delete(char_id)                # bool
main_chars = char_manager.get_main_characters()  # List[str]
```

### ProjectManager (Zeile 1775)
```python
proj_manager = app_state.projects
all_projects = proj_manager.get_all()       # Dict[str, Dict]
new_id = proj_manager.add(data_dict)        # str
proj_manager.delete(proj_id)                # bool
```

### LocationManager (Zeile 2300)
```python
loc_manager = app_state.locations
all_locations = loc_manager.get_all()       # Dict[str, Dict]
new_id = loc_manager.add(data_dict)         # str
loc_manager.delete(loc_id)                  # bool
```

### StorylineManager (Zeile 2432)
```python
story_manager = app_state.storylines
all_stories = story_manager.get_all()       # Dict[str, Dict]
new_id = story_manager.add(data_dict)       # str
story_manager.delete(story_id)              # bool
```

---

## 🎨 Widget-Namen pro Fenster

### [2.1] show_locations_window()
- `titleLocations` (QLineEdit)
- `dateEditCreatedLocations`, `dateEditEditedLocations` (QDateEdit)
- `comboBoxLocationsStatus` (QComboBox)
- `textDescriptionLocations` (QTextEdit)
- Buttons: `newBtnLocations`, `deleteBtnLocations`, `saveBtnLocations`, `exitBtnLocations`

### [2.2] show_storylines_window()
- `titleStorylines` (QLineEdit)
- `dateEditCreatedStorylines`, `dateEditEditedStorylines` (QDateEdit)
- `comboBoxStorylinesStatus` (QComboBox)
- `textDescriptionStorylines` (QTextEdit)
- Buttons: `newBtnStorylines`, `deleteBtnStorylines`, `saveBtnStorylines`, `exitBtnStorylines`

### [1.1] show_references_window()
- Dialog mit QTableWidget für Referenzenliste
- Felder: type, title, authors, year, source
- **CitationManager** für Zitierformate!
- Spezial-Buttons: validate, duplicates, citation format

### [1.3] show_projects_window()
- `titleProjects` (QLineEdit)
- `comboBoxProjectsGenre`, `comboBoxProjectsStatus` (QComboBox)
- `wordCountProjects` (QSpinBox)
- `textDescriptionProjects` (QTextEdit)
- Buttons: `newBtnProjects`, `deleteBtnProjects`, `saveBtnProjects`, `exitBtnProjects`

### [1.2] show_characters_window()
- `titleCharacter`, `characterName` (QLineEdit)
- `gender`, `bodyType`, `faceShape`, `eyeShape`, `status` (QComboBox) - VIELE!
- `age`, `height`, `weight` (QSpinBox)
- `textDescriptionCharacter`, `biography` (QTextEdit)
- Buttons: `newBtnCharacter`, `deleteBtnCharacter`, `saveBtnCharacter`, `exitBtnCharacter`

---

## ⚡ Code-Template (Kopier-Paste Ready)

### Minimal Template für einfache Fenster (Orte, Handlung)
```python
def show_locations_window(parent=None):
    """Fenster für Standorte/Schauplätze."""
    try:
        from csNova_main import app_state
        
        # Manager abrufen
        loc_manager = app_state.locations
        
        # Dialog erstellen
        dialog = QMainWindow()
        dialog.setWindowTitle("csNova - Handlungsorte")
        
        # Daten laden
        all_locations = loc_manager.get_all()
        
        # UI füllen
        for loc_id, loc_data in all_locations.items():
            # ... Widget befüllen
            pass
        
        # Buttons verbinden
        dialog.newBtn.clicked.connect(lambda: add_location(loc_manager, dialog))
        dialog.deleteBtn.clicked.connect(lambda: delete_location(loc_manager, dialog))
        dialog.saveBtn.clicked.connect(lambda: save_location(loc_manager, dialog))
        
        dialog.exec()
        
    except Exception as e:
        log_error(f"Fehler in show_locations_window: {e}")
        QMessageBox.critical(None, "Fehler", str(e))

def add_location(manager, dialog):
    """Neuen Standort hinzufügen."""
    try:
        data = {
            "title": dialog.titleLocations.text(),
            "status": dialog.comboBoxLocationsStatus.currentText(),
            "description": dialog.textDescriptionLocations.toPlainText(),
        }
        new_id = manager.add(data)
        log_info(f"Standort hinzugefügt: {new_id}")
        refresh_locations_table(manager, dialog)
    except Exception as e:
        log_error(f"Fehler beim Hinzufügen: {e}")

def delete_location(manager, dialog):
    """Standort löschen."""
    try:
        reply = QMessageBox.question(dialog, "Bestätigung", 
                                     "Standort wirklich löschen?")
        if reply == QMessageBox.Yes:
            manager.delete(selected_id)
            log_info(f"Standort gelöscht: {selected_id}")
            refresh_locations_table(manager, dialog)
    except Exception as e:
        log_error(f"Fehler beim Löschen: {e}")

def refresh_locations_table(manager, dialog):
    """Tabelle aktualisieren."""
    dialog.table.setRowCount(0)
    all_locations = manager.get_all()
    for loc_id, loc_data in all_locations.items():
        row = dialog.table.rowCount()
        dialog.table.insertRow(row)
        dialog.table.setItem(row, 0, QTableWidgetItem(loc_id))
        dialog.table.setItem(row, 1, QTableWidgetItem(loc_data.get("title", "")))
```

---

## 🚀 Empfohlene Reihenfolge

**LEICHT ANFANGEN:**
1. ✅ show_locations_window() - 20 Min - Nur 7 Felder
2. ✅ show_storylines_window() - 20 Min - Nur 7 Felder

**DANN MITTELSCHWER:**
3. ✅ show_references_window() - 45 Min - CitationManager!

**DANN KOMPLEX:**
4. ✅ show_projects_window() - 35 Min - Viele Felder
5. ✅ show_characters_window() - 40 Min - 90 Felder!

**TOTAL: ~160 Min = 2,5 Stunden**

---

## ✅ Erfolgs-Kriterien

Pro Fenster fertig wenn:
- [ ] Manager wird genutzt (nicht direkt JSON)
- [ ] Add/Delete/Save funktionieren
- [ ] Tabelle/UI wird mit echten Daten gefüllt
- [ ] UI aktualisiert sich nach Änderungen
- [ ] Fehlerbehandlung vorhanden
- [ ] Getestet mit mindestens 3 Einträgen
- [ ] Bestätigung vor Delete
- [ ] Log-Meldungen vorhanden

---

## 🔗 Verwandte Dateien

- **PHASE6_CHECKLIST_UPDATED.md** - Ausführliche Checkliste mit Details
- **PHASE6_UI_INTEGRATION_PLAN.md** - Detaillierter Plan mit Code-Templates
- **UI_INTEGRATION.md** - API-Referenz
- **ui_integration_examples.py** - 7 funktionierende Beispiele

---

## 💡 Tipps & Tricks

### Widget nach Namen finden
```python
# In Designer definierten Widget-Namen nutzen
widget = self.ui.widgetName
# oder
widget = dialog.findChild(QLineEdit, "titleLocations")
```

### Daten zwischen Widgets synchronisieren
```python
# Form-Felder von Manager-Daten füllen
data = manager.get(item_id)
form.titleField.setText(data.get("title", ""))
form.descField.setPlainText(data.get("description", ""))
```

### Fehlerbehandlung
```python
try:
    result = manager.add(data)
    log_info(f"Erfolgreich: {result}")
except KeyError as e:
    log_error(f"Feld fehlt: {e}")
except Exception as e:
    log_error(f"Unbekannter Fehler: {e}")
```

### Bestätigung vor gefährlichen Operationen
```python
from PySide6.QtWidgets import QMessageBox

reply = QMessageBox.question(
    self, 
    "Bestätigung", 
    "Wirklich löschen?",
    QMessageBox.Yes | QMessageBox.No
)
if reply == QMessageBox.Yes:
    # löschen
```

---

## 🆘 Wenn etwas nicht funktioniert

1. **Überprüfe Widget-Namen** - Müssen exakt wie in UI-Datei sein
2. **Überprüfe Manager-Name** - `app_state.references`, `app_state.characters`, etc.
3. **Überprüfe Datentypen** - Manager erwartet Dict, nicht List
4. **Überprüfe Exception** - `try-except` und Log-Meldung lesen
5. **Überprüfe Test-Daten** - Sind überhaupt Daten in der JSON-Datei?
6. **Konsole anschauen** - Fehler-Meldungen ausgeben

---

**Viel Erfolg mit Phase 6! 🎯**

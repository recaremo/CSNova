# Phase 6: UI-Fenster Integration - Detaillierter Action Plan

## 🎯 Ziel: Update aller UI-Fenster für Manager-Integration

Konvertiere die 5 wichtigsten UI-Fenster vom alten direkten Dateizugriff zu den neuen Managern.

---

## 📋 Schritt-für-Schritt Anleitung

### SCHRITT 1: show_references_window() - Referenzen anzeigen

**Datei**: `csNova_main.py` (Zeile 3221)

**Was ändern:**
- ✅ Tabelle mit echten Daten füllen (statt leer)
- ✅ "Referenz hinzufügen" Button funktional
- ✅ "Löschen" Button funktional
- ✅ "Validieren" Button funktional
- ✅ "Duplikate prüfen" Button funktional
- ✅ Zitate generieren

**Code-Template:**
```python
def show_references_window(parent=None):
    """Referenz-Verwaltung mit neuen Managern."""
    from csNova_main import app_state
    from core.logger import log_info, log_error
    
    dialog = QDialog(parent)
    # ... UI Setup ...
    
    # WICHTIG: Daten laden
    ref_manager = app_state.references
    all_refs = ref_manager.get_all()
    
    # Tabelle füllen
    for idx, (ref_id, ref) in enumerate(all_refs.items()):
        table.setItem(idx, 0, QTableWidgetItem(ref_id))
        table.setItem(idx, 1, QTableWidgetItem(ref.get("type", "")))
        table.setItem(idx, 2, QTableWidgetItem(ref.get("title", "")))
        # ... weitere Felder
    
    # Button-Funktionen verbinden
    add_btn.clicked.connect(lambda: add_reference(ref_manager, table))
    delete_btn.clicked.connect(lambda: delete_reference(ref_manager, table))
    validate_btn.clicked.connect(lambda: validate_all_references(ref_manager))
    duplicate_btn.clicked.connect(lambda: check_duplicates(ref_manager))
    
    # Zitat-Generierung
    def generate_citation():
        cite_manager = app_state.citations
        selected_row = table.currentRow()
        if selected_row >= 0:
            ref_id = table.item(selected_row, 0).text()
            ref = ref_manager.get(ref_id)
            fmt = citation_format.currentText()
            citation = cite_manager.get_citation(ref, fmt)
            citation_text.setText(citation)
    
    table.itemSelectionChanged.connect(generate_citation)
    citation_format.currentTextChanged.connect(generate_citation)
    
    dialog.exec()
    return dialog
```

**Unterfunktionen zu implementieren:**
```python
def add_reference(ref_manager, table):
    """Dialog zum Hinzufügen neuer Referenz."""
    # Formular für Referenzdaten
    # Speichern mit ref_manager.add()
    pass

def delete_reference(ref_manager, table):
    """Löscht ausgewählte Referenz."""
    # Bestätigung
    # ref_manager.delete(ref_id)
    # Tabelle aktualisieren
    pass

def validate_all_references(ref_manager):
    """Validiert alle Referenzen."""
    errors = ref_manager.validate_all()
    # Zeige Fehlerbericht
    pass

def check_duplicates(ref_manager):
    """Prüft auf doppelte Referenzen."""
    duplicates = ref_manager.check_duplicates()
    # Zeige Duplikate
    pass
```

---

### SCHRITT 2: show_characters_window() - Charaktere verwalten

**Datei**: `csNova_main.py` (suche nach der Funktion)

**Was ändern:**
- ✅ Charakterliste laden und anzeigen
- ✅ Charaktere filtern (nach Name, Rolle, etc.)
- ✅ Nur Hauptcharaktere zeigen (Option)
- ✅ Neuen Charakter hinzufügen
- ✅ Charakter löschen
- ✅ Charakter-Details bearbeiten

**Code-Template:**
```python
def show_characters_window(parent=None):
    """Charaktere-Verwaltung mit Manager."""
    from csNova_main import app_state
    
    char_manager = app_state.characters
    
    # Filter für Charaktere
    filter_input = QLineEdit()
    main_only_checkbox = QCheckBox("Nur Hauptcharaktere")
    
    def load_characters():
        all_chars = char_manager.get_all()
        
        # Optional: Filter anwenden
        filter_text = filter_input.text().lower()
        main_only = main_only_checkbox.isChecked()
        
        filtered_chars = {}
        for char_id, char in all_chars.items():
            name = char.get("character_name", "").lower()
            is_main = char.get("character_mainCharacter", False)
            
            if filter_text and filter_text not in name:
                continue
            if main_only and not is_main:
                continue
            
            filtered_chars[char_id] = char
        
        # Tabelle/Liste aktualisieren
        for idx, (char_id, char) in enumerate(filtered_chars.items()):
            # Anzeigen im UI
            pass
        
        return filtered_chars
    
    # Filter-Events verbinden
    filter_input.textChanged.connect(load_characters)
    main_only_checkbox.stateChanged.connect(load_characters)
    
    # Buttons
    add_btn.clicked.connect(lambda: add_character(char_manager))
    delete_btn.clicked.connect(lambda: delete_character(char_manager, char_list))
    
    # Initial laden
    load_characters()
    
    dialog.exec()
```

**Unterfunktionen:**
```python
def add_character(char_manager):
    """Dialog für neuen Charakter."""
    # Form mit 90+ Charakter-Feldern (vereinfacht)
    pass

def delete_character(char_manager, char_list):
    """Löscht einen Charakter."""
    pass
```

---

### SCHRITT 3: show_projects_window() - Projekte verwalten

**Was ändern:**
- ✅ Projektliste laden
- ✅ Neues Projekt erstellen
- ✅ Projekt-Details bearbeiten
- ✅ Projekt löschen

**Code-Template:**
```python
def show_projects_window(parent=None):
    """Projekte-Verwaltung mit Manager."""
    from csNova_main import app_state
    
    proj_manager = app_state.projects
    
    # Liste aller Projekte laden
    all_projects = proj_manager.get_all()
    
    # Tabelle füllen mit:
    # - project_title
    # - project_author
    # - project_status
    # - project_word_goal
    # - project_deadline
    
    # Buttons verbinden
    add_btn.clicked.connect(lambda: add_project(proj_manager))
    edit_btn.clicked.connect(lambda: edit_project(proj_manager, table))
    delete_btn.clicked.connect(lambda: delete_project(proj_manager, table))
```

---

### SCHRITT 4: show_locations_window() / show_objects_window() - Einfache Listen

**Was ändern:**
- ✅ Daten laden über LocationManager / ObjectManager
- ✅ Add / Delete implementieren
- ✅ Einfaches Bearbeitungs-Formular

**Code-Template:**
```python
def show_locations_window(parent=None):
    """Schauplätze-Verwaltung."""
    from csNova_main import app_state
    
    loc_manager = app_state.locations
    
    # Lade alle Schauplätze
    all_locations = loc_manager.get_all()
    
    # Zeige in Liste/Tabelle
    for loc_id, loc in all_locations.items():
        # loc_id
        # location_title
        # location_status
        # location_created
        # location_modified
        pass
    
    # Buttons für Add/Delete/Edit
```

---

### SCHRITT 5: show_storylines_window() - Handlungsstränge

**Was ändern:**
- ✅ StorylineManager Integration
- ✅ Handlungsstränge auflisten
- ✅ Verknüpfung mit Szenen
- ✅ Add/Delete implementieren

---

## 🔄 Übergeordneter Workflow

### Für JEDES Fenster:

1. **Manager abrufen:**
   ```python
   manager = app_state.references  # oder characters, projects, etc.
   ```

2. **Daten laden:**
   ```python
   all_data = manager.get_all()
   ```

3. **UI füllen:**
   ```python
   for item_id, item in all_data.items():
       # Zeige in Tabelle/Liste
   ```

4. **Add-Funktion:**
   ```python
   new_id = manager.add(form_data)
   # UI aktualisieren
   ```

5. **Delete-Funktion:**
   ```python
   manager.delete(item_id)
   # UI aktualisieren
   ```

---

## 📚 Hilfsfunktionen (reusable)

Diese Funktionen kannst du für mehrere Fenster verwenden:

```python
def refresh_table(manager, table):
    """Aktualisiert eine Tabelle mit Manager-Daten."""
    all_items = manager.get_all()
    table.setRowCount(len(all_items))
    
    for idx, (item_id, item) in enumerate(all_items.items()):
        # Tabelle füllen
        pass

def get_selected_id(table):
    """Holt die ID der ausgewählten Zeile."""
    row = table.currentRow()
    if row >= 0:
        return table.item(row, 0).text()
    return None

def show_message_box(title, message, icon=QMessageBox.Information):
    """Zeigt einfache Nachricht."""
    box = QMessageBox()
    box.setWindowTitle(title)
    box.setText(message)
    box.setIcon(icon)
    box.exec()

def show_confirmation(title, message):
    """Fragt um Bestätigung."""
    box = QMessageBox()
    box.setWindowTitle(title)
    box.setText(message)
    box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    return box.exec() == QMessageBox.Yes
```

---

## 🎬 Reihenfolge zum Abarbeiten

### Priority 1 (Wichtigste):
1. ✅ **show_references_window()** - Schon teilweise vorhanden, nur vervollständigen
2. ✅ **show_characters_window()** - Mit Filter-Logik
3. ✅ **show_projects_window()** - Hauptdatentyp

### Priority 2 (Wichtig):
4. ✅ **show_locations_window()**
5. ✅ **show_storylines_window()**

### Priority 3 (Optional):
6. ⭕ **show_objects_window()**
7. ⭕ **show_ideas_window()**
8. ⭕ **show_chapters_window()** (komplexer - mit Szenen)

---

## 💡 Tipps

### DO's:
- ✅ Immer `app_state.manager_name` verwenden
- ✅ Manager-Methoden nutzen (add, delete, get_all)
- ✅ UI nach Änderungen aktualisieren
- ✅ Fehler abfangen und zeigen
- ✅ Bestätigungen für Löschungen

### DON'Ts:
- ❌ Keine direkten JSON-Operationen mehr
- ❌ Nicht auf alte `ref_manager`/`cite_manager` verlassen
- ❌ Keine fehlende Fehlerbehandlung
- ❌ UI nicht nach add/delete aktualisieren

---

## ✅ Abnahme-Kriterien für Phase 6

Ein Fenster ist fertig, wenn:

- [ ] Manager-Daten werden geladen und angezeigt
- [ ] Add-Funktion funktioniert
- [ ] Delete-Funktion funktioniert (mit Bestätigung)
- [ ] UI wird nach Änderung aktualisiert
- [ ] Fehlerbehandlung vorhanden
- [ ] Keine Hardcoded-Daten mehr
- [ ] Tests mit realen Daten funktionieren

---

## 🚀 Nach Phase 6

- Phase 7: Advanced Features (Suche, Filter, Batch-Ops)
- Phase 8: Optimierungen (Caching, Lazy Loading)
- Phase 9: GUI Testing mit PySide6

---

## 📞 Support

Falls bei der Implementierung Fragen auftreten:
- Siehe: `UI_INTEGRATION.md` - Detaillierte API-Referenz
- Siehe: `ui_integration_examples.py` - Code-Beispiele
- Siehe: `INTEGRATION_GUIDE.md` - Manager-Dokumentation

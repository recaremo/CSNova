# UI Integration Guide für CSNova Manager

## Übersicht

Nach der erfolgreichen Integration sind alle 9 Manager über das globale `app_state` Objekt in csNova_main.py verfügbar.

## app_state Struktur

```python
# In csNova_main.py
app_state = CSNovaApp()

# Nach Initialisierung stehen folgende Manager zur Verfügung:
app_state.references    # ReferenceManager
app_state.citations     # CitationManager
app_state.projects      # ProjectManager
app_state.characters    # CharacterManager
app_state.locations     # LocationManager
app_state.objects       # ObjectManager
app_state.storylines    # StorylineManager
app_state.ideas         # IdeaManager
app_state.chapters      # ChapterManager

# Backwards Compatibility
app_state.ref_manager   # = references
app_state.cite_manager  # = citations
```

## Zugriff auf Manager aus UI-Funktionen

### 1. Referenzen anzeigen

```python
def show_references_window():
    """Zeigt Referenzen-Verwaltung."""
    ref_manager = app_state.references
    
    all_references = ref_manager.get_all()
    for ref_id, ref in all_references.items():
        title = ref.get('title', 'Untitled')
        authors = ref.get('authors', [])
        # ... Anzeige in UI
```

### 2. Charaktere filtern

```python
def show_main_characters():
    """Zeigt nur Hauptcharaktere."""
    char_manager = app_state.characters
    
    main_chars = char_manager.get_main_characters()
    for char_id, char in main_chars.items():
        name = char.get('character_name', '')
        # ... Anzeige in UI
```

### 3. Neue Referenz hinzufügen

```python
def add_new_reference_from_form(form_data):
    """Fügt neue Referenz aus Formular hinzu."""
    ref_manager = app_state.references
    
    new_reference = {
        "type": form_data["ref_type"],
        "title": form_data["title"],
        "authors": form_data["authors"],
        # ... weitere Felder
    }
    
    ref_id = ref_manager.add(new_reference)
    return ref_id
```

### 4. Projekt aktualisieren

```python
def update_project(project_id, project_data):
    """Aktualisiert ein Projekt."""
    project_manager = app_state.projects
    
    # Lade aktuelles Projekt
    current = project_manager.get(project_id)
    
    # Aktualisiere Felder
    current.update(project_data)
    
    # Speichere
    project_manager.data[project_id] = current
    project_manager.save()
```

### 5. Charakter löschen

```python
def delete_character(char_id):
    """Löscht einen Charakter."""
    char_manager = app_state.characters
    
    success = char_manager.delete(char_id)
    if success:
        log_info(f"Charakter {char_id} gelöscht")
    else:
        log_error(f"Konnte Charakter {char_id} nicht löschen")
    
    return success
```

### 6. Zitat generieren

```python
def generate_citation(ref_id, format_style="APA"):
    """Generiert ein Zitat."""
    ref_manager = app_state.references
    cite_manager = app_state.citations
    
    reference = ref_manager.get(ref_id)
    if not reference:
        return None
    
    citation = cite_manager.get_citation(reference, format_style)
    return citation
```

### 7. Alle Ideen auflisten

```python
def show_ideas():
    """Zeigt alle Ideen."""
    idea_manager = app_state.ideas
    
    all_ideas = idea_manager.get_all()
    for idea_id, idea in all_ideas.items():
        title = idea.get('title', '')
        description = idea.get('description', '')
        # ... Anzeige in UI
```

### 8. Szenen eines Kapitels

```python
def get_chapter_scenes(chapter_id):
    """Ruft alle Szenen eines Kapitels ab."""
    chapter_manager = app_state.chapters
    
    chapter = chapter_manager.get(chapter_id)
    if chapter:
        # Hinweis: Szenen sind verschachtelt in den Kapiteln
        # Struktur: chapter["scenes"] = [...]
        return chapter.get('scenes', [])
    
    return []
```

## Integration in bestehende UI-Funktionen

### Beispiel: show_references_window() aktualisieren

**Vorher:**
```python
def show_references_window():
    # Alte Logik mit direktem Dateizugriff
    with open("data/references/data_references.json") as f:
        references = json.load(f)
```

**Nachher:**
```python
def show_references_window():
    # Neue Logik mit Manager
    ref_manager = app_state.references
    references = ref_manager.get_all()
```

## Best Practices

### ✅ DO:
- Immer über app_state auf Manager zugreifen
- manager.get_all() für alle Daten verwenden
- manager.add() / manager.delete() / manager.save() verwenden
- Auto-Speichern funktioniert automatisch
- Type Hints verwenden für bessere IDE-Unterstützung

### ❌ DON'T:
- Direkten Dateizugriff mit open() nicht mehr verwenden
- Nicht directly in JSON-Dateien schreiben
- Nicht auf alte ref_manager/cite_manager Attribute verlassen (sind nur für Backwards Compatibility)

## Fehlerbehandlung

```python
def safe_get_reference(ref_id):
    """Sichere Referenz-Abrufe."""
    try:
        ref_manager = app_state.references
        if ref_manager is None:
            log_error("ReferenceManager nicht initialisiert")
            return None
        
        reference = ref_manager.get(ref_id)
        if reference is None:
            log_error(f"Referenz {ref_id} nicht gefunden")
            return None
        
        return reference
    
    except Exception as e:
        log_error(f"Fehler beim Abruf von Referenz {ref_id}: {e}")
        return None
```

## Manager-API Referenz

### Alle Manager bieten:
```python
manager.load()                  # Lade Daten
manager.save()                  # Speichere Daten
manager.ensure_structure()      # Erstelle Datei falls nicht vorhanden
manager.auto_complete_keys()    # Ergänze fehlende Felder

manager.get_all()               # Alle Einträge als Dictionary
manager.get(entry_id)           # Einzelnen Eintrag abrufen
manager.add(entry_data)         # Neuen Eintrag hinzufügen
manager.delete(entry_id)        # Eintrag löschen
```

### Spezial-Methoden:

**ReferenceManager:**
```python
manager.validate_all()          # Validiere alle Referenzen
manager.check_duplicates()      # Finde doppelte Referenzen
```

**CharacterManager:**
```python
manager.get_main_characters()   # Nur Hauptcharaktere
```

**CitationManager:**
```python
manager.list_supported_formats()    # Verfügbare Formate
manager.get_format_definition(fmt)  # Format-Definition
manager.get_citation(ref, fmt)      # Zitat generieren
```

## Nächste Schritte für Entwickler

1. **Schritt 1**: Finde alle `def show_*_window()` Funktionen
2. **Schritt 2**: Ersetze direkten Dateizugriff mit Manager-Aufrufen
3. **Schritt 3**: Teste jede Funktion mit den neuen Managern
4. **Schritt 4**: Aktualisiere Fehlerbehandlung
5. **Schritt 5**: Dokumentiere Custom Logic

## Testing

```bash
# Test einzelner Manager-Zugriff
python3 -c "
from csNova_main import app_state
import csNova_start

managers = csNova_start.initialize_all_managers()
app_state.references = managers['references']

# Test Zugriff
print(f'Referenzen: {len(app_state.references.get_all())}')
"
```

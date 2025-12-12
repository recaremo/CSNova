# Phase 6 Abarbeitungs-Checkliste - MIT UI-ANALYSE

## 🎯 Ziel
Update der 5 wichtigsten UI-Fenster zur Verwendung der neuen Manager statt direktem Dateizugriff.

**Basis-UI-Struktur**: Alle Fenster verwenden QSplitter mit 3-teiligem Layout:
- **Links**: Help-Text (QTextEdit, read-only)
- **Mitte**: Formular + Tabelle/Liste
- **Rechts**: Buttons (New, Next, Previous, Delete, Save, Exit)

---

## ✅ TODO PRIORITÄT 1 - MUSS IMPLEMENTIERT WERDEN

### [1.1] show_references_window() - Referenzen ⭐
- **Datei**: [csNova_main.py](csNova_main.py#L3221) Zeile 3221
- **UI-Datei**: gui/csNova.ui (in csNova_main geladen)
- **Manager**: app_state.references + app_state.citations
- **Status**: ⭕ TODO
- **Besonderheit**: Verwendet CitationManager für Zitierformate!

**Wichtigste Widgets im Formular**:
```
Left Panel (Help):
├─ textEditHelpcsNovaMain (read-only Help-Text)

Right Panel (Buttons):
├─ newBtnReferences → add_reference()
├─ deleteBtnReferences → delete_reference()
├─ saveBtnReferences → save_reference()
├─ exitBtnReferences → close()
```

**Aufgaben**:
- [ ] Manager-Instanzen abrufen:
  ```python
  from csNova_main import app_state
  ref_manager = app_state.references
  cite_manager = app_state.citations
  ```

- [ ] Referenzenliste laden: `all_refs = ref_manager.get_all()`
- [ ] Tabelle mit Spalten: ID | Typ | Titel | Autoren | Jahr | Quelle
- [ ] Jede Zeile: `table.setItem(row, 0, QTableWidgetItem(ref["id"]))`
  
- [ ] Add-Referenz-Dialog:
  ```python
  new_id = ref_manager.add({
      "type": form.comboBoxRefType.currentText(),
      "title": form.titleReferences.text(),
      "authors": form.authorsReferences.text(),
      "year": form.yearReferences.text(),
      "source": form.sourceReferences.text(),
      # ... weitere Felder
  })
  refresh_table()
  ```

- [ ] Delete mit Bestätigung:
  ```python
  if confirm("Referenz wirklich löschen?"):
      ref_manager.delete(selected_id)
      refresh_table()
  ```

- [ ] Validierungs-Button:
  ```python
  errors = ref_manager.validate_all()
  if errors:
      show_message(f"Fehler: {errors}")
  ```

- [ ] Duplikate-Check:
  ```python
  duplicates = ref_manager.check_duplicates()
  if duplicates:
      show_message(f"Duplikate gefunden: {duplicates}")
  ```

- [ ] Zitierformat-Wechsel mit CitationManager:
  ```python
  formats = cite_manager.list_supported_formats()  # APA, MLA, Chicago, etc.
  citation = cite_manager.get_citation(ref_id, selected_format)
  textEditCitation.setText(citation)
  ```

- [ ] Fehlerbehandlung: try-except, Log-Meldungen
- [ ] Testen: mindestens 3 Referenzen laden, add, delete, validate

**Geschätzte Zeit**: 45 Min
**Code-Vorlage**: PHASE6_UI_INTEGRATION_PLAN.md, SCHRITT 1
**Tests bestanden**: ❌

---

### [1.2] show_characters_window() - Charaktere
- **Datei**: [csNova_main.py](csNova_main.py#L1958) Zeile 1958
- **UI-Datei**: gui/csNova_Characters.ui (1. moderne Datei)
- **Manager**: app_state.characters
- **Status**: ⭕ TODO
- **Besonderheit**: Großes Formular mit ~90 Feldern (Body Type, Face Shape, Gender, etc.)

**Wichtigste Widgets**:
```
Left Panel (Help):
├─ textEditHelpCharacter (read-only)

Center Panel (Formular/Tabelle):
├─ QTableWidget für Charakterliste (ID, Name, Rolle)
├─ QLineEdit: titleCharacter, characterName
├─ QComboBox: gender, bodyType, faceShape, eyeShape, status
├─ QSpinBox: age, height, weight
├─ QDateEdit: dateEditCreated, dateEditEdited
├─ QTextEdit: textDescription, biography
├─ QLabel: characterImage (für Bilder)

Right Panel (Buttons):
├─ newBtnCharacter
├─ nextBtnCharacter
├─ previousBtnCharacter
├─ deleteBtnCharacter
├─ imageBtnCharacter (Charakterbild)
├─ saveBtnCharacter
├─ exitBtnCharacter
```

**Aufgaben**:
- [ ] Manager abrufen: `char_manager = app_state.characters`

- [ ] Charaktere laden: `all_chars = char_manager.get_all()`

- [ ] Tabelle mit 3 Spalten füllen:
  ```python
  for char_id, char_data in all_chars.items():
      table.setItem(row, 0, QTableWidgetItem(char_id))
      table.setItem(row, 1, QTableWidgetItem(char_data.get("character_name", "")))
      table.setItem(row, 2, QTableWidgetItem(char_data.get("character_role", "")))
  ```

- [ ] Filter nach Name implementieren:
  ```python
  search_text = filterLineEdit.text()
  for char_id, char_data in all_chars.items():
      if search_text.lower() in char_data.get("character_name", "").lower():
          # show this row
  ```

- [ ] Filter nach Hauptcharaktere (Checkbox):
  ```python
  if filterMainCharactersCheckBox.isChecked():
      main_chars = char_manager.get_main_characters()
      # nur diese anzeigen
  ```

- [ ] Add-Character-Dialog:
  ```python
  new_id = char_manager.add({
      "character_name": form.titleCharacter.text(),
      "character_role": form.roleCombo.currentText(),
      "gender": form.genderCombo.currentText(),
      "bodyType": form.bodyTypeCombo.currentText(),
      "age": form.ageSpinBox.value(),
      # ... weitere Felder
  })
  refresh_table()
  ```

- [ ] Delete mit Bestätigung
- [ ] Navigation (next/previous) durch Charaktere
- [ ] Formular mit aktuellen Daten füllen beim Klick auf Tabelleneintrag
- [ ] Fehlerbehandlung
- [ ] Testen: Filter, Add, Delete, verschiedene Charaktere

**Geschätzte Zeit**: 40 Min
**Code-Vorlage**: PHASE6_UI_INTEGRATION_PLAN.md, SCHRITT 2
**Tests bestanden**: ❌

---

### [1.3] show_projects_window() - Projekte
- **Datei**: [csNova_main.py](csNova_main.py#L1775) Zeile 1775
- **UI-Datei**: gui/csNova_Projects.ui (komplexe Struktur)
- **Manager**: app_state.projects
- **Status**: ⭕ TODO
- **Besonderheit**: Tabelle mit komplexem Projekt-Formular

**Wichtigste Widgets**:
```
Left Panel (Help):
├─ textEditProjects (Help-Text)

Center Panel (Tabelle + Formular):
├─ frameProjectsContainer
├─ QTableWidget: projectsTable (ID, Title, Genre, Status)
├─ QLineEdit: titleProjects, publisherProjects, translatorProjects
├─ QComboBox: comboBoxProjectsGenre, comboBoxProjectsStyle,
│             comboBoxProjectsWorkingType, comboBoxProjectsStatus
├─ QSpinBox: wordCountProjects
├─ QDateEdit: dateEditCreatedProjects, dateEditEditedProjects
├─ QTextEdit: textDescriptionProjects
├─ QLabel: projectImage

Right Panel (Buttons):
├─ newBtnProjects
├─ nextBtnProjects
├─ previousBtnProjects
├─ deleteBtnProjects
├─ imageBtnProjects
├─ saveBtnProjects
├─ exitBtnProjects
```

**Aufgaben**:
- [ ] Manager abrufen: `proj_manager = app_state.projects`

- [ ] Projekte laden: `all_projects = proj_manager.get_all()`

- [ ] Tabelle mit 4 Spalten füllen (ID | Titel | Genre | Status):
  ```python
  for proj_id, proj_data in all_projects.items():
      table.setItem(row, 0, QTableWidgetItem(proj_id))
      table.setItem(row, 1, QTableWidgetItem(proj_data.get("project_name", "")))
      table.setItem(row, 2, QTableWidgetItem(proj_data.get("genre", "")))
      table.setItem(row, 3, QTableWidgetItem(proj_data.get("status", "")))
  ```

- [ ] Add-Project-Dialog oder Inline-Formular:
  ```python
  new_id = proj_manager.add({
      "project_name": form.titleProjects.text(),
      "genre": form.comboBoxProjectsGenre.currentText(),
      "publisher": form.publisherProjects.text(),
      "status": form.comboBoxProjectsStatus.currentText(),
      "word_count": form.wordCountProjects.value(),
      "description": form.textDescriptionProjects.toPlainText(),
      # ... weitere Felder
  })
  refresh_table()
  ```

- [ ] Edit-Funktion (Daten in Formular laden beim Klick auf Zeile):
  ```python
  selected_proj = proj_manager.get(selected_id)
  form.titleProjects.setText(selected_proj.get("project_name", ""))
  form.comboBoxProjectsGenre.setCurrentText(selected_proj.get("genre", ""))
  # ... weitere Felder
  ```

- [ ] Delete mit Bestätigung
- [ ] Navigation (next/previous)
- [ ] Save aktueller Projekt-Daten
- [ ] Fehlerbehandlung
- [ ] Testen: mindestens 3 Projekte, Add, Delete, Edit

**Geschätzte Zeit**: 35 Min
**Code-Vorlage**: PHASE6_UI_INTEGRATION_PLAN.md, SCHRITT 3
**Tests bestanden**: ❌

---

## ✅ TODO PRIORITÄT 2 - SOLLTE IMPLEMENTIERT WERDEN

### [2.1] show_locations_window() - Schauplätze
- **Datei**: [csNova_main.py](csNova_main.py#L2300) Zeile 2300
- **UI-Datei**: gui/csNova_Locations.ui
- **Manager**: app_state.locations
- **Status**: ⭕ TODO
- **Struktur**: Standard 3-Panel Layout wie Objekte/Storylines

**Wichtigste Widgets**:
```
Center Panel:
├─ titleLocations (QLineEdit)
├─ dateEditCreatedLocations, dateEditEditedLocations
├─ comboBoxLocationsStatus
├─ textDescriptionLocations (QTextEdit)
├─ imageBtnLocations

Buttons:
├─ newBtnLocations, deleteBtnLocations, saveBtnLocations, exitBtnLocations
```

**Aufgaben**:
- [ ] Manager abrufen: `loc_manager = app_state.locations`
- [ ] Schauplätze laden und anzeigen
- [ ] Formular-Felder mit Daten füllen
- [ ] Add/Delete/Save implementieren
- [ ] UI aktualisieren nach Änderungen
- [ ] Fehlerbehandlung

**Geschätzte Zeit**: 20 Min
**Tests bestanden**: ❌

---

### [2.2] show_storylines_window() - Handlungsstränge
- **Datei**: [csNova_main.py](csNova_main.py#L2432) Zeile 2432
- **UI-Datei**: gui/csNova_Storylines.ui
- **Manager**: app_state.storylines
- **Status**: ⭕ TODO
- **Struktur**: Standard 3-Panel Layout

**Wichtigste Widgets**:
```
Center Panel:
├─ titleStorylines (QLineEdit)
├─ dateEditCreatedStorylines, dateEditEditedStorylines
├─ comboBoxStorylinesStatus
├─ textDescriptionStorylines (QTextEdit)
├─ imageBtnStorylines

Buttons:
├─ newBtnStorylines, deleteBtnStorylines, saveBtnStorylines, exitBtnStorylines
```

**Aufgaben**:
- [ ] Manager abrufen: `story_manager = app_state.storylines`
- [ ] Handlungsstränge laden und anzeigen
- [ ] Formular mit Daten füllen
- [ ] Add/Delete/Save implementieren
- [ ] UI aktualisieren nach Änderungen
- [ ] Fehlerbehandlung

**Geschätzte Zeit**: 20 Min
**Tests bestanden**: ❌

---

## ⭕ TODO PRIORITÄT 3 - OPTIONAL (SPÄTER)

### [3.1] show_objects_window() - Objekte
- **Datei**: [csNova_main.py](csNova_main.py#L2163) Zeile 2163
- **UI-Datei**: gui/csNova_Objects.ui
- **Manager**: app_state.objects
- **Status**: ⭕ OPTIONAL
- **Aufwand**: 30 Min

### [3.2] show_ideas_window() - Ideen
- **Status**: ⭕ OPTIONAL
- **Aufwand**: 20 Min (wenige Felder)

### [3.3] show_chapters_window() - Kapitel/Szenen
- **Status**: ⭕ OPTIONAL
- **Aufwand**: 60 Min (KOMPLEX! - Hierarchische Struktur)

---

## 📋 GENERISCHE AUFGABEN FÜR ALLE FENSTER

### Für jedes Fenster zu tun:
- [ ] Manager importieren und abrufen
- [ ] Daten mit manager.get_all() laden
- [ ] UI mit realen Daten füllen
- [ ] Add-Button funktional (manager.add())
- [ ] Delete-Button funktional (manager.delete()) mit Bestätigung
- [ ] Save-Button (manager.save(), falls nötig)
- [ ] UI nach Änderung aktualisieren (refresh_table())
- [ ] Fehlerbehandlung mit try-except
- [ ] Log-Meldungen für wichtige Operationen
- [ ] Mit realen Daten testen (mind. 3 Einträge)
- [ ] Keine Hardcoded-Werte mehr
- [ ] Keine direkten JSON-Operationen mehr

---

## 🧪 TESTING-CHECKLISTE

### Für show_references_window():
- [ ] Referenzenliste wird angezeigt (mindestens 3)
- [ ] "Add" - Neue Referenz wird gespeichert
- [ ] "Delete" - Referenz wird gelöscht (nach Bestätigung)
- [ ] "Validieren" - Validierungsergebnis wird angezeigt
- [ ] "Duplikate" - Duplikate werden erkannt
- [ ] Zitate - Format wechseln funktioniert (APA, MLA, Chicago, etc.)
- [ ] Tabelle - Aktualisiert sich nach Änderungen
- [ ] CitationManager wird korrekt genutzt

### Für show_characters_window():
- [ ] Charakterliste wird angezeigt
- [ ] Filter nach Name funktioniert (dynamisch)
- [ ] Filter nach Hauptcharaktere funktioniert (get_main_characters)
- [ ] "Add" - Neuer Charakter wird gespeichert
- [ ] "Delete" - Charakter wird gelöscht
- [ ] Formular - Alle ~90 Felder werden angezeigt
- [ ] Navigation - Next/Previous funktioniert
- [ ] Tabelle - Aktualisiert sich sofort

### Für show_projects_window():
- [ ] Projektliste wird angezeigt
- [ ] "Add" - Neues Projekt wird gespeichert
- [ ] "Delete" - Projekt wird gelöscht
- [ ] Projektdetails - Alle Felder werden angezeigt
- [ ] Tabelle - Aktualisiert sich nach Änderungen
- [ ] ComboBoxen - Genre, Style, WorkingType, Status funktionieren
- [ ] Word Count - wird korrekt gespeichert/angezeigt
- [ ] Daten werden in Manager gespeichert (nicht lokal)

### Für show_locations_window():
- [ ] Schauplätze werden angezeigt
- [ ] Add/Delete/Save funktioniert
- [ ] Status-ComboBox funktioniert
- [ ] Beschreibung wird gespeichert

### Für show_storylines_window():
- [ ] Handlungsstränge werden angezeigt
- [ ] Add/Delete/Save funktioniert
- [ ] Status-ComboBox funktioniert
- [ ] Beschreibung wird gespeichert

---

## 📚 RESSOURCEN

| Datei | Zweck |
|-------|-------|
| PHASE6_UI_INTEGRATION_PLAN.md | Detaillierter Plan mit Code-Templates |
| UI_INTEGRATION.md | API-Referenz für Manager |
| ui_integration_examples.py | 7 Beispiel-Funktionen |
| INTEGRATION_GUIDE.md | Manager-Grundlagen |
| PHASE6_CHECKLIST_UPDATED.md | Diese Datei (mit UI-Analyse) |

---

## 🚀 WORKFLOW PRO FENSTER

```
1. Plan lesen (5 Min)
   └─ Diese Checkliste
   └─ PHASE6_UI_INTEGRATION_PLAN.md, SCHRITT X

2. UI verstehen (3 Min)
   └─ UI-Datei in Designer öffnen
   └─ Widget-Namen notieren

3. Funktion finden (2 Min)
   └─ csNova_main.py, Zeile X

4. Code schreiben (20-30 Min)
   └─ Template kopieren
   └─ Manager-Aufrufe anpassen
   └─ Widget-Namen korrekt

5. Testen (10 Min)
   └─ Mit realen Daten testen
   └─ Add/Delete/Filter prüfen
   └─ Fehler beheben

6. Dokumentieren (2 Min)
   └─ Diese Checkliste aktualisieren
   └─ Haken setzen ✅
```

---

## 📊 FORTSCHRITT

```
PRIORITÄT 1 (MUSS):
[▯▯▯] [1.1] show_references_window()     0%
[▯▯▯] [1.2] show_characters_window()     0%
[▯▯▯] [1.3] show_projects_window()       0%

PRIORITÄT 2 (SOLLTE):
[▯▯▯] [2.1] show_locations_window()      0%
[▯▯▯] [2.2] show_storylines_window()     0%

PRIORITÄT 3 (OPTIONAL):
[▯▯▯] [3.1] show_objects_window()        0%
[▯▯▯] [3.2] show_ideas_window()          0%
[▯▯▯] [3.3] show_chapters_window()       0%

GESAMT-FORTSCHRITT: 0/8 = 0%
```

---

## 📝 NOTIZEN ZUR IMPLEMENTIERUNG

### Allgemein:
- **Import**: `from csNova_main import app_state`
- **Manager abrufen**: `manager = app_state.references` (oder other manager name)
- **Daten laden**: `all_data = manager.get_all()` → Dict[str, Dict]
- **Daten hinzufügen**: `new_id = manager.add(data_dict)` → str (ID)
- **Daten löschen**: `manager.delete(item_id)` → bool (Erfolg)
- **Daten speichern**: `manager.save()` → bool (Erfolg)

### Wichtig:
- ✅ Immer try-except verwenden
- ✅ UI aktualisieren nach Änderungen (refresh_table(), refresh_form())
- ✅ Bestätigung vor Delete
- ✅ Log-Meldungen für Debugging
- ✅ Mit realen Daten testen, nicht mit leeren Listen
- ✅ Manager-Methoden nutzen, nicht direkt auf JSON zugreifen
- ✅ Widgets korrekt mit dem Namen aus der UI-Datei referenzieren

### Fehler vermeiden:
- ❌ Keine hardcodierten Werte
- ❌ Keine direkten JSON-Operationen (json.load/dump)
- ❌ Keine globalen Variablen für Daten
- ❌ Keine blocking UI-Operationen (synchron ✅ ist OK für kleine Datenmengen)
- ❌ Nicht vergessen: `self.ui.widgetName` oder `self.findChild(...)` nutzen

---

## 🎯 ERFOLGS-KRITERIUM

Phase 6 ist erfolgreich abgeschlossen wenn:

✅ Priorität 1 (3 Fenster) vollständig implementiert
✅ Alle Fenster nutzen Manager statt direkter Dateizugriff
✅ Alle Tests bestanden
✅ Keine hardcodierten Daten mehr
✅ Fehlerbehandlung vorhanden
✅ Logging funktioniert
✅ Mit realen Daten getestet

**DANN:** Phase 7 (Advanced Features: Search, Filter, Batch Operations)

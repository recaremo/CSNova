# Phase 6 Abarbeitungs-Checkliste

## 🎯 Ziel
Update der 5 wichtigsten UI-Fenster zur Verwendung der neuen Manager statt direktem Dateizugriff.

---

## ✅ TODO PRIORITÄT 1 - MUSS IMPLEMENTIERT WERDEN

### [1.1] show_references_window() - Referenzen
- **Datei**: csNova_main.py, Zeile 3221
- **Status**: ⭕ TODO
- **Aufgaben**:
  - [ ] Manager-Instanz abrufen: `ref_manager = app_state.references`
  - [ ] Alle Referenzen laden: `all_refs = ref_manager.get_all()`
  - [ ] Tabelle mit echten Daten füllen (ID, Typ, Titel, Autoren, Jahr)
  - [ ] "Add" Button - `add_reference()` Funktion implementieren
  - [ ] "Delete" Button - `delete_reference()` Funktion implementieren
  - [ ] "Validieren" Button - `validate_all_references()` Funktion
  - [ ] "Duplikate" Button - `check_duplicates()` Funktion
  - [ ] Zitierformat wechseln - `generate_citation()` mit CitationManager
  - [ ] Tabelle aktualisieren nach Add/Delete
  - [ ] Fehlerbehandlung hinzufügen
  - [ ] Testen mit realen Daten
- **Geschätzte Zeit**: 45 Min
- **Code-Vorlage**: Siehe PHASE6_UI_INTEGRATION_PLAN.md, SCHRITT 1
- **Tests bestanden**: ❌

### [1.2] show_characters_window() - Charaktere
- **Datei**: csNova_main.py (suche nach der Funktion)
- **Status**: ⭕ TODO
- **Aufgaben**:
  - [ ] Manager abrufen: `char_manager = app_state.characters`
  - [ ] Charaktere laden: `all_chars = char_manager.get_all()`
  - [ ] Charakterliste anzeigen (character_ID, character_name, character_role)
  - [ ] Filter nach Name implementieren (text input)
  - [ ] Filter nach Hauptcharaktere implementieren (checkbox)
  - [ ] `load_characters()` Funktion mit Filter-Logik
  - [ ] "Add" Button für neue Charaktere
  - [ ] "Delete" Button mit Bestätigung
  - [ ] Hauptcharaktere filtern: `char_manager.get_main_characters()`
  - [ ] UI nach Änderung aktualisieren
  - [ ] Testen mit Filtern
- **Geschätzte Zeit**: 40 Min
- **Code-Vorlage**: Siehe PHASE6_UI_INTEGRATION_PLAN.md, SCHRITT 2
- **Tests bestanden**: ❌

### [1.3] show_projects_window() - Projekte
- **Datei**: csNova_main.py (suche nach der Funktion)
- **Status**: ⭕ TODO
- **Aufgaben**:
  - [ ] Manager abrufen: `proj_manager = app_state.projects`
  - [ ] Projekte laden: `all_projects = proj_manager.get_all()`
  - [ ] Projektliste anzeigen (ID, Titel, Autor, Status, Wort-Ziel)
  - [ ] "Neues Projekt" Button - Dialog implementieren
  - [ ] Projekt-Formular (title, author, status, word_goal, deadline)
  - [ ] "Projekt speichern" mit `proj_manager.add()`
  - [ ] "Löschen" Button mit Bestätigung
  - [ ] Projekt aktualisieren funktional machen
  - [ ] UI nach Add/Delete aktualisieren
  - [ ] Testen mit realen Projekten
- **Geschätzte Zeit**: 35 Min
- **Code-Vorlage**: Siehe PHASE6_UI_INTEGRATION_PLAN.md, SCHRITT 3
- **Tests bestanden**: ❌

---

## ✅ TODO PRIORITÄT 2 - SOLLTE IMPLEMENTIERT WERDEN

### [2.1] show_locations_window() - Schauplätze
- **Datei**: csNova_main.py (suche nach der Funktion)
- **Status**: ⭕ TODO
- **Aufgaben**:
  - [ ] Manager abrufen: `loc_manager = app_state.locations`
  - [ ] Schauplätze laden und anzeigen
  - [ ] Felder: ID, Titel, Status, Erstellt, Bearbeitet, Notizen
  - [ ] Add/Delete implementieren
  - [ ] UI aktualisieren nach Änderungen
- **Geschätzte Zeit**: 20 Min
- **Tests bestanden**: ❌

### [2.2] show_storylines_window() - Handlungsstränge
- **Datei**: csNova_main.py (suche nach der Funktion)
- **Status**: ⭕ TODO
- **Aufgaben**:
  - [ ] Manager abrufen: `story_manager = app_state.storylines`
  - [ ] Handlungsstränge laden und anzeigen
  - [ ] Felder: ID, Titel, Status, Erstellt, Bearbeitet, Notizen
  - [ ] Add/Delete implementieren
  - [ ] UI aktualisieren nach Änderungen
- **Geschätzte Zeit**: 20 Min
- **Tests bestanden**: ❌

---

## ⭕ TODO PRIORITÄT 3 - OPTIONAL (SPÄTER)

### [3.1] show_objects_window() - Objekte
- **Status**: ⭕ OPTIONAL

### [3.2] show_ideas_window() - Ideen
- **Status**: ⭕ OPTIONAL

### [3.3] show_chapters_window() - Kapitel/Szenen
- **Status**: ⭕ OPTIONAL (komplexer!)

---

## 📋 GENERISCHE AUFGABEN FÜR ALLE FENSTER

### Für jedes Fenster zu tun:
- [ ] Manager importieren und abrufen
- [ ] Daten mit manager.get_all() laden
- [ ] UI mit realen Daten füllen
- [ ] Add-Button funktional (manager.add())
- [ ] Delete-Button funktional (manager.delete())
- [ ] Bestätigung vor Löschung
- [ ] UI nach Änderung aktualisieren
- [ ] Fehlerbehandlung
- [ ] Log-Meldungen für Operationen
- [ ] Mit realen Daten testen
- [ ] Keine Hardcoded-Werte
- [ ] Keine direkten JSON-Operationen

---

## 🧪 TESTING-CHECKLISTE

Nach Implementierung jedes Fensters testen:

### Für show_references_window():
- [ ] Referenzenliste wird angezeigt (mindestens 3)
- [ ] "Add" - Neue Referenz wird gespeichert
- [ ] "Delete" - Referenz wird gelöscht (nach Bestätigung)
- [ ] "Validieren" - Validierungsergebnis wird angezeigt
- [ ] "Duplikate" - Duplikate werden erkannt
- [ ] Zitate - Format wechseln funktioniert
- [ ] Tabelle - Aktualisiert sich nach Änderungen

### Für show_characters_window():
- [ ] Charakterliste wird angezeigt
- [ ] Filter nach Name funktioniert
- [ ] Filter nach Hauptcharaktere funktioniert
- [ ] "Add" - Neuer Charakter wird gespeichert
- [ ] "Delete" - Charakter wird gelöscht
- [ ] Tabelle - Aktualisiert sich sofort

### Für show_projects_window():
- [ ] Projektliste wird angezeigt
- [ ] "Add" - Neues Projekt wird gespeichert
- [ ] "Delete" - Projekt wird gelöscht
- [ ] Projektdetails - Alle Felder werden angezeigt
- [ ] Tabelle - Aktualisiert sich nach Änderungen

---

## 📚 RESSOURCEN

| Datei | Zweck |
|-------|-------|
| PHASE6_UI_INTEGRATION_PLAN.md | Detaillierter Plan mit Code-Templates |
| UI_INTEGRATION.md | API-Referenz für Manager |
| ui_integration_examples.py | 7 Beispiel-Funktionen |
| INTEGRATION_GUIDE.md | Manager-Grundlagen |

---

## 🚀 WORKFLOW PRO FENSTER

```
1. Plan lesen (5 Min)
   └─ PHASE6_UI_INTEGRATION_PLAN.md, SCHRITT X

2. Funktion finden (2 Min)
   └─ grep oder Suche in csNova_main.py

3. Code schreiben (20-30 Min)
   └─ Template kopieren
   └─ Anpassen an echte Daten
   └─ Manager nutzen

4. Testen (10 Min)
   └─ Mit realen Daten testen
   └─ Add/Delete testen
   └─ Fehler prüfen

5. Dokumentieren (2 Min)
   └─ Diese Checkliste aktualisieren
   └─ Haken setzen ✅
```

---

## 📊 FORTSCHRITT

```
PRIORITÄT 1 (MUSS):
[▯▯▯] show_references_window()     0%
[▯▯▯] show_characters_window()     0%
[▯▯▯] show_projects_window()       0%

PRIORITÄT 2 (SOLLTE):
[▯▯▯] show_locations_window()      0%
[▯▯▯] show_storylines_window()     0%

PRIORITÄT 3 (OPTIONAL):
[▯▯▯] show_objects_window()        0%
[▯▯▯] show_ideas_window()          0%
[▯▯▯] show_chapters_window()       0%
```

---

## 💾 SPEICHERPLATZ FÜR NOTIZEN

### show_references_window() - Notizen
```
(Schreib deine Notizen hier, wenn du arbeiten wirst)



```

### show_characters_window() - Notizen
```
(Schreib deine Notizen hier, wenn du arbeiten wirst)



```

### show_projects_window() - Notizen
```
(Schreib deine Notizen hier, wenn du arbeiten wirst)



```

---

## 🎯 NEXT STEPS

1. **Jetzt**: PHASE6_UI_INTEGRATION_PLAN.md komplett durchlesen
2. **Dann**: Mit [1.1] show_references_window() starten
3. **Dann**: [1.2] show_characters_window() implementieren
4. **Dann**: [1.3] show_projects_window() implementieren
5. **Optional**: [2.1] und [2.2] implementieren

---

**Geschätzter Gesamtaufwand**:
- PRIORITÄT 1: 2,5-3 Stunden
- PRIORITÄT 2: 1-1,5 Stunden
- Testing: 1 Stunde
- **TOTAL: 4,5-5,5 Stunden**

**Viel Spaß beim Coding! 🚀**

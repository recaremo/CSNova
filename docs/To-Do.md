# CSNova To-Do-Liste (Stand 2025-09-03)

## 1. Architektur & Datenmodell

**Priorität 1**
1. Zentrale Felddefinitionen für alle Formulare als JSON-Konfiguration (form_fields.json) ergänzen und in die Formulare einbinden.
2. Automatisierte Validierung: Prüfe Konsistenz zwischen Datenbanktabellen, form_fields.json, translations.json und translator.py.
3. Dependency Injection für zentrale Services (Datenbank, Translator, Settings) konsequent nutzen.
4. Redundanzen und Wiederholungen in Datenmodell und Code entfernen.
5. Datenbankbeziehungen und Mapping im Mermaid-Diagramm aktuell halten.

## 2. Übersetzung & Mehrsprachigkeit

**Priorität 2**
6. Automatisierte Generierung und Pflege der translation-Keys aus Tabellen und form_fields.json.
7. Validierung: Jeder Datenbank-Feldname und jedes UI-Element muss einen eindeutigen Schlüssel in translations.json und im Mapping von translator.py haben.
8. Mehrsprachigkeit in der GUI und Dokumentation konsequent umsetzen.
9. Dynamische Sprachauswahl und automatische Anpassung aller Menü- und UI-Texte sicherstellen.

## 3. GUI & Styles

**Priorität 3**
10. Styles und Formularlogik vollständig zentralisieren (keine Inline-Styles).
11. Styles optimieren: Icons für vintage, modern, future; light, middle, dark korrigieren und konsistent einbinden.
12. Hinweise zur Barrierefreiheit der GUI ergänzen.
13. Debug-Panel im GUI für Logging und Fehleranzeige implementieren.
14. Bilder anzeigen – über gespeicherten Hyperlink in einem Imagefenster.
15. Editorfenster fertigstellen und Formatbefehle (Text, Überschrift, etc.) integrieren.
16. Interviewmodus für Charaktere und Projekte spezifizieren und integrieren.

## 4. Logging, Fehlerbehandlung & Tests

**Priorität 4**
17. Validierungsfehler bei Benutzereingaben und Benutzeraktionen loggen.
18. Optionale Anzeige des Logs im GUI (Debug-Panel).
19. Hinweise zur Testabdeckung und Teststrategie ergänzen.
20. Automatisierte Tests für alle Kernfunktionen und GUI-Module ergänzen.

## 5. Release, Backup & Dokumentation

**Priorität 5**
21. Changelog-Prozess und Automatisierung konkret dokumentieren.
22. Backup- und Update-Strategie beschreiben und regelmäßig prüfen.
23. Installationsanleitung für alle Plattformen (Linux, Windows, macOS) ergänzen.
24. Lizenztext kürzen und als Kurzfassung bereitstellen.
25. Barrierefreiheit in der GUI und Dokumentation konkret beschreiben.
26. KI-Modul-Spezifikationen und API-Dokumentation ergänzen.

---

**Hinweis:**  
Korrekturen, Anpassungen und Updates erfolgen im Idealfall nur noch über die Tabellen und zentrale JSON-Konfigurationen (form_fields.json, translations.json).  
Alle anderen Bereiche werden programmatisch und automatisch korrekt übernommen.
# CSNova To-Do-Liste (Stand 2025-09-01)

## 1. Architektur & Utility

1. [x] Utility-Funktionen zentralisieren.
2. [x] Modul-Abhängigkeiten dokumentieren (Diagramm/Tabelle).
3. [ ] Dependency Injection für zentrale Services (z.B. Datenbank, Translator, Settings) konsequent nutzen.
4. [ ] Felddefinitionen für Formulare zentralisieren (z.B. als JSON-Konfiguration).
5. [~] Dokumentation aktuell halten und neue Strukturen ergänzen.

---

## 2. Styles & GUI

6. [~] Styles und Formularlogik vollständig zentralisieren.
7. [x] Style- und Modus-Labels in allen Fenstern mehrsprachig machen (Translator nutzen).
8. [x] Panels und Toolbars überall zentral über die Stylesheet-Funktionen stylen.
9. [ ] Icon-Factory zentral implementieren und Icons für alle Styles und Modi konsistent einbinden.
10. [~] Default-Indizes für Style und Mode robust und dynamisch setzen (aus Dictionaries ableiten).
11. [ ] Styles optimieren: Icons für vintage, modern, future; light, middle, dark korrigieren.
12. [x] Alle Formulare korrekt einbinden und anzeigen.
13. [ ] Bilder anzeigen – über gespeicherten Hyperlink in einem Imagefenster.
14. [x] Style des Fensters und Buttons in preferences.py verbessern.
15. [x] Styleauswahl direkt auf das preferences.py Fenster anwenden (keine Button-Vorschau).
16. [ ] Hinweise zur Barrierefreiheit der GUI ergänzen.

---

## 3. Logging & Fehlerbehandlung

17. [x] Logging vereinheitlichen.
18. [x] Fehlerbehandlung in allen Modulen, wo externe Ressourcen verwendet werden, erweitern.
19. [~] Validierungsfehler bei Benutzereingaben und Benutzeraktionen loggen.
20. [x] log_exception überall dort nutzen, wo ein Fehler auftreten kann.
21. [x] Event-Handler (z.B. Button-Klicks, Fensterwechsel) mit Fehlerbehandlung und Logging ausstatten.
22. [x] Decorator @log_call für kritische Funktionen nutzen.
23. [x] Stacktrace bei Fehlern loggen.
24. [x] Logging-Level (INFO, DEBUG, ERROR) ergänzen und Umschaltung ermöglichen.
25. [x] Log-Datei-Rotation/Größenbegrenzung implementieren.
26. [ ] Optionale Anzeige im GUI (Debug-Panel).
27. [ ] Hinweise zur Testabdeckung und Teststrategie ergänzen.

---

## 4. Projektfenster, Editor & KI-Funktionen

28. [ ] Editorfenster fertigstellen und Formatbefehle (Text, Überschrift, etc.) integrieren.
29. [x] Hilfetexte für Editor und Projektfenster in translations.json integriert.
30. [x] Alle Funktionen in project_window.py integrieren: Save, Delete, Next, Preview, New.
31. [ ] Interviewmodus in project_window.py und preferences.py integrieren.
32. [ ] Sicherheitsabfrage: Programm wirklich beenden? (start_window.py).
33. [x] Projekt laden und Hilfen/Tutorials anzeigen (start_window.py).
34. [~] KI-Funktionen und API-Spezifikationen konkretisieren.
35. [ ] Bild des Charakters anhand seiner Daten erstellen.
36. [ ] Tabelle mit benutzerdefinierten Daten generieren.
37. [ ] Ortbeschreibung anhand von Daten generieren.
38. [ ] Typische Namen (z.B. Frauenname aus Island) generieren.
39. [ ] Weitere KI-gestützte Funktionen ergänzen.

---

## 5. Release & Updates

40. [x] Automatisierte Changelog-Erstellung (auto-changelog).
41. [ ] Changelog-Prozess und Automatisierung konkret dokumentieren.
42. [ ] Wichtige Änderungen regelmäßig in release.md übertragen.
43. [ ] Backup- und Update-Strategie beschreiben.
44. [~] Programmcode, Tabellenstrukturen, Datenbank und Backups aktuell halten.

---

## 6. Dokumentation & Struktur

45. [~] Redundanzen und Wiederholungen entfernen, Aufgaben zusammenfassen.
46. [~] Kapitelstruktur klarer gliedern, lange Abschnitte aufteilen.
47. [~] Formatierung der Dokumentation vereinheitlichen, Code und Tabellen ggf. auslagern.
48. [~] Mehrsprachigkeit in der GUI und Dokumentation konsequent umsetzen.
49. [ ] Lizenzbedingungen und rechtliche Hinweise kürzen und präzisieren.
50. [~] Installationsanleitung für alle Plattformen ergänzen.
51. [x] Datenbankbeziehungen als Diagramm direkt einbinden.
52. [ ] Backup- und Update-Strategie in der Dokumentation beschreiben.
53. [ ] Changelog-Prozess und Automatisierung in der Dokumentation konkretisieren.
54. [ ] Hinweise zur Barrierefreiheit und Testabdeckung ergänzen.

---

## 7. Neue Aufgaben

55. [ ] Zentrale Felddefinitionen für Formulare als JSON-Konfiguration ergänzen und in die Formulare einbinden.
56. [ ] Debug-Panel im GUI für Logging und Fehleranzeige implementieren.
57. [ ] Interviewmodus für Charaktere und Projekte spezifizieren und integrieren.
58. [ ] Automatisierte Tests für alle Kernfunktionen und GUI-Module ergänzen.
59. [ ] Installationsanleitung für Windows und macOS ergänzen.
60. [ ] Lizenztext kürzen und als Kurzfassung bereitstellen.
61. [ ] KI-Modul-Spezifikationen und API-Dokumentation ergänzen.
62. [ ] Barrierefreiheit in der GUI und Dokumentation konkret beschreiben.
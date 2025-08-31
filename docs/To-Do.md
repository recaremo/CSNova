1. [x] Utility-Funktionen zentralisieren.
2. [x] Modul-Abhängigkeiten dokumentieren (Diagramm/Tabelle).
3. [] Dependency Injection für zentrale Objekte nutzen.
4. [] Styles und Formularlogik zentralisieren.
5. [x] Logging vereinheitlichen.


# Logging

Empfehlung:

6. [x] Erweitere die Fehlerbehandlung in allen Modulen, wo externe Ressourcen (Dateien, Datenbank, Netzwerk) verwendet werden.
7. [] Logge auch Validierungsfehler bei Benutzereingaben (z.B. ungültige Daten im Formular).
8. [x] Nutze log_exception überall dort, wo ein Fehler auftreten kann, um den Stacktrace zu sichern.
9. [x] Prüfe, ob alle Event-Handler (z.B. Button-Klicks, Fensterwechsel) mit Fehlerbehandlung und Logging ausgestattet sind.

# Für noch mehr Robustheit und Nachvollziehbarkeit:

10. [x] Nutze den Decorator @log_call für kritische Funktionen.
11. [x] Logge alle Fehler mit Stacktrace (log_exception).
12. [] Ergänze Logging für Validierungsfehler und alle Benutzeraktionen.
13. [] Prüfe, ob alle externen Zugriffe und Event-Handler mit Fehlerbehandlung und Logging ausgestattet sind.

# Was fehlt oder kann verbessert werden?

 14. [x] Logging-Level (INFO, DEBUG, ERROR):
  . Es gibt nur INFO und ERROR. Ein DEBUG-Level fehlt.
  - Das Umschalten des Log-Levels (z.B. über Settings) ist nicht möglich.
 15. [x] Decorator für automatisches Logging von Funktionsaufrufen und Fehlern:
  - Ein Decorator, der Funktionsaufrufe und Fehler automatisch loggt, ist nicht vorhanden.
 16. [x] Log-Datei-Rotation/Größenbegrenzung:
  - Die Log-Datei wächst unbegrenzt. Eine Rotation oder Begrenzung fehlt.
 17. [x] Stacktrace bei Fehlern:
  - Fehler werden nur als Text geloggt, ein Stacktrace fehlt.
 18. [] Optionale Anzeige im GUI (Debug-Panel):
  - Keine Integration in die GUI, aber das ist optional.

# Abhängigkeiten

 19. [x] Erstelle ein Modul-Abhängigkeitsdiagramm (z.B. mit Mermaid oder als Grafik).
 20. [] Prüfe, ob du die Felddefinitionen für Formulare zentralisieren kannst (z.B. als JSON-Konfiguration).
 21. [] Nutze Dependency Injection konsequent für alle zentralen Services (z.B. Datenbank, Translator, Settings).
 22. [] Halte die Dokumentation aktuell und ergänze die neuen Strukturen.

# Release Changelog

npm install -g auto-changelog
auto-changelog -o docs/release.md

Automatisierungstipp
Führe regelmäßig git log --oneline aus und übertrage die wichtigsten Änderungen in die release.md.
Nutze Tools wie auto-changelog für die automatische Generierung und ergänze manuell die Highlights.

# project_load.py
 23. [] Editorfenster
 24. [] Formatbefehle: Text, Überschrift, ...
 25. [] Hilfedateien

 # project_window.py
 26. [] alle Funktionen integrieren: Save - Delete - Next - Preview - New 
 27. [] Hilfedateien
 28. [] Interviewmodus
 29. [] Styles optimieren: Icons für vintage, modern, future. ligth- middle - dark korrigieren
 30. [] alle Formulare korrekt einbinden und anzeigen
 31. [] Bilder anzeigen - über gespeicherten Hyperlink in einem Imagefenster

 # preferences.py
 32. [] soll der Interviewmodus aktivert werden?
 33. [] sollen Hilfenangezeigt werden?
 34. [] Style des Fensters an sich verbessern - Buttons!
 35. [] Styleauswahl nicht am Bespiel Button anzeigen sondern direkt, das preference.py Fenster anpassen

 # start_window.py
 34. [] Projekt laden
 35. [] Hilfen/Tutorials
 36. [] Sicherheitsabfrage: Programm wirklich beenden?

 # KI
 0. [] erstelle ein Bild des Charakters anhand seiner Daten
 0. [] erstelle eine Tabelle mit folgenden Daten: x,y,z
 0. [] erstelle eine Ortbeschreibung zum dem Ort: x,y,z
 0. [] was ist eine typischer Frauenname aus Island: Vor- und Nachname
 0. [] etc. 

 # Updates

 0. [] Programmcode
 0. [] Tabellenstrukuren, Datenbank
 0. [] Backups


Analyse Kapitel 6 (csNova_de.md) – Stylesheets-Zentralisierung

Ergebnis:
Fast alle Stylesheets werden bereits zentral über form_styles.py generiert und in den Widgets/Fenstern verwendet.

Zentrale Nutzung
Die Funktionen load_global_stylesheet, load_button_style, load_active_button_style, load_form_style aus form_styles.py werden in den wichtigsten GUI-Modulen und Widgets verwendet.
Die Styles für Buttons, Panels, Tabs, Listen, Eingabefelder, Labels usw. werden über diese zentralen Funktionen gesetzt.
Die Style-Auswahl und Vorschau in preferences.py nutzt die zentralen Style-Funktionen.
Lokale Stylesheets
In form_toolbar.py gibt es noch ein lokales Stylesheet für die Toolbar:

→ Optimierung: Diesen Teil könntest du in form_styles.py als Funktion auslagern (z.B. load_toolbar_style()).

In help_panel.py wird das Stylesheet direkt im Widget gesetzt, aber die Werte kommen aus get_current_style().
→ Das ist bereits zentral, aber du könntest auch hier eine Funktion in form_styles.py nutzen.

In preferences.py wird die Vorschau für den Button-Style direkt im Code generiert, aber die Werte kommen aus den zentralen Style-Funktionen.

Fazit
Fast alle Stylesheets sind zentralisiert.
Einzelne lokale CSS-Fragmente (z.B. in form_toolbar.py) können noch in form_styles.py ausgelagert werden.
Die Style-Werte werden überall aus den zentralen Style-Modulen geladen.
Empfehlung:

Lagere alle noch vorhandenen lokalen Stylesheet-Fragmente als eigene Funktionen in form_styles.py aus (z.B. load_toolbar_style()).
Damit ist die Stylesheet-Generierung vollständig zentralisiert und konsistent.
Du bist fast am Ziel – nur wenige lokale Reste sind noch zu vereinheitlichen!
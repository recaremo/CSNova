# Codices Scriptoria Nova (CSNova)

[Projektbeschreibung](/readme.md)

## 1. Projektfahrplan & Fortschritt

[ToDo](../To-Do.md)

[Projektbaum](/project_tree.md)

[Mermaid-Diagramm: Projektstruktur und Datenbank](../csNova_mermaid.mmd)

## 2. JSON Translation

In der JSON Translation werden alle GUI-Elemente, Tabellenfelder und Hilfetexte in die Sprachen: Deutsch, Englisch, Spanisch und Französisch übersetzt und mit einem eindeutigen Schlüssel (key) versehen.  
Die Reihenfolge und die Bezeichnungen der Schlüssel müssen in allen Sprachen identisch sein.  
Diese Schlüssel = Übersetzungen können beliebig erweitert werden, müssen aber die Reihenfolge und Eindeutigkeit der Schlüssel in den Sprachblöcken sicherstellen.

Die Übersetzungen werden zentral in **translator.py** erstellt.  
Der Aufruf und die Initialisierung erfolgen zentral über **csNova.py** und **preferences.py** – wenn eine andere Sprache von den Anwender:innen ausgewählt wird.

Diese JSON muss mit dem Modul **translations.json** identisch sein.  
Der Code ` ```json ` am Anfang und ` ``` ` am Ende wird nur in der Dokumentation verwendet.  
Der in dieser Dokumentation und in der **translations.json** verwendete Inhalt muss den Richtlinien für das JSON-Format entsprechen:

* keine Kommentare
* beginnt und endet mit einer {}
* die Sprachblöcke werden durch die internationalen Kürzel für Sprachen definiert: "de":, "en": usw.
* jeder Sprachblock beginnt ebenfalls mit einer {}
* zwischen den einzelnen Sprachblöcken muss in der schließenden geschweiften Klammer ein Komma stehen },
* dieses Komma entfällt nach dem letzten Sprachblock
* die Schlüssel verwenden folgendes Format: "key": "Text" und werden mit einem Komma voneinander getrennt
* beim letzten Schlüssel entfällt das Komma


```json
 {
    "de": {
  "proj_ma_01": "Projekt",
  "proj_ma_02": "Titel",
  "proj_ma_03": "Untertitel",
  "proj_ma_04": "Autor",
  "proj_ma_05": "Prämisse",
  "proj_ma_06": "Genre",
  "proj_ma_07": "Titelbild",
  "proj_ma_08": "Zielgruppe",
  "proj_ma_09": "Erzählperspektive",
  "proj_ma_10": "Abgabedatum",
  "proj_ma_11": "Startdatum",
  "proj_ma_12": "Ziel Wortanzahl",
  "proj_ma_13": "Zeitlinie",

  "proj_ch_01": "Kapitel",
  "proj_ch_02": "Kapitel-Titel",
  "proj_ch_03": "Kapitel-Prämisse",

  "proj_cs_01": "Szene",
  "proj_cs_02": "Titel",
  "proj_cs_03": "Prämisse",
  "proj_cs_04": "Ziel",
  "proj_cs_05": "Konflikt",
  "proj_cs_06": "Ergebnis",
  "proj_cs_07": "Typ",
  "proj_cs_08": "Stimmung",
  "proj_cs_09": "Dauer",
  "proj_cs_10": "Charaktere",
  "proj_cs_11": "Orte",
  "proj_cs_12": "Notizen",

  "proj_lo_01": "Ort",
  "proj_lo_02": "Titel",
  "proj_lo_03": "Beschreibung",

  "proj_st_01": "Erzählstrang",
  "proj_st_02": "Titel",
  "proj_st_03": "Prämisse",
  "proj_st_04": "Beschreibung",
  "proj_st_05": "Transformation",
  "proj_st_06": "Zeitlinie",
  "proj_st_07": "Notizen",

  "proj_ob_01": "Objekt",
  "proj_ob_02": "Titel",
  "proj_ob_03": "Beschreibung",

  "char_ma_01": "Charakter",
  "char_ma_02": "Hauptcharakter",
  "char_ma_03": "Name",
  "char_ma_04": "Vorname",
  "char_ma_05": "Spitzname",
  "char_ma_06": "Geburtsdatum",
  "char_ma_07": "Alter",
  "char_ma_08": "Rolle",
  "char_ma_09": "Status",
  "char_ma_10": "Geschlecht",
  "char_ma_11": "Sexuelle Orientierung",
  "char_ma_12": "Notizen",

  "char_gr_01": "Gruppe",
  "char_gr_02": "Gruppen-Titel",
  "char_gr_03": "Gruppen-Beschreibung",

  "char_or_01": "Herkunft",
  "char_or_02": "Vater",
  "char_or_03": "Mutter",
  "char_or_04": "Bezugsperson",
  "char_or_05": "Geschwister",
  "char_or_06": "Geburtsort",
  "char_or_07": "Notizen",

  "char_ed_01": "Ausbildung",
  "char_ed_02": "Schule",
  "char_ed_03": "Universität",
  "char_ed_04": "Berufsausbildung",
  "char_ed_05": "Autodidaktisch",
  "char_ed_06": "Beruf",
  "char_ed_07": "Kunst/Musik",
  "char_ed_08": "Sport",
  "char_ed_09": "Technik",
  "char_ed_10": "Notizen",

  "char_am_01": "Aussehen",
  "char_am_02": "Größe",
  "char_am_03": "Körpertyp",
  "char_am_04": "Statur",
  "char_am_05": "Gesichtsform",
  "char_am_06": "Augenform",
  "char_am_07": "Augenfarbe",
  "char_am_08": "Haare",
  "char_am_09": "Haarfarbe",
  "char_am_10": "Haut",
  "char_am_11": "Ausstrahlung",
  "char_am_12": "Besonderheiten",
  "char_am_13": "Notizen",

  "char_ad_01": "Aussehen Details",
  "char_ad_02": "Kopf",
  "char_ad_03": "Nacken",
  "char_ad_04": "Schultern",
  "char_ad_05": "Arme",
  "char_ad_06": "Hände",
  "char_ad_07": "Finger",
  "char_ad_08": "Brust",
  "char_ad_09": "Hüfte, Taille",
  "char_ad_10": "Gesäß",
  "char_ad_11": "Beine",
  "char_ad_12": "Füße",
  "char_ad_13": "Zehen",
  "char_ad_14": "Notizen",

  "char_ps_01": "Persönlichkeit",
  "char_ps_02": "Positive Eigenschaft",
  "char_ps_03": "Negative Eigenschaft",
  "char_ps_04": "Ängste",
  "char_ps_05": "Schwächen",
  "char_ps_06": "Stärken",
  "char_ps_07": "Talente",
  "char_ps_08": "Glaubensgrundsatz",
  "char_ps_09": "Lebensziel",
  "char_ps_10": "Motivation",
  "char_ps_11": "Verhalten",
  "char_ps_12": "Notizen",

  "char_pp_01": "Psychologisches Profil",
  "char_pp_02": "Diagnose",
  "char_pp_03": "Symptome",
  "char_pp_04": "Therapie",
  "char_pp_05": "Medikamente",
  "char_pp_06": "Temperament",
  "char_pp_07": "Werte",
  "char_pp_08": "Moralvorstellungen",
  "char_pp_09": "Charakterstärke",
  "char_pp_10": "Charakterschwäche",
  "char_pp_11": "Selbstbild",
  "char_pp_12": "Humor",
  "char_pp_13": "Aggressivität",
  "char_pp_14": "Trauma",
  "char_pp_15": "Prägung",
  "char_pp_16": "Sozialisation",
  "char_pp_17": "Normen",
  "char_pp_18": "Tabus",
  "char_pp_19": "Notizen",

  "sexo_sx_01": "Sexuelle Orientierung",
  "sexo_sx_02": "Orientierung",
  "sexo_sx_03": "Kurzbeschreibung",

  "gend_ge_01": "Geschlecht",
  "gend_ge_02": "Geschlecht",
  "gend_ge_03": "Kurzbeschreibung",

  "stat_pr_01": "Wörter pro Tag",
  "stat_pr_02": "Tage gezählt",
  "stat_pr_03": "Kapitel gezählt",
  "stat_pr_04": "Szenen gezählt",
  "stat_pr_05": "Erzählstränge gezählt",
  "stat_pr_06": "Hauptcharaktere gezählt",
  "stat_pr_07": "Nebencharaktere gezählt",
  "stat_pr_08": "Gruppen gezählt",
  "stat_pr_09": "Orte gezählt",
  "stat_pr_10": "Objekte gezählt",

  "PrefWinTitle": "Einstellungen",
  "PreferenceLanguage": "Sprache",
  "PreferenceStyle": "Stil",
  "PreferenceTheme": "Thema",

  "PreferenceLanguageDe": "Deutsch",
  "PreferenceLanguageEn": "Englisch",
  "PreferenceLanguageEs": "Spanisch",
  "PreferenceLanguageFr": "Französisch",

  "PreferenceStyleOld": "Klassisch",
  "PreferenceStyleVintage": "Vintage",
  "PreferenceStyleModern": "Modern",
  "PreferenceStyleFuture": "Futuristisch",
  "PreferenceStyleMinimal": "Minimalistisch",

  "PreferenceThemeDark": "Dunkel",
  "PreferenceThemeNeutral": "Neutral",
  "PreferenceThemeLight": "Hell",

  "PreferenceActionSave": "Speichern",
  "PreferenceActionCancel": "Abbrechen",

  "botn_st_01": "Datenbank",
  "botn_st_02": "Projekt öffnen...",
  "botn_st_03": "Einstellungen",
  "botn_st_04": "Hilfe && Tutorials",
  "botn_st_05": "Beenden",
  "WinStartTitle": "Codicies Scriptoria Nova (CSNova)",

  "botn_fo_01": "Projekt",
  "botn_fo_02": "Kapitel",
  "botn_fo_03": "Szenen",
  "botn_fo_04": "Erzählstränge",
  "botn_fo_05": "Hauptcharaktere",
  "botn_fo_06": "Nebencharaktere",
  "botn_fo_07": "Gruppen",
  "botn_fo_08": "Orte",
  "botn_fo_09": "Objekte",
  "botn_fo_10": "Zurück",
  "ProWinTitle": "Projektverwaltung",

  "botn_pr_01": "Neu",
  "botn_pr_02": "Löschen",
  "botn_pr_03": "Vor",
  "botn_pr_04": "Zurück",
  "botn_pr_05": "Speichern",

  "botn_ch_01": "Neu",
  "botn_ch_02": "Löschen",
  "botn_ch_03": "Vor",
  "botn_ch_04": "Zurück",
  "botn_ch_05": "Speichern",

  "botn_cp_01": "Neu",
  "botn_cp_02": "Löschen",
  "botn_cp_03": "Vor",
  "botn_cp_04": "Zurück",
  "botn_cp_05": "Speichern",

  "botn_lo_01": "Neu",
  "botn_lo_02": "Löschen",
  "botn_lo_03": "Vor",
  "botn_lo_04": "Zurück",
  "botn_lo_05": "Speichern",

  "botn_ob_01": "Neu",
  "botn_ob_02": "Löschen",
  "botn_ob_03": "Vor",
  "botn_ob_04": "Zurück",
  "botn_ob_05": "Speichern",

  "botn_sc_01": "Neu",
  "botn_sc_02": "Löschen",
  "botn_sc_03": "Vor",
  "botn_sc_04": "Zurück",
  "botn_sc_05": "Speichern",

  "botn_sl_01": "Neu", 
  "botn_sl_02": "Löschen",
  "botn_sl_03": "Vor",
  "botn_sl_04": "Zurück",
  "botn_sl_05": "Speichern",

  "help_pr_01": "Hier kannst du dein Projekt verwalten. Wähle links den Bereich aus, den du bearbeiten möchtest.",
  "help_pr_02": "Im Projektformular kannst du alle wichtigen Informationen zu deinem Projekt eingeben, wie Titel, Autor, Genre und Zielgruppe.",
  "help_pr_03": "Im Charakterformular kannst du zwischen Haupt- und Nebencharaktere erstellen, die in einem oder mehreren Projekten eine Rolle spielen.",
  "help_pr_04": "Im Objektformular kannst du Objekte verwalten, die in einem oder mehreren Projekten verwendet werden.",
  "help_pr_05": "Im Ortsformular kannst du Orte verwalten, die in einem oder mehreren Projekten verwendet werden.",
  "help_wi_01": "",
  "help_wi_02": "Projekte",
  "help_wi_03": "Charakter",
  "help_wi_04": "Objekte",
  "help_wi_05": "Orte"
},  
"en": {
  "proj_ma_01": "Project",
  "proj_ma_02": "Title",
  "proj_ma_03": "Subtitle",
  "proj_ma_04": "Author",
  "proj_ma_05": "Premise",
  "proj_ma_06": "Genre",
  "proj_ma_07": "Cover Image",
  "proj_ma_08": "Target Group",
  "proj_ma_09": "Narrative Perspective",
  "proj_ma_10": "Deadline",
  "proj_ma_11": "Start Date",
  "proj_ma_12": "Word Count Goal",
  "proj_ma_13": "Timeline",

  "proj_ch_01": "Chapter",
  "proj_ch_02": "Chapter Title",
  "proj_ch_03": "Chapter Premise",

  "proj_cs_01": "Scene",
  "proj_cs_02": "Title",
  "proj_cs_03": "Premise",
  "proj_cs_04": "Goal",
  "proj_cs_05": "Conflict",
  "proj_cs_06": "Outcome",
  "proj_cs_07": "Type",
  "proj_cs_08": "Mood",
  "proj_cs_09": "Duration",
  "proj_cs_10": "Characters",
  "proj_cs_11": "Locations",
  "proj_cs_12": "Notes",

  "proj_lo_01": "Location",
  "proj_lo_02": "Title",
  "proj_lo_03": "Description",

  "proj_st_01": "Storyline",
  "proj_st_02": "Title",
  "proj_st_03": "Premise",
  "proj_st_04": "Description",
  "proj_st_05": "Transformation",
  "proj_st_06": "Timeline",
  "proj_st_07": "Notes",

  "proj_ob_01": "Object",
  "proj_ob_02": "Title",
  "proj_ob_03": "Description",

  "char_ma_01": "Character",
  "char_ma_02": "Main Character",
  "char_ma_03": "Name",
  "char_ma_04": "First Name",
  "char_ma_05": "Nickname",
  "char_ma_06": "Date of Birth",
  "char_ma_07": "Age",
  "char_ma_08": "Role",
  "char_ma_09": "Status",
  "char_ma_10": "Gender",
  "char_ma_11": "Sexual Orientation",
  "char_ma_12": "Notes",

  "char_gr_01": "Group",
  "char_gr_02": "Group Title",
  "char_gr_03": "Group Description",

  "char_or_01": "Origin",
  "char_or_02": "Father",
  "char_or_03": "Mother",
  "char_or_04": "Reference Person",
  "char_or_05": "Siblings",
  "char_or_06": "Birthplace",
  "char_or_07": "Notes",

  "char_ed_01": "Education",
  "char_ed_02": "School",
  "char_ed_03": "University",
  "char_ed_04": "Vocational Training",
  "char_ed_05": "Autodidactic",
  "char_ed_06": "Job",
  "char_ed_07": "Art/Music",
  "char_ed_08": "Sport",
  "char_ed_09": "Technology",
  "char_ed_10": "Notes",

  "char_am_01": "Appearance",
  "char_am_02": "Height",
  "char_am_03": "Body Type",
  "char_am_04": "Build",
  "char_am_05": "Face Shape",
  "char_am_06": "Eye Shape",
  "char_am_07": "Eye Color",
  "char_am_08": "Hair",
  "char_am_09": "Hair Color",
  "char_am_10": "Skin",
  "char_am_11": "Charisma",
  "char_am_12": "Special Features",
  "char_am_13": "Notes",

  "char_ad_01": "Appearance Details",
  "char_ad_02": "Head",
  "char_ad_03": "Neck",
  "char_ad_04": "Shoulders",
  "char_ad_05": "Arms",
  "char_ad_06": "Hands",
  "char_ad_07": "Fingers",
  "char_ad_08": "Chest",
  "char_ad_09": "Hip, Waist",
  "char_ad_10": "Buttocks",
  "char_ad_11": "Legs",
  "char_ad_12": "Feet",
  "char_ad_13": "Toes",
  "char_ad_14": "Notes",

  "char_ps_01": "Personality",
  "char_ps_02": "Positive Trait",
  "char_ps_03": "Negative Trait",
  "char_ps_04": "Fears",
  "char_ps_05": "Weaknesses",
  "char_ps_06": "Strengths",
  "char_ps_07": "Talents",
  "char_ps_08": "Belief",
  "char_ps_09": "Life Goal",
  "char_ps_10": "Motivation",
  "char_ps_11": "Behavior",
  "char_ps_12": "Notes",

  "char_pp_01": "Psychological Profile",
  "char_pp_02": "Diagnosis",
  "char_pp_03": "Symptoms",
  "char_pp_04": "Therapy",
  "char_pp_05": "Medication",
  "char_pp_06": "Temperament",
  "char_pp_07": "Values",
  "char_pp_08": "Morals",
  "char_pp_09": "Strength",
  "char_pp_10": "Weakness",
  "char_pp_11": "Self-Image",
  "char_pp_12": "Humor",
  "char_pp_13": "Aggressiveness",
  "char_pp_14": "Trauma",
  "char_pp_15": "Formative Influence",
  "char_pp_16": "Socialization",
  "char_pp_17": "Norms",
  "char_pp_18": "Taboos",
  "char_pp_19": "Notes",

  "sexo_sx_01": "Sexual Orientation",
  "sexo_sx_02": "Orientation",
  "sexo_sx_03": "Short Description",

  "gend_ge_01": "Gender",
  "gend_ge_02": "Gender",
  "gend_ge_03": "Short Description",

  "stat_pr_01": "Words per Day",
  "stat_pr_02": "Days Counted",
  "stat_pr_03": "Chapters Counted",
  "stat_pr_04": "Scenes Counted",
  "stat_pr_05": "Storylines Counted",
  "stat_pr_06": "Main Characters Counted",
  "stat_pr_07": "Supporting Characters Counted",
  "stat_pr_08": "Groups Counted",
  "stat_pr_09": "Locations Counted",
  "stat_pr_10": "Objects Counted",

  "PrefWinTitle": "Settings",
  "PreferenceLanguage": "Language",
  "PreferenceStyle": "Style",
  "PreferenceTheme": "Theme",

  "PreferenceLanguageDe": "German",
  "PreferenceLanguageEn": "English",
  "PreferenceLanguageEs": "Spanish",
  "PreferenceLanguageFr": "French",

  "PreferenceStyleOld": "Classic",
  "PreferenceStyleVintage": "Vintage",
  "PreferenceStyleModern": "Modern",
  "PreferenceStyleFuture": "Futuristic",
  "PreferenceStyleMinimal": "Minimalist",

  "PreferenceThemeDark": "Dark",
  "PreferenceThemeNeutral": "Neutral",
  "PreferenceThemeLight": "Light",

  "PreferenceActionSave": "Save",
  "PreferenceActionCancel": "Cancel",

  "botn_st_01": "Database",
  "botn_st_02": "Open Project...",
  "botn_st_03": "Settings",
  "botn_st_04": "Help && Tutorials",
  "botn_st_05": "Exit",
  "WinStartTitle": "Codicies Scriptoria Nova (CSNova)",

  "botn_fo_01": "Project",
  "botn_fo_02": "Chapter",
  "botn_fo_03": "Scenes",
  "botn_fo_04": "Storylines",
  "botn_fo_05": "Main Characters",
  "botn_fo_06": "Supporting Characters",
  "botn_fo_07": "Groups",
  "botn_fo_08": "Locations",
  "botn_fo_09": "Objects",
  "botn_fo_10": "Back",
  "ProWinTitle": "Project Management",

  "botn_pr_01": "New",
  "botn_pr_02": "Delete",
  "botn_pr_03": "Next",
  "botn_pr_04": "Back",
  "botn_pr_05": "Save",

  "botn_ch_01": "New",
  "botn_ch_02": "Delete",
  "botn_ch_03": "Next",
  "botn_ch_04": "Back",
  "botn_ch_05": "Save",

  "botn_cp_01": "New",
  "botn_cp_02": "Delete",
  "botn_cp_03": "Next",
  "botn_cp_04": "Back",
  "botn_cp_05": "Save",

  "botn_lo_01": "New",
  "botn_lo_02": "Delete",
  "botn_lo_03": "Next",
  "botn_lo_04": "Back",
  "botn_lo_05": "Save",

  "botn_ob_01": "New",
  "botn_ob_02": "Delete",
  "botn_ob_03": "Next",
  "botn_ob_04": "Back",
  "botn_ob_05": "Save",

  "botn_sc_01": "New",
  "botn_sc_02": "Delete",
  "botn_sc_03": "Next",
  "botn_sc_04": "Back",
  "botn_sc_05": "Save",

  "botn_sl_01": "New", 
  "botn_sl_02": "Delete",
  "botn_sl_03": "Next",
  "botn_sl_04": "Back",
  "botn_sl_05": "Save",

  "help_pr_01": "Here you can manage your project. Select the area you want to edit on the left.",
  "help_pr_02": "In the project form, you can enter all the important information about your project, such as title, author, genre, and target audience.",
  "help_pr_03": "In the character form, you can create main and supporting characters that play a role in one or more projects.",
  "help_pr_04": "In the object form, you can manage objects that are used in one or more projects.",
  "help_pr_05": "In the location form, you can manage locations that are used in one or more projects.",
  "help_wi_01": "",
  "help_wi_02": "Projects",
  "help_wi_03": "Character",
  "help_wi_04": "Objects",
  "help_wi_05": "Locations"
},
  "es": {
    "proj_ma_01": "Proyecto",
    "proj_ma_02": "Título",
    "proj_ma_03": "Subtítulo",
    "proj_ma_04": "Autor",
    "proj_ma_05": "Premisa",
    "proj_ma_06": "Género",
    "proj_ma_07": "Imagen de portada",
    "proj_ma_08": "Grupo objetivo",
    "proj_ma_09": "Perspectiva narrativa",
    "proj_ma_10": "Fecha de entrega",
    "proj_ma_11": "Fecha de inicio",
    "proj_ma_12": "Meta de palabras",
    "proj_ma_13": "Cronología",

    "proj_ch_01": "Capítulo",
    "proj_ch_02": "Título del capítulo",
    "proj_ch_03": "Premisa del capítulo",

    "proj_cs_01": "Escena",
    "proj_cs_02": "Título",
    "proj_cs_03": "Premisa",
    "proj_cs_04": "Objetivo",
    "proj_cs_05": "Conflicto",
    "proj_cs_06": "Resultado",
    "proj_cs_07": "Tipo",
    "proj_cs_08": "Estado de ánimo",
    "proj_cs_09": "Duración",
    "proj_cs_10": "Personajes",
    "proj_cs_11": "Lugares",
    "proj_cs_12": "Notas",

    "proj_lo_01": "Lugar",
    "proj_lo_02": "Título",
    "proj_lo_03": "Descripción",

    "proj_st_01": "Trama",
    "proj_st_02": "Título",
    "proj_st_03": "Premisa",
    "proj_st_04": "Descripción",
    "proj_st_05": "Transformación",
    "proj_st_06": "Cronología",
    "proj_st_07": "Notas",

    "proj_ob_01": "Objeto",
    "proj_ob_02": "Título",
    "proj_ob_03": "Descripción",

    "char_ma_01": "Personaje",
    "char_ma_02": "Personaje principal",
    "char_ma_03": "Nombre",
    "char_ma_04": "Nombre de pila",
    "char_ma_05": "Apodo",
    "char_ma_06": "Fecha de nacimiento",
    "char_ma_07": "Edad",
    "char_ma_08": "Rol",
    "char_ma_09": "Estado",
    "char_ma_10": "Género",
    "char_ma_11": "Orientación sexual",
    "char_ma_12": "Notas",

    "char_gr_01": "Grupo",
    "char_gr_02": "Título del grupo",
    "char_gr_03": "Descripción del grupo",

    "char_or_01": "Origen",
    "char_or_02": "Padre",
    "char_or_03": "Madre",
    "char_or_04": "Persona de referencia",
    "char_or_05": "Hermanos",
    "char_or_06": "Lugar de nacimiento",
    "char_or_07": "Notas",

    "char_ed_01": "Educación",
    "char_ed_02": "Escuela",
    "char_ed_03": "Universidad",
    "char_ed_04": "Formación profesional",
    "char_ed_05": "Autodidacta",
    "char_ed_06": "Trabajo",
    "char_ed_07": "Arte/Música",
    "char_ed_08": "Deporte",
    "char_ed_09": "Tecnología",
    "char_ed_10": "Notas",

    "char_am_01": "Apariencia",
    "char_am_02": "Altura",
    "char_am_03": "Tipo de cuerpo",
    "char_am_04": "Constitución",
    "char_am_05": "Forma de la cara",
    "char_am_06": "Forma de los ojos",
    "char_am_07": "Color de ojos",
    "char_am_08": "Cabello",
    "char_am_09": "Color de cabello",
    "char_am_10": "Piel",
    "char_am_11": "Carisma",
    "char_am_12": "Características especiales",
    "char_am_13": "Notas",

    "char_ad_01": "Detalles de apariencia",
    "char_ad_02": "Cabeza",
    "char_ad_03": "Cuello",
    "char_ad_04": "Hombros",
    "char_ad_05": "Brazos",
    "char_ad_06": "Manos",
    "char_ad_07": "Dedos",
    "char_ad_08": "Pecho",
    "char_ad_09": "Cadera, cintura",
    "char_ad_10": "Glúteos",
    "char_ad_11": "Piernas",
    "char_ad_12": "Pies",
    "char_ad_13": "Dedos de los pies",
    "char_ad_14": "Notas",

    "char_ps_01": "Personalidad",
    "char_ps_02": "Rasgo positivo",
    "char_ps_03": "Rasgo negativo",
    "char_ps_04": "Miedos",
    "char_ps_05": "Debilidades",
    "char_ps_06": "Fortalezas",
    "char_ps_07": "Talentos",
    "char_ps_08": "Creencias",
    "char_ps_09": "Meta de vida",
    "char_ps_10": "Motivación",
    "char_ps_11": "Comportamiento",
    "char_ps_12": "Notas",

    "char_pp_01": "Perfil psicológico",
    "char_pp_02": "Diagnóstico",
    "char_pp_03": "Síntomas",
    "char_pp_04": "Terapia",
    "char_pp_05": "Medicamentos",
    "char_pp_06": "Temperamento",
    "char_pp_07": "Valores",
    "char_pp_08": "Moral",
    "char_pp_09": "Fortaleza",
    "char_pp_10": "Debilidad",
    "char_pp_11": "Autoimagen",
    "char_pp_12": "Humor",
    "char_pp_13": "Agresividad",
    "char_pp_14": "Trauma",
    "char_pp_15": "Influencias formativas",
    "char_pp_16": "Socialización",
    "char_pp_17": "Normas",
    "char_pp_18": "Tabúes",
    "char_pp_19": "Notas",

    "sexo_sx_01": "Orientación sexual",
    "sexo_sx_02": "Orientación",
    "sexo_sx_03": "Descripción corta",

    "gend_ge_01": "Género",
    "gend_ge_02": "Género",
    "gend_ge_03": "Descripción corta",

    "stat_pr_01": "Palabras por día",
    "stat_pr_02": "Días contados",
    "stat_pr_03": "Capítulos contados",
    "stat_pr_04": "Escenas contadas",
    "stat_pr_05": "Tramas contadas",
    "stat_pr_06": "Personajes principales contados",
    "stat_pr_07": "Personajes secundarios contados",
    "stat_pr_08": "Grupos contados",
    "stat_pr_09": "Lugares contados",
    "stat_pr_10": "Objetos contados",

    "PrefWinTitle": "Configuración",
    "PreferenceLanguage": "Idioma",
    "PreferenceStyle": "Estilo",
    "PreferenceTheme": "Tema",

    "PreferenceLanguageDe": "Alemán",
    "PreferenceLanguageEn": "Inglés",
    "PreferenceLanguageEs": "Español",
    "PreferenceLanguageFr": "Francés",

    "PreferenceStyleOld": "Clásico",
    "PreferenceStyleVintage": "Vintage",
    "PreferenceStyleModern": "Moderno",
    "PreferenceStyleFuture": "Futurista",
    "PreferenceStyleMinimal": "Minimalista",

    "PreferenceThemeDark": "Oscuro",
    "PreferenceThemeNeutral": "Neutro",
    "PreferenceThemeLight": "Claro",

    "PreferenceActionSave": "Guardar",
    "PreferenceActionCancel": "Cancelar",

    "botn_st_01": "Base de datos",
    "botn_st_02": "Abrir proyecto...",
    "botn_st_03": "Configuración",
    "botn_st_04": "Ayuda && Tutoriales",
    "botn_st_05": "Salir",
    "WinStartTitle": "Codicies Scriptoria Nova (CSNova)",

    "botn_fo_01": "Proyecto",
    "botn_fo_02": "Capítulo",
    "botn_fo_03": "Escenas",
    "botn_fo_04": "Tramas",
    "botn_fo_05": "Personajes principales",
    "botn_fo_06": "Personajes secundarios",
    "botn_fo_07": "Grupos",
    "botn_fo_08": "Lugares",
    "botn_fo_09": "Objetos",
    "botn_fo_10": "Atrás",
    "ProWinTitle": "Gestión de proyectos",

    "botn_pr_01": "Nuevo",
    "botn_pr_02": "Eliminar",
    "botn_pr_03": "Siguiente",
    "botn_pr_04": "Atrás",
    "botn_pr_05": "Guardar",

    "botn_ch_01": "Nuevo",
    "botn_ch_02": "Eliminar",
    "botn_ch_03": "Siguiente",
    "botn_ch_04": "Atrás",
    "botn_ch_05": "Guardar",

    "botn_cp_01": "Nuevo",
    "botn_cp_02": "Eliminar",
    "botn_cp_03": "Siguiente",
    "botn_cp_04": "Atrás",
    "botn_cp_05": "Guardar",

    "botn_lo_01": "Nuevo",
    "botn_lo_02": "Eliminar",
    "botn_lo_03": "Siguiente",
    "botn_lo_04": "Atrás",
    "botn_lo_05": "Guardar",

    "botn_ob_01": "Nuevo",
    "botn_ob_02": "Eliminar",
    "botn_ob_03": "Siguiente",
    "botn_ob_04": "Atrás",
    "botn_ob_05": "Guardar",

    "botn_sc_01": "Nuevo",
    "botn_sc_02": "Eliminar",
    "botn_sc_03": "Siguiente",
    "botn_sc_04": "Atrás",
    "botn_sc_05": "Guardar",

    "botn_sl_01": "Nuevo",
    "botn_sl_02": "Eliminar",
    "botn_sl_03": "Siguiente",
    "botn_sl_04": "Atrás",
    "botn_sl_05": "Guardar",

    "help_pr_01": "Aquí puedes gestionar tu proyecto. Selecciona el área que deseas editar a la izquierda.",
    "help_pr_02": "En el formulario del proyecto, puedes ingresar toda la información importante sobre tu proyecto, como título, autor, género y público objetivo.",
    "help_pr_03": "En el formulario de personajes, puedes crear personajes principales y secundarios que juegan un papel en uno o más proyectos.",
    "help_pr_04": "En el formulario de objetos, puedes gestionar objetos que se utilizan en uno o más proyectos.",
    "help_pr_05": "En el formulario de lugares, puedes gestionar lugares que se utilizan en uno o más proyectos.",
    "help_wi_01": "",
    "help_wi_02": "Proyectos",
    "help_wi_03": "Personaje",
    "help_wi_04": "Objetos",
    "help_wi_05": "Lugares"
    
  },
  "fr": {
    "proj_ma_01": "Projet",
    "proj_ma_02": "Titre",
    "proj_ma_03": "Sous-titre",
    "proj_ma_04": "Auteur",
    "proj_ma_05": "Prémisse",
    "proj_ma_06": "Genre",
    "proj_ma_07": "Image de couverture",
    "proj_ma_08": "Groupe cible",
    "proj_ma_09": "Perspective narrative",
    "proj_ma_10": "Date limite",
    "proj_ma_11": "Date de début",
    "proj_ma_12": "Objectif de mots",
    "proj_ma_13": "Chronologie",

    "proj_ch_01": "Chapitre",
    "proj_ch_02": "Titre du chapitre",
    "proj_ch_03": "Prémisse du chapitre",

    "proj_cs_01": "Scène",
    "proj_cs_02": "Titre",
    "proj_cs_03": "Prémisse",
    "proj_cs_04": "Objectif",
    "proj_cs_05": "Conflit",
    "proj_cs_06": "Résultat",
    "proj_cs_07": "Type",
    "proj_cs_08": "Ambiance",
    "proj_cs_09": "Durée",
    "proj_cs_10": "Personnages",
    "proj_cs_11": "Lieux",
    "proj_cs_12": "Notes",

    "proj_lo_01": "Lieu",
    "proj_lo_02": "Titre",
    "proj_lo_03": "Description",

    "proj_st_01": "Intrigue",
    "proj_st_02": "Titre",
    "proj_st_03": "Prémisse",
    "proj_st_04": "Description",
    "proj_st_05": "Transformation",
    "proj_st_06": "Chronologie",
    "proj_st_07": "Notes",

    "proj_ob_01": "Objet",
    "proj_ob_02": "Titre",
    "proj_ob_03": "Description",

    "char_ma_01": "Personnage",
    "char_ma_02": "Personnage principal",
    "char_ma_03": "Nom",
    "char_ma_04": "Prénom",
    "char_ma_05": "Surnom",
    "char_ma_06": "Date de naissance",
    "char_ma_07": "Âge",
    "char_ma_08": "Rôle",
    "char_ma_09": "Statut",
    "char_ma_10": "Genre",
    "char_ma_11": "Orientation sexuelle",
    "char_ma_12": "Notes",

    "char_gr_01": "Groupe",
    "char_gr_02": "Titre du groupe",
    "char_gr_03": "Description du groupe",

    "char_or_01": "Origine",
    "char_or_02": "Père",
    "char_or_03": "Mère",
    "char_or_04": "Personne de référence",
    "char_or_05": "Frères et sœurs",
    "char_or_06": "Lieu de naissance",
    "char_or_07": "Notes",

    "char_ed_01": "Éducation",
    "char_ed_02": "École",
    "char_ed_03": "Université",
    "char_ed_04": "Formation professionnelle",
    "char_ed_05": "Autodidacte",
    "char_ed_06": "Métier",
    "char_ed_07": "Art/Musique",
    "char_ed_08": "Sport",
    "char_ed_09": "Technologie",
    "char_ed_10": "Notes",

    "char_am_01": "Apparence",
    "char_am_02": "Taille",
    "char_am_03": "Type de corps",
    "char_am_04": "Constitution",
    "char_am_05": "Forme du visage",
    "char_am_06": "Forme des yeux",
    "char_am_07": "Couleur des yeux",
    "char_am_08": "Cheveux",
    "char_am_09": "Couleur des cheveux",
    "char_am_10": "Peau",
    "char_am_11": "Charisme",
    "char_am_12": "Caractéristiques particulières",
    "char_am_13": "Notes",

    "char_ad_01": "Détails de l'apparence",
    "char_ad_02": "Tête",
    "char_ad_03": "Cou",
    "char_ad_04": "Épaules",
    "char_ad_05": "Bras",
    "char_ad_06": "Mains",
    "char_ad_07": "Doigts",
    "char_ad_08": "Poitrine",
    "char_ad_09": "Hanches, taille",
    "char_ad_10": "Fesses",
    "char_ad_11": "Jambes",
    "char_ad_12": "Pieds",
    "char_ad_13": "Orteils",
    "char_ad_14": "Notes",

    "char_ps_01": "Personnalité",
    "char_ps_02": "Trait positif",
    "char_ps_03": "Trait négatif",
    "char_ps_04": "Peurs",
    "char_ps_05": "Faiblesses",
    "char_ps_06": "Forces",
    "char_ps_07": "Talents",
    "char_ps_08": "Croyances",
    "char_ps_09": "Objectif de vie",
    "char_ps_10": "Motivation",
    "char_ps_11": "Comportement",
    "char_ps_12": "Notes",

    "char_pp_01": "Profil psychologique",
    "char_pp_02": "Diagnostic",
    "char_pp_03": "Symptômes",
    "char_pp_04": "Thérapie",
    "char_pp_05": "Médicaments",
    "char_pp_06": "Tempérament",
    "char_pp_07": "Valeurs",
    "char_pp_08": "Morale",
    "char_pp_09": "Force",
    "char_pp_10": "Faiblesse",
    "char_pp_11": "Image de soi",
    "char_pp_12": "Humour",
    "char_pp_13": "Agressivité",
    "char_pp_14": "Traumatisme",
    "char_pp_15": "Influences formatrices",
    "char_pp_16": "Socialisation",
    "char_pp_17": "Normes",
    "char_pp_18": "Tabous",
    "char_pp_19": "Notes",

    "sexo_sx_01": "Orientation sexuelle",
    "sexo_sx_02": "Orientation",
    "sexo_sx_03": "Description courte",

    "gend_ge_01": "Genre",
    "gend_ge_02": "Genre",
    "gend_ge_03": "Description courte",

    "stat_pr_01": "Mots par jour",
    "stat_pr_02": "Jours comptés",
    "stat_pr_03": "Chapitres comptés",
    "stat_pr_04": "Scènes comptées",
    "stat_pr_05": "Intrigues comptées",
    "stat_pr_06": "Personnages principaux comptés",
    "stat_pr_07": "Personnages secondaires comptés",
    "stat_pr_08": "Groupes comptés",
    "stat_pr_09": "Lieux comptés",
    "stat_pr_10": "Objets comptés",

    "PrefWinTitle": "Paramètres",
    "PreferenceLanguage": "Langue",
    "PreferenceStyle": "Style",
    "PreferenceTheme": "Thème",

    "PreferenceLanguageDe": "Allemand",
    "PreferenceLanguageEn": "Anglais",
    "PreferenceLanguageEs": "Espagnol",
    "PreferenceLanguageFr": "Français",

    "PreferenceStyleOld": "Classique",
    "PreferenceStyleVintage": "Vintage",
    "PreferenceStyleModern": "Moderne",
    "PreferenceStyleFuture": "Futuriste",
    "PreferenceStyleMinimal": "Minimaliste",

    "PreferenceThemeDark": "Sombre",
    "PreferenceThemeNeutral": "Neutre",
    "PreferenceThemeLight": "Clair",

    "PreferenceActionSave": "Enregistrer",
    "PreferenceActionCancel": "Annuler",

    "botn_st_01": "Base de données",
    "botn_st_02": "Ouvrir le projet...",
    "botn_st_03": "Paramètres",
    "botn_st_04": "Aide && Tutoriels",
    "botn_st_05": "Quitter",
    "WinStartTitle": "Codicies Scriptoria Nova (CSNova)",

    "botn_fo_01": "Projet",
    "botn_fo_02": "Chapitre",
    "botn_fo_03": "Scènes",
    "botn_fo_04": "Intrigues",
    "botn_fo_05": "Personnages principaux",
    "botn_fo_06": "Personnages secondaires",
    "botn_fo_07": "Groupes",
    "botn_fo_08": "Lieux",
    "botn_fo_09": "Objets",
    "botn_fo_10": "Retour",
    "ProWinTitle": "Gestion de projet",

    "botn_pr_01": "Nouveau",
    "botn_pr_02": "Supprimer",
    "botn_pr_03": "Suivant",
    "botn_pr_04": "Retour",
    "botn_pr_05": "Enregistrer",

    "botn_ch_01": "Nouveau",
    "botn_ch_02": "Supprimer",
    "botn_ch_03": "Suivant",
    "botn_ch_04": "Retour",
    "botn_ch_05": "Enregistrer",

    "botn_cp_01": "Nouveau",
    "botn_cp_02": "Supprimer",
    "botn_cp_03": "Suivant",
    "botn_cp_04": "Retour",
    "botn_cp_05": "Enregistrer",

    "botn_lo_01": "Nouveau",
    "botn_lo_02": "Supprimer",
    "botn_lo_03": "Suivant",
    "botn_lo_04": "Retour",
    "botn_lo_05": "Enregistrer",

    "botn_ob_01": "Nouveau",
    "botn_ob_02": "Supprimer",
    "botn_ob_03": "Suivant",
    "botn_ob_04": "Retour",
    "botn_ob_05": "Enregistrer",

    "botn_sc_01": "Nouveau",
    "botn_sc_02": "Supprimer",
    "botn_sc_03": "Suivant",
    "botn_sc_04": "Retour",
    "botn_sc_05": "Enregistrer",

    "botn_sl_01": "Nouveau",
    "botn_sl_02": "Supprimer",
    "botn_sl_03": "Suivant",
    "botn_sl_04": "Retour",
    "botn_sl_05": "Enregistrer",

    "help_pr_01": "Ici, vous pouvez gérer votre projet. Sélectionnez la zone que vous souhaitez modifier à gauche.",
    "help_pr_02": "Dans le formulaire de projet, vous pouvez saisir toutes les informations importantes sur votre projet, telles que le titre, l'auteur, le genre et le public cible.",
    "help_pr_03": "Dans le formulaire de personnage, vous pouvez créer des personnages principaux et secondaires qui jouent un rôle dans un ou plusieurs projets.",
    "help_pr_04": "Dans le formulaire d'objet, vous pouvez gérer des objets qui sont utilisés dans un ou plusieurs projets.",
    "help_pr_05": "Dans le formulaire de lieu, vous pouvez gérer des lieux qui sont utilisés dans un ou plusieurs projets.",
    "help_wi_01": "",
    "help_wi_02": "Projets",
    "help_wi_03": "Personnage",
    "help_wi_04": "Objets",
    "help_wi_05": "Lieux"
  }
}
```

## 3. Projekttabellen

Die SQL-Definitionen der Projekttabellen befinden sich im Verzeichnis **/core/tables**.  
Die Projekttabellen bestehen aus:

* **project.py**: Erfasst alle notwendigen Daten für ein Projekt. 
    + Ein Projekt darf innerhalb der Datenbank nur einmal vorkommen.
    + Folgende Datenfelder verwenden ausschließlich Daten aus den Bezugstabellen: 
        + **project_style** ← **project_style.py**
        + **genre** ← **project_genre.py**
        + **targetgroup** ← **project_targetgroup.py**
        + **narrative_perspective** ← **narrative_perspektive.py**
    + Folgende Datenfelder werden berechnet und erwarten keine Eingaben:
        + **project_words_count_days** = project_words_count_goal / project_days_count
        + **project_days_count** = project_deadline - project_startdate
    + Folgende Datenfelder werden auf Basis der Inhalte anderer Tabellen mit statistischen Werten gefüllt und erwarten keine Eingaben:
        + **project_chapters** ← project_chapters.py = Anzahl Kapitel zur Anzahl der fertigen Artikel
        + **project_scenes** ← project_scenes.py = Anzahl Szenen zur Anzahl der fertigen Szenen
        + **project_storylines** ← project_storylines.py = Anzahl Storylines zur Anzahl der fertigen Storylines
        + **project_locations** ← project_locations.py = Anzahl der Orte im Projekt = definiert
        + **project_objects** ← project_objects.py = Anzahl der Objekte = definiert
        + **project_main_character** ← characters.py = Anzahl Charaktere = definiert
        + **project_supporting_characters** ← characters.py = Anzahl Nebencharaktere = definiert
        + **project_groups_characters** ← character_groups.py = Anzahl Gruppen = definiert
    + Die Zuordnung der externen Parameter erfolgt über ein Mapping der benötigten Tabellen.

* **project_storylines.py**: Umfasst alle Storylines, die zu einem Projekt gehören. Bei Serien kann es vorkommen, dass eine Storyline über mehrere Projekte entwickelt wird.
* **project_chapters.py**: Umfasst alle Kapitel eines Projekts. Ein Kapitel ist einmalig und findet nur in einem Projekt Verwendung.
* **project_chapters_scenes.py**: Umfasst alle Szenen innerhalb eines Kapitels (siehe Mapping-Tabellen unten).
* **project_objects.py**: Umfasst alle Objekte eines Projekts. Da Objekte auch in anderen Projekten genutzt werden können, ohne dass es einen inhaltlichen Bezug zwischen den Projekten gibt, erfolgt die Zuweisung über **project_scene_object_map.py**.
* **project_locations.py**: Die Zuordnung erfolgt über die Mapping-Tabelle **project_scene_location_map.py**.
* **project_characters.py**: Die Zuordnung erfolgt über die Mapping-Tabelle **project_scene_character_map.py**.

### 3.1 project.py

```python
# project.py
# table: project
# description: central project database, main statistic of work done
# project_words_count_days = How many words a day do I "have to" write
# project_days_count = How many days are left until the deadline
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project (
        project_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_style TEXT,
        project_premise TEXT,
        project_title TEXT,
        project_subtitle TEXT,
        project_author TEXT,
        project_genre TEXT,
        project_cover_image TEXT,
        project_targetgroup TEXT,
        project_narrative_perspective TEXT,
        project_deadline DATE,
        project_startdate DATE,     
        project_words_count_goal INTEGER,
        project_words_count_days INTEGER,
        project_days_count INTEGER,  
        project_chapters INTEGER,
        project_scenes INTEGER,
        project_storylines INTEGER,
        project_main_characters INTEGER,
        project_supporting_characters INTEGER,
        project_groups_characters INTEGER,
        project_locatons INTEGER,
        project_objects INTEGER,
        project_timeline TEXT
    );
    """)
```

### 3.2 project_storylines.py

```python
# project_storylines.py
# table: project_storylines
# description: storylines in project
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_storylines (
        project_storylines_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_storylines_premise TEXT,
        project_storylines_title TEXT,
        project_storylines_description TEXT,
        project_storylines_transformation TEXT,
        project_storylines_timeline TEXT,
        project_storylines_notes TEXT
    );
    """)
```

### 3.3 project_chapters.py

```python
# project_chapters.py
# # table: project_chapters
# description: chapters inside a project
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_chapters (
        project_chapter_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_ID INTEGER NOT NULL,
        project_chapters_premise TEXT,
        project_chapters_title TEXT,
        FOREIGN KEY(project_ID) REFERENCES project(project_ID)
    );
    """)
```

### 3.4 project_chapters_scenes.py

```python
# project_chapters_scenes.py
# # table: project_chapters_scenes
# description: scenes inside a chapter
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_chapters_scenes (
        project_chapters_scenes_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_chapters_ID INTEGER NOT NULL,
        project_chapters_scenes_premise TEXT,
        project_chapters_scenes_title TEXT,
        project_chapters_scenes_goal TEXT,
        project_chapters_scenes_conflict TEXT,
        project_chapters_scenes_outcome TEXT,
        project_chapters_scenes_type TEXT,
        project_chapters_scenes_mood TEXT,
        project_chapters_scenes_duration TEXT,
        project_chapters_scenes_characters TEXT,
        project_chapters_scenes_locations TEXT,
        project_chapters_scenes_notes TEXT,
        FOREIGN KEY(project_chapters_ID) REFERENCES project_chapters(project_chapters_ID)
    );
    """)
```

### 3.5 project_objects.py

```python
# project_objects.py
# table: project_objects
# description: objects can be used in different scenes
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_objects (
        project_objects_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_objects_title TEXT,
        project_objects_description TEXT
    );
    """)
```

### 3.6 project_locations.py

```python
# project_locations.py
# table: project_locations
# description: locations can be used in different scenes
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_locations (
        project_locations_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_locations_title TEXT,
        project_locations_description TEXT
    );
    """)
```

### 3.7 project_characters.py

```python
# project_characters.py
# table: project_characters.py
# description: locations can be used in different scenes
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_characters (
        project_characters_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_characters_title TEXT,
        project_characters_description TEXT
    );
    """)
```

## 4. Mapping

Die Mapping-Tabellen sind die Schnittstelle zwischen den Projekt- und den Charaktertabellen.  
Die **form_fields.json** stellt eine zentralisierte Definition und Formate für alle Datenfelder aus allen Tabellen zur Verfügung. Im Programm werden diese Formatierungen dann auf die Formulare übertragen:

* base_form_widget.py: Lädt alle Felder und Labels aus **form_fields.json**, initialisiert die dynamischen Übersetzungen via **translator.py** und wendet alle Styles an.
* center_panel.py → initialisiert:
    + form_center_start.py
    + form_chapters.py
    + form_characters.py
    + form_locations.py
    + form_projects.py
    + form_scenes.py
    + form_storylines.py
    + form_toolbar.py

* help_panel.py → initialisiert und formatiert alle Hilfetexte → siehe auch [GUI](#65-gui)  
* navigation_panel.py → initialisiert und formatiert alle Navigations-Buttons → siehe auch [GUI](#65-gui)  

Die Mapping-Tabellen sorgen für die korrekte Verknüpfung und Datenintegrität zwischen den einzelnen Projekt- und Charaktertabellen. Sie gewährleisten, dass Beziehungen und Zuordnungen konsistent und nachvollziehbar in der Datenbank abgebildet werden.


### 4.1 project_scene_character_map.py
```python
# project_scene_character_map.py
# table: scene_character_map
# description: links characters to scenes

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scene_character_map (
        scene_character_map_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        scene_ID INTEGER NOT NULL,
        character_ID INTEGER NOT NULL,
        role_in_scene TEXT,
        FOREIGN KEY(scene_ID) REFERENCES project_chapters_scenes(project_chapters_scenes_ID),
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)
```

### 4.2 project_scene_location_map.py
```python
# project_scene_location_map.py
# table: scene_location_map
# description: links locations to scenes

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scene_location_map (
        scene_location_map_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        scene_ID INTEGER NOT NULL,
        location_ID INTEGER NOT NULL,
        FOREIGN KEY(scene_ID) REFERENCES project_chapters_scenes(project_chapters_scenes_ID),
        FOREIGN KEY(location_ID) REFERENCES project_locations(project_locations_ID)
    );
    """)
```

### 4.3 project_scene_object_map.py
```python
# scene_objects_map.py
# table: scene_objects_map
# description: links objects to scenes

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scene_objects_map (
        scene_object_map_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        scene_ID INTEGER NOT NULL,
        object_ID INTEGER NOT NULL,
        FOREIGN KEY(scene_ID) REFERENCES project_chapters_scenes(project_chapters_scenes_ID),
        FOREIGN KEY(object_ID) REFERENCES project_objects(project_objects_ID)
    );
    """)
```

### 4.4 project_scene_storyline_map.py
```python
# project_scene_storyline_map.py
# table: scene_storyline_map
# description: links scenes to storylines

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scene_storyline_map (
        scene_storyline_map_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        scene_ID INTEGER NOT NULL,
        storyline_ID INTEGER NOT NULL,
        FOREIGN KEY(scene_ID) REFERENCES project_chapters_scenes(project_chapters_scenes_ID),
        FOREIGN KEY(storyline_ID) REFERENCES project_storylines(project_storylines_ID)
    );
    """)
```

### 4.5 project_character_group_map.py
```python
# project_character_group_map.py
# table: character_group_map
# description: links characters to groups

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_group_map (
        character_group_map_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        group_ID INTEGER NOT NULL,
        role_in_group TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID),
        FOREIGN KEY(group_ID) REFERENCES character_groups(groups_ID)
    );
    """)
```

### 4.6 project_charcter_storyline_map.py
```python
# project_character_storyline_map.py
# table: character_storyline_map
# description: links characters to storylines

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_storyline_map (
        character_storyline_map_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        storyline_ID INTEGER NOT NULL,
        role_in_storyline TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID),
        FOREIGN KEY(storyline_ID) REFERENCES project_storylines(project_storylines_ID)
    );
    """)
```

### 4.7 form_fields.json
```json
{
  "projects": [
    {"name": "pro_header", "label_key": "proj_ma_01", "type": "header", "datafield_name": null},
    {"name": "title", "label_key": "proj_ma_02", "type": "text", "required": true, "max_length": 120, "datafield_name": "project_title"},
    {"name": "subtitle", "label_key": "proj_ma_03", "type": "text", "required": false, "max_length": 120, "datafield_name": "project_subtitle"},
    {"name": "author", "label_key": "proj_ma_04", "type": "text", "required": true, "max_length": 80, "datafield_name": "project_author"},
    {"name": "premise", "label_key": "proj_ma_05", "type": "text", "required": false, "max_length": 200, "datafield_name": "project_premise"},
    {"name": "genre", "label_key": "proj_ma_06", "type": "text", "required": false, "max_length": 80, "datafield_name": "project_genre"},
    {"name": "cover_image", "label_key": "proj_ma_07", "type": "text", "required": false, "max_length": 120, "datafield_name": "project_cover_image"},
    {"name": "target_group", "label_key": "proj_ma_08", "type": "text", "required": false, "max_length": 80, "datafield_name": "project_targetgroup"},
    {"name": "narrative_perspective", "label_key": "proj_ma_09", "type": "text", "required": false, "max_length": 80, "datafield_name": "project_narrative_perspective"},
    {"name": "deadline", "label_key": "proj_ma_10", "type": "date", "required": false, "datafield_name": "project_deadline"},
    {"name": "start_date", "label_key": "proj_ma_11", "type": "date", "required": false, "datafield_name": "project_startdate"},
    {"name": "words_count_goal", "label_key": "proj_ma_12", "type": "spin", "required": false, "max": 1000000, "datafield_name": "project_words_count_goal"},
    {"name": "timeline", "label_key": "proj_ma_13", "type": "text", "required": false, "max_length": 80, "datafield_name": "project_timeline"}
  ],

  "project_chapters": [
    {"name": "chapters_header", "label_key": "proj_ch_01", "type": "header", "datafield_name": null},
    {"name": "chapter_title", "label_key": "proj_ch_02", "type": "text", "required": true, "max_length": 120, "datafield_name": "project_chapters_title"},
    {"name": "chapter_premise", "label_key": "proj_ch_03", "type": "text", "required": false, "max_length": 200, "datafield_name": "project_chapters_premise"}
  ],

  "project_chapters_scenes": [
    {"name": "scenes_header", "label_key": "proj_cs_01", "type": "header", "datafield_name": null},
    {"name": "scene_title", "label_key": "proj_cs_02", "type": "text", "required": true, "max_length": 120, "datafield_name": "project_chapters_scenes_title"},
    {"name": "scene_premise", "label_key": "proj_cs_03", "type": "text", "required": false, "max_length": 200, "datafield_name": "project_chapters_scenes_premise"},
    {"name": "scene_goal", "label_key": "proj_cs_04", "type": "text", "required": false, "max_length": 120, "datafield_name": "project_chapters_scenes_goal"},
    {"name": "scene_conflict", "label_key": "proj_cs_05", "type": "text", "required": false, "max_length": 120, "datafield_name": "project_chapters_scenes_conflict"},
    {"name": "scene_outcome", "label_key": "proj_cs_06", "type": "text", "required": false, "max_length": 120, "datafield_name": "project_chapters_scenes_outcome"},
    {"name": "scene_type", "label_key": "proj_cs_07", "type": "text", "required": false, "max_length": 80, "datafield_name": "project_chapters_scenes_type"},
    {"name": "scene_mood", "label_key": "proj_cs_08", "type": "text", "required": false, "max_length": 80, "datafield_name": "project_chapters_scenes_mood"},
    {"name": "scene_duration", "label_key": "proj_cs_09", "type": "text", "required": false, "max_length": 80, "datafield_name": "project_chapters_scenes_duration"},
    {"name": "scene_characters", "label_key": "proj_cs_10", "type": "text", "required": false, "max_length": 200, "datafield_name": "project_chapters_scenes_characters"},
    {"name": "scene_locations", "label_key": "proj_cs_11", "type": "text", "required": false, "max_length": 200, "datafield_name": "project_chapters_scenes_locations"},
    {"name": "scene_notes", "label_key": "proj_cs_12", "type": "text", "required": false, "max_length": 500, "datafield_name": "project_chapters_scenes_notes"}
  ],

  "project_locations": [
    {"name": "locations_header", "label_key": "proj_lo_01", "type": "header", "datafield_name": null},
    {"name": "location_title", "label_key": "proj_lo_02", "type": "text", "required": true, "max_length": 120, "datafield_name": "project_locations_title"},
    {"name": "location_description", "label_key": "proj_lo_03", "type": "text", "required": false, "max_length": 500, "datafield_name": "project_locations_description"}
  ],

  "project_storylines": [
    {"name": "storylines_header", "label_key": "proj_st_01", "type": "header", "datafield_name": null},
    {"name": "storyline_title", "label_key": "proj_st_02", "type": "text", "required": true, "max_length": 120, "datafield_name": "project_storylines_title"},
    {"name": "storyline_premise", "label_key": "proj_st_03", "type": "text", "required": false, "max_length": 200, "datafield_name": "project_storylines_premise"},
    {"name": "storyline_description", "label_key": "proj_st_04", "type": "text", "required": false, "max_length": 500, "datafield_name": "project_storylines_description"},
    {"name": "storyline_transformation", "label_key": "proj_st_05", "type": "text", "required": false, "max_length": 200, "datafield_name": "project_storylines_transformation"},
    {"name": "storyline_timeline", "label_key": "proj_st_06", "type": "text", "required": false, "max_length": 200, "datafield_name": "project_storylines_timeline"},
    {"name": "storyline_notes", "label_key": "proj_st_07", "type": "text", "required": false, "max_length": 500, "datafield_name": "project_storylines_notes"}
  ],

  "project_objects": [
    {"name": "objects_header", "label_key": "proj_ob_01", "type": "header", "datafield_name": null},
    {"name": "object_title", "label_key": "proj_ob_02", "type": "text", "required": true, "max_length": 120, "datafield_name": "project_objects_title"},
    {"name": "object_description", "label_key": "proj_ob_03", "type": "text", "required": false, "max_length": 500, "datafield_name": "project_objects_description"}
  ],

  "character_main": [
    {"name": "main_header", "label_key": "char_ma_01", "type": "header", "datafield_name": null},
    {"name": "main_character", "label_key": "char_ma_02", "type": "checkbox", "required": false, "datafield_name": "main_character"},
    {"name": "name", "label_key": "char_ma_03", "type": "text", "required": true, "max_length": 80, "datafield_name": "name"},
    {"name": "first_name", "label_key": "char_ma_04", "type": "text", "required": true, "max_length": 80, "datafield_name": "first_name"},
    {"name": "nick_name", "label_key": "char_ma_05", "type": "text", "required": false, "max_length": 80, "datafield_name": "nick_name"},
    {"name": "born", "label_key": "char_ma_06", "type": "date", "required": false, "datafield_name": "born"},
    {"name": "age", "label_key": "char_ma_07", "type": "spin", "required": false, "max": 150, "datafield_name": "age"},
    {"name": "role", "label_key": "char_ma_08", "type": "text", "required": false, "max_length": 80, "datafield_name": "role"},
    {"name": "status", "label_key": "char_ma_09", "type": "text", "required": false, "max_length": 80, "datafield_name": "status"},
    {"name": "gender_ID", "label_key": "char_ma_10", "type": "select", "required": false, "datafield_name": "gender_ID"},
    {"name": "sex_orientation_ID", "label_key": "char_ma_11", "type": "select", "required": false, "datafield_name": "sex_orientation_ID"},
    {"name": "notes", "label_key": "char_ma_12", "type": "text", "required": false, "max_length": 500, "datafield_name": "notes"}
  ],

  "character_groups": [
    {"name": "groups_header", "label_key": "char_gr_01", "type": "header", "datafield_name": null},
    {"name": "groups_title", "label_key": "char_gr_02", "type": "text", "required": true, "max_length": 80, "datafield_name": "groups_title"},
    {"name": "groups_description", "label_key": "char_gr_03", "type": "text", "required": false, "max_length": 200, "datafield_name": "groups_description"}
  ],

  "character_origin": [
    {"name": "origin_header", "label_key": "char_or_01", "type": "header", "datafield_name": null},
    {"name": "father", "label_key": "char_or_02", "type": "text", "required": false, "max_length": 80, "datafield_name": "father"},
    {"name": "mother", "label_key": "char_or_03", "type": "text", "required": false, "max_length": 80, "datafield_name": "mother"},
    {"name": "reference_person", "label_key": "char_or_04", "type": "text", "required": false, "max_length": 80, "datafield_name": "reference_person"},
    {"name": "siblings", "label_key": "char_or_05", "type": "text", "required": false, "max_length": 120, "datafield_name": "siblings"},
    {"name": "birthplace", "label_key": "char_or_06", "type": "text", "required": false, "max_length": 120, "datafield_name": "birthplace"},
    {"name": "notes", "label_key": "char_or_07", "type": "text", "required": false, "max_length": 500, "datafield_name": "notes"}
  ],

  "character_education": [
    {"name": "education_header", "label_key": "char_ed_01", "type": "header", "datafield_name": null},
    {"name": "school", "label_key": "char_ed_02", "type": "text", "required": false, "max_length": 120, "datafield_name": "school"},
    {"name": "university", "label_key": "char_ed_03", "type": "text", "required": false, "max_length": 120, "datafield_name": "university"},
    {"name": "job_education", "label_key": "char_ed_04", "type": "text", "required": false, "max_length": 120, "datafield_name": "job_education"},
    {"name": "autodidactic", "label_key": "char_ed_05", "type": "text", "required": false, "max_length": 120, "datafield_name": "autodidactic"},
    {"name": "job", "label_key": "char_ed_06", "type": "text", "required": false, "max_length": 120, "datafield_name": "job"},
    {"name": "art_music", "label_key": "char_ed_07", "type": "text", "required": false, "max_length": 120, "datafield_name": "art_music"},
    {"name": "sport", "label_key": "char_ed_08", "type": "text", "required": false, "max_length": 120, "datafield_name": "sport"},
    {"name": "technology", "label_key": "char_ed_09", "type": "text", "required": false, "max_length": 120, "datafield_name": "technology"},
    {"name": "notes", "label_key": "char_ed_10", "type": "text", "required": false, "max_length": 500, "datafield_name": "notes"}
  ],

  "character_appearance_main": [
    {"name": "appearance_main_header", "label_key": "char_am_01", "type": "header", "datafield_name": null},
    {"name": "height", "label_key": "char_am_02", "type": "text", "required": false, "max_length": 80, "datafield_name": "height"},
    {"name": "body_type", "label_key": "char_am_03", "type": "text", "required": false, "max_length": 80, "datafield_name": "body_type"},
    {"name": "posture", "label_key": "char_am_04", "type": "text", "required": false, "max_length": 80, "datafield_name": "posture"},
    {"name": "face_shape", "label_key": "char_am_05", "type": "text", "required": false, "max_length": 80, "datafield_name": "face_shape"},
    {"name": "eye_shape", "label_key": "char_am_06", "type": "text", "required": false, "max_length": 80, "datafield_name": "eye_shape"},
    {"name": "eye_color", "label_key": "char_am_07", "type": "text", "required": false, "max_length": 80, "datafield_name": "eye_color"},
    {"name": "hair", "label_key": "char_am_08", "type": "text", "required": false, "max_length": 80, "datafield_name": "hair"},
    {"name": "hair_color", "label_key": "char_am_09", "type": "text", "required": false, "max_length": 80, "datafield_name": "hair_color"},
    {"name": "skin", "label_key": "char_am_10", "type": "text", "required": false, "max_length": 80, "datafield_name": "skin"},
    {"name": "charisma", "label_key": "char_am_11", "type": "text", "required": false, "max_length": 80, "datafield_name": "charisma"},
    {"name": "specials", "label_key": "char_am_12", "type": "text", "required": false, "max_length": 120, "datafield_name": "specials"},
    {"name": "notes", "label_key": "char_am_13", "type": "text", "required": false, "max_length": 500, "datafield_name": "notes"}
  ],

  "character_appearance_detail": [
    {"name": "appearance_detail_header", "label_key": "char_ad_01", "type": "header", "datafield_name": null},
    {"name": "head", "label_key": "char_ad_02", "type": "text", "required": false, "max_length": 80, "datafield_name": "head"},
    {"name": "neck", "label_key": "char_ad_03", "type": "text", "required": false, "max_length": 80, "datafield_name": "neck"},
    {"name": "shoulder", "label_key": "char_ad_04", "type": "text", "required": false, "max_length": 80, "datafield_name": "shoulder"},
    {"name": "arms", "label_key": "char_ad_05", "type": "text", "required": false, "max_length": 80, "datafield_name": "arms"},
    {"name": "hands", "label_key": "char_ad_06", "type": "text", "required": false, "max_length": 80, "datafield_name": "hands"},
    {"name": "finger", "label_key": "char_ad_07", "type": "text", "required": false, "max_length": 80, "datafield_name": "finger"},
    {"name": "chest", "label_key": "char_ad_08", "type": "text", "required": false, "max_length": 80, "datafield_name": "chest"},
    {"name": "hips_waist", "label_key": "char_ad_09", "type": "text", "required": false, "max_length": 80, "datafield_name": "hips_waist"},
    {"name": "buttocks", "label_key": "char_ad_10", "type": "text", "required": false, "max_length": 80, "datafield_name": "buttocks"},
    {"name": "legs", "label_key": "char_ad_11", "type": "text", "required": false, "max_length": 80, "datafield_name": "legs"},
    {"name": "feet", "label_key": "char_ad_12", "type": "text", "required": false, "max_length": 80, "datafield_name": "feet"},
    {"name": "toes", "label_key": "char_ad_13", "type": "text", "required": false, "max_length": 80, "datafield_name": "toes"},
    {"name": "notes", "label_key": "char_ad_14", "type": "text", "required": false, "max_length": 500, "datafield_name": "notes"}
  ],

  "character_personality": [
    {"name": "personality_header", "label_key": "char_ps_01", "type": "header", "datafield_name": null},
    {"name": "pos_characteristic", "label_key": "char_ps_02", "type": "text", "required": false, "max_length": 120, "datafield_name": "pos_characteristic"},
    {"name": "neg_characteristic", "label_key": "char_ps_03", "type": "text", "required": false, "max_length": 120, "datafield_name": "neg_characteristic"},
    {"name": "fears", "label_key": "char_ps_04", "type": "text", "required": false, "max_length": 120, "datafield_name": "fears"},
    {"name": "weaknesses", "label_key": "char_ps_05", "type": "text", "required": false, "max_length": 120, "datafield_name": "weaknesses"},
    {"name": "strengths", "label_key": "char_ps_06", "type": "text", "required": false, "max_length": 120, "datafield_name": "strengths"},
    {"name": "talents", "label_key": "char_ps_07", "type": "text", "required": false, "max_length": 120, "datafield_name": "talents"},
    {"name": "beliefs", "label_key": "char_ps_08", "type": "text", "required": false, "max_length": 120, "datafield_name": "beliefs"},
    {"name": "life_goals", "label_key": "char_ps_09", "type": "text", "required": false, "max_length": 120, "datafield_name": "life_goals"},
    {"name": "motivation", "label_key": "char_ps_10", "type": "text", "required": false, "max_length": 120, "datafield_name": "motivation"},
    {"name": "behavior", "label_key": "char_ps_11", "type": "text", "required": false, "max_length": 120, "datafield_name": "behavior"},
    {"name": "notes", "label_key": "char_ps_12", "type": "text", "required": false, "max_length": 500, "datafield_name": "notes"}
  ],

  "character_psychological_profile": [
    {"name": "psychological_profile_header", "label_key": "char_pp_01", "type": "header", "datafield_name": null},
    {"name": "diagnosis", "label_key": "char_pp_02", "type": "text", "required": false, "max_length": 120, "datafield_name": "diagnosis"},
    {"name": "symptoms", "label_key": "char_pp_03", "type": "text", "required": false, "max_length": 120, "datafield_name": "symptoms"},
    {"name": "therapy", "label_key": "char_pp_04", "type": "text", "required": false, "max_length": 120, "datafield_name": "therapy"},
    {"name": "medication", "label_key": "char_pp_05", "type": "text", "required": false, "max_length": 120, "datafield_name": "medication"},
    {"name": "temperament", "label_key": "char_pp_06", "type": "text", "required": false, "max_length": 120, "datafield_name": "temperament"},
    {"name": "values_set", "label_key": "char_pp_07", "type": "text", "required": false, "max_length": 120, "datafield_name": "values_set"},
    {"name": "moral_concepts", "label_key": "char_pp_08", "type": "text", "required": false, "max_length": 120, "datafield_name": "moral_concepts"},
    {"name": "character_strength", "label_key": "char_pp_09", "type": "text", "required": false, "max_length": 120, "datafield_name": "character_strength"},
    {"name": "character_weakness", "label_key": "char_pp_10", "type": "text", "required": false, "max_length": 120, "datafield_name": "character_weakness"},
    {"name": "self_image", "label_key": "char_pp_11", "type": "text", "required": false, "max_length": 120, "datafield_name": "self_image"},
    {"name": "humor", "label_key": "char_pp_12", "type": "text", "required": false, "max_length": 120, "datafield_name": "humor"},
    {"name": "aggression", "label_key": "char_pp_13", "type": "text", "required": false, "max_length": 120, "datafield_name": "aggression"},
    {"name": "trauma", "label_key": "char_pp_14", "type": "text", "required": false, "max_length": 120, "datafield_name": "trauma"},
    {"name": "formative_personality", "label_key": "char_pp_15", "type": "text", "required": false, "max_length": 120, "datafield_name": "formative_personality"},
    {"name": "socialization", "label_key": "char_pp_16", "type": "text", "required": false, "max_length": 120, "datafield_name": "socialization"},
    {"name": "norms", "label_key": "char_pp_17", "type": "text", "required": false, "max_length": 120, "datafield_name": "norms"},
    {"name": "taboos", "label_key": "char_pp_18", "type": "text", "required": false, "max_length": 120, "datafield_name": "taboos"},
    {"name": "notes", "label_key": "char_pp_19", "type": "text", "required": false, "max_length": 500, "datafield_name": "notes"}
  ],

  "sex_orientation": [
    {"name": "sex_orientation_header", "label_key": "sexo_sx_01", "type": "header", "datafield_name": null},
    {"name": "sex_orientation", "label_key": "sexo_sx_02", "type": "text", "required": true, "max_length": 80, "datafield_name": "sex_orientation"},
    {"name": "short_description", "label_key": "sexo_sx_03", "type": "text", "required": false, "max_length": 200, "datafield_name": "short_description"}
  ],

  "gender": [
    {"name": "gender_header", "label_key": "gend_ge_01", "type": "header", "datafield_name": null},
    {"name": "gender", "label_key": "gend_ge_02", "type": "text", "required": true, "max_length": 80, "datafield_name": "gender"},
    {"name": "short_description", "label_key": "gend_ge_03", "type": "text", "required": false, "max_length": 200, "datafield_name": "short_description"}
  ],

  "project_statistics": [
    {"name": "words_count_days", "label_key": "stat_pr_01", "type": "display", "datafield_name": "project_words_count_days"},
    {"name": "days_count", "label_key": "stat_pr_02", "type": "display", "datafield_name": "project_days_count"},
    {"name": "chapters_count", "label_key": "stat_pr_03", "type": "display", "datafield_name": "project_chapters"},
    {"name": "scenes_count", "label_key": "stat_pr_04", "type": "display", "datafield_name": "project_scenes"},
    {"name": "storylines_count", "label_key": "stat_pr_05", "type": "display", "datafield_name": "project_storylines"},
    {"name": "main_characters_count", "label_key": "stat_pr_06", "type": "display", "datafield_name": "project_main_characters"},
    {"name": "supporting_characters_count", "label_key": "stat_pr_07", "type": "display", "datafield_name": "project_supporting_characters"},
    {"name": "groups_characters_count", "label_key": "stat_pr_08", "type": "display", "datafield_name": "project_groups_characters"},
    {"name": "locations_count", "label_key": "stat_pr_09", "type": "display", "datafield_name": "project_locations"},
    {"name": "objects_count", "label_key": "stat_pr_10", "type": "display", "datafield_name": "project_objects"}
  ],

  "preferences": [
    {
      "name": "language",
      "label_key": "PreferenceLanguage",
      "type": "combobox",
      "required": true,
      "datafield_name": "preference_language",
      "options": [
        {"key": "de", "label_key": "PreferenceLanguageDe"},
        {"key": "en", "label_key": "PreferenceLanguageEn"},
        {"key": "es", "label_key": "PreferenceLanguageEs"},
        {"key": "fr", "label_key": "PreferenceLanguageFr"}
      ]
    },
    {
      "name": "style",
      "label_key": "PreferenceStyle",
      "type": "combobox",
      "required": true,
      "datafield_name": "preference_style",
      "options": [
        {"key": "style_old", "label_key": "PreferenceStyleOld"},
        {"key": "style_vintage", "label_key": "PreferenceStyleVintage"},
        {"key": "style_modern", "label_key": "PreferenceStyleModern"},
        {"key": "style_future", "label_key": "PreferenceStyleFuture"},
        {"key": "style_minimal", "label_key": "PreferenceStyleMinimal"}
      ]
    },
    {
      "name": "theme",
      "label_key": "PreferenceTheme",
      "type": "combobox",
      "required": true,
      "datafield_name": "preference_theme",
      "options": [
        {"key": "theme_dark", "label_key": "PreferenceThemeDark"},
        {"key": "theme_neutral", "label_key": "PreferenceThemeNeutral"},
        {"key": "theme_light", "label_key": "PreferenceThemeLight"}
      ]
    }
  ]
}
```

## 5. Charakter-Tabellen

Die SQL-Definitionen der Charakter-Tabellen befinden sich im Verzeichnis **/core/tables**.  
In diesem Abschnitt sind alle Tabellen zur Erstellung und Verwaltung von Charakteren zusammengefasst.  
Die Charakter-Tabellen bilden die Grundlage für die Erfassung, Zuordnung und Auswertung aller relevanten Charakterdaten innerhalb eines Projekts.  
Die Beziehungen zwischen den einzelnen Tabellen gewährleisten eine konsistente und nachvollziehbare Abbildung von Eigenschaften, Herkunft, Ausbildung, Persönlichkeit und weiteren Merkmalen der Charaktere in der Datenbank.

Die Charakter-Tabellen bestehen aus:

* **character_main.py**: Erfasst die Basisdaten eines Charakters, wie Name, Hauptcharakter-Status, Geschlecht, sexuelle Orientierung und weitere Grundinformationen.
* **gender.py** und **gender_data.py**: Enthalten die verschiedenen Geschlechtsidentitäten, die einem Charakter zugeordnet werden können.
* **sex_orientation.py** und **sex_orientation_data.py**: Enthalten die verschiedenen sexuellen Orientierungen, die einem Charakter zugeordnet werden können.
* **character_origin.py**: Erfasst die familiäre Herkunft eines Charakters, wie Vater, Mutter, Bezugspersonen, Geschwister und Geburtsort.
* **character_education.py**: Dokumentiert die Ausbildung eines Charakters, einschließlich Schule, Universität, Berufsausbildung, autodidaktischer Bildung, Beruf, künstlerischer und sportlicher Aktivitäten sowie technischer Kenntnisse.
* **character_personality.py**: Beschreibt die Persönlichkeit eines Charakters, einschließlich positiver und negativer Eigenschaften, Ängste, Schwächen, Stärken, Talente, Glaubenssätze, Lebensziele, Motivation und Verhalten.
* **character_psychological_profile.py**: Erfasst das psychologische Profil eines Charakters, wie Diagnosen, Symptome, Therapien, Medikamente, Temperament, Werte, Moralvorstellungen, Charakterstärken und -schwächen, Selbstbild, Humor, Aggressivität, Traumata, Prägungen, Sozialisation, Normen und Tabus.
* **character_appearance_main.py** und **character_appearance_detail.py**: Dokumentieren das äußere Erscheinungsbild eines Charakters, von allgemeinen Merkmalen wie Größe, Körperbau, Gesicht, Augen, Haare, Haut und Ausstrahlung bis hin zu detaillierten Merkmalen wie Kopf, Nacken, Schultern, Arme, Hände, Finger, Brust, Hüfte, Gesäß, Beine, Füße und Zehen.
* **character_groups.py**: Erfasst die Gruppenzugehörigkeit eines Charakters und beschreibt die jeweiligen Gruppen und deren Eigenschaften.

Diese Tabellen ermöglichen eine umfassende und strukturierte Erfassung aller relevanten Charaktermerkmale und deren Beziehungen innerhalb eines


### 5.1 character_main.py

```python
# character_main.py
# table: character_main
# description: base stats for a character
# access to the tables: gender.py, sex_orientation.py
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_main (
        character_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        main_character BOOL,
        name TEXT,
        first_name TEXT,
        nick_name TEXT,
        born DATE,
        age INTEGER,
        role TEXT,
        status TEXT,
        gender_ID INTEGER,
        sex_orientation_ID INTEGER,
        notes TEXT
    );
    """)
```

#### 5.1.1 gender.py

```python
# gender.py
# table: gender_data.py
# description: the different types of gender that can be assigned to a character
# access from the tables: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gender (
        gender_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        gender TEXT,
        short_description TEXT
    );
    """)
```
##### gender_data.py

```python
# gender_data.py
# description: data for gender.py

def data_gender(cursor):
    cursor.executemany("""
        INSERT INTO gender (gender, short_description)
        VALUES (?, ?)
    """, [
        ('Male', 'Identifies as male'),
        ('Female', 'Identifies as female'),
        ('Non-binary', 'Does not identify exclusively as male or female'),
        ('Transgender', 'Gender identity differs from assigned sex at birth'),
        ('Intersex', 'Born with physical sex characteristics that don’t fit typical definitions'),
        ('Agender', 'Does not identify with any gender'),
        ('Genderfluid', 'Gender identity varies over time'),
        ('Bigender', 'Identifies as two genders'),
        ('Other', 'Gender identity not listed above')
    ])
```

#### 5.1.2 sex_orientation.py

```python
# sex_orientation.py
# table: sex_orientation_data.py
# description: the different types of sexual orientation that can be assigned to a character
# access from the tables: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sex_orientation (
        sex_orientation_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        sex_orientation TEXT,
        short_description TEXT
    );
    """)
```
##### sex_orientation_data.py

```python
# sex_orientation_data.py
# description: data for sex_orientation.py

def sex_orientation_data(cursor):
    cursor.executemany("""
        INSERT INTO sex_orientation (sex_orientation, short_description)
        VALUES (?, ?)
    """, [
        ('Heterosexual', 'Attracted to the opposite gender'),
        ('Homosexual', 'Attracted to the same gender'),
        ('Bisexual', 'Attracted to both genders'),
        ('Asexual', 'Experiences little or no sexual attraction'),
        ('Pansexual', 'Attracted to people regardless of gender'),
        ('Queer', 'Non-normative sexual orientation'),
        ('Questioning', 'Exploring or unsure about sexual orientation')
    ])
```

### 5.2 character_origin.py

```python
# character_origin.py
# table: subtable for character_main
# description: family and origin of a character
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_origin (
        origin_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        father TEXT,
        mother TEXT,
        reference_person TEXT,
        siblings TEXT,
        birthplace TEXT,
        notes TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)
```

### 5.3 character_education.py

```python
# character_education.py
# table: subtable for character_main
# description: educations of a character
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_education (
        education_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        school TEXT,
        university TEXT,
        job_education TEXT,
        autodidactic TEXT,
        job TEXT,
        art_music TEXT,
        sport TEXT,
        technology TEXT,
        notes TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)
```

### 5.4 character_personality.py

```python
# character_personality.py
# table: subtable for character_main
# description: personality of a character
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_personality (
        personality_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        pos_characteristic TEXT,
        neg_characteristic TEXT,
        fears TEXT,
        weaknesses TEXT,
        strengths TEXT,
        talents TEXT,
        beliefs TEXT,
        life_goals TEXT,
        motivation TEXT,
        behavior TEXT,
        notes TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)
```

### 5.5 character_psychological_profile.py

```python
# character_psychological_profile.py
# table: subtable for character_main
# description: psychological profile of a character
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_psychological_profile (
        psychological_profile_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        diagnosis TEXT,
        symptoms TEXT,
        therapy TEXT,
        medication TEXT,
        temperament TEXT,
        values_set TEXT,
        moral_concepts TEXT,
        character_strength TEXT,
        character_weakness TEXT,
        self_image TEXT,
        humor TEXT,
        aggression TEXT,
        trauma TEXT,
        formative_personality TEXT,
        socialization TEXT,
        norms TEXT,
        taboos TEXT,
        notes TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)
```

### 5.6 character_appearance_main.py

```python
# character_appearance_main.py
# table: subtable for character_main
# description: main appearance of a character
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_appearance_main (
        appearance_main_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        height TEXT,
        body_type TEXT,
        posture TEXT,
        face_shape TEXT,
        eye_shape TEXT,
        eye_color TEXT,
        hair TEXT,
        hair_color TEXT,
        skin TEXT,
        charisma TEXT,
        specials TEXT,
        notes TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)
```

### 5.7 character_appearance_detail.py

```python
# character_appearance_detail.py
# table: subtable for character_main
# description: more appearance details of a character
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_appearance_detail (
        appearance_detail_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        head TEXT,
        neck TEXT,
        shoulder TEXT,
        arms TEXT,
        hands TEXT,
        finger TEXT,
        chest TEXT,
        hips_waist TEXT,
        buttocks TEXT,
        legs TEXT,
        feet TEXT,
        toes TEXT,
        notes TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)
```

### 5.8 character_groups.py

```python
# character_groups.py
# table: subtable for character_main
# description: character membership in a group
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_groups (
        groups_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        groups_title TEXT,
        groups_description TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)
```



## 6. Programmcode

Die Programmcodes von CSNova sind modular aufgebaut und befinden sich in den Verzeichnissen **/core**, **/config** und **/gui**.  
In diesem Kapitel sind alle zentralen Module, Hilfsfunktionen und GUI-Komponenten zusammengefasst, die für die Funktionalität, Datenverwaltung und Benutzeroberfläche der Anwendung verantwortlich sind.  
Die klare Strukturierung der Module gewährleistet eine effiziente Entwicklung, Wartung und Erweiterbarkeit des Programms.

Die wichtigsten Module und Komponenten sind:

* **Hauptprogramm**
    * **csNova.py**: Hauptprogramm, steuert den Programmstart, das Laden der Einstellungen und die Initialisierung der Hauptfenster.
    * **Einstellungen**
    * **settings.py**: Verwaltung und Speicherung der Benutzereinstellungen.
    * **dev.py**: Definition der Verzeichnisse, Dateipfade und zentralen Variablen.
    * **logger.py**: Zentrales Logging-Modul für Fehler, Informationen und Debug-Ausgaben.

* **Datenbank**
    * **database.py**: Initialisierung und Verwaltung der Datenbank, Tabellen und Seed-Daten.

* **Übersetzungen**
    * **translator.py**: Verwaltung der Übersetzungen und dynamische Sprachumschaltung.
    * **user_settings.json**: Speicherung der Spracheinstellungen und weiterer Nutzerpräferenzen.

* **GUI**
    * **Styles**
        + **base_style.py**: Zentrale CSS-Templates für alle GUI-Komponenten.
        + **themes_style.py**: Definition der verfügbaren Themes und Farbschemata.
        + **registry_style.py**: Auswahl und Anwendung des aktuellen Styles und Themes.
        + **form_styles.py**: Laden und Anwenden der Stylesheets für die GUI.
    * **Panels**
        + **navigation_panel.py**: Panel für die Navigation zwischen den Hauptbereichen.
        + **center_panel.py**: Panel für die Anzeige und Steuerung der Hauptinhalte.
        + **help_panel.py**: Panel für die Anzeige von Hilfetexten und Kontextinformationen.
    * **Widgets**
        + **form_toolbar.py**: Zentrale Toolbar für Formularaktionen.
        + **base_form_widget.py**: Generisches Widget für die dynamische Erstellung von Formularen.
        + **form_projects.py**, **form_chapters.py**, **form_characters.py**, **form_locations.py**, **form_objects.py**, **form_scenes.py**, **form_storylines.py**: Spezifische Formulare für die jeweiligen Datenbereiche.
        + **form_center_start.py**: Widget für die Startansicht im CenterPanel.
    * **Fenster**
        + **start_window.py**: Hauptfenster der Anwendung mit zentralen Buttons und Hintergrundbild.
        + **preferences.py**: Dialogfenster für Sprache, Stil und Theme-Einstellungen.
        + **project_window.py**: Projektfenster mit Navigation, Hauptinhalt und Hilfepanel.

Diese Module bilden die Grundlage für die gesamte Funktionalität und das Erscheinungsbild von CSNova.

### 6.1 Hauptprogramm (csNova.py)

```python
import sys
import json
from PySide6.QtWidgets import QApplication
from core.translator import Translator
from config.dev import USER_SETTINGS_FILE
from gui.start_window import StartWindow
from core.logger import log_section, log_subsection, log_info, log_exception
from gui.styles.form_styles import load_global_stylesheet

# Default settings used as fallback if user_settings.json is missing or incomplete
DEFAULT_SETTINGS = {
    "first_start": True,
    "screen_resolution": "1920x1080",
    "screen_dpi": 96,
    "scale_factor": 1.0,
    "language": "en",
    "style": "style_modern",
    "theme": "theme_neutral",
    "splitter_sizes": [
    200,
    1200,
    520
  ],
    "mode": "neutral",
    "start_window_bnt_width": 240,
    "start_window_bnt_height": 60,
    "start_window_bnt_top_offset": 270,
    "start_window_bnt_left_offset": 1350,
    "start_window_bnt_spacing": 42
}

def load_user_settings():
    """
    Loads user settings from user_settings.json.
    If loading fails or keys are missing, uses DEFAULT_SETTINGS as fallback.
    Logs success or error.
    """
    try:
        with open(USER_SETTINGS_FILE, "r", encoding="utf-8") as f:
            settings = json.load(f)
        # Fill missing keys with defaults
        for key, value in DEFAULT_SETTINGS.items():
            if key not in settings:
                settings[key] = value
                log_info(f"Missing key '{key}' set to default: {value}")
        log_info("user_settings.json loaded successfully.")
        return settings
    except Exception as e:
        log_exception("Error loading user_settings.json, using defaults.", e)
        return DEFAULT_SETTINGS.copy()

def save_user_settings(settings):
    """
    Saves user settings to user_settings.json.
    Logs success or error.
    """
    try:
        with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=2)
        log_info("user_settings.json saved successfully.")
    except Exception as e:
        log_exception("Error saving user_settings.json", e)

def initialize_screen_settings(settings, app):
    """
    Initializes and saves screen-dependent settings (resolution, DPI, scale factor, button positions)
    for the first program start or after a screen change.
    """
    screen = app.primaryScreen()
    size = screen.size()
    dpi = screen.logicalDotsPerInch()
    scale_factor = dpi / 96  # 96 DPI is standard

    settings["screen_resolution"] = f"{size.width()}x{size.height()}"
    settings["screen_dpi"] = dpi
    settings["scale_factor"] = scale_factor

    # Adjust button values according to scale factor
    settings["start_window_bnt_width"] = int(240 * scale_factor)
    settings["start_window_bnt_height"] = int(60 * scale_factor)
    settings["start_window_bnt_top_offset"] = int(270 * scale_factor)
    settings["start_window_bnt_left_offset"] = int(1350 * scale_factor)
    settings["start_window_bnt_spacing"] = int(42 * scale_factor)

    settings["first_start"] = False
    save_user_settings(settings)
    log_info("Screen settings initialized and saved.")

def check_and_update_screen_settings(settings, app):
    """
    Checks if the screen resolution or DPI has changed.
    If changed, re-initializes and saves screen-dependent settings.
    """
    screen = app.primaryScreen()
    size = screen.size()
    dpi = screen.logicalDotsPerInch()
    current_resolution = f"{size.width()}x{size.height()}"
    current_dpi = dpi

    # Check for changes in resolution or DPI
    if (settings.get("screen_resolution") != current_resolution or
        settings.get("screen_dpi") != current_dpi):
        settings["screen_resolution_changed"] = True
        initialize_screen_settings(settings, app)
        log_info("Screen resolution or DPI changed, settings updated.")
    else:
        settings["screen_resolution_changed"] = False

    return settings

def main():
    """
    Main entry point for CSNova.
    Loads and checks user settings, initializes screen settings if needed,
    and starts the main window.
    """
    log_section("csNova.py")
    log_subsection("main")
    try:
        app = QApplication(sys.argv)
        app.setStyleSheet(load_global_stylesheet())

        settings = load_user_settings()
        # If first_start is True, initialize screen settings
        if settings.get("first_start", True):
            initialize_screen_settings(settings, app)
        else:
            settings = check_and_update_screen_settings(settings, app)

        language = settings.get("language", "en")
        translator = Translator(language)
        window = StartWindow(default_language=language)
        window.show()
        log_info("CSNova main window shown.")
        sys.exit(app.exec())
    except Exception as e:
        log_exception("Error in csNova main execution", e)

if __name__ == "__main__":
    main()
```

### 6.2 Settings 
#### 6.2.1 settings.py

```python
import json
import os
from config.dev import USER_SETTINGS_FILE  # Use the unified variable

def load_settings():
    # Import logging only inside the function to avoid circular import
    try:
        from core.logger import log_info
    except ImportError:
        log_info = lambda msg: None
    try:
        if os.path.exists(USER_SETTINGS_FILE):
            with open(USER_SETTINGS_FILE, "r", encoding="utf-8") as f:
                settings = json.load(f)
                log_info(f"Settings loaded from {USER_SETTINGS_FILE}.")
                return settings
        return {"language": "en"}
    except Exception:
        return {"language": "en"}

def save_settings(settings):
    try:
        from core.logger import log_info, log_exception
    except ImportError:
        log_info = lambda msg: None
        log_exception = lambda msg, exc=None: None
    try:
        json_str = json.dumps(settings, indent=2)
        log_info(f"Saving settings to {USER_SETTINGS_FILE}.")
        log_info(f"JSON preview:\n{json_str}")
        with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
            f.write(json_str)
        log_info("Settings saved successfully.")
    except Exception as e:
        log_exception("Error while saving settings", e)

#### 6.2.2 dev.py

```python
from pathlib import Path
import sys

# Determine base directory (supports both frozen and script mode)
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).resolve().parent.parent

# Main directories
DATA_DIR         = BASE_DIR / "data"
CONFIG_DIR       = BASE_DIR / "config"
ASSETS_DIR       = BASE_DIR / "assets"
DOCS_DIR         = BASE_DIR / "docs"
GUI_DIR          = BASE_DIR / "gui"
CORE_DIR         = BASE_DIR / "core"
TRANSLATIONS_DIR = CORE_DIR / "translations"
TABLES_DIR       = CORE_DIR / "tables"

# Important files
DB_PATH          = DATA_DIR / "csnova.db"
USER_SETTINGS_FILE    = CONFIG_DIR / "user_settings.json"
FORM_FIELDS_FILE = CORE_DIR / "config" / "form_fields.json"
BG_IMAGE_PATH    = ASSETS_DIR / "media" / "csNova_background_start.png"

# Ensure directories exist (no logging here!)
for dir_path in [DATA_DIR, CONFIG_DIR, ASSETS_DIR, DOCS_DIR]:
    dir_path.mkdir(exist_ok=True)

LOG_FILE = BASE_DIR / "csnova.log"
```

#### 6.2.3 logger.py
```python
import datetime
import os
import traceback
from config.dev import LOG_FILE
from config.settings import load_settings

# Logging configuration
MAX_LOG_SIZE = 10 * 1024 * 1024  # 10 MB

# Default log level, can be set via settings
LOG_LEVEL = "INFO"  # Possible values: "DEBUG", "INFO", "ERROR"

def _write_log(message):
    # Log rotation: archive old log if too large
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > MAX_LOG_SIZE:
        try:
            os.rename(LOG_FILE, LOG_FILE + ".old")
        except Exception:
            pass  # Ignore rotation errors, continue logging
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def log_section(section):
    _write_log(f"\n=== [{datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] SECTION: {section} ===")

def log_subsection(subsection):
    _write_log(f"-- [{datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] SUBSECTION: {subsection}")

def log_debug(message):
    if LOG_LEVEL == "DEBUG":
        _write_log(f"[DEBUG {datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] {message}")

def log_info(message):
    if LOG_LEVEL in ("INFO", "DEBUG"):
        _write_log(f"[INFO {datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] {message}")

def log_error(message):
    _write_log(f"[ERROR {datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] {message}")

def log_exception(message, exc=None):
    _write_log(f"[ERROR {datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] {message}")
    if exc is not None:
        _write_log(traceback.format_exc())

def setup_logging():
    # Load log level from settings if available
    global LOG_LEVEL
    try:
        settings = load_settings()
        LOG_LEVEL = settings.get("log_level", LOG_LEVEL)
    except Exception:
        pass  # Use default if settings not available
    log_section("Logging started")

def log_header():
    _write_log("\n==================== CSNova Application Start ====================\n")

def log_call(func):
    """Decorator for automatic logging of function calls and exceptions."""
    def wrapper(*args, **kwargs):
        log_info(f"Calling {func.__name__}")
        try:
            result = func(*args, **kwargs)
            log_info(f"{func.__name__} finished successfully")
            return result
        except Exception as e:
            log_exception(f"Error in {func.__name__}: {e}", e)
            raise
    return wrapper
```

### 6.3 Datenbank

```python
import sqlite3
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import DB_PATH

from core.tables.gender_data import data_gender
from core.tables.sex_orientation_data import sex_orientation_data

from core.tables import (
    character_main,
    gender,
    sex_orientation,
    character_psychological_profile,
    character_origin,
    character_education,
    character_personality,
    character_appearance_main,
    character_appearance_detail,
    character_groups,
    project,
    project_storylines,
    project_chapters,
    project_chapters_scenes,
    project_objects,
    project_locations,
    project_scene_object_map,
    project_scene_location_map,
    project_scene_storyline_map,
    project_scene_character_map,
    project_character_storyline_map,
    project_character_group_map
)

def init_schema():
    log_section("database.py")
    log_subsection("init_schema")
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            log_info("Database connection established.")
            # Enable foreign key support
            cursor.execute("PRAGMA foreign_keys = ON")
            log_info("Foreign key support enabled.")

            # Initialize tables
            for module in [
                character_main,
                gender,
                sex_orientation,
                character_psychological_profile,
                character_origin,
                character_education,
                character_personality,
                character_appearance_main,
                character_appearance_detail,
                character_groups,
                project,
                project_storylines,
                project_chapters,
                project_chapters_scenes,
                project_objects,
                project_locations,
                project_scene_object_map,
                project_scene_location_map,
                project_scene_storyline_map,
                project_scene_character_map,
                project_character_storyline_map,
                project_character_group_map
            ]:
                try:
                    module.create_table(cursor)
                    log_info(f"Table created: {module.__name__}")
                except Exception as e:
                    log_exception(f"Error creating table {module.__name__}", e)

            # Insert seed data
            try:
                data_gender(cursor)
                log_info("Seed data for gender inserted.")
            except Exception as e:
                log_exception("Error inserting gender seed data", e)
            try:
                sex_orientation_data(cursor)
                log_info("Seed data for sex orientation inserted.")
            except Exception as e:
                log_exception("Error inserting sex orientation seed data", e)

            conn.commit()
            log_info("Database schema initialized and committed successfully.")
    except Exception as e:
        log_exception("An error occurred during database initialization", e)
```

### 6.4 Translation 

#### 6.4.1 user_settings.json

```json
{
  "first_start": true,
  "screen_resolution": "1920x1080",
  "screen_dpi": 96.0,
  "scale_factor": 1.0,
  "language": "en",
  "style": "style_old",
  "theme": "theme_neutral",
  "splitter_sizes": [
    176,
    1270,
    466
  ],
  "mode": "neutral",
  "start_window_bnt_width": 240,
  "start_window_bnt_height": 60,
  "start_window_bnt_top_offset": 270,
  "start_window_bnt_left_offset": 1350,
  "start_window_bnt_spacing": 42,
  "screen_resolution_changed": true,
  "sreen_resolution": "1920x1080"
}
```

#### 6.4.2 Translator (translator.py)

```python
import json
from config.dev import TRANSLATIONS_DIR
from core.logger import log_section, log_subsection, log_info, log_exception

class Translator:
    """
    Translator class for dynamic UI translation.
    Loads translations from translations.json and provides translation lookup for label_keys.
    Dependencies:
      - config.dev.TRANSLATIONS_DIR: Directory path for translations.json
      - core.logger: Logging functions for error and info tracking
    Used by:
      - All GUI forms and windows to translate labels, buttons, help texts, etc.
    """

    def __init__(self, lang="en"):
        """
        Initialize the Translator with a language code.
        Loads translations for the selected language.
        """
        log_section("translator.py")
        log_subsection("__init__")
        self.lang = lang
        self.translations = {}
        self._load_translations()

    def _load_translations(self):
        """
        Loads translations from translations.json for the current language.
        The file contains a dict with language codes as keys.
        Stores the translation dict for the selected language in self.translations.
        Logs errors if loading fails.
        """
        log_subsection("_load_translations")
        try:
            path = TRANSLATIONS_DIR / "translations.json"
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Get the translation dict for the current language
            self.translations = data.get(self.lang, {})
            log_info(f"Translations loaded for language '{self.lang}'.")
        except Exception as e:
            log_exception("Error loading translations", e)
            self.translations = {}

    def set_language(self, lang_code):
        """
        Change the language and reload translations.
        Used when the user switches the UI language.
        """
        log_subsection("set_language")
        self.lang = lang_code
        self._load_translations()

    def tr(self, label_key):
        """
        Translate a label_key using the loaded translations.
        If the key is not found, returns the key itself as fallback.
        Used by all forms and windows to get the correct UI label.
        """
        log_subsection("tr")
        return self.translations.get(label_key, label_key)

    def help_text(self, label_key):
        """
        Returns help text for a given label_key.
        Internally uses tr(), so it works for any key in translations.json.
        """
        log_subsection("help_text")
        return self.tr(label_key)
```

### 6.5 GUI
Module für das GUI.

#### 6.5.1 Styles

##### 6.5.1.1 base_style.py

```python
# Central CSS templates for all GUI components

CSS_TEMPLATES = {
    "window": """
        QWidget, QDialog {{
            background-color: {background};
            color: {foreground};
            font-family: {font_family};
            font-size: {font_size}px;
        }}
    """,
    "label": """
        QLabel {{
            color: {foreground};
            font-size: {font_size}px;
            background: transparent;
        }}
    """,
    "groupbox": """
        QGroupBox {{
            border: 1px solid {border};
            border-radius: {border_radius}px;
            margin-top: 10px;
            color: {foreground};
            font-size: {font_size}px;
        }}
        QGroupBox::title {{
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 3px 0 3px;
        }}
    """,
    "button": """
        QPushButton {{
            background-color: {button_bg};
            color: {button_fg};
            border-radius: {border_radius}px;
            border: 1px solid {border};
            font-size: {font_size}px;
            padding: 6px 18px;
        }}
        QPushButton:hover {{
            background-color: {button_hover};
        }}
        QPushButton:pressed {{
            background-color: {button_active};
        }}
        QPushButton:disabled {{
            background-color: #cccccc;
            color: #888888;
        }}
    """,
    "input": """
        QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QComboBox {{
            background-color: {input_bg};
            color: {input_fg};
            border-radius: {border_radius}px;
            border: 1px solid {border};
            font-size: {font_size}px;
            padding: 4px 8px;
            min-width: {input_width}px;
        }}
        QComboBox QAbstractItemView {{
            background-color: {input_bg};
            color: {input_fg};
            selection-background-color: {highlight};
        }}
    """,
    "tab": """
        QTabWidget::pane {{
            border: 1px solid {border};
            border-radius: {border_radius}px;
        }}
        QTabBar::tab {{
            background: {button_bg};
            color: {button_fg};
            border: 1px solid {border};
            border-radius: {border_radius}px;
            padding: 6px 18px;
            font-size: {font_size}px;
        }}
        QTabBar::tab:selected {{
            background: {button_active};
            color: {highlight};
        }}
        QTabBar::tab:hover {{
            background: {button_hover};
        }}
    """,
    "list": """
        QListView, QTreeView {{
            background: {input_bg};
            color: {input_fg};
            border: 1px solid {border};
            border-radius: {border_radius}px;
            font-size: {font_size}px;
        }}
        QListView::item:selected, QTreeView::item:selected {{
            background: {highlight};
            color: {foreground};
        }}
    """,
    "table": """
        QTableView {{
            background: {input_bg};
            color: {input_fg};
            border: 1px solid {border};
            border-radius: {border_radius}px;
            font-size: {font_size}px;
            gridline-color: {border};
        }}
        QHeaderView::section {{
            background: {button_bg};
            color: {button_fg};
            border: 1px solid {border};
            font-size: {font_size}px;
        }}
    """,
    "progress": """
        QProgressBar {{
            border: 1px solid {border};
            border-radius: {border_radius}px;
            text-align: center;
            background: {input_bg};
            color: {input_fg};
            font-size: {font_size}px;
        }}
        QProgressBar::chunk {{
            background-color: {highlight};
            width: 20px;
        }}
    """,
    "slider": """
        QSlider::groove:horizontal {{
            border: 1px solid {border};
            height: 8px;
            background: {input_bg};
            border-radius: 4px;
        }}
        QSlider::handle:horizontal {{
            background: {highlight};
            border: 1px solid {border};
            width: 18px;
            margin: -5px 0;
            border-radius: 9px;
        }}
    """,
    "splitter": """
        QSplitter::handle {{
            background: {border};
        }}
    """,
    "panel": """
        QWidget#NavigationPanel, QWidget#HelpPanel, QWidget#CenterPanel {{
            background: {background};
            color: {foreground};
            border-radius: {border_radius}px;
        }}
    """,
    "toolbar": """
        QToolBar {{
            background: {button_bg};
            border-bottom: 1px solid {border};
            spacing: 6px;
        }}
    """,
    "form": """
        QFormLayout QLabel {{
            color: {foreground};
            font-size: {font_size}px;
        }}
        QFormLayout QLineEdit, QFormLayout QDateEdit, QFormLayout QSpinBox {{
            background: {input_bg};
            color: {input_fg};
            border-radius: {border_radius}px;
            border: 1px solid {border};
            font-size: {font_size}px;
        }}
    """,
    "tooltip": """
        QToolTip {{
            background: {button_bg};
            color: {button_fg};
            border: 1px solid {border};
            font-size: {font_size}px;
        }}
    """,
    "menu": """
        QMenu {{
            background: {button_bg};
            color: {button_fg};
            border: 1px solid {border};
            font-size: {font_size}px;
        }}
        QMenu::item:selected {{
            background: {highlight};
            color: {foreground};
        }}
    """,
    "contextmenu": """
        QMenu {{
            background: {button_bg};
            color: {button_fg};
            border: 1px solid {border};
            font-size: {font_size}px;
        }}
        QMenu::item:selected {{
            background: {highlight};
            color: {foreground};
        }}
    """,
    "error": """
        QLabel#error, QLineEdit[error="true"], QTextEdit[error="true"] {{
            color: {error};
            border: 1px solid {error};
            background: #fff0f0;
        }}
    """
}

def extract_params(theme):
    """
    Converts the nested theme dict from themes_style.py into flat parameters for CSS rendering.
    Assumes all relevant values are set in the theme.
    """
    params = {}
    params.update({k: v for k, v in theme.items() if not isinstance(v, dict)})
    # Button
    button = theme.get("button", {})
    params["button_bg"] = button.get("background")
    params["button_fg"] = button.get("foreground")
    params["button_hover"] = button.get("hover")
    params["button_active"] = button.get("active")
    # Input
    input_ = theme.get("input", {})
    params["input_bg"] = input_.get("background")
    params["input_fg"] = input_.get("foreground")
    return params

def render_css(theme):
    """
    Renders the full CSS stylesheet for all GUI components using the given theme dict.
    """
    params = extract_params(theme)
    css = ""
    for key, template in CSS_TEMPLATES.items():
        css += template.format(**params)
    return css
```

##### 6.5.1.2 themes_style.py

```python
THEMES = {
    "oldschool": {
        "light": {
            "background": "#ffffff",
            "foreground": "#222326",
            "border": "#cfcfcf",
            "highlight": "#0078d7",
            "error": "#e81123",
            "font_size": 14,
            "font_family": "Segoe UI, Arial, sans-serif",
            "border_radius": 8,
            "input_width": 400,
            "button": {
                "background": "#f3f3f3",
                "foreground": "#222326",
                "hover": "#e5e5e5",
                "active": "#d0d0d0"
            },
            "input": {
                "background": "#f9f9f9",
                "foreground": "#222326"
            }
        },
        "middle": {
            "background": "#b0b0b0",
            "foreground": "#222326",
            "border": "#888888",
            "highlight": "#0078d7",
            "error": "#e81123",
            "font_size": 14,
            "font_family": "Segoe UI, Arial, sans-serif",
            "border_radius": 8,
            "input_width": 400,
            "button": {
                "background": "#a0a0a0",
                "foreground": "#222326",
                "hover": "#888888",
                "active": "#707070"
            },
            "input": {
                "background": "#bcbcbc",
                "foreground": "#222326"
            }
        },
        "dark": {
            "background": "#1e1e1e",
            "foreground": "#f3f3f3",
            "border": "#3c3c3c",
            "highlight": "#0078d7",
            "error": "#e81123",
            "font_size": 14,
            "font_family": "Segoe UI, Arial, sans-serif",
            "border_radius": 8,
            "input_width": 400,
            "button": {
                "background": "#2d2d2d",
                "foreground": "#f3f3f3",
                "hover": "#3c3c3c",
                "active": "#0078d7"
            },
            "input": {
                "background": "#252526",
                "foreground": "#f3f3f3"
            }
        }
    },
    "vintage": {
        "light": {
            "background": "#f5eee6",
            "foreground": "#5a4632",
            "border": "#cbb393",
            "highlight": "#b48a78",
            "error": "#a94442",
            "font_size": 15,
            "font_family": "Georgia, serif",
            "border_radius": 10,
            "input_width": 420,
            "button": {
                "background": "#e2d3c3",
                "foreground": "#5a4632",
                "hover": "#d6c3a3",
                "active": "#cbb393"
            },
            "input": {
                "background": "#f8f3ed",
                "foreground": "#5a4632"
            }
        },
        "middle": {
            "background": "#b8ae9c",
            "foreground": "#5a4632",
            "border": "#8c7c5a",
            "highlight": "#a67c52",
            "error": "#a94442",
            "font_size": 15,
            "font_family": "Georgia, serif",
            "border_radius": 10,
            "input_width": 420,
            "button": {
                "background": "#a89c7c",
                "foreground": "#5a4632",
                "hover": "#8c7c5a",
                "active": "#6c5a32"
            },
            "input": {
                "background": "#cfc6b3",
                "foreground": "#5a4632"
            }
        },
        "dark": {
            "background": "#3b2c23",
            "foreground": "#e2d3c3",
            "border": "#7c624a",
            "highlight": "#b48a78",
            "error": "#a94442",
            "font_size": 15,
            "font_family": "Georgia, serif",
            "border_radius": 10,
            "input_width": 420,
            "button": {
                "background": "#5a4632",
                "foreground": "#e2d3c3",
                "hover": "#7c624a",
                "active": "#a67c52"
            },
            "input": {
                "background": "#4e3b2a",
                "foreground": "#e2d3c3"
            }
        }
    },
    "modern": {
        "light": {
            "background": "#f3f6fd",
            "foreground": "#1a1a1a",
            "border": "#cfd8dc",
            "highlight": "#2563eb",
            "error": "#ef4444",
            "font_size": 14,
            "font_family": "Segoe UI, Arial, sans-serif",
            "border_radius": 8,
            "input_width": 400,
            "button": {
                "background": "#e7eaf3",
                "foreground": "#1a1a1a",
                "hover": "#d0d6e6",
                "active": "#b6c2e1"
            },
            "input": {
                "background": "#ffffff",
                "foreground": "#1a1a1a"
            }
        },
        "middle": {
            "background": "#b0b5bb",
            "foreground": "#23272f",
            "border": "#888d92",
            "highlight": "#2563eb",
            "error": "#ef4444",
            "font_size": 14,
            "font_family": "Segoe UI, Arial, sans-serif",
            "border_radius": 8,
            "input_width": 400,
            "button": {
                "background": "#a0a5ab",
                "foreground": "#23272f",
                "hover": "#888d92",
                "active": "#70757a"
            },
            "input": {
                "background": "#bfc4ca",
                "foreground": "#23272f"
            }
        },
        "dark": {
            "background": "#181a20",
            "foreground": "#e7eaf3",
            "border": "#2563eb",
            "highlight": "#60a5fa",
            "error": "#ef4444",
            "font_size": 14,
            "font_family": "Segoe UI, Arial, sans-serif",
            "border_radius": 8,
            "input_width": 400,
            "button": {
                "background": "#23272f",
                "foreground": "#e7eaf3",
                "hover": "#2563eb",
                "active": "#1e293b"
            },
            "input": {
                "background": "#23272f",
                "foreground": "#e7eaf3"
            }
        }
    },
    "future": {
        "light": {
            "background": "rgba(245, 250, 255, 0.85)",
            "foreground": "#22223b",
            "border": "#a3bffa",
            "highlight": "#7f9acb",
            "error": "#ff6b6b",
            "font_size": 15,
            "font_family": "Montserrat, Arial, sans-serif",
            "border_radius": 12,
            "input_width": 420,
            "button": {
                "background": "rgba(230, 240, 255, 0.95)",
                "foreground": "#22223b",
                "hover": "#b8c6db",
                "active": "#7f9acb"
            },
            "input": {
                "background": "rgba(255,255,255,0.95)",
                "foreground": "#22223b"
            }
        },
        "middle": {
            "background": "rgba(160, 170, 190, 0.90)",
            "foreground": "#22223b",
            "border": "#5a6a8b",
            "highlight": "#a3bffa",
            "error": "#ff6b6b",
            "font_size": 15,
            "font_family": "Montserrat, Arial, sans-serif",
            "border_radius": 12,
            "input_width": 420,
            "button": {
                "background": "#a3bffa",
                "foreground": "#22223b",
                "hover": "#7f9acb",
                "active": "#5a6a8b"
            },
            "input": {
                "background": "rgba(180,190,210,0.95)",
                "foreground": "#22223b"
            }
        },
        "dark": {
            "background": "rgba(30, 34, 45, 0.92)",
            "foreground": "#e0eaff",
            "border": "#7f9acb",
            "highlight": "#a3bffa",
            "error": "#ff6b6b",
            "font_size": 15,
            "font_family": "Montserrat, Arial, sans-serif",
            "border_radius": 12,
            "input_width": 420,
            "button": {
                "background": "#22223b",
                "foreground": "#e0eaff",
                "hover": "#7f9acb",
                "active": "#a3bffa"
            },
            "input": {
                "background": "rgba(40,44,54,0.95)",
                "foreground": "#e0eaff"
            }
        }
    },
    "minimal": {
        "light": {
            "background": "#ffffff",
            "foreground": "#222222",
            "border": "#cccccc",
            "highlight": "#1976d2",
            "error": "#d32f2f",
            "font_size": 13,
            "font_family": "Arial, sans-serif",
            "border_radius": 4,
            "input_width": 380,
            "button": {
                "background": "#f7f7f7",
                "foreground": "#222222",
                "hover": "#e0e0e0",
                "active": "#bdbdbd"
            },
            "input": {
                "background": "#fafafa",
                "foreground": "#222222"
            }
        },
        "middle": {
            "background": "#bdbdbd",
            "foreground": "#222222",
            "border": "#888888",
            "highlight": "#1976d2",
            "error": "#d32f2f",
            "font_size": 13,
            "font_family": "Arial, sans-serif",
            "border_radius": 4,
            "input_width": 380,
            "button": {
                "background": "#b0b0b0",
                "foreground": "#222222",
                "hover": "#888888",
                "active": "#1976d2"
            },
            "input": {
                "background": "#cfcfcf",
                "foreground": "#222222"
            }
        },
        "dark": {
            "background": "#222222",
            "foreground": "#f7f7f7",
            "border": "#424242",
            "highlight": "#1976d2",
            "error": "#d32f2f",
            "font_size": 13,
            "font_family": "Arial, sans-serif",
            "border_radius": 4,
            "input_width": 380,
            "button": {
                "background": "#333333",
                "foreground": "#f7f7f7",
                "hover": "#1976d2",
                "active": "#424242"
            },
            "input": {
                "background": "#2c2c2c",
                "foreground": "#f7f7f7"
            }
        }
    }
}

def get_theme(style, mode):
    """
    Returns the theme dictionary for the given style and mode.
    Falls back to 'modern' and 'light' if not found.
    """
    style_dict = THEMES.get(style, THEMES["modern"])
    return style_dict.get(mode, style_dict.get("light"))
```

##### 6.5.1.3 registry_style.py

```python
from config.settings import load_settings
from gui.styles.themes_style import get_theme
from gui.styles.base_style import extract_params

def get_current_style(style_code=None, mode_code=None):
    """
    Loads the current style and mode from settings and returns a flat theme dictionary for CSS rendering.
    Falls back to 'modern' and 'light' if not found.
    """
    settings = load_settings()
    style = style_code if style_code else settings.get("style", "modern")
    mode = mode_code if mode_code else settings.get("mode", "light")
    theme = get_theme(style, mode)
    return extract_params(theme)
```

##### 6.5.1.4 form_styles.py

```python
from gui.styles.base_style import render_css, CSS_TEMPLATES
from gui.styles.registry_style import get_current_style
from core.logger import log_section, log_subsection, log_info, log_exception

def load_global_stylesheet(style_code=None, mode_code=None):
    """
    Loads the global stylesheet for the application using the given style and mode.
    If style_code or mode_code are not provided, uses current settings.
    """
    log_section("form_styles.py")
    log_subsection("load_global_stylesheet")
    try:
        style = get_current_style(style_code, mode_code)
        # Render all CSS templates at once
        stylesheet = ""
        for key in CSS_TEMPLATES:
            stylesheet += CSS_TEMPLATES[key].format(**style)
        log_info("Global stylesheet loaded.")
        return stylesheet
    except Exception as e:
        log_exception("Error loading global stylesheet", e)
        return ""

def load_button_style(style_code=None, mode_code=None):
    """
    Loads the stylesheet for buttons and toolbars.
    """
    log_section("form_styles.py")
    log_subsection("load_button_style")
    try:
        style = get_current_style(style_code, mode_code)
        css = CSS_TEMPLATES["button"].format(**style)
        css += CSS_TEMPLATES["toolbar"].format(**style)
        return css
    except Exception as e:
        log_exception("Error loading button stylesheet", e)
        return ""

def load_active_button_style(style_code=None, mode_code=None):
    """
    Loads the stylesheet for active buttons.
    """
    log_section("form_styles.py")
    log_subsection("load_active_button_style")
    try:
        style = get_current_style(style_code, mode_code)
        if "active_button" in CSS_TEMPLATES:
            return CSS_TEMPLATES["active_button"].format(**style)
        else:
            return CSS_TEMPLATES["button"].format(**style)
    except Exception as e:
        log_exception("Error loading active button stylesheet", e)
        return ""

def load_form_style(style_code=None, mode_code=None):
    """
    Loads the stylesheet for forms and input fields.
    """
    log_section("form_styles.py")
    log_subsection("load_form_style")
    try:
        style = get_current_style(style_code, mode_code)
        return CSS_TEMPLATES["form"].format(**style)
    except Exception as e:
        log_exception("Error loading form stylesheet", e)
        return ""
```

#### 6.5.2 Panels

##### 6.5.2.1 navigation_panel.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception

class NavigationPanel(QWidget):
    """
    Centralized navigation panel widget.
    Applies global style from preferences.
    All button labels are translated via translator.py.
    """

    def __init__(self, translator, nav_keys=None, parent=None, start_window=None, help_panel=None):
        """
        Initializes the navigation panel with translated buttons.
        nav_keys: List of label_keys for navigation buttons.
        start_window: Reference to the StartWindow instance for back navigation.
        help_panel: Reference to the HelpPanel instance for updating help text.
        """
        log_section("navigation_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.start_window = start_window
            self.project_window = parent  # Save reference to the actual ProjectWindow
            self.help_panel = help_panel
            self.setStyleSheet(load_form_style())

            layout = QVBoxLayout(self)
            layout.setContentsMargins(12, 12, 12, 12)
            layout.setSpacing(14)  # slightly larger spacing

            self.buttons = {}
            if nav_keys is None:
                # Use keys from translations.json for project navigation
                nav_keys = [
                    "botn_fo_01",  # Project
                    "botn_fo_05",  # Main Characters
                    "botn_fo_06",  # Supporting Characters
                    "botn_fo_07",  # Groups
                    "botn_fo_08",  # Locations
                    "botn_fo_09",  # Objects
                    "botn_fo_10"   # Back
                ]

            # Add all buttons except the last one (Back) at the top
            for key in nav_keys[:-1]:
                btn = QPushButton(self.translator.tr(key), self)
                btn.setObjectName(key)
                self.buttons[key] = btn
                layout.addWidget(btn)
                # Connect navigation buttons to update help panel
                btn.clicked.connect(lambda checked, k=key: self.update_help_panel(k))

            # Add a stretch to push the last button to the bottom
            layout.addStretch()

            # Add the last button (Back) at the bottom
            back_key = nav_keys[-1]
            back_btn = QPushButton(self.translator.tr(back_key), self)
            back_btn.setObjectName(back_key)
            self.buttons[back_key] = back_btn
            layout.addWidget(back_btn)

            # Connect back button to close project window and show start window
            back_btn.clicked.connect(self.go_back_to_start)

            self.setLayout(layout)
            log_info("NavigationPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing NavigationPanel", e)

    def go_back_to_start(self):
        """
        Closes the project window and shows the start window.
        """
        try:
            if self.start_window is not None and self.project_window is not None:
                self.project_window.close()
                self.start_window.show()
                log_info("Returned to StartWindow from ProjectWindow.")
        except Exception as e:
            log_exception("Error returning to StartWindow", e)

    def update_help_panel(self, nav_key):
        """
        Updates the help panel based on the navigation key.
        """
        if self.help_panel is not None:
            # Map navigation keys to help topics
            nav_to_topic = {
                "botn_fo_01": "projects",
                "botn_fo_05": "characters",
                "botn_fo_08": "locations",
                "botn_fo_09": "objects"
            }
            topic = nav_to_topic.get(nav_key)
            if topic:
                self.help_panel.update_translations(topic)

    def update_translations(self):
        """
        Updates all button texts after a language change.
        """
        for key, btn in self.buttons.items():
            btn.setText(self.translator.tr(key))
```

##### 6.5.2.2 help_panel.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception

class HelpPanel(QWidget):
    """
    Centralized help panel widget.
    Applies global style from preferences.
    All labels and help texts are translated via translator.py.
    """

    def __init__(self, translator, help_key="help_pr_01", parent=None):
        """
        Initializes the help panel with translated title and help text.
        help_key: Key for the help text in translations.json (e.g. 'help_pr_01').
        """
        log_section("help_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.help_key = help_key
            self.setStyleSheet(load_form_style())

            layout = QVBoxLayout(self)
            layout.setContentsMargins(24, 24, 24, 24)
            layout.setSpacing(16)

            # Title label (translated, now dynamic)
            self.title_label = QLabel(self.translator.tr("help_wi_01"), self)
            self.title_label.setObjectName("helpPanelTitleLabel")
            layout.addWidget(self.title_label)

            # Help text (translated)
            self.help_text = QTextEdit(self)
            self.help_text.setReadOnly(True)
            self.help_text.setObjectName("helpPanelText")
            self.help_text.setText(self.translator.tr(self.help_key))
            layout.addWidget(self.help_text)

            layout.addStretch()
            self.setLayout(layout)
            log_info("HelpPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing HelpPanel", e)

    def update_translations(self, help_key=None):
        """
        Updates all labels and help text after a language change or help topic change.
        If help_key is given, updates to the new help topic.
        Supports shortcut keys for common help topics and dynamic titles.
        """
        # Map shortcut topic names to translation keys and titles
        topic_map = {
            "projects": ("help_pr_02", "help_wi_02"),
            "characters": ("help_pr_03", "help_wi_03"),
            "objects": ("help_pr_04", "help_wi_04"),
            "locations": ("help_pr_05", "help_wi_05")
        }
        if help_key is not None:
            # Allow both direct translation keys and shortcut topic names
            if help_key in topic_map:
                self.help_key, title_key = topic_map[help_key]
                self.title_label.setText(self.translator.tr(title_key))
            else:
                self.help_key = help_key
                self.title_label.setText(self.translator.tr("help_wi_01"))
        else:
            # Default title
            self.title_label.setText(self.translator.tr("help_wi_01"))
        self.help_text.setText(self.translator.tr(self.help_key))
```

##### 6.5.2.3 center_panel.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QStackedWidget
from gui.styles.form_styles import load_form_style
from gui.widgets.form_toolbar import FormToolbar
from gui.widgets.form_center_start import FormCenterStart
from gui.widgets.form_projects import FormProjects
from gui.widgets.form_characters import FormCharacters
from gui.widgets.form_locations import FormLocations
from gui.widgets.form_objects import FormObjects
from core.logger import log_section, log_subsection, log_info, log_exception

class CenterPanel(QWidget):
    """
    Central panel widget for main content area.
    Shows FormCenterStart on first launch, then dynamically displays the correct toolbar,
    heading, and form fields for each form type.
    All styles and formatting are loaded from the central style modules.
    """

    # Mapping for header translation keys
    HEADER_KEYS = {
        "projects": "proj_ma_01",
        "characters": "char_ma_01",
        "locations": "help_wi_05",
        "objects": "proj_ob_01"
    }

    def __init__(self, translator, parent=None):
        """
        Initializes the center panel with a stacked widget for dynamic content.
        Adds all available forms and shows the start/empty form initially.
        """
        log_section("center_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            self.layout = QVBoxLayout(self)
            self.layout.setContentsMargins(24, 24, 24, 24)
            self.layout.setSpacing(18)

            # Stacked widget for switching between forms
            self.stacked_widget = QStackedWidget(self)
            self.layout.addWidget(self.stacked_widget)
            self.setLayout(self.layout)

            # Dictionary to hold form widgets
            self.forms = {}

            # Add all available forms
            self.add_form("center_start", FormCenterStart(parent=self))
            self.add_form("projects", FormProjects(self.translator, parent=self))
            self.add_form("characters", FormCharacters(self.translator, parent=self))
            self.add_form("locations", FormLocations(self.translator, parent=self))
            self.add_form("objects", FormObjects(self.translator, parent=self))

            # Show the start/empty form initially
            self.stacked_widget.setCurrentWidget(self.forms["center_start"])

            log_info("CenterPanel initialized successfully and shows FormCenterStart.")
        except Exception as e:
            log_exception("Error initializing CenterPanel", e)

    def add_form(self, form_type, form_widget):
        """
        Adds a form widget to the stacked widget and keeps a reference for switching.
        """
        self.forms[form_type] = form_widget
        self.stacked_widget.addWidget(form_widget)

    def show_form(self, form_type):
        """
        Shows the selected form in the stacked widget.
        Dynamically adds toolbar and heading above the form fields.
        Uses correct translation keys for headings.
        """
        if form_type not in self.forms:
            log_info(f"Form type '{form_type}' not found in CenterPanel.")
            return

        # Remove previous toolbar and heading if present
        for i in reversed(range(self.layout.count())):
            item = self.layout.itemAt(i)
            widget = item.widget()
            if widget and widget != self.stacked_widget:
                self.layout.removeWidget(widget)
                widget.setParent(None)

        # Do not show toolbar or heading for the start/empty form
        if form_type != "center_start":
            # Dynamically create toolbar for the form
            toolbar = FormToolbar(self.translator, form_prefix=form_type, parent=self)
            self.layout.insertWidget(0, toolbar)

            # Use correct translation key for heading
            header_key = self.HEADER_KEYS.get(form_type, "")
            heading_label = QLabel(self.translator.tr(header_key), self)
            heading_label.setObjectName("FormHeadingLabel")
            heading_label.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 12px;")
            self.layout.insertWidget(1, heading_label)

        # Show the form
        form_widget = self.forms[form_type]
        self.stacked_widget.setCurrentWidget(form_widget)

    def show_empty(self):
        """
        Shows the initial empty form (FormCenterStart).
        Removes any toolbar or heading.
        """
        for i in reversed(range(self.layout.count())):
            item = self.layout.itemAt(i)
            widget = item.widget()
            if widget and widget != self.stacked_widget:
                self.layout.removeWidget(widget)
                widget.setParent(None)
        self.stacked_widget.setCurrentWidget(self.forms["center_start"])

    def update_translations(self):
        """
        Updates all labels, headings, and toolbars after a language change.
        """
        for form in self.forms.values():
            if hasattr(form, "update_translations"):
                form.update_translations()
        # Update toolbar and heading for the current form
        current_index = self.stacked_widget.currentIndex()
        current_form_type = list(self.forms.keys())[current_index] if current_index >= 0 and current_index < len(self.forms) else None
        if current_form_type:
            self.show_form(current_form_type)
```

#### 6.5.3 Widgets

##### 6.5.3.1 form_toolbar.py

```python
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from gui.styles.form_styles import load_button_style
from core.logger import log_section, log_subsection, log_info, log_exception

class FormToolbar(QWidget):
    """
    Centralized toolbar widget for forms.
    Applies global button styles from preferences.
    All button labels are translated via translator.py.
    No local styles or translations are used.
    """

    BUTTON_KEY_MAP = {
        "projects": [
            "botn_pr_01", "botn_pr_05", "botn_pr_02", "botn_pr_03", "botn_pr_04"
        ],
        "locations": [
            "botn_lo_01", "botn_lo_05", "botn_lo_02", "botn_lo_03", "botn_lo_04"
        ],
        "objects": [
            "botn_ob_01", "botn_ob_05", "botn_ob_02", "botn_ob_03", "botn_ob_04"
        ],
        "characters": [
            "botn_ch_01", "botn_ch_05", "botn_ch_02", "botn_ch_03", "botn_ch_04"
        ],
        "chapters": [
            "botn_ch_01", "botn_ch_05", "botn_ch_02", "botn_ch_03", "botn_ch_04"
        ],
        "scenes": [
            "botn_sc_01", "botn_sc_05", "botn_sc_02", "botn_sc_03", "botn_sc_04"
        ],
        "storylines": [
            "botn_sl_01", "botn_sl_05", "botn_sl_02", "botn_sl_03", "botn_sl_04"
        ],
        "groups": [
            "botn_cp_01", "botn_cp_05", "botn_cp_02", "botn_cp_03", "botn_cp_04"
        ]
    }

    def __init__(self, translator, form_prefix, parent=None):
        """
        Initializes the toolbar with translated buttons for form actions.
        """
        log_section("form_toolbar.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_button_style())

            layout = QHBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(10)

            # Use correct button keys for the form type
            self.button_keys = self.BUTTON_KEY_MAP.get(form_prefix, [])
            self.buttons = {}

            for key in self.button_keys:
                btn = QPushButton(self.translator.tr(key), self)
                btn.setObjectName(key)
                self.buttons[key] = btn
                layout.addWidget(btn)

            layout.addStretch()
            self.setLayout(layout)
            log_info("FormToolbar initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormToolbar", e)

    def update_translations(self):
        """
        Updates all button texts after a language change.
        """
        for key, btn in self.buttons.items():
            btn.setText(self.translator.tr(key))
```

##### 6.5.3.2 base_form_widget.py

```python
import json
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QSpinBox, QDateEdit, QComboBox, QCheckBox
)
from PySide6.QtCore import Qt
from gui.widgets.form_toolbar import FormToolbar
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception

class BaseFormWidget(QWidget):
    """
    Generic form widget: loads all fields and labels from form_fields.json,
    translates all labels and options dynamically via translator.py,
    updates labels and options after language change.
    All styles are applied centrally via form_styles.py.
    Field-specific settings (e.g. width) are applied if present.
    """

    def __init__(self, title, fields, toolbar_actions, form_prefix, translator, parent=None):
        """
        Initializes the form widget with dynamic fields, translations, and toolbar.
        Applies field-specific settings such as width if defined in fields.
        """
        log_section("base_form_widget.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            main_layout = QVBoxLayout(self)
            main_layout.setSpacing(12)

            # Toolbar always shown
            self.toolbar = FormToolbar(self.translator, form_prefix, self)
            main_layout.addWidget(self.toolbar)
            if toolbar_actions:
                toolbar_actions(self.toolbar)

            self.form_layout = QFormLayout()
            self.inputs = {}
            self.labels = {}
            self.option_keys = {}

            # Store fields for translation updates
            self._fields = fields

            for field in fields:
                if field.get("type") == "header":
                    header_text = self.translator.tr(field["label_key"])
                    header_label = QLabel(header_text if header_text else field.get("default_label", ""), self)
                    header_label.setObjectName("FormHeaderLabel")
                    header_label.setProperty("header", True)
                    self.form_layout.addRow(header_label)
                    continue

                label_text = self.translator.tr(field["label_key"])
                label = QLabel(label_text if label_text else field.get("default_label", ""), self)
                label.setProperty("label_key", field["label_key"])
                self.labels[field["name"]] = label
                input_widget = None

                # --- Widget creation with field-specific settings ---
                if field["type"] == "text":
                    input_widget = QLineEdit(self)
                    if "max_length" in field:
                        input_widget.setMaxLength(field["max_length"])
                    if "width" in field:
                        input_widget.setFixedWidth(field["width"])
                elif field["type"] == "spin":
                    input_widget = QSpinBox(self)
                    if "max" in field:
                        input_widget.setMaximum(field["max"])
                    if "min" in field:
                        input_widget.setMinimum(field["min"])
                    if "width" in field:
                        input_widget.setFixedWidth(field["width"])
                elif field["type"] == "date":
                    input_widget = QDateEdit(self)
                    if "width" in field:
                        input_widget.setFixedWidth(field["width"])
                elif field["type"] == "select":
                    input_widget = QComboBox(self)
                    self.option_keys[field["name"]] = []
                    for option in field.get("options", []):
                        option_label = self.translator.tr(option.get("label_key", str(option)))
                        input_widget.addItem(option_label)
                        self.option_keys[field["name"]].append(option.get("label_key", option_label))
                    if "width" in field:
                        input_widget.setFixedWidth(field["width"])
                elif field["type"] == "display":
                    input_widget = QLabel("", self)
                    if "width" in field:
                        input_widget.setFixedWidth(field["width"])
                elif field["type"] == "checkbox":
                    input_widget = QCheckBox(self)
                    if "width" in field:
                        input_widget.setFixedWidth(field["width"])
                else:
                    input_widget = QLineEdit(self)
                    if "width" in field:
                        input_widget.setFixedWidth(field["width"])

                self.inputs[field["name"]] = input_widget
                self.form_layout.addRow(label, input_widget)

            main_layout.addLayout(self.form_layout)
            main_layout.addStretch()
            self.setLayout(main_layout)
            log_info("BaseFormWidget initialized successfully.")
        except Exception as e:
            log_exception("Error initializing BaseFormWidget", e)

    def update_translations(self):
        """
        Updates all labels and option texts after a language change.
        """
        try:
            for field in self._fields:
                field_name = field["name"]
                if field.get("type") == "header":
                    # Update header label
                    for i in range(self.form_layout.count()):
                        item = self.form_layout.itemAt(i)
                        widget = item.widget()
                        if isinstance(widget, QLabel) and widget.property("header"):
                            widget.setText(self.translator.tr(field["label_key"]))
                else:
                    label = self.labels.get(field_name)
                    if label:
                        label.setText(self.translator.tr(field["label_key"]))
                    input_widget = self.inputs.get(field_name)
                    if isinstance(input_widget, QComboBox) and field_name in self.option_keys:
                        input_widget.blockSignals(True)
                        input_widget.clear()
                        for option_label_key in self.option_keys[field_name]:
                            input_widget.addItem(self.translator.tr(option_label_key))
                        input_widget.blockSignals(False)
            log_info("BaseFormWidget translations updated.")
        except Exception as e:
            log_exception("Error updating translations in BaseFormWidget", e)
```

##### 6.5.3.3 form_chapters.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import FORM_FIELDS_FILE
import json

class FormChapters(QWidget):
    """
    FormChapters widget for editing project chapters.
    Loads field definitions from form_fields.json,
    applies global styles from preferences,
    translates all labels and options via translator.py,
    and updates translations after language change.
    All formatting and styles are centralized.
    """

    def __init__(self, translator, toolbar_actions=None, parent=None):
        """
        Initializes the chapters form with dynamic fields and translations.
        """
        log_section("form_chapters.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            # Load chapter fields from form_fields.json
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                fields_config = json.load(f)
            chapter_fields = fields_config.get("project_chapters", [])

            # Create the base form widget
            self.form_widget = BaseFormWidget(
                title=self.translator.tr("Chapter"),
                fields=chapter_fields,
                toolbar_actions=toolbar_actions,
                form_prefix="chapter",
                translator=self.translator,
                parent=self
            )

            layout = QVBoxLayout(self)
            layout.addWidget(self.form_widget)
            layout.addStretch()
            self.setLayout(layout)
            log_info("FormChapters initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormChapters", e)

    def update_translations(self):
        """
        Updates all labels and option texts after a language change.
        """
        self.form_widget.update_translations()
```

##### 6.5.3.4 form_characters.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import FORM_FIELDS_FILE
import json

class FormCharacters(QWidget):
    """
    FormCharacters widget for editing character data.
    Loads field definitions from form_fields.json,
    applies global styles from preferences,
    translates all labels and options via translator.py,
    and updates translations after language change.
    All formatting and styles are centralized.
    Robust error handling is implemented for file and JSON operations.
    """

    def __init__(self, translator, toolbar_actions=None, parent=None):
        """
        Initializes the characters form with dynamic fields and translations.
        """
        log_section("form_characters.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            # Load character fields from form_fields.json with robust error handling
            try:
                with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                    fields_config = json.load(f)
                character_fields = fields_config.get("character_main", [])
            except FileNotFoundError as fnf_error:
                log_exception("form_fields.json not found for FormCharacters.", fnf_error)
                character_fields = []
            except json.JSONDecodeError as json_error:
                log_exception("JSON decode error in form_fields.json for FormCharacters.", json_error)
                character_fields = []
            except Exception as e:
                log_exception("Unexpected error loading character fields in FormCharacters.", e)
                character_fields = []

            # Create the base form widget
            self.form_widget = BaseFormWidget(
                title=self.translator.tr("char_ma_header"),
                fields=character_fields,
                toolbar_actions=toolbar_actions,
                form_prefix="char_ma",
                translator=self.translator,
                parent=self
            )

            layout = QVBoxLayout(self)
            layout.addWidget(self.form_widget)
            layout.addStretch()
            self.setLayout(layout)
            log_info("FormCharacters initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormCharacters", e)

    def update_translations(self):
        """
        Updates all labels and option texts after a language change.
        """
        try:
            self.form_widget.update_translations()
        except Exception as e:
            log_exception("Error updating translations in FormCharacters", e)
```

##### 6.5.3.5 form_locations.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import FORM_FIELDS_FILE
import json

class FormLocations(QWidget):
    """
    FormLocations widget for editing location data.
    Loads field definitions from form_fields.json,
    applies global styles from preferences,
    translates all labels and options via translator.py,
    and updates translations after language change.
    All formatting and styles are centralized.
    Robust error handling is implemented for file and JSON operations.
    """

    def __init__(self, translator, toolbar_actions=None, parent=None):
        """
        Initializes the locations form with dynamic fields and translations.
        """
        log_section("form_locations.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            # Load location fields from form_fields.json with robust error handling
            try:
                with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                    fields_config = json.load(f)
                location_fields = fields_config.get("project_locations", [])
            except FileNotFoundError as fnf_error:
                log_exception("form_fields.json not found for FormLocations.", fnf_error)
                location_fields = []
            except json.JSONDecodeError as json_error:
                log_exception("JSON decode error in form_fields.json for FormLocations.", json_error)
                location_fields = []
            except Exception as e:
                log_exception("Unexpected error loading location fields in FormLocations.", e)
                location_fields = []

            # Create the base form widget
            self.form_widget = BaseFormWidget(
                title=self.translator.tr("proj_lo_header"),
                fields=location_fields,
                toolbar_actions=toolbar_actions,
                form_prefix="proj_lo",
                translator=self.translator,
                parent=self
            )

            layout = QVBoxLayout(self)
            layout.addWidget(self.form_widget)
            layout.addStretch()
            self.setLayout(layout)
            log_info("FormLocations initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormLocations", e)

    def update_translations(self):
        """
        Updates all labels and option texts after a language change.
        """
        try:
            self.form_widget.update_translations()
        except Exception as e:
            log_exception("Error updating translations in FormLocations", e)
```

##### 6.5.3.6 form_objects.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import FORM_FIELDS_FILE
import json

class FormObjects(QWidget):
    """
    FormObjects widget for editing object data.
    Loads field definitions from form_fields.json,
    applies global styles from preferences,
    translates all labels and options via translator.py,
    and updates translations after language change.
    All formatting and styles are centralized.
    Robust error handling is implemented for file and JSON operations.
    """

    def __init__(self, translator, toolbar_actions=None, parent=None):
        """
        Initializes the objects form with dynamic fields and translations.
        """
        log_section("form_objects.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            # Load object fields from form_fields.json with robust error handling
            try:
                with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                    fields_config = json.load(f)
                object_fields = fields_config.get("project_objects", [])
            except FileNotFoundError as fnf_error:
                log_exception("form_fields.json not found for FormObjects.", fnf_error)
                object_fields = []
            except json.JSONDecodeError as json_error:
                log_exception("JSON decode error in form_fields.json for FormObjects.", json_error)
                object_fields = []
            except Exception as e:
                log_exception("Unexpected error loading object fields in FormObjects.", e)
                object_fields = []

            # Create the base form widget
            self.form_widget = BaseFormWidget(
                title=self.translator.tr("proj_ob_header"),
                fields=object_fields,
                toolbar_actions=toolbar_actions,
                form_prefix="proj_ob",
                translator=self.translator,
                parent=self
            )

            layout = QVBoxLayout(self)
            layout.addWidget(self.form_widget)
            layout.addStretch()
            self.setLayout(layout)
            log_info("FormObjects initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormObjects", e)

    def update_translations(self):
        """
        Updates all labels and option texts after a language change.
        """
        try:
            self.form_widget.update_translations()
        except Exception as e:
            log_exception("Error updating translations in FormObjects", e)
```

##### 6.5.3.7 form_projects.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import FORM_FIELDS_FILE
import json

class FormProjects(QWidget):
    """
    FormProjects widget for editing project data.
    Loads field definitions from form_fields.json,
    applies global styles from preferences,
    translates all labels and options via translator.py,
    and updates translations after language change.
    All formatting and styles are centralized.
    Robust error handling is implemented for file and JSON operations.
    """

    def __init__(self, translator, toolbar_actions=None, parent=None):
        """
        Initializes the projects form with dynamic fields and translations.
        """
        log_section("form_projects.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            # Load project fields from form_fields.json with robust error handling
            try:
                with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                    fields_config = json.load(f)
                project_fields = fields_config.get("projects", [])
            except FileNotFoundError as fnf_error:
                log_exception("form_fields.json not found for FormProjects.", fnf_error)
                project_fields = []
            except json.JSONDecodeError as json_error:
                log_exception("JSON decode error in form_fields.json for FormProjects.", json_error)
                project_fields = []
            except Exception as e:
                log_exception("Unexpected error loading project fields in FormProjects.", e)
                project_fields = []

            # Create the base form widget
            self.form_widget = BaseFormWidget(
                title=self.translator.tr("proj_ma_header"),
                fields=project_fields,
                toolbar_actions=toolbar_actions,
                form_prefix="proj_ma",
                translator=self.translator,
                parent=self
            )

            layout = QVBoxLayout(self)
            layout.addWidget(self.form_widget)
            layout.addStretch()
            self.setLayout(layout)
            log_info("FormProjects initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormProjects", e)

    def update_translations(self):
        """
        Updates all labels and option texts after a language change.
        """
        try:
            self.form_widget.update_translations()
        except Exception as e:
            log_exception("Error updating translations in FormProjects", e)
```

##### 6.5.3.8 form_scenes.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import FORM_FIELDS_FILE
import json

class FormScenes(QWidget):
    """
    FormScenes widget for editing scene data.
    Loads field definitions from form_fields.json,
    applies global styles from preferences,
    translates all labels and options via translator.py,
    and updates translations after language change.
    All formatting and styles are centralized.
    """

    def __init__(self, translator, toolbar_actions=None, parent=None):
        """
        Initializes the scenes form with dynamic fields and translations.
        """
        log_section("form_scenes.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            # Load scene fields from form_fields.json
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                fields_config = json.load(f)
            scene_fields = fields_config.get("project_chapters_scenes", [])

            # Create the base form widget
            self.form_widget = BaseFormWidget(
                title=self.translator.tr("Scene"),
                fields=scene_fields,
                toolbar_actions=toolbar_actions,
                form_prefix="scene",
                translator=self.translator,
                parent=self
            )

            layout = QVBoxLayout(self)
            layout.addWidget(self.form_widget)
            layout.addStretch()
            self.setLayout(layout)
            log_info("FormScenes initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormScenes", e)

    def update_translations(self):
        """
        Updates all labels and option texts after a language change.
        """
        self.form_widget.update_translations()
```

##### 6.5.3.9 form_storylines.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import FORM_FIELDS_FILE
import json

class FormStorylines(QWidget):
    """
    FormStorylines widget for editing storylines data.
    Loads field definitions from form_fields.json,
    applies global styles from preferences,
    translates all labels and options via translator.py,
    and updates translations after language change.
    All formatting and styles are centralized.
    """

    def __init__(self, translator, toolbar_actions=None, parent=None):
        """
        Initializes the storylines form with dynamic fields and translations.
        """
        log_section("form_storylines.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            # Load storyline fields from form_fields.json
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                fields_config = json.load(f)
            storyline_fields = fields_config.get("project_storylines", [])

            # Create the base form widget
            self.form_widget = BaseFormWidget(
                title=self.translator.tr("Storyline"),
                fields=storyline_fields,
                toolbar_actions=toolbar_actions,
                form_prefix="storyline",
                translator=self.translator,
                parent=self
            )

            layout = QVBoxLayout(self)
            layout.addWidget(self.form_widget)
            layout.addStretch()
            self.setLayout(layout)
            log_info("FormStorylines initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormStorylines", e)

    def update_translations(self):
        """
        Updates all labels and option texts after a language change.
        """
        self.form_widget.update_translations()
```

##### 6.5.3.10 form_center_start.py
```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from gui.styles.form_styles import load_form_style

class FormCenterStart(QWidget):
    """
    Placeholder widget for the initial empty state of CenterPanel.
    Displays a message or nothing until a form is selected.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(load_form_style())
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(18)
        # Show placeholder text in the center
        label = QLabel("Hier Inhalte ergänzen", self)
        label.setObjectName("CenterStartLabel")
        label.setStyleSheet("font-size: 18px; color: #888; margin-top: 120px;")
        layout.addWidget(label)
        layout.addStretch()
        self.setLayout(layout)
```

#### 6.5.4 Fenster
##### 6.5.4.1 start_window.py

```python
import sys
import json
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QColor, QPixmap, QPainter
from PySide6.QtCore import QTimer
from gui.preferences import PreferencesWindow
from core.translator import Translator
from gui.project_window import ProjectWindow
from gui.styles.form_styles import load_button_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import BG_IMAGE_PATH, USER_SETTINGS_FILE
from config.settings import load_settings

class StartWindow(QWidget):
    """
    Main window for CSNova application.
    Handles initialization, button layout, translations, and saving window settings.
    Robust error handling is implemented for all UI and file operations.
    """
    def __init__(self, default_language="en"):
        """
        Initializes the StartWindow.
        Loads settings, sets up translations, window size, background, and buttons.
        """
        log_section("start_window.py")
        log_subsection("__init__")
        try:
            super().__init__()
            self.settings = load_settings()
            lang = self.settings.get("language", default_language)
            self.translator = Translator(lang)
            self.setWindowTitle(self.translator.tr("WinStartTitle"))
            # Set window size from settings
            res = self.settings.get("screen_resolution", "1920x1080")
            w, h = [int(x) for x in res.split("x")]
            self.resize(w, h)
            self.setAutoFillBackground(False)
            try:
                self.bg_pixmap = QPixmap(str(BG_IMAGE_PATH))
            except Exception as e:
                log_exception("Error loading background image", e)
                self.bg_pixmap = QPixmap(w, h)
            self.pref_window = None
            # Load button layout values from settings
            self.BUTTON_WIDTH      = self.settings.get("start_window_bnt_width", 240)
            self.BUTTON_HEIGHT     = self.settings.get("start_window_bnt_height", 60)
            self.BUTTON_TOP_OFFSET = self.settings.get("start_window_bnt_top_offset", 270)
            self.BUTTON_LEFT_OFFSET= self.settings.get("start_window_bnt_left_offset", 1350)
            self.BUTTON_SPACING    = self.settings.get("start_window_bnt_spacing", 42)
            self._create_ui()
            self._retranslate_and_position()
            log_info("StartWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing StartWindow", e)

    def _create_ui(self):
        """
        Creates all main buttons for the start window and connects their signals.
        Applies drop shadow effects for better visuals.
        Robust error handling for UI creation.
        """
        log_subsection("_create_ui")
        try:
            self.button_keys = [
                "botn_st_01",
                "botn_st_02",
                "botn_st_03",
                "botn_st_04",
                "botn_st_05"
            ]
            self.buttons = []
            for key in self.button_keys:
                btn = QPushButton(parent=self)
                try:
                    shadow = QGraphicsDropShadowEffect(btn)
                    shadow.setBlurRadius(10)
                    shadow.setXOffset(4)
                    shadow.setYOffset(4)
                    shadow.setColor(QColor(0, 0, 0, 80))
                    btn.setGraphicsEffect(shadow)
                except Exception as e:
                    log_exception("Error applying drop shadow effect", e)
                self.buttons.append(btn)
            # Connect button actions
            try:
                self.buttons[0].clicked.connect(self._new_project)
                self.buttons[1].clicked.connect(self._load_project)
                self.buttons[2].clicked.connect(self._open_preferences)
                self.buttons[3].clicked.connect(self._help)
                self.buttons[4].clicked.connect(self._exit_application)
            except Exception as e:
                log_exception("Error connecting button signals", e)
            log_info("UI created and buttons connected.")
        except Exception as e:
            log_exception("Error creating UI", e)

    def _open_preferences(self):
        """
        Opens the preferences dialog window.
        If already open, brings it to the front.
        Robust error handling for preferences window.
        """
        log_subsection("_open_preferences")
        try:
            if self.pref_window is None or not self.pref_window.isVisible():
                self.pref_window = PreferencesWindow(self)
                self.pref_window.show()
                log_info("Preferences window opened.")
            else:
                self.pref_window.raise_()
                self.pref_window.activateWindow()
                log_info("Preferences window focused.")
        except Exception as e:
            log_exception("Error opening preferences window", e)

    def _new_project(self):
        """
        Opens the project window for creating a new project.
        Hides the start window.
        Robust error handling for project window.
        """
        log_subsection("_new_project")
        try:
            log_info("Preparing new project...")
            self.project_window = ProjectWindow(translator=self.translator, parent=None, start_window=self)
            self.project_window.show()
            self.hide()
            QTimer.singleShot(100, lambda: self.hide())
            log_info("ProjectWindow shown and StartWindow hidden.")
        except Exception as e:
            log_exception("Error preparing new project", e)

    def _load_project(self):
        """
        Placeholder for loading an existing project.
        Robust error handling for load project.
        """
        log_subsection("_load_project")
        try:
            log_info("Preparing to load project...")
            # Implement loading logic here
        except Exception as e:
            log_exception("Error preparing to load project", e)

    def _help(self):
        """
        Placeholder for help and tutorial functionality.
        Robust error handling for help function.
        """
        log_subsection("_help")
        try:
            log_info("Preparing help function...")
            # Implement help logic here
        except Exception as e:
            log_exception("Error preparing help function", e)

    def _exit_application(self):
        """
        Exits the application.
        Robust error handling for application exit.
        """
        log_subsection("_exit_application")
        try:
            log_info("Exiting application...")
            QApplication.instance().quit()
        except Exception as e:
            log_exception("Error during application exit", e)

    def _on_language_changed(self, code):
        """
        Changes the application language and updates all translations.
        Robust error handling for language change.
        """
        log_subsection("_on_language_changed")
        try:
            self.translator.set_language(code)
            self.settings["language"] = code
            self._retranslate_and_position()
            log_info(f"Language changed to {code}.")
        except Exception as e:
            log_exception("Error changing language", e)

    def _retranslate_and_position(self):
        """
        Updates all button texts and window title after a language change.
        Also updates button positions.
        Robust error handling for translation and positioning.
        """
        log_subsection("_retranslate_and_position")
        try:
            for key, btn in zip(self.button_keys, self.buttons):
                btn.setText(self.translator.tr(key))
            self.setWindowTitle(self.translator.tr("WinStartTitle"))
            self.update_button_positions()
            log_info("Button texts and window title updated.")
        except Exception as e:
            log_exception("Error updating translations and positions", e)

    def paintEvent(self, event):
        """
        Paints the background image, scaled to fit the window size.
        Robust error handling for painting.
        """
        try:
            painter = QPainter(self)
            rect = self.contentsRect()
            w, h = rect.width(), rect.height()
            pw, ph = self.bg_pixmap.width(), self.bg_pixmap.height()
            scale = max(w / pw, h / ph)
            sw, sh = pw * scale, ph * scale
            x_off = rect.x() + (w - sw) / 2
            y_off = rect.y() + (h - sh) / 2
            painter.drawPixmap(
                int(x_off), int(y_off),
                int(sw),   int(sh),
                self.bg_pixmap
            )
            super().paintEvent(event)
        except Exception as e:
            log_exception("Error painting background", e)

    def resizeEvent(self, event):
        """
        Handles window resize events.
        Updates button positions and saves new window settings.
        Robust error handling for resize event.
        """
        try:
            self.update_button_positions()
            self.save_window_settings()
            super().resizeEvent(event)
        except Exception as e:
            log_exception("Error handling resize event", e)
    
    def update_translations(self):
        """
        Updates translations after a language change.
        Called by PreferencesWindow.
        Robust error handling for translation update.
        """
        try:
            self.settings = load_settings()
            lang = self.settings.get("language", "en")
            self.translator.set_language(lang)
            self._retranslate_and_position()
        except Exception as e:
            log_exception("Error updating translations in StartWindow", e)
       
    def update_button_positions(self):
        """
        Calculates and sets the positions and sizes of all buttons
        based on the current window size and scaling.
        Robust error handling for button positioning.
        """
        log_subsection("update_button_positions")
        try:
            rect = self.contentsRect()
            w, h = rect.width(), rect.height()
            pw, ph = self.bg_pixmap.width(), self.bg_pixmap.height()
            scale = max(w / pw, h / ph)
            sw, sh = pw * scale, ph * scale
            x_off = rect.x() + (w - sw) / 2 + self.BUTTON_LEFT_OFFSET * scale
            y_off = rect.y() + (h - sh) / 2 + self.BUTTON_TOP_OFFSET  * scale
            bw      = int(self.BUTTON_WIDTH   * scale)
            bh      = int(self.BUTTON_HEIGHT  * scale)
            spacing = int(self.BUTTON_SPACING * scale)
            font_px = max(10, int(bh * 0.4))
            style = load_button_style(font_px)
            for i, btn in enumerate(self.buttons):
                x = int(x_off)
                y = int(y_off + i * (bh + spacing))
                btn.setGeometry(x, y, bw, bh)
                btn.setStyleSheet(style)
            log_info("Button positions updated.")
        except Exception as e:
            log_exception("Error updating button positions", e)

    def save_window_settings(self):
        """
        Saves the current window size and button layout values to user_settings.json.
        Called after window resize.
        Robust error handling for saving window settings.
        """
        try:
            settings = load_settings()
            settings["screen_resolution"] = f"{self.width()}x{self.height()}"
            settings["start_window_bnt_width"] = self.BUTTON_WIDTH
            settings["start_window_bnt_height"] = self.BUTTON_HEIGHT
            settings["start_window_bnt_top_offset"] = self.BUTTON_TOP_OFFSET
            settings["start_window_bnt_left_offset"] = self.BUTTON_LEFT_OFFSET
            settings["start_window_bnt_spacing"] = self.BUTTON_SPACING
            with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
                json.dump(settings, f, indent=2)
            log_info("Window settings saved to user_settings.json.")
        except Exception as e:
            log_exception("Error saving window settings", e)

if __name__ == "__main__":
    """
    Main entry point for standalone execution of StartWindow.
    Initializes the application and shows the start window.
    Robust error handling for main execution.
    """
    log_section("start_window.py")
    log_subsection("__main__")
    try:
        app = QApplication(sys.argv)
        window = StartWindow()
        window.show()
        log_info("StartWindow shown.")
        sys.exit(app.exec())
    except Exception as e:
        log_exception("Error in main execution", e)
```

##### 6.5.4.2 preferences.py

```python
from PySide6.QtWidgets import (
    QDialog, QLabel, QComboBox, QPushButton,
    QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QApplication
)
from core.translator import Translator
from config.settings import load_settings, save_settings
from core.logger import log_section, log_subsection, log_info, log_exception
import json

from gui.styles.form_styles import load_global_stylesheet

class PreferencesWindow(QDialog):
    """
    PreferencesWindow: Dialog for user settings such as language, style and theme.
    All options and translations are loaded centrally from form_fields.json and translations.json.
    Styles and themes are applied immediately in the preferences window and globally.
    Robust error handling is implemented for file and UI operations.
    """

    def __init__(self, parent=None):
        log_section("preferences.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = parent.translator if parent and hasattr(parent, "translator") else Translator()
            self.setWindowTitle(self.translator.tr("PrefWinTitle"))
            self.setMinimumSize(500, 320)
            self.settings = load_settings()
            self.original_settings = self.settings.copy()  # Save original settings for cancel
            self._load_fields()
            self._init_ui()
            self._apply_current_style(global_apply=True)
            log_info("PreferencesWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing PreferencesWindow", e)

    def _load_fields(self):
        """
        Loads preference field definitions from form_fields.json.
        Robust error handling for file operations.
        """
        try:
            with open("/home/frank/Dokumente/CSNova/core/config/form_fields.json", "r", encoding="utf-8") as f:
                self.form_fields = json.load(f).get("preferences", [])
        except FileNotFoundError as fnf_error:
            log_exception("form_fields.json not found in PreferencesWindow.", fnf_error)
            self.form_fields = []
        except json.JSONDecodeError as json_error:
            log_exception("JSON decode error in form_fields.json for PreferencesWindow.", json_error)
            self.form_fields = []
        except Exception as e:
            log_exception("Unexpected error loading form_fields.json in PreferencesWindow.", e)
            self.form_fields = []

    def _init_ui(self):
        """
        Initializes all UI elements for the preferences dialog.
        All options are loaded from central sources. Layout is compact and buttons are at the bottom.
        Robust error handling for UI initialization.
        """
        log_subsection("_init_ui")
        try:
            main_layout = QVBoxLayout(self)
            main_layout.setSpacing(8)
            main_layout.setContentsMargins(24, 18, 24, 18)

            self.combos = {}
            self.labels = {}

            # Dynamically create fields from form_fields.json
            for field in self.form_fields:
                label = QLabel(self.translator.tr(field.get("label_key", "")), self)
                combo = QComboBox(self)
                option_labels = []
                option_keys = []
                for opt in field.get("options", []):
                    option_labels.append(self.translator.tr(opt.get("label_key", "")))
                    option_keys.append(opt.get("key", ""))
                combo.addItems(option_labels)
                # Set current value from settings
                current_value = self.settings.get(field.get("datafield_name", "").replace("preference_", ""), option_keys[0] if option_keys else "")
                try:
                    idx = option_keys.index(current_value)
                except ValueError:
                    idx = 0
                combo.setCurrentIndex(idx)
                main_layout.addWidget(label)
                main_layout.addWidget(combo)
                self.combos[field.get("name", "")] = (combo, option_keys)
                self.labels[field.get("name", "")] = label

                # Connect style and theme changes to handlers
                if field.get("name", "") == "style":
                    combo.currentIndexChanged.connect(self._on_style_changed)
                if field.get("name", "") == "theme":
                    combo.currentIndexChanged.connect(self._on_theme_changed)

            main_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

            # Action buttons at the bottom
            btn_layout = QHBoxLayout()
            btn_layout.setSpacing(15)
            btn_layout.setContentsMargins(0, 0, 0, 0)
            self.save_btn = QPushButton(self.translator.tr("PreferenceActionSave"), self)
            self.cancel_btn = QPushButton(self.translator.tr("PreferenceActionCancel"), self)
            btn_layout.addStretch(1)
            btn_layout.addWidget(self.save_btn)
            btn_layout.addWidget(self.cancel_btn)
            btn_layout.addStretch(1)
            main_layout.addLayout(btn_layout)

            self.setLayout(main_layout)

            # Connect signals to slots for user interaction
            self.save_btn.clicked.connect(self._on_save)
            self.cancel_btn.clicked.connect(self._on_cancel)
            # Language change updates translations
            if "language" in self.combos:
                self.combos["language"][0].currentIndexChanged.connect(self._on_language_changed)
            log_info("UI initialized successfully.")
        except Exception as e:
            log_exception("Error initializing UI in PreferencesWindow", e)

    def _apply_current_style(self, global_apply=False):
        """
        Applies the currently selected style and theme to the preferences window.
        If global_apply is True, applies the style globally to the application.
        Robust error handling for stylesheet application.
        """
        try:
            style = self.settings.get("style", "modern")
            mode = self.settings.get("mode", "light")
            stylesheet = load_global_stylesheet(style, mode)
            self.setStyleSheet(stylesheet)
            if global_apply:
                QApplication.instance().setStyleSheet(stylesheet)
        except Exception as e:
            log_exception("Error applying stylesheet in PreferencesWindow", e)

    def update_translations(self):
        """
        Updates all UI texts after a language change.
        Also updates translated items in all comboboxes.
        Robust error handling for translation updates.
        """
        try:
            self.setWindowTitle(self.translator.tr("PrefWinTitle"))
            for field in self.form_fields:
                name = field.get("name", "")
                self.labels[name].setText(self.translator.tr(field.get("label_key", "")))
                combo, option_keys = self.combos[name]
                combo.blockSignals(True)
                combo.clear()
                for opt in field.get("options", []):
                    combo.addItem(self.translator.tr(opt.get("label_key", "")))
                # Set current value from settings
                current_value = self.settings.get(field.get("datafield_name", "").replace("preference_", ""), option_keys[0] if option_keys else "")
                try:
                    idx = option_keys.index(current_value)
                except ValueError:
                    idx = 0
                combo.setCurrentIndex(idx)
                combo.blockSignals(False)
            self.save_btn.setText(self.translator.tr("PreferenceActionSave"))
            self.cancel_btn.setText(self.translator.tr("PreferenceActionCancel"))
            self._apply_current_style(global_apply=True)
        except Exception as e:
            log_exception("Error updating translations in PreferencesWindow", e)

    def _on_save(self):
        """
        Saves the selected settings and closes the dialog.
        Notifies parent window to update translations if possible.
        Robust error handling for saving settings.
        """
        log_subsection("_on_save")
        try:
            for field in self.form_fields:
                name = field.get("name", "")
                combo, option_keys = self.combos[name]
                self.settings[field.get("datafield_name", "").replace("preference_", "")] = option_keys[combo.currentIndex()]
            save_settings(self.settings)
            # Notify parent to update translations if method exists
            if hasattr(self.parent(), "update_translations"):
                self.parent().update_translations()
            self._apply_current_style(global_apply=True)
            self.accept()
            log_info("Settings saved and dialog accepted.")
        except Exception as e:
            log_exception("Error saving settings in PreferencesWindow", e)

    def _on_cancel(self):
        """
        Cancels the dialog and reverts any unsaved changes.
        Restores original settings and translations.
        Robust error handling for cancel operation.
        """
        log_subsection("_on_cancel")
        try:
            self.settings = self.original_settings.copy()
            # Restore original language in translator
            original_lang = self.original_settings.get("language", "de")
            self.translator.set_language(original_lang)
            self.update_translations()
            self._apply_current_style(global_apply=True)
            self.reject()
            log_info("Dialog canceled and settings reverted.")
        except Exception as e:
            log_exception("Error canceling PreferencesWindow", e)

    def _on_language_changed(self, idx):
        """
        Handles language change event and updates translations.
        Sets the language immediately in settings.
        Robust error handling for language change.
        """
        log_subsection("_on_language_changed")
        try:
            combo, option_keys = self.combos["language"]
            lang_code = option_keys[idx]
            self.translator.set_language(lang_code)
            self.settings["language"] = lang_code  # Set immediately!
            self.update_translations()
            log_info(f"Language changed to {lang_code}.")
        except Exception as e:
            log_exception("Error changing language in PreferencesWindow", e)

    def _on_style_changed(self, idx):
        """
        Applies the selected style immediately to the preferences window and globally.
        Robust error handling for style change.
        """
        log_subsection("_on_style_changed")
        try:
            combo, option_keys = self.combos["style"]
            style_key = option_keys[idx].replace("style_", "")
            self.settings["style"] = style_key
            mode = self.settings.get("mode", "light")
            self._apply_current_style(global_apply=True)
            log_info(f"Style changed to {style_key}.")
        except Exception as e:
            log_exception("Error changing style in PreferencesWindow", e)

    def _on_theme_changed(self, idx):
        """
        Applies the selected theme immediately to the preferences window and globally.
        Robust error handling for theme change.
        """
        log_subsection("_on_theme_changed")
        try:
            combo, option_keys = self.combos["theme"]
            mode_key = option_keys[idx].replace("theme_", "")
            self.settings["mode"] = mode_key
            style = self.settings.get("style", "modern")
            self._apply_current_style(global_apply=True)
            log_info(f"Theme changed to {mode_key}.")
        except Exception as e:
            log_exception("Error changing theme in PreferencesWindow", e)
```

##### 6.5.4.3 project_window.py

```python
from PySide6.QtWidgets import QWidget, QSplitter, QHBoxLayout
from PySide6.QtCore import Qt
from gui.widgets.navigation_panel import NavigationPanel
from gui.widgets.center_panel import CenterPanel
from gui.widgets.help_panel import HelpPanel
from config.settings import load_settings, save_settings
from core.logger import log_section, log_subsection, log_info, log_exception

class ProjectWindow(QWidget):
    """
    Main project window with three panels:
    - Left: NavigationPanel
    - Center: CenterPanel (main content)
    - Right: HelpPanel
    The splitter sizes are loaded from user_settings.json and saved on change.
    If missing, fallback values are used based on the current window size.
    All GUI elements are defined in form_fields.json.
    Styles and modes are set globally via preferences.py and style modules.
    Translations are handled by the globally initialized Translator.
    Robust error handling is implemented for all UI and file operations.
    """

    def __init__(self, translator, parent=None, start_window=None):
        """
        Initializes the ProjectWindow with navigation, center, and help panels.
        Loads splitter sizes and window size from user_settings.json or uses fallback values.
        Passes start_window reference to NavigationPanel for back navigation.
        Passes help_panel and center_panel references to NavigationPanel for help text and form updates.
        """
        log_section("project_window.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.settings = load_settings()
            self.start_window = start_window
            self.setWindowTitle(self.translator.tr("ProWinTitle"))

            # Use the current start window size from settings
            try:
                win_size = self.settings.get("screen_resolution", "1920x1080")
                w, h = [int(x) for x in win_size.split("x")]
                self.resize(w, h)
            except Exception as e:
                log_exception("Error reading screen resolution from settings", e)
                self.resize(1920, 1080)

            # Create center and help panels first
            try:
                self.center_panel = CenterPanel(self.translator, parent=self)
            except Exception as e:
                log_exception("Error initializing CenterPanel", e)
                self.center_panel = None

            try:
                self.help_panel = HelpPanel(self.translator, parent=self)
            except Exception as e:
                log_exception("Error initializing HelpPanel", e)
                self.help_panel = None

            # Pass help_panel and center_panel to NavigationPanel
            try:
                self.navigation_panel = NavigationPanel(
                    self.translator,
                    parent=self,
                    start_window=self.start_window,
                    help_panel=self.help_panel,
                    center_panel=self.center_panel
                )
            except Exception as e:
                log_exception("Error initializing NavigationPanel", e)
                self.navigation_panel = None

            # Create splitter for three panels
            try:
                self.splitter = QSplitter(self)
                self.splitter.setOrientation(Qt.Horizontal)
                if self.navigation_panel:
                    self.splitter.addWidget(self.navigation_panel)
                if self.center_panel:
                    self.splitter.addWidget(self.center_panel)
                if self.help_panel:
                    self.splitter.addWidget(self.help_panel)

                # Fallback for splitter sizes based on window width
                default_splitter_sizes = [
                    int(w * 0.18),  # left panel ~18%
                    int(w * 0.64),  # center panel ~64%
                    int(w * 0.18)   # right panel ~18%
                ]
                splitter_sizes = self.settings.get("splitter_sizes", default_splitter_sizes)
                self.splitter.setSizes(splitter_sizes)

                # Save splitter sizes on change
                self.splitter.splitterMoved.connect(self.save_splitter_sizes)
            except Exception as e:
                log_exception("Error initializing splitter", e)
                self.splitter = None

            # Layout
            try:
                layout = QHBoxLayout(self)
                layout.setContentsMargins(0, 0, 0, 0)
                if self.splitter:
                    layout.addWidget(self.splitter)
                self.setLayout(layout)
            except Exception as e:
                log_exception("Error initializing layout in ProjectWindow", e)

            log_info("ProjectWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing ProjectWindow", e)

    def save_splitter_sizes(self, pos, index):
        """
        Saves the current splitter sizes to user_settings.json when the splitter is moved.
        Robust error handling for saving splitter sizes.
        """
        try:
            if self.splitter:
                sizes = self.splitter.sizes()
                self.settings["splitter_sizes"] = sizes
                save_settings(self.settings)
                log_info(f"Splitter sizes saved: {sizes}")
        except Exception as e:
            log_exception("Error saving splitter sizes", e)

    def update_translations(self):
        """
        Updates translations for all panels after a language change.
        Robust error handling for translation update.
        """
        try:
            if self.navigation_panel:
                self.navigation_panel.update_translations()
            if self.center_panel:
                self.center_panel.update_translations()
            if self.help_panel:
                self.help_panel.update_translations()
        except Exception as e:
            log_exception("Error updating translations in ProjectWindow", e)
```

## 7 Vorbereitungen für die Installation unter Linux-Mint

[.gitignore](/.gitignore)

[requirements](/requirements.txt)

[pyinstaller-code](/pyinstaller.txt)

[csNova-install](/install_csnova.sh)

[Lizenz](/license.md)
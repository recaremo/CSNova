# Codices Scriptoria Nova (CSNova)

[Projektbeschreibung](/readme.md)

## 1. Hauptfunktionen

- Projektverwaltung: Anlegen, Bearbeiten und Archivieren von Buchprojekten  
- Charakterdatenbank: Haupt- und Nebentabellen (Physiognomie, Psychologie, Ausbildung, Herkunft, …)  
- Kapitel- & Szeneverwaltung inkl. Handlungsstränge, Zeitlinien, Orte, Gegenstände  
- Beziehungs- und Mindmap‑Modul (Charaktere, Gruppen, Verbindungen)  
- Statistiken & Übersichten (Steckbriefe, ToDo‑Listen, Fortschritt)  
- Integrierte Schreib‑Tipps, Genre‑Guides, Quellenverwaltung, Brainstorming‑Tools  
- Multimedia‑Integration (Bilder, Audio, Video, Animationen)  
- Export in diverse Formate (EPUB, PDF, HTML, eigenes Reader‑Format)  
- Custom Multimedia‑Reader mit responsivem Layout pro Plattform  
- KI‑Interviewfunktion für Figurenentwicklung, Plotideen, Textanalyse  
- Sprachen: Deutsch (Standard), Englisch, Französisch, Spanisch  
- Rechtschreibprüfung: Deutsch, Englisch  
- Dynamische Sprachauswahl mit automatischer Anpassung aller Menü- und UI-Texte

## 2. Projektfahrplan & Fortschritt

[ToDo](../To-Do.md)

[Projektbaum](/project_tree.md)

[Mermaid-Diagramm: Projektstruktur und Datenbank](../csNova_mermaid.mmd)

## 3. JSON Translation

```json
[
  {
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
  "proj_ma_13": "Zeitlinie"
},
{
  "proj_ch_01": "Kapitel",
  "proj_ch_02": "Kapitel-Titel",
  "proj_ch_03": "Kapitel-Prämisse"
},
{
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
  "proj_cs_12": "Notizen"
},
{
  "proj_lo_01": "Ort",
  "proj_lo_02": "Titel",
  "proj_lo_03": "Beschreibung"
},
{
  "proj_st_01": "Erzählstrang",
  "proj_st_02": "Titel",
  "proj_st_03": "Prämisse",
  "proj_st_04": "Beschreibung",
  "proj_st_05": "Transformation",
  "proj_st_06": "Zeitlinie",
  "proj_st_07": "Notizen"
},
{
  "proj_ob_01": "Objekt",
  "proj_ob_02": "Titel",
  "proj_ob_03": "Beschreibung"
},
{
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
  "char_ma_12": "Notizen"
},
{
  "char_gr_01": "Gruppe",
  "char_gr_02": "Gruppen-Titel",
  "char_gr_03": "Gruppen-Beschreibung"
},
{
  "char_or_01": "Herkunft",
  "char_or_02": "Vater",
  "char_or_03": "Mutter",
  "char_or_04": "Bezugsperson",
  "char_or_05": "Geschwister",
  "char_or_06": "Geburtsort",
  "char_or_07": "Notizen"
},
{
  "char_ed_01": "Ausbildung",
  "char_ed_02": "Schule",
  "char_ed_03": "Universität",
  "char_ed_04": "Berufsausbildung",
  "char_ed_05": "Autodidaktisch",
  "char_ed_06": "Beruf",
  "char_ed_07": "Kunst/Musik",
  "char_ed_08": "Sport",
  "char_ed_09": "Technik",
  "char_ed_10": "Notizen"
},
{
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
  "char_am_13": "Notizen"
},
{
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
  "char_ad_14": "Notizen"
},
{
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
  "char_ps_12": "Notizen"
},
{
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
  "char_pp_19": "Notizen"
},
{
  "sexo_sx_01": "Sexuelle Orientierung",
  "sexo_sx_02": "Orientierung",
  "sexo_sx_03": "Kurzbeschreibung"
},
{
  "gend_ge_01": "Geschlecht",
  "gend_ge_02": "Geschlecht",
  "gend_ge_03": "Kurzbeschreibung"
},
{
  "stat_pr_01": "Wörter pro Tag",
  "stat_pr_02": "Tage gezählt",
  "stat_pr_03": "Kapitel gezählt",
  "stat_pr_04": "Szenen gezählt",
  "stat_pr_05": "Erzählstränge gezählt",
  "stat_pr_06": "Hauptcharaktere gezählt",
  "stat_pr_07": "Nebencharaktere gezählt",
  "stat_pr_08": "Gruppen gezählt",
  "stat_pr_09": "Orte gezählt",
  "stat_pr_10": "Objekte gezählt"
},
{
  "stat_pr_01": "Wörter pro Tag",
  "stat_pr_02": "Tage gezählt",
  "stat_pr_03": "Kapitel gezählt",
  "stat_pr_04": "Szenen gezählt",
  "stat_pr_05": "Erzählstränge gezählt",
  "stat_pr_06": "Hauptcharaktere gezählt",
  "stat_pr_07": "Nebencharaktere gezählt",
  "stat_pr_08": "Gruppen gezählt",
  "stat_pr_09": "Orte gezählt",
  "stat_pr_10": "Objekte gezählt"
},
{
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
  "PreferenceThemeLight": "Hell"
},
{
  "botn_st_01": "Datenbank",
  "botn_st_02": "Projekt öffnen...",
  "botn_st_03": "Einstellungen",
  "botn_st_04": "Hilfe && Tutorials",
  "botn_st_05": "Beenden",
  "WinStartTitle": "Codicies Scriptoria Nova (CSNova)"
},
{
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
  "ProWinTitle": "Projektverwaltung"
},
{
  "botn_pr_01": "Neu",
  "botn_pr_02": "Löschen",
  "botn_pr_03": "Vor",
  "botn_pr_04": "Zurück",
  "botn_pr_05": "Speichern"
},
{
  "botn_ch_01": "Neu",
  "botn_ch_02": "Löschen",
  "botn_ch_03": "Vor",
  "botn_ch_04": "Zurück",
  "botn_ch_05": "Speichern"
},
{  
  "botn_cp_01": "Neu",
  "botn_cp_02": "Löschen",
  "botn_cp_03": "Vor",
  "botn_cp_04": "Zurück",
  "botn_cp_05": "Speichern"
},
{
  "botn_lo_01": "Neu",
  "botn_lo_02": "Löschen",
  "botn_lo_03": "Vor",
  "botn_lo_04": "Zurück",
  "botn_lo_05": "Speichern"
},
{
  "botn_ob_01": "Neu",
  "botn_ob_02": "Löschen",
  "botn_ob_03": "Vor",
  "botn_ob_04": "Zurück",
  "botn_ob_05": "Speichern"
},
{
  "botn_sc_01": "Neu",
  "botn_sc_02": "Löschen",
  "botn_sc_03": "Vor",
  "botn_sc_04": "Zurück",
  "botn_sc_05": "Speichern"
},
{
  "botn_sl_01": "Neu", 
  "botn_sl_02": "Löschen",
  "botn_sl_03": "Vor",
  "botn_sl_04": "Zurück",
  "botn_sl_05": "Speichern"
},
  
{
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
    "proj_ma_13": "Timeline"
  },
  {
    "proj_ch_01": "Chapter",
    "proj_ch_02": "Chapter Title",
    "proj_ch_03": "Chapter Premise"
  },
  {
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
    "proj_cs_12": "Notes"
  },
  {
    "proj_lo_01": "Location",
    "proj_lo_02": "Title",
    "proj_lo_03": "Description"
  },
  {
    "proj_st_01": "Storyline",
    "proj_st_02": "Title",
    "proj_st_03": "Premise",
    "proj_st_04": "Description",
    "proj_st_05": "Transformation",
    "proj_st_06": "Timeline",
    "proj_st_07": "Notes"
  },
  {
    "proj_ob_01": "Object",
    "proj_ob_02": "Title",
    "proj_ob_03": "Description"
  },
  {
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
    "char_ma_12": "Notes"
  },
  {
    "char_gr_01": "Group",
    "char_gr_02": "Group Title",
    "char_gr_03": "Group Description"
  },
  {
    "char_or_01": "Origin",
    "char_or_02": "Father",
    "char_or_03": "Mother",
    "char_or_04": "Reference Person",
    "char_or_05": "Siblings",
    "char_or_06": "Birthplace",
    "char_or_07": "Notes"
  },
  {
    "char_ed_01": "Education",
    "char_ed_02": "School",
    "char_ed_03": "University",
    "char_ed_04": "Vocational Training",
    "char_ed_05": "Autodidactic",
    "char_ed_06": "Job",
    "char_ed_07": "Art/Music",
    "char_ed_08": "Sport",
    "char_ed_09": "Technology",
    "char_ed_10": "Notes"
  },
  {
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
    "char_am_13": "Notes"
  },
  {
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
    "char_ad_14": "Notes"
  },
  {
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
    "char_ps_12": "Notes"
  },
  {
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
    "char_pp_19": "Notes"
  },
  {
    "sexo_sx_01": "Sexual Orientation",
    "sexo_sx_02": "Orientation",
    "sexo_sx_03": "Short Description"
  },
  {
    "gend_ge_01": "Gender",
    "gend_ge_02": "Gender",
    "gend_ge_03": "Short Description"
  },
  {
    "stat_pr_01": "Words per Day",
    "stat_pr_02": "Days Counted",
    "stat_pr_03": "Chapters Counted",
    "stat_pr_04": "Scenes Counted",
    "stat_pr_05": "Storylines Counted",
    "stat_pr_06": "Main Characters Counted",
    "stat_pr_07": "Supporting Characters Counted",
    "stat_pr_08": "Groups Counted",
    "stat_pr_09": "Locations Counted",
    "stat_pr_10": "Objects Counted"
  },
  {
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
    "PreferenceThemeLight": "Light"
  },
  {
    "botn_st_01": "Database",
    "botn_st_02": "Open Project...",
    "botn_st_03": "Settings",
    "botn_st_04": "Help && Tutorials",
    "botn_st_05": "Exit",
    "WinStartTitle": "Codicies Scriptoria Nova (CSNova)"
  },
  {
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
    "ProWinTitle": "Project Management"
  },
  {
    "botn_pr_01": "New",
    "botn_pr_02": "Delete",
    "botn_pr_03": "Next",
    "botn_pr_04": "Back",
    "botn_pr_05": "Save"
  },
  {
    "botn_ch_01": "New",
    "botn_ch_02": "Delete",
    "botn_ch_03": "Next",
    "botn_ch_04": "Back",
    "botn_ch_05": "Save"
  },
  {
    "botn_cp_01": "New",
    "botn_cp_02": "Delete",
    "botn_cp_03": "Next",
    "botn_cp_04": "Back",
    "botn_cp_05": "Save"
  },
  {
    "botn_lo_01": "New",
    "botn_lo_02": "Delete",
    "botn_lo_03": "Next",
    "botn_lo_04": "Back",
    "botn_lo_05": "Save"
  },
  {
    "botn_ob_01": "New",
    "botn_ob_02": "Delete",
    "botn_ob_03": "Next",
    "botn_ob_04": "Back",
    "botn_ob_05": "Save"
  },
  {
    "botn_sc_01": "New",
    "botn_sc_02": "Delete",
    "botn_sc_03": "Next",
    "botn_sc_04": "Back",
    "botn_sc_05": "Save"
  },
  {
    "botn_sl_01": "New",
    "botn_sl_02": "Delete",
    "botn_sl_03": "Next",
    "botn_sl_04": "Back",
    "botn_sl_05": "Save"
  },
    
  {
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
    "proj_ma_13": "Cronología"
  },
  {
    "proj_ch_01": "Capítulo",
    "proj_ch_02": "Título del capítulo",
    "proj_ch_03": "Premisa del capítulo"
  },
  {
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
    "proj_cs_12": "Notas"
  },
  {
    "proj_lo_01": "Lugar",
    "proj_lo_02": "Título",
    "proj_lo_03": "Descripción"
  },
  {
    "proj_st_01": "Trama",
    "proj_st_02": "Título",
    "proj_st_03": "Premisa",
    "proj_st_04": "Descripción",
    "proj_st_05": "Transformación",
    "proj_st_06": "Cronología",
    "proj_st_07": "Notas"
  },
  {
    "proj_ob_01": "Objeto",
    "proj_ob_02": "Título",
    "proj_ob_03": "Descripción"
  },
  {
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
    "char_ma_12": "Notas"
  },
  {
    "char_gr_01": "Grupo",
    "char_gr_02": "Título del grupo",
    "char_gr_03": "Descripción del grupo"
  },
  {
    "char_or_01": "Origen",
    "char_or_02": "Padre",
    "char_or_03": "Madre",
    "char_or_04": "Persona de referencia",
    "char_or_05": "Hermanos",
    "char_or_06": "Lugar de nacimiento",
    "char_or_07": "Notas"
  },
  {
    "char_ed_01": "Educación",
    "char_ed_02": "Escuela",
    "char_ed_03": "Universidad",
    "char_ed_04": "Formación profesional",
    "char_ed_05": "Autodidacta",
    "char_ed_06": "Trabajo",
    "char_ed_07": "Arte/Música",
    "char_ed_08": "Deporte",
    "char_ed_09": "Tecnología",
    "char_ed_10": "Notas"
  },
  {
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
    "char_am_13": "Notas"
  },
  {
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
    "char_ad_14": "Notas"
  },
  {
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
    "char_ps_12": "Notas"
  },
  {
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
    "char_pp_19": "Notas"
  },
  {
    "sexo_sx_01": "Orientación sexual",
    "sexo_sx_02": "Orientación",
    "sexo_sx_03": "Descripción corta"
  },
  {
    "gend_ge_01": "Género",
    "gend_ge_02": "Género",
    "gend_ge_03": "Descripción corta"
  },
  {
    "stat_pr_01": "Palabras por día",
    "stat_pr_02": "Días contados",
    "stat_pr_03": "Capítulos contados",
    "stat_pr_04": "Escenas contadas",
    "stat_pr_05": "Tramas contadas",
    "stat_pr_06": "Personajes principales contados",
    "stat_pr_07": "Personajes secundarios contados",
    "stat_pr_08": "Grupos contados",
    "stat_pr_09": "Lugares contados",
    "stat_pr_10": "Objetos contados"
  },
  {
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
    "PreferenceThemeLight": "Claro"
  },
  {
    "botn_st_01": "Base de datos",
    "botn_st_02": "Abrir proyecto...",
    "botn_st_03": "Configuración",
    "botn_st_04": "Ayuda && Tutoriales",
    "botn_st_05": "Salir",
    "WinStartTitle": "Codicies Scriptoria Nova (CSNova)"
  },
  {
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
    "ProWinTitle": "Gestión de proyectos"
  },
  {
    "botn_pr_01": "Nuevo",
    "botn_pr_02": "Eliminar",
    "botn_pr_03": "Siguiente",
    "botn_pr_04": "Atrás",
    "botn_pr_05": "Guardar"
  },
  {
    "botn_ch_01": "Nuevo",
    "botn_ch_02": "Eliminar",
    "botn_ch_03": "Siguiente",
    "botn_ch_04": "Atrás",
    "botn_ch_05": "Guardar"
  },
  {
    "botn_cp_01": "Nuevo",
    "botn_cp_02": "Eliminar",
    "botn_cp_03": "Siguiente",
    "botn_cp_04": "Atrás",
    "botn_cp_05": "Guardar"
  },
  {
    "botn_lo_01": "Nuevo",
    "botn_lo_02": "Eliminar",
    "botn_lo_03": "Siguiente",
    "botn_lo_04": "Atrás",
    "botn_lo_05": "Guardar"
  },
  {
    "botn_ob_01": "Nuevo",
    "botn_ob_02": "Eliminar",
    "botn_ob_03": "Siguiente",
    "botn_ob_04": "Atrás",
    "botn_ob_05": "Guardar"
  },
  {
    "botn_sc_01": "Nuevo",
    "botn_sc_02": "Eliminar",
    "botn_sc_03": "Siguiente",
    "botn_sc_04": "Atrás",
    "botn_sc_05": "Guardar"
  },
  {
    "botn_sl_01": "Nuevo",
    "botn_sl_02": "Eliminar",
    "botn_sl_03": "Siguiente",
    "botn_sl_04": "Atrás",
    "botn_sl_05": "Guardar"
  },
  {
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
    "proj_ma_13": "Chronologie"
  },
  {
    "proj_ch_01": "Chapitre",
    "proj_ch_02": "Titre du chapitre",
    "proj_ch_03": "Prémisse du chapitre"
  },
  {
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
    "proj_cs_12": "Notes"
  },
  {
    "proj_lo_01": "Lieu",
    "proj_lo_02": "Titre",
    "proj_lo_03": "Description"
  },
  {
    "proj_st_01": "Intrigue",
    "proj_st_02": "Titre",
    "proj_st_03": "Prémisse",
    "proj_st_04": "Description",
    "proj_st_05": "Transformation",
    "proj_st_06": "Chronologie",
    "proj_st_07": "Notes"
  },
  {
    "proj_ob_01": "Objet",
    "proj_ob_02": "Titre",
    "proj_ob_03": "Description"
  },
  {
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
    "char_ma_12": "Notes"
  },
  {
    "char_gr_01": "Groupe",
    "char_gr_02": "Titre du groupe",
    "char_gr_03": "Description du groupe"
  },
  {
    "char_or_01": "Origine",
    "char_or_02": "Père",
    "char_or_03": "Mère",
    "char_or_04": "Personne de référence",
    "char_or_05": "Frères et sœurs",
    "char_or_06": "Lieu de naissance",
    "char_or_07": "Notes"
  },
  {
    "char_ed_01": "Éducation",
    "char_ed_02": "École",
    "char_ed_03": "Université",
    "char_ed_04": "Formation professionnelle",
    "char_ed_05": "Autodidacte",
    "char_ed_06": "Métier",
    "char_ed_07": "Art/Musique",
    "char_ed_08": "Sport",
    "char_ed_09": "Technologie",
    "char_ed_10": "Notes"
  },
  {
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
    "char_am_13": "Notes"
  },
  {
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
    "char_ad_14": "Notes"
  },
  {
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
    "char_ps_12": "Notes"
  },
  {
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
    "char_pp_19": "Notes"
  },
  {
    "sexo_sx_01": "Orientation sexuelle",
    "sexo_sx_02": "Orientation",
    "sexo_sx_03": "Description courte"
  },
  {
    "gend_ge_01": "Genre",
    "gend_ge_02": "Genre",
    "gend_ge_03": "Description courte"
  },
  {
    "stat_pr_01": "Mots par jour",
    "stat_pr_02": "Jours comptés",
    "stat_pr_03": "Chapitres comptés",
    "stat_pr_04": "Scènes comptées",
    "stat_pr_05": "Intrigues comptées",
    "stat_pr_06": "Personnages principaux comptés",
    "stat_pr_07": "Personnages secondaires comptés",
    "stat_pr_08": "Groupes comptés",
    "stat_pr_09": "Lieux comptés",
    "stat_pr_10": "Objets comptés"
  },
  {
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
    "PreferenceThemeLight": "Clair"
  },
  {
    "botn_st_01": "Base de données",
    "botn_st_02": "Ouvrir le projet...",
    "botn_st_03": "Paramètres",
    "botn_st_04": "Aide && Tutoriels",
    "botn_st_05": "Quitter",
    "WinStartTitle": "Codicies Scriptoria Nova (CSNova)"
  },
  {
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
    "ProWinTitle": "Gestion de projet"
  },
  {
    "botn_pr_01": "Nouveau",
    "botn_pr_02": "Supprimer",
    "botn_pr_03": "Suivant",
    "botn_pr_04": "Retour",
    "botn_pr_05": "Enregistrer"
  },
  {
    "botn_ch_01": "Nouveau",
    "botn_ch_02": "Supprimer",
    "botn_ch_03": "Suivant",
    "botn_ch_04": "Retour",
    "botn_ch_05": "Enregistrer"
  },
  {
    "botn_cp_01": "Nouveau",
    "botn_cp_02": "Supprimer",
    "botn_cp_03": "Suivant",
    "botn_cp_04": "Retour",
    "botn_cp_05": "Enregistrer"
  },
  {
    "botn_lo_01": "Nouveau",
    "botn_lo_02": "Supprimer",
    "botn_lo_03": "Suivant",
    "botn_lo_04": "Retour",
    "botn_lo_05": "Enregistrer"
  },
  {
    "botn_ob_01": "Nouveau",
    "botn_ob_02": "Supprimer",
    "botn_ob_03": "Suivant",
    "botn_ob_04": "Retour",
    "botn_ob_05": "Enregistrer"
  },
  {
    "botn_sc_01": "Nouveau",
    "botn_sc_02": "Supprimer",
    "botn_sc_03": "Suivant",
    "botn_sc_04": "Retour",
    "botn_sc_05": "Enregistrer"
  },
  {
    "botn_sl_01": "Nouveau",
    "botn_sl_02": "Supprimer",
    "botn_sl_03": "Suivant",
    "botn_sl_04": "Retour",
    "botn_sl_05": "Enregistrer"
  }
]

```

## 4. Character Tabellen

In diesem Abschnitt sind die Tabellen zur Erstellung von Charakteren zusammengefasst.

### 4.1 character_main.py

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

#### 4.1.1 gender.py

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

#### 4.1.2 sex_orientation.py

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

### 4.2 character_origin.py

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

### 4.3 character_education.py

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

### 4.4 character_personality.py

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

### 4.5 character_psychological_profile.py

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

### 4.6 character_appearance_main.py

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

### 4.7 character_appearance_detail.py

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

### 4.8 character_groups.py

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

## 5. Projekttabellen

In diesem Abschnitt sind die Tabellen zur Erstellung von Projekten zusammengefasst.

### 5.1 project.py

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

### 5.2 project_storylines.py

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

### 5.3 project_chapters.py

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

### 5.4 project_chapters_scenes.py

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

### 5.5 project_objects.py

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

### 5.6 project_locations.py

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

### 5.7 Mapping

In diesem Abschnitt werden die gemappten Tabellen sowie deren Verbindungen übersichtlich dargestellt.

#### 5.7.1 project_scene_character_map.py
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

#### 5.7.2 project_scene_location_map.py
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

#### 5.7.3 scene_objects_map.py
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

#### 5.7.4 project_scene_storyline_map.py
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

#### 5.7.5 project_character_group_map.py
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

#### 5.7.6 project_charcter_storyline_map.py
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

### 5.8 form_fields.json
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
  {"name": "locations_count", "label_key": "stat_pr_09", "type": "display", "datafield_name": "project_locatons"},
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

## 6. - Programmecode

In diesem Abschnitt sind alle Programmcodes zusammengefasst.

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

def load_language():
    """
    Loads the language from user_settings.json, defaults to 'en' if not set.
    """
    try:
        with open(USER_SETTINGS_FILE, "r", encoding="utf-8") as f:
            settings = json.load(f)
        return settings.get("language", "en")
    except Exception as e:
        log_exception("Error loading language from user_settings.json", e)
        return "en"

def main():
    log_section("csNova.py")
    log_subsection("main")
    try:
        app = QApplication(sys.argv)
        app.setStyleSheet(load_global_stylesheet())
        language = load_language()
        translator = Translator(language)
        window = StartWindow(default_language=language)
        window.show()
        log_info("csNova main window shown.")
        sys.exit(app.exec())
    except Exception as e:
        log_exception("Error in csNova main execution", e)

if __name__ == "__main__":
    main()
```

### 6.2 Settings 
#### 6.2.1 setting.py

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
```

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
  "language": "de",
  "splitter_sizes": [
    316,
    948,
    316
  ],
  "style": "modern",
  "mode": "middle"
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
from gui.styles.form_styles import load_button_style, load_active_button_style
from core.logger import log_section, log_subsection, log_info, log_exception

class NavigationPanel(QWidget):
    """
    NavigationPanel: displays navigation buttons for the main sections.
    All button labels are set dynamically via translator.py.
    After language change, call update_translations() to refresh all button texts.
    """
    def __init__(self, keys, translator, parent=None, callbacks=None):
        log_section("navigation_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.setObjectName("NavigationPanel")
            self.translator = translator
            self.callbacks = callbacks or {}
            self.active_key = None
            self.layout = QVBoxLayout()
            self.buttons = {}

            button_style = load_button_style()
            button_style_active = load_active_button_style()

            for key in keys:
                btn = QPushButton(self.translator.tr(key), self)
                btn.setStyleSheet(button_style)
                btn.setFixedSize(240, 70)
                btn.clicked.connect(lambda checked, k=key: self._on_nav_clicked(k))
                self.layout.addWidget(btn)
                self.buttons[key] = btn

            self.setLayout(self.layout)
            log_info("NavigationPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing NavigationPanel", e)

    def _on_nav_clicked(self, key):
        log_subsection(f"_on_nav_clicked: {key}")
        try:
            button_style = load_button_style()
            button_style_active = load_active_button_style()
            for k, btn in self.buttons.items():
                btn.setStyleSheet(button_style)
            self.buttons[key].setStyleSheet(button_style_active)
            self.active_key = key
            if key in self.callbacks:
                self.callbacks[key]()
            log_info(f"Navigation button '{key}' clicked.")
        except Exception as e:
            log_exception(f"Error in navigation click handler for '{key}'", e)

    def update_translations(self):
        """
        Update all button labels after language change.
        """
        button_style = load_button_style()
        button_style_active = load_active_button_style()
        for key, btn in self.buttons.items():
            btn.setText(self.translator.tr(key))
            if key == self.active_key:
                btn.setStyleSheet(button_style_active)
            else:
                btn.setStyleSheet(button_style)
```

##### 6.5.2.2 help_panel.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from core.logger import log_section, log_subsection, log_info, log_exception

class HelpPanel(QWidget):
    """
    HelpPanel: displays help texts and tips.
    All labels and texts are set dynamically via translator.py.
    After language change, call update_translations() to refresh all texts.
    """
    def __init__(self, translator, parent=None):
        log_section("help_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.layout = QVBoxLayout(self)
            self.help_label = QLabel(self.translator.tr("help_panel_main"), self)
            self.layout.addWidget(self.help_label)
            self.setLayout(self.layout)
            log_info("HelpPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing HelpPanel", e)

    def update_translations(self):
        """
        Update all help texts after language change.
        """
        self.help_label.setText(self.translator.tr("help_panel_main"))

    def set_help_text(self, text):
        """
        Set the help text in the label.
        """
        self.help_label.setText(text)
```

##### 6.5.2.3 center_panel.py

```python
from PySide6.QtWidgets import QWidget, QSplitter, QHBoxLayout
from gui.widgets.navigation_panel import NavigationPanel
from gui.styles.form_styles import load_global_stylesheet
from core.logger import log_section, log_subsection, log_info, log_exception

class CenterPanel(QWidget):
    """
    CenterPanel: combines navigation, content, and help panels.
    All labels and buttons in navigation/help/content are set dynamically via translator.py.
    After language change, call update_translations() on all child panels.
    """
    def __init__(self, navigation_panel, content_widget, help_panel, parent=None):
        log_section("center_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.setObjectName("CenterPanel")
            self.setStyleSheet(load_global_stylesheet())

            self.navigation_panel = navigation_panel
            self.content_widget = content_widget
            self.help_panel = help_panel

            self.splitter = QSplitter(self)
            self.splitter.addWidget(self.navigation_panel)
            self.splitter.addWidget(self.content_widget)
            self.splitter.addWidget(self.help_panel)
            self.splitter.setSizes([200, 800, 200])  # Adjust as needed

            layout = QHBoxLayout(self)
            layout.addWidget(self.splitter)
            self.setLayout(layout)
            log_info("CenterPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing CenterPanel", e)

    def update_translations(self):
        """
        Update all labels after language change.
        """
        if hasattr(self.navigation_panel, "update_translations"):
            self.navigation_panel.update_translations()
        if hasattr(self.content_widget, "update_translations"):
            self.content_widget.update_translations()
        if hasattr(self.help_panel, "update_translations"):
            self.help_panel.update_translations()
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

            # Define button keys for common actions
            self.button_keys = [
                "BtnNew", "BtnSave", "BtnDelete", "BtnPreview", "BtnNext"
            ]
            self.buttons = {}

            for key in self.button_keys:
                label_key = f"{form_prefix}{key}"
                btn = QPushButton(self.translator.tr(label_key), self)
                btn.setObjectName(label_key)
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
            label_key = btn.objectName()
            btn.setText(self.translator.tr(label_key))
```

##### 6.5.3.2 base_form_widget.py

```python
import json
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFormLayout,
    QLineEdit, QSpinBox, QDateEdit, QComboBox
)
from gui.widgets.form_toolbar import FormToolbar
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import FORM_FIELDS_FILE

class BaseFormWidget(QWidget):
    """
    Generic form widget: loads all fields and labels from form_fields.json,
    translates all labels and options dynamically via translator.py,
    updates labels and options after language change.
    All styles are applied centrally via form_styles.py.
    """

    def __init__(self, title, fields, toolbar_actions, form_prefix, translator, parent=None):
        """
        Initializes the form widget with dynamic fields, translations, and toolbar.
        """
        log_section("base_form_widget.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            main_layout = QVBoxLayout()

            # Toolbar
            self.toolbar = FormToolbar(self.translator, form_prefix, self)
            if toolbar_actions:
                toolbar_actions(self.toolbar)
                main_layout.addWidget(self.toolbar)
                main_layout.addSpacing(12)

            # Form fields
            self.form_layout = QFormLayout()
            self.inputs = {}
            self.labels = {}
            self.option_keys = {}

            for field in fields:
                if field.get("type") == "header":
                    header_text = self.translator.tr(field["label_key"])
                    header_label = QLabel(header_text if header_text else field.get("default_label", ""), self)
                    # Use centralized style for header if available, else fallback
                    header_label.setProperty("header", True)
                    self.form_layout.addRow(header_label)
                    continue

                label_text = self.translator.tr(field["label_key"])
                label = QLabel(label_text if label_text else field.get("default_label", ""), self)
                self.labels[field["name"]] = label
                input_widget = None

                if field["type"] == "text":
                    input_widget = QLineEdit(self)
                    if "max_length" in field:
                        input_widget.setMaxLength(field["max_length"])
                elif field["type"] == "spin":
                    input_widget = QSpinBox(self)
                    if "max" in field:
                        input_widget.setMaximum(field["max"])
                    if "min" in field:
                        input_widget.setMinimum(field["min"])
                elif field["type"] == "date":
                    input_widget = QDateEdit(self)
                elif field["type"] == "select":
                    input_widget = QComboBox(self)
                    self.option_keys[field["name"]] = []
                    for option in field.get("options", []):
                        # Use translated label for each option
                        option_label = self.translator.tr(option.get("label_key", str(option)))
                        input_widget.addItem(option_label)
                        self.option_keys[field["name"]].append(option.get("key", option_label))
                elif field["type"] == "display":
                    input_widget = QLabel("", self)
                else:
                    input_widget = QLineEdit(self)

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
        for field_name, label in self.labels.items():
            # Find the field definition for this label
            field = next((f for f in self.inputs if f == field_name), None)
            if field:
                label_key = None
                # Try to get label_key from form_fields.json if available
                # This assumes you pass the fields array to the widget and can access it here
                # If not, you may need to store label_keys in self.labels
                label_key = getattr(label, "label_key", None)
                if not label_key:
                    # Fallback: try to get from label text
                    label_key = field_name
                label.setText(self.translator.tr(label_key))

            # Update options for QComboBox
            input_widget = self.inputs.get(field_name)
            if isinstance(input_widget, QComboBox) and field_name in self.option_keys:
                input_widget.blockSignals(True)
                input_widget.clear()
                for idx, option_key in enumerate(self.option_keys[field_name]):
                    # Try to get the label_key from form_fields.json options
                    option_label = self.translator.tr(option_key)
                    input_widget.addItem(option_label)
                input_widget.blockSignals(False)
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

            # Load character fields from form_fields.json
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                fields_config = json.load(f)
            character_fields = fields_config.get("character_main", [])

            # Create the base form widget
            self.form_widget = BaseFormWidget(
                title=self.translator.tr("Char"),
                fields=character_fields,
                toolbar_actions=toolbar_actions,
                form_prefix="char",
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
        self.form_widget.update_translations()
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

            # Load location fields from form_fields.json
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                fields_config = json.load(f)
            location_fields = fields_config.get("project_locations", [])

            # Create the base form widget
            self.form_widget = BaseFormWidget(
                title=self.translator.tr("Location"),
                fields=location_fields,
                toolbar_actions=toolbar_actions,
                form_prefix="location",
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
        self.form_widget.update_translations()
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

            # Load object fields from form_fields.json
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                fields_config = json.load(f)
            object_fields = fields_config.get("project_objects", [])

            # Create the base form widget
            self.form_widget = BaseFormWidget(
                title=self.translator.tr("Object"),
                fields=object_fields,
                toolbar_actions=toolbar_actions,
                form_prefix="object",
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
        self.form_widget.update_translations()
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

            # Load project fields from form_fields.json
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                fields_config = json.load(f)
            project_fields = fields_config.get("projects", [])

            # Create the base form widget
            self.form_widget = BaseFormWidget(
                title=self.translator.tr("Pro"),
                fields=project_fields,
                toolbar_actions=toolbar_actions,
                form_prefix="project",
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
        self.form_widget.update_translations()
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

##### 6.5.3.10 form_start.py
```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception

class FormStart(QWidget):
    """
    Placeholder widget for the start screen after StartBtnNewProject is pressed.
    Applies global style from preferences.
    Displays only a translated label as placeholder.
    No local styles or translations are used.
    """

    def __init__(self, translator, parent=None):
        """
        Initializes the start form with a translated placeholder label.
        """
        log_section("form_start.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            layout = QVBoxLayout(self)
            layout.setContentsMargins(40, 40, 40, 40)
            layout.setSpacing(20)

            # Placeholder label (translated)
            self.placeholder_label = QLabel(self.translator.tr("WinStartTitle"), self)
            self.placeholder_label.setObjectName("startPlaceholderLabel")
            layout.addWidget(self.placeholder_label)
            layout.addStretch()

            self.setLayout(layout)
            log_info("FormStart initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormStart", e)

    def update_translations(self):
        """
        Updates the placeholder label after a language change.
        """
        self.placeholder_label.setText(self.translator.tr("WinStartTitle"))
```

#### 6.5.4 Fenster
##### 6.5.4.1 start_window.py

```python
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QColor, QPixmap, QPainter
from PySide6.QtCore import QTimer
from gui.preferences import PreferencesWindow
from core.translator import Translator
from gui.project_window import ProjectWindow
from gui.widgets.help_panel import HelpPanel
from gui.styles.form_styles import load_button_style
import sys

from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import BG_IMAGE_PATH
from config.settings import load_settings

class StartWindow(QWidget):
    DEFAULT_WIDTH        = 1920
    DEFAULT_HEIGHT       = 1080
    BUTTON_WIDTH         = 240
    BUTTON_HEIGHT        = 70
    BUTTON_TOP_OFFSET    = 220
    BUTTON_LEFT_OFFSET   = 1380
    BUTTON_SPACING       = 44

    def __init__(self, default_language="en"):
        log_section("start_window.py")
        log_subsection("__init__")
        try:
            super().__init__()
            self.settings = load_settings()
            lang = self.settings.get("language", default_language)
            self.translator = Translator(lang)
            self.setWindowTitle(self.translator.tr("WinStartTitle"))
            self.resize(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)
            self.setAutoFillBackground(False)
            self.bg_pixmap = QPixmap(str(BG_IMAGE_PATH))
            self.pref_window = None
            self._create_ui()
            self._retranslate_and_position()
            help_text = self.translator.help_text("help_new_project")
            self.help_panel = HelpPanel(self.translator, self)
            self.help_panel.set_help_text(help_text)
            log_info("StartWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing StartWindow", e)

    def _create_ui(self):
        log_subsection("_create_ui")
        try:
            self.button_keys = [
                "StartBtnNewProject",
                "StartBtnLoadProject",
                "StartBtnSettings",
                "StartBtnHelp",
                "StartBtnExit"
            ]

            self.buttons = []
            for key in self.button_keys:
                btn = QPushButton(parent=self)
                shadow = QGraphicsDropShadowEffect(btn)
                shadow.setBlurRadius(10)
                shadow.setXOffset(4)
                shadow.setYOffset(4)
                shadow.setColor(QColor(0, 0, 0, 80))
                btn.setGraphicsEffect(shadow)
                self.buttons.append(btn)

            self.buttons[0].clicked.connect(self._new_project)
            self.buttons[1].clicked.connect(self._load_project)
            self.buttons[2].clicked.connect(self._open_preferences)
            self.buttons[3].clicked.connect(self._help)
            self.buttons[4].clicked.connect(self._exit_application)
            log_info("UI created and buttons connected.")
        except Exception as e:
            log_exception("Error creating UI", e)

    def _open_preferences(self):
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
        log_subsection("_load_project")
        try:
            log_info("Preparing to load project...")
            # Implement loading logic here
        except Exception as e:
            log_exception("Error preparing to load project", e)

    def _help(self):
        log_subsection("_help")
        try:
            log_info("Preparing help function...")
            # Implement help logic here
        except Exception as e:
            log_exception("Error preparing help function", e)

    def _exit_application(self):
        log_subsection("_exit_application")
        try:
            log_info("Exiting application...")
            QApplication.instance().quit()
        except Exception as e:
            log_exception("Error during application exit", e)

    def _on_language_changed(self, code):
        log_subsection("_on_language_changed")
        try:
            self.translator.set_language(code)
            self.settings["language"] = code
            self._retranslate_and_position()
            log_info(f"Language changed to {code}.")
        except Exception as e:
            log_exception("Error changing language", e)

    def _retranslate_and_position(self):
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

    def resizeEvent(self, event):
        self.update_button_positions()
        super().resizeEvent(event)
    
    def update_translations(self):
        # Called by PreferencesWindow after language change
        self.settings = load_settings()
        lang = self.settings.get("language", "en")
        self.translator.set_language(lang)
        self._retranslate_and_position()
        help_text = self.translator.help_text("help_new_project")
        self.help_panel.set_help_text(help_text)

    def update_button_positions(self):
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

if __name__ == "__main__":
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
    """

    def __init__(self, parent=None):
        log_section("preferences.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = parent.translator if parent and hasattr(parent, "translator") else Translator()
            self.setWindowTitle(self.translator.tr("WinPreferenceTitle"))
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
        """
        try:
            with open("/home/frank/Dokumente/CSNova/core/config/form_fields.json", "r", encoding="utf-8") as f:
                self.form_fields = json.load(f)["preferences"]
        except Exception as e:
            log_exception("Error loading form_fields.json", e)
            self.form_fields = []

    def _init_ui(self):
        """
        Initializes all UI elements for the preferences dialog.
        All options are loaded from central sources. Layout is compact and buttons are at the bottom.
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
                label = QLabel(self.translator.tr(field["label_key"]), self)
                combo = QComboBox(self)
                option_labels = []
                option_keys = []
                for opt in field.get("options", []):
                    option_labels.append(self.translator.tr(opt["label_key"]))
                    option_keys.append(opt["key"])
                combo.addItems(option_labels)
                # Set current value from settings
                current_value = self.settings.get(field["datafield_name"].replace("preference_", ""), option_keys[0])
                try:
                    idx = option_keys.index(current_value)
                except ValueError:
                    idx = 0
                combo.setCurrentIndex(idx)
                main_layout.addWidget(label)
                main_layout.addWidget(combo)
                self.combos[field["name"]] = (combo, option_keys)
                self.labels[field["name"]] = label

                # Connect style and theme changes to handlers
                if field["name"] == "style":
                    combo.currentIndexChanged.connect(self._on_style_changed)
                if field["name"] == "theme":
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
        """
        style = self.settings.get("style", "modern")
        mode = self.settings.get("mode", "light")
        stylesheet = load_global_stylesheet(style, mode)
        self.setStyleSheet(stylesheet)
        if global_apply:
            QApplication.instance().setStyleSheet(stylesheet)

    def update_translations(self):
        """
        Updates all UI texts after a language change.
        Also updates translated items in all comboboxes.
        """
        self.setWindowTitle(self.translator.tr("WinPreferenceTitle"))
        for field in self.form_fields:
            self.labels[field["name"]].setText(self.translator.tr(field["label_key"]))
            combo, option_keys = self.combos[field["name"]]
            combo.blockSignals(True)
            combo.clear()
            for opt in field.get("options", []):
                combo.addItem(self.translator.tr(opt["label_key"]))
            # Set current value from settings
            current_value = self.settings.get(field["datafield_name"].replace("preference_", ""), option_keys[0])
            try:
                idx = option_keys.index(current_value)
            except ValueError:
                idx = 0
            combo.setCurrentIndex(idx)
            combo.blockSignals(False)
        self.save_btn.setText(self.translator.tr("PreferenceActionSave"))
        self.cancel_btn.setText(self.translator.tr("PreferenceActionCancel"))
        self._apply_current_style(global_apply=True)

    def _on_save(self):
        """
        Saves the selected settings and closes the dialog.
        Notifies parent window to update translations if possible.
        """
        log_subsection("_on_save")
        try:
            for field in self.form_fields:
                combo, option_keys = self.combos[field["name"]]
                self.settings[field["datafield_name"].replace("preference_", "")] = option_keys[combo.currentIndex()]
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
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QSplitter, QHBoxLayout

from gui.styles.form_styles import load_button_style, load_active_button_style
from core.translator import Translator
from config.settings import load_settings, save_settings
from gui.widgets.navigation_panel import NavigationPanel
from gui.widgets.help_panel import HelpPanel

from gui.widgets.form_projects import FormProjects
from gui.widgets.form_characters import FormCharacters
from gui.widgets.form_storylines import FormStorylines
from gui.widgets.form_chapters import FormChapters
from gui.widgets.form_scenes import FormScenes
from gui.widgets.form_objects import FormObjects
from gui.widgets.form_locations import FormLocations
from gui.widgets.form_start import FormStart

from core.logger import log_section, log_subsection, log_info, log_exception

class ProjectWindow(QWidget):
    BUTTON_WIDTH = 240
    BUTTON_HEIGHT = 70

    def __init__(self, translator=None, parent=None, start_window=None):
        """
        Main project window for csNova.
        Initializes navigation, help, and form panels.
        Applies global styles and translations.
        """
        log_section("project_window.py")
        log_subsection("__init__")
        try:
            self.translator = translator or Translator(lang="en")
            super().__init__(parent)
            self.resize(1600, 900)
            self.setWindowTitle(self.translator.tr("ProWinTitle"))
            self.settings = load_settings()
            self.button_style = load_button_style(18)
            self.button_style_active = load_active_button_style(18)
            self.active_nav_key = None
            self.start_window = start_window

            self.splitter = QSplitter(Qt.Horizontal)
            self.splitter.setObjectName("MainSplitter")

            self._set_background()
            self._init_ui()
            log_info("ProjectWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing ProjectWindow", e)

    def _set_background(self):
        """
        Sets the background color for the main window.
        """
        log_subsection("_set_background")
        try:
            palette = self.palette()
            palette.setColor(QPalette.Window, QColor("#f0f0f0"))
            self.setPalette(palette)
            self.setAutoFillBackground(True)
            log_info("Background set successfully.")
        except Exception as e:
            log_exception("Error setting background", e)

    def _init_ui(self):
        """
        Initializes navigation, help, and form panels.
        """
        log_subsection("_init_ui")
        try:
            keys = [
                "ProBtnProject", "ProBtnCharacters", "ProBtnStorylines",
                "ProBtnChapters", "ProBtnScenes", "ProBtnObjects", "ProBtnLocations", "ProBtnExit"
            ]
            callbacks = {
                "ProBtnProject": lambda: self._on_nav_clicked("ProBtnProject", self._show_project_form),
                "ProBtnCharacters": lambda: self._on_nav_clicked("ProBtnCharacters", self._show_characters_form),
                "ProBtnStorylines": lambda: self._on_nav_clicked("ProBtnStorylines", self._show_storylines_form),
                "ProBtnChapters": lambda: self._on_nav_clicked("ProBtnChapters", self._show_chapters_form),
                "ProBtnScenes": lambda: self._on_nav_clicked("ProBtnScenes", self._show_scenes_form),
                "ProBtnObjects": lambda: self._on_nav_clicked("ProBtnObjects", self._show_objects_form),
                "ProBtnLocations": lambda: self._on_nav_clicked("ProBtnLocations", self._show_locations_form),
                "ProBtnExit": self._exit_application
            }
            self.navigation_panel = NavigationPanel(
                self.translator, keys, self, callbacks
            )

            self.help_panel = HelpPanel(self.translator, self)
            self.help_panel.set_help_text(self.translator.help_text("HelpNewProject"))
            self.form_widget = FormStart(self.translator, self)

            self.splitter.addWidget(self.navigation_panel)
            self.splitter.addWidget(self.form_widget)
            self.splitter.addWidget(self.help_panel)
            self.splitter.setSizes(self.settings.get("splitter_sizes", [300, 900, 300]))

            # Corrected layout assignment
            layout = QHBoxLayout()
            layout.addWidget(self.splitter)
            self.setLayout(layout)
            log_info("UI initialized successfully.")
        except Exception as e:
            log_exception("Error initializing UI", e)

    def _on_nav_clicked(self, key, handler):
        """
        Handles navigation button clicks and displays the corresponding form.
        """
        log_subsection(f"_on_nav_clicked: {key}")
        try:
            self.active_nav_key = key
            handler()
            log_info(f"Navigation button '{key}' clicked.")
        except Exception as e:
            log_exception(f"Error in navigation click handler for '{key}'", e)

    def _show_project_form(self):
        """
        Displays the project form.
        """
        log_subsection("_show_project_form")
        try:
            form_widget = FormProjects(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("HelpProject")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Project form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying project form", e)

    def _show_characters_form(self):
        """
        Displays the characters form.
        """
        log_subsection("_show_characters_form")
        try:
            form_widget = FormCharacters(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("HelpChars")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Characters form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying characters form", e)

    def _show_storylines_form(self):
        """
        Displays the storylines form.
        """
        log_subsection("_show_storylines_form")
        try:
            form_widget = FormStorylines(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("HelpStorylines")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Storylines form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying storylines form", e)

    def _show_chapters_form(self):
        """
        Displays the chapters form.
        """
        log_subsection("_show_chapters_form")
        try:
            form_widget = FormChapters(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("HelpChapters")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Chapters form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying chapters form", e)

    def _show_scenes_form(self):
        """
        Displays the scenes form.
        """
        log_subsection("_show_scenes_form")
        try:
            form_widget = FormScenes(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("HelpScenes")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Scenes form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying scenes form", e)

    def _show_objects_form(self):
        """
        Displays the objects form.
        """
        log_subsection("_show_objects_form")
        try:
            form_widget = FormObjects(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("HelpObjects")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Objects form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying objects form", e)

    def _show_locations_form(self):
        """
        Displays the locations form.
        """
        log_subsection("_show_locations_form")
        try:
            form_widget = FormLocations(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("HelpLocations")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Locations form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying locations form", e)

    def _replace_form_widget(self, new_widget):
        """
        Replaces the current form widget in the splitter with a new one.
        """
        old_widget = self.splitter.widget(1)
        if old_widget:
            old_widget.setParent(None)
        self.splitter.insertWidget(1, new_widget)

    def _exit_application(self):
        """
        Handles application exit and shows the start window.
        """
        log_subsection("_exit_application")
        try:
            if self.start_window:
                self.start_window.show()
            self.close()
            log_info("Application exit triggered, StartWindow shown.")
        except Exception as e:
            log_exception("Error during application exit", e)

    def closeEvent(self, event):
        """
        Saves splitter sizes and handles window close event.
        """
        log_subsection("closeEvent")
        try:
            self.settings["splitter_sizes"] = self.splitter.sizes()
            save_settings(self.settings)
            event.accept()
            log_info("Splitter sizes saved and application closed.")
        except Exception as e:
            log_exception("Error saving splitter sizes on close", e)
            event.accept()
```

## 7 Vorbereitungen für die Installation unter Linux-Mint

[.gitignore](/.gitignore)

[requirements](/requirements.txt)

[pyinstaller-code](/pyinstaller.txt)

[csNova-install](/install_csnova.sh)

[Lizenz](/license.md)
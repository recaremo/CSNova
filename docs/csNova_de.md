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
    "ID": "de",
    "chapter": "Kapitel",
    "chapter_btn_delete": "Löschen",
    "chapter_btn_new": "Neu",
    "chapter_btn_next": "Vor",
    "chapter_btn_preview": "Zurück",
    "chapter_btn_save": "Speichern",
    "chapter_number": "Nummer",
    "chapter_summary": "Zusammenfassung",
    "chapter_characters": "Charaktere",
    "chapter_locations": "Orte",
    "chapter_notes": "Notizen",
    "chapter_opjects": "Objekte",
    "chapter_premise": "Prämisse",
    "chapter_scenes": "Szenen",
    "chapter_title": "Titel",
    "char": "Charaktere",
    "char_app": "Aussehen",
    "char_app_body_type": "Körpertyp",
    "char_app_charisma": "Ausstrahlung",
    "char_app_eye_color": "Augenfarbe",
    "char_app_eye_shape": "Augenform",
    "char_app_face_shape": "Gesichtsform",
    "char_app_hair": "Haare",
    "char_app_hair_color": "Haarfarbe",
    "char_app_height": "Größe",
    "char_app_notes": "Notizen",
    "char_app_posture": "Statur",
    "char_app_skin": "Haut",
    "char_app_specials": "Besonderheiten",
    "char_app2": "Aussehen Details",
    "char_app2_arms": "Arme",
    "char_app2_buttocks": "Gesäß",
    "char_app2_chest": "Brust",
    "char_app2_feet": "Füße",
    "char_app2_finger": "Finger",
    "char_app2_hands": "Hände",
    "char_app2_head": "Kopf",
    "char_app2_hip_waist": "Hüfte, Taille",
    "char_app2_legs": "Beine",
    "char_app2_notes": "Notizen",
    "char_app2_shoulder": "Schultern",
    "char_app2_toes": "Zehen",
    "char_bas": "Grunddaten",
    "char_bas_age": "Alter",
    "char_bas_born": "Geburtsdatum",
    "char_bas_firstname": "Vorname",
    "char_bas_gender": "Geschlecht",
    "char_bas_group": "Gruppe",
    "char_bas_name": "Name",
    "char_bas_nickname": "Spitzname",
    "char_bas_notes": "Notizen",
    "char_bas_role": "Rolle",
    "char_bas_sex_orientation": "sexuelle Orientierung",
    "char_bas_status": "Status",
    "char_btn": "Schaltflächen",
    "char_btn_delete": "Löschen",
    "char_btn_new": "Neu",
    "char_btn_next": "Vor",
    "char_btn_preview": "Zurück",
    "char_btn_save": "Speichern",
    "char_edu": "Ausbildung",
    "char_edu_art_music": "Kunst/Musik",
    "char_edu_autodidactic": "autodidaktisch",
    "char_edu_job": "Beruf",
    "char_edu_job_education": "Berufsausbildung",
    "char_edu_notes": "Notizen",
    "char_edu_school": "Schule",
    "char_edu_sport": "Sport",
    "char_edu_technologie": "Technik",
    "char_edu_unitversity": "Universität",
    "char_groups": "Gruppen",
    "char_groups_des": "Beschreibung",
    "char_groups_title": "Bezeichnung",
    "char_origin": "Herkunft",
    "char_origin_birthplace": "Geburtsort",
    "char_origin_father": "Vater",
    "char_origin_mother": "Mutter",
    "char_origin_notes": "Notizen",
    "char_origin_reference_person": "Bezugsperson",
    "char_origin_siblings": "Geschwister",
    "char_person": "Persönlichkeit",
    "char_person_behavior": "Verhalten",
    "char_person_beliefs": "Glaubensgrundsatz",
    "char_person_fears": "Ängste",
    "char_person_life_goals": "Lebensziel",
    "char_person_motivaton": "Motivation",
    "char_person_neg": "negative Charaktereigenschaft",
    "char_person_notes": "Notizen",
    "char_person_pos": "positve Charaktereigenschaft",
    "char_person_strengths": "Stärken",
    "char_person_talente": "Talente",
    "char_person_weakness": "Schwächen",
    "char_psy": "Psychologie Profil",
    "char_psy_aggression": "Aggressivität",
    "char_psy_diagnostics": "Diagnose",
    "char_psy_formative": "Prägung",
    "char_psy_humor": "Humor",
    "char_psy_medication": "Medikamente",
    "char_psy_moral": "Moral",
    "char_psy_norms": "Normen",
    "char_psy_notes": "Notizen",
    "char_psy_selfimage": "Selbstbild",
    "char_psy_socialization": "Sozialisation",
    "char_psy_symptoms": "Symptome",
    "char_psy_taboos": "Tabus",
    "char_psy_temperament": "Temperament",
    "char_psy_therapy": "Therapie",
    "char_psy_trauma": "Trauma",
    "char_psy_values": "Werte",
    "help": "Hilfe",
    "help_chapters": "Organisieren Sie Ihre Geschichte in Kapitel und beschreiben Sie deren Inhalt.",
    "help_chars": "Definieren Sie Ihre Charaktere: Namen, Rollen, Eigenschaften und Beziehungen.",
    "help_editorwindow": "Editor Fenster",
    "help_helpwindow": "Hilfe Fenster",
    "help_locations": "Beschreiben Sie die in Ihrer Geschichte verwendeten Orte, einschließlich Atmosphäre und Relevanz.",
    "help_objects": "isten Sie wichtige Objekte und deren Bedeutung in der Geschichte auf.",
    "help_preferencewindow": "Nehmen Sie die gewünschten Einstellungen vor",
    "help_project": "Geben Sie allgemeine Informationen zu Ihrem Schreibprojekt an, wie Titel, Genre und Ziele.",
    "help_projectwindow": "Wählen die Tabelle, die Sie berarbieten wollen",
    "help_scenes": "eschreiben Sie einzelne Szenen, deren Zweck und Umgebung.",
    "help_startwindow": "Wählen Sie die gewünschte Funktion",
    "help_storylines": "Skizzieren Sie die Haupt-Handlungsstränge und deren Entwicklung im Laufe der Zeit.",
    "location": "Orte",
    "location_btn_delete": "Löschen",
    "location_btn_new": "Neu",
    "location_btn_next": "Vor",
    "location_btn_preview": "Zurück",
    "location_btn_save": "Speichern",
    "location_title": "Titel",
    "location_description": "Beschreibung",
    "location_notes": "Notizen",
    "menu": "Menü",
    "menu_edit": "Bearbeiten",
    "menu_file": "Datei",
    "menu_help": "Hilfe ",
    "menu_language": "Sprache",
    "menu_settings": "Einstellungen",
    "object_btn_delete": "Löschen",
    "object_btn_new": "Neu",
    "object_btn_next": "Vor",
    "object_btn_preview": "Zurück",
    "object_btn_save": "Speichern",
    "object_notes": "Notizen",
    "object": "Objekte",
    "object_title": "Titel",
    "object_description": "Beschreibung",
    "preference_action_save": "Speichern",
    "preference_action_cancel": "Abbrechen",
    "pro": "Projekte",
    "pro_btn_project": "Projekt",
    "pro_btn_characters": "Charaktere", 
    "pro_btn_storylines": "Erzählstränge",
    "pro_btn_chapters": "Kapitel",
    "pro_btn_scenes": "Szenen",
    "pro_btn_objects": "Objekte",
    "pro_btn_locations": "Orte",
    "pro_btn_exit": "Beenden",
    "pro_btn": "Schaltflächen",
    "pro_btn_delete": "Löschen",
    "pro_btn_new": "Neu",
    "pro_btn_next": "Vor",
    "pro_btn_preview": "Zurück",
    "pro_btn_save": "Speichern",
    "pro_detail": "Details",
    "pro_detail_author": "Autor",
    "pro_detail_chapters": "Kapitel",
    "pro_detail_cover_image": "Titelbild",
    "pro_detail_day": "Tage bis Abgabe",
    "pro_detail_deadline": "Abgabedatum",
    "pro_detail_form_label": "Projekt",
    "pro_detail_genre": "Genre",
    "pro_detail_groups": "Gruppen",
    "pro_detail_locations": "Orte",
    "pro_detail_main_char": "Hauptcharaktere",
    "pro_detail_narrative_perpective": "Perspektive Erzähler:in",
    "pro_detail_objects": "Objekte",
    "pro_detail_premise": "Prämisse",
    "pro_detail_scenes": "Szenen",
    "pro_detail_startdate": "Startdatum",
    "pro_detail_storylines": "Erzählstränge",
    "pro_detail_subtitle": "Untertitel",
    "pro_detail_support_char": "Nebencharaktere",
    "pro_detail_targetgroup": "Zielgruppe",
    "pro_detail_timeline_": "Zeitlinie",
    "pro_detail_timline": "Zeitlinie",
    "pro_detail_title": "Titel",
    "pro_detail_window_title": "Datenbanken",
    "pro_detail_words_count_day": "Wörter am Tag",
    "pro_detail_words_count_goal": "Ziel Wortanzahl",
    "scene": "Szenen",
    "scene_btn_delete": "Löschen",
    "scene_btn_new": "Neu",
    "scene_btn_next": "Vor",
    "scene_btn_preview": "Zurück",
    "scene_btn_save": "Speichern",
    "scene_title": "Titel",
    "scene_number": "Nummer",
    "scene_summary": "Zusammenfassung",
    "scene_characters": "Charaktere",
    "scene_conflict": "Konflikt",
    "scene_duration": "Dauer",
    "scene_goal": "Ziel",
    "scene_locations": "Orte",
    "scene_mood": "Stimmung",
    "scene_notes": "Notizen",
    "scene_objects": "Objekte",
    "scene_outcome": "Ergebnis",
    "scene_premise": "Prämisse",
    "scene_type": "Typ",
    "start": "csNova",
    "start_btn_exit": "Beenden",
    "start_btn_help": "Hilfe && Tutorial",
    "start_btn_settings": "Einstellungen",
    "start_btn_load_project": "Projekt laden ...",
    "start_btn_new_project": "Datenbanken",
    "storyline": "Erzählstränge",
    "storyline_btn_delete": "Löschen",
    "storyline_btn_new": "Neu",
    "storyline_btn_next": "Vor",
    "storyline_btn_preview": "Zurück",
    "storyline_btn_save": "Speichern",
    "storyline_chapters": "Kapitel",
    "storyline_characters": "Charaktere",
    "storyline_description": "Beschreibung",
    "storyline_notes": "Notizen",
    "storyline_objects": "Objekte",
    "storyline_premise": "Prämisse",
    "storyline_scenes": "Scenen",
    "storyline_timeline": "Zeitlinie",
    "storyline_title": "Titel",
    "storyline_transformation": "Transformation",
    "win": "Fenster",
    "win_editor_title": "Editor Fenster",
    "win_help_title": "Hilfe",
    "win_preference_title": "Einstellungen",
    "win_start_title": "csNova"
  },
  {
    "ID": "en",
    "chapter": "Chapter",
    "chapter_btn_delete": "Delete",
    "chapter_btn_new": "New",
    "chapter_btn_next": "Before",
    "chapter_btn_preview": "Back",
    "chapter_btn_save": "Save",
    "chapter_number": "Number", 
    "chapter_summary": "Summary",
    "chapter_characters": "Characters",
    "chapter_locations": "Places",
    "chapter_notes": "Notes",
    "chapter_opjects": "Objects",
    "chapter_premise": "premise",
    "chapter_scenes": "Scenes",
    "chapter_title": "title",
    "char": "Characters",
    "char_app": "Look",
    "char_app_body_type": "Body type",
    "char_app_charisma": "Charisma",
    "char_app_eye_color": "Eye color",
    "char_app_eye_shape": "Eye shape",
    "char_app_face_shape": "Face shape",
    "char_app_hair": "Hair",
    "char_app_hair_color": "Hair color",
    "char_app_height": "Size",
    "char_app_notes": "Notes",
    "char_app_posture": "stature",
    "char_app_skin": "skin",
    "char_app_specials": "Special features",
    "char_app2": "Appearance Details",
    "char_app2_arms": "poor",
    "char_app2_buttocks": "buttocks",
    "char_app2_chest": "Breast",
    "char_app2_feet": "Feet",
    "char_app2_finger": "finger",
    "char_app2_hands": "hands",
    "char_app2_head": "Head",
    "char_app2_hip_waist": "hips, waist",
    "char_app2_legs": "Legs",
    "char_app2_notes": "Notes",
    "char_app2_shoulder": "Shoulder",
    "char_app2_toes": "toes",
    "char_bas": "Basic data",
    "char_bas_age": "Old",
    "char_bas_born": "birth date",
    "char_bas_firstname": "First name",
    "char_bas_gender": "Gender",
    "char_bas_group": "group",
    "char_bas_name": "name",
    "char_bas_nickname": "Nickname",
    "char_bas_notes": "Notes",
    "char_bas_role": "role",
    "char_bas_sex_orientation": "sexual orientation",
    "char_bas_status": "status",
    "char_btn": "Buttons",
    "char_btn_delete": "Delete",
    "char_btn_new": "New",
    "char_btn_next": "Before",
    "char_btn_preview": "Back",
    "char_btn_save": "Save",
    "char_edu": "Training",
    "char_edu_art_music": "Art/Music",
    "char_edu_autodidactic": "autodidactic",
    "char_edu_job": "Profession",
    "char_edu_job_education": "Vocational training",
    "char_edu_notes": "Notes",
    "char_edu_school": "School",
    "char_edu_sport": "sport",
    "char_edu_technologie": "Technology",
    "char_edu_unitversity": "university",
    "char_groups": "Groups",
    "char_groups_des": "Description",
    "char_groups_title": "Designation",
    "char_origin": "Origin",
    "char_origin_birthplace": "Place of birth",
    "char_origin_father": "Father",
    "char_origin_mother": "Mother",
    "char_origin_notes": "Notes",
    "char_origin_reference_person": "Reference person",
    "char_origin_siblings": "Siblings",
    "char_person": "personality",
    "char_person_behavior": "Behave",
    "char_person_beliefs": "Article of faith",
    "char_person_fears": "Fears",
    "char_person_life_goals": "Life goal",
    "char_person_motivaton": "motivation",
    "char_person_neg": "negative character trait",
    "char_person_notes": "Notes",
    "char_person_pos": "positive character trait",
    "char_person_strengths": "Strengthen",
    "char_person_talente": "Talents",
    "char_person_weakness": "Weaken",
    "char_psy": "Psychology Profile",
    "char_psy_aggression": "aggressiveness",
    "char_psy_diagnostics": "diagnosis",
    "char_psy_formative": "Embossing",
    "char_psy_humor": "humor",
    "char_psy_medication": "Medications",
    "char_psy_moral": "Moral",
    "char_psy_norms": "Standards",
    "char_psy_notes": "Notes",
    "char_psy_selfimage": "Self-image",
    "char_psy_socialization": "socialization",
    "char_psy_symptoms": "Symptoms",
    "char_psy_taboos": "Taboos",
    "char_psy_temperament": "temperament",
    "char_psy_therapy": "therapy",
    "char_psy_trauma": "trauma",
    "char_psy_values": "Values",
    "help": "Help",
    "help_chapters": "Organize your story into chapters and describe their content.",
    "help_chars": "Define your characters: names, roles, characteristics and relationships.",
    "help_editorwindow": "Editor window",
    "help_helpwindow": "Help window",
    "help_locations": "Describe the locations used in your story, including atmosphere and relevance.",
    "help_objects": "Identify important objects and their significance in history.",
    "help_preferencewindow": "Make the desired settings",
    "help_project": "Provide general information about your writing project, such as title, genre, and goals.",
    "help_projectwindow": "Select the table you want to edit",
    "help_scenes": "Describe individual scenes, their purpose and setting.",
    "help_startwindow": "Select the desired function",
    "help_storylines": "Outline the main plot lines and their development over time.",
    "location": "Places",
    "location_btn_delete": "Delete",
    "location_btn_new": "New",
    "location_btn_next": "Before",
    "location_btn_preview": "Back",
    "location_btn_save": "Save",
    "location_title": "title",
    "location_description": "Description",
    "location_notes": "Notes",
    "menu": "menu",
    "menu_edit": "Edit",
    "menu_file": "file",
    "menu_help": "Help ",
    "menu_language": "Language",
    "menu_settings": "Settings",
    "object_btn_delete": "Delete",
    "object_btn_new": "New",
    "object_btn_next": "Before",
    "object_btn_preview": "Back",
    "object_btn_save": "Save",
    "object_notes": "Notes",
    "object": "Objects",
    "object_title": "title",
    "object_description": "Description",
    "preference_action_save": "Save",
    "preference_action_cancel": "Cancel",
    "pro": "Projects",
    "pro_btn_project": "Project",
    "pro_btn_characters": "Characters",
    "pro_btn_storylines": "Storylines",
    "pro_btn_chapters": "Chapters",
    "pro_btn_scenes": "Scenes",
    "pro_btn_objects": "Objects",
    "pro_btn_locations": "Locations",
    "pro_btn_exit": "Exit",
    "pro_btn": "Buttons",
    "pro_btn_delete": "Delete",
    "pro_btn_new": "New",
    "pro_btn_next": "Before",
    "pro_btn_preview": "Back",
    "pro_btn_save": "Save",
    "pro_detail": "Details",
    "pro_detail_author": "author",
    "pro_detail_chapters": "Chapter",
    "pro_detail_cover_image": "Cover image",
    "pro_detail_day": "Days until delivery",
    "pro_detail_deadline": "Submission date",
    "pro_detail_form_label": "project",
    "pro_detail_genre": "genre",
    "pro_detail_groups": "Groups",
    "pro_detail_locations": "Places",
    "pro_detail_main_char": "Main characters",
    "pro_detail_narrative_perpective": "Perspective narrator",
    "pro_detail_objects": "Objects",
    "pro_detail_premise": "premise",
    "pro_detail_scenes": "Scenes",
    "pro_detail_startdate": "Start date",
    "pro_detail_storylines": "narrative threads",
    "pro_detail_subtitle": "Subtitles",
    "pro_detail_support_char": "supporting characters",
    "pro_detail_targetgroup": "Target group",
    "pro_detail_timeline_": "Timeline",
    "pro_detail_timline": "Timeline",
    "pro_detail_title": "title",
    "pro_detail_window_title": "databases",
    "pro_detail_words_count_day": "Words a day",
    "pro_detail_words_count_goal": "Target word count",
    "scene": "Scenes",
    "scene_btn_delete": "Delete",
    "scene_btn_new": "New",
    "scene_btn_next": "Before",
    "scene_btn_preview": "Back",
    "scene_btn_save": "Save",
    "scene_number": "Number",
    "scene_summary": "Summary", 
    "scene_title": "title",
    "scene_characters": "Characters",
    "scene_conflict": "conflict",
    "scene_duration": "Length of time",
    "scene_goal": "Goal",
    "scene_locations": "Places",
    "scene_mood": "Mood",
    "scene_notes": "Notes",
    "scene_objects": "Objects",
    "scene_outcome": "Result",
    "scene_premise": "premise",
    "scene_type": "type",
    "start": "csNova",
    "start_btn_exit": "Finish",
    "start_btn_help": "Help && Tutorial",
    "start_btn_settings": "Settings",
    "start_btn_load_project": "Load project...",
    "start_btn_new_project": "databases",
    "storyline": "narrative threads",
    "storyline_btn_delete": "Delete",
    "storyline_btn_new": "New",
    "storyline_btn_next": "Before",
    "storyline_btn_preview": "Back",
    "storyline_btn_save": "Save",
    "storyline_chapters": "Chapter",
    "storyline_characters": "Characters",
    "storyline_description": "Description",
    "storyline_notes": "Notes",
    "storyline_objects": "Objects",
    "storyline_premise": "premise",
    "storyline_scenes": "Scenes",
    "storyline_timeline": "Timeline",
    "storyline_title": "title",
    "storyline_transformation": "transformation",
    "win": "Window",
    "win_editor_title": "Editor window",
    "win_help_title": "Help",
    "win_preference_title": "Settings",
    "win_start_title": "csNova"
  },
  {
    "ID": "es",
    "chapter": "Capítulo",
    "chapter_btn_delete": "Borrar",
    "chapter_btn_new": "Nuevo",
    "chapter_btn_next": "Antes",
    "chapter_btn_preview": "Atrás",
    "chapter_btn_save": "Ahorrar",
    "chapter_number": "Número",
    "chapter_summary": "Resumen",
    "chapter_characters": "Personajes",
    "chapter_locations": "Lugares",
    "chapter_notes": "Notas",
    "chapter_opjects": "Objetos",
    "chapter_premise": "premisa",
    "chapter_scenes": "Escenas",
    "chapter_title": "título",
    "char": "Personajes",
    "char_app": "Mirar",
    "char_app_body_type": "Tipo de cuerpo",
    "char_app_charisma": "Carisma",
    "char_app_eye_color": "Color de los ojos",
    "char_app_eye_shape": "Forma del ojo",
    "char_app_face_shape": "Forma de la cara",
    "char_app_hair": "Cabello",
    "char_app_hair_color": "Color de pelo",
    "char_app_height": "Tamaño",
    "char_app_notes": "Notas",
    "char_app_posture": "estatura",
    "char_app_skin": "piel",
    "char_app_specials": "Características especiales",
    "char_app2": "Detalles de apariencia",
    "char_app2_arms": "pobre",
    "char_app2_buttocks": "nalgas",
    "char_app2_chest": "Mama",
    "char_app2_feet": "Pies",
    "char_app2_finger": "dedo",
    "char_app2_hands": "manos",
    "char_app2_head": "Cabeza",
    "char_app2_hip_waist": "caderas, cintura",
    "char_app2_legs": "Piernas",
    "char_app2_notes": "Notas",
    "char_app2_shoulder": "Hombro",
    "char_app2_toes": "dedos de los pies",
    "char_bas": "Datos básicos",
    "char_bas_age": "Viejo",
    "char_bas_born": "fecha de nacimiento",
    "char_bas_firstname": "Nombre de pila",
    "char_bas_gender": "Género",
    "char_bas_group": "grupo",
    "char_bas_name": "nombre",
    "char_bas_nickname": "Apodo",
    "char_bas_notes": "Notas",
    "char_bas_role": "role",
    "char_bas_sex_orientation": "orientación sexual",
    "char_bas_status": "estado",
    "char_btn": "Botones",
    "char_btn_delete": "Borrar",
    "char_btn_new": "Nuevo",
    "char_btn_next": "Antes",
    "char_btn_preview": "Atrás",
    "char_btn_save": "Ahorrar",
    "char_edu": "Capacitación",
    "char_edu_art_music": "Arte/Música",
    "char_edu_autodidactic": "autodidáctico",
    "char_edu_job": "Profesión",
    "char_edu_job_education": "Formación profesional",
    "char_edu_notes": "Notas",
    "char_edu_school": "Escuela",
    "char_edu_sport": "deporte",
    "char_edu_technologie": "Tecnología",
    "char_edu_unitversity": "universidad",
    "char_groups": "Grupos",
    "char_groups_des": "Descripción",
    "char_groups_title": "Designación",
    "char_origin": "Origen",
    "char_origin_birthplace": "Lugar de nacimiento",
    "char_origin_father": "Padre",
    "char_origin_mother": "Madre",
    "char_origin_notes": "Notas",
    "char_origin_reference_person": "Persona de referencia",
    "char_origin_siblings": "Hermanos",
    "char_person": "personalidad",
    "char_person_behavior": "Comportarse",
    "char_person_beliefs": "Artículo de fe",
    "char_person_fears": "Miedos",
    "char_person_life_goals": "Objetivo de vida",
    "char_person_motivaton": "motivación",
    "char_person_neg": "rasgo de carácter negativo",
    "char_person_notes": "Notas",
    "char_person_pos": "rasgo de carácter positivo",
    "char_person_strengths": "Fortalecer",
    "char_person_talente": "Prendas",
    "char_person_weakness": "Debilitar",
    "char_psy": "Perfil de Psicología",
    "char_psy_aggression": "agresividad",
    "char_psy_diagnostics": "diagnóstico",
    "char_psy_formative": "Realce",
    "char_psy_humor": "humor",
    "char_psy_medication": "Medicamentos",
    "char_psy_moral": "Moral",
    "char_psy_norms": "Normas",
    "char_psy_notes": "Notas",
    "char_psy_selfimage": "Autoimagen",
    "char_psy_socialization": "socialización",
    "char_psy_symptoms": "Síntomas",
    "char_psy_taboos": "Tabúes",
    "char_psy_temperament": "temperamento",
    "char_psy_therapy": "terapia",
    "char_psy_trauma": "trauma",
    "char_psy_values": "Valores",
    "help": "Ayuda",
    "help_chapters": "Organiza tu historia en capítulos y describe su contenido.",
    "help_chars": "Define tus personajes: nombres, roles, características y relaciones.",
    "help_editorwindow": "Ventana del editor",
    "help_helpwindow": "Ventana de ayuda",
    "help_locations": "Describe los lugares utilizados en tu historia, incluyendo la atmósfera y la relevancia.",
    "help_objects": "Identificar objetos importantes y su significado en la historia.",
    "help_preferencewindow": "Realice los ajustes deseados",
    "help_project": "Proporcione información general sobre su proyecto de escritura, como título, género y objetivos.",
    "help_projectwindow": "Seleccione la tabla que desea editar",
    "help_scenes": "Describe escenas individuales, su propósito y entorno.",
    "help_startwindow": "Seleccione la función deseada",
    "help_storylines": "Esbozar las principales líneas argumentales y su desarrollo a lo largo del tiempo.",
    "location": "Lugares",
    "location_btn_delete": "Borrar",
    "location_btn_new": "Nuevo",
    "location_btn_next": "Antes",
    "location_btn_preview": "Atrás",
    "location_btn_save": "Ahorrar",
    "location_title": "título",
    "location_description": "Descripción",
    "location_notes": "Notas",
    "menu": "menú",
    "menu_edit": "Editar",
    "menu_file": "archivo",
    "menu_help": "Ayuda ",
    "menu_language": "Idioma",
    "menu_settings": "Ajustes",
    "object_btn_delete": "Borrar",
    "object_btn_new": "Nuevo",
    "object_btn_next": "Antes",
    "object_btn_preview": "Atrás",
    "object_btn_save": "Ahorrar",
    "object_notes": "Notas",
    "object": "Objetos",
    "object_title": "título",
    "object_description": "Descripción",
    "preference_action_save": "Ahorrar",
    "preference_action_cancel": "Cancelar",
    "pro": "Proyectos",
    "pro_btn_project": "Proyecto",
    "pro_btn_characters": "Personajes",
    "pro_btn_storylines": "Líneas argumentales",
    "pro_btn_chapters": "Capítulos",
    "pro_btn_scenes": "Escenas",
    "pro_btn_objects": "Objetos",
    "pro_btn_locations": "Lugares",
    "pro_btn_exit": "Salir",
    "pro_btn": "Botones",
    "pro_btn_delete": "Borrar",
    "pro_btn_new": "Nuevo",
    "pro_btn_next": "Antes",
    "pro_btn_preview": "Atrás",
    "pro_btn_save": "Ahorrar",
    "pro_detail": "Detalles",
    "pro_detail_author": "autor",
    "pro_detail_chapters": "Capítulo",
    "pro_detail_cover_image": "Imagen de portada",
    "pro_detail_day": "Días hasta la entrega",
    "pro_detail_deadline": "Fecha de presentación",
    "pro_detail_form_label": "proyecto",
    "pro_detail_genre": "género",
    "pro_detail_groups": "Grupos",
    "pro_detail_locations": "Lugares",
    "pro_detail_main_char": "Personajes principales",
    "pro_detail_narrative_perpective": "Narrador en perspectiva",
    "pro_detail_objects": "Objetos",
    "pro_detail_premise": "premisa",
    "pro_detail_scenes": "Escenas",
    "pro_detail_startdate": "Fecha de inicio",
    "pro_detail_storylines": "hilos narrativos",
    "pro_detail_subtitle": "Subtítulos",
    "pro_detail_support_char": "personajes secundarios",
    "pro_detail_targetgroup": "Grupo objetivo",
    "pro_detail_timeline_": "Cronología",
    "pro_detail_timline": "Cronología",
    "pro_detail_title": "título",
    "pro_detail_window_title": "bases de datos",
    "pro_detail_words_count_day": "Palabras al día",
    "pro_detail_words_count_goal": "Recuento de palabras objetivo",
    "scene": "Escenas",
    "scene_btn_delete": "Borrar",
    "scene_btn_new": "Nuevo",
    "scene_btn_next": "Antes",
    "scene_btn_preview": "Atrás",
    "scene_btn_save": "Ahorrar",
    "scene_number": "Número",
    "scene_summary": "Resumen",
    "scene_title": "título",
    "scene_characters": "Personajes",
    "scene_conflict": "conflicto",
    "scene_duration": "Duración del tiempo",
    "scene_goal": "Meta",
    "scene_locations": "Lugares",
    "scene_mood": "Ánimo",
    "scene_notes": "Notas",
    "scene_objects": "Objetos",
    "scene_outcome": "Resultado",
    "scene_premise": "premisa",
    "scene_type": "tipo",
    "start": "csNova",
    "start_btn_exit": "Finalizar",
    "start_btn_help": "Ayuda y tutorial",
    "start_btn_settings": "Ajustes",
    "start_btn_load_project": "Cargar proyecto...",
    "start_btn_new_project": "bases de datos",
    "storyline": "hilos narrativos",
    "storyline_btn_delete": "Borrar",
    "storyline_btn_new": "Nuevo",
    "storyline_btn_next": "Antes",
    "storyline_btn_preview": "Atrás",
    "storyline_btn_save": "Ahorrar",
    "storyline_chapters": "Capítulo",
    "storyline_characters": "Personajes",
    "storyline_description": "Descripción",
    "storyline_notes": "Notas",
    "storyline_objects": "Objetos",
    "storyline_premise": "premisa",
    "storyline_scenes": "Escenas",
    "storyline_timeline": "Cronología",
    "storyline_title": "título",
    "storyline_transformation": "transformación",
    "win": "Ventana",
    "win_editor_title": "Ventana del editor",
    "win_help_title": "Ayuda",
    "win_preference_title": "Ajustes",
    "win_start_title": "csNova"
  },
  {
    "ID": "fr",
    "chapter": "Chapitre",
    "chapter_btn_delete": "Supprimer",
    "chapter_btn_new": "Nouveau",
    "chapter_btn_next": "Avant",
    "chapter_btn_preview": "Dos",
    "chapter_btn_save": "Sauvegarder",
    "chapter_number": "Numéro",
    "chapter_summary": "Résumé",
    "chapter_characters": "Personnages",
    "chapter_locations": "Lieux",
    "chapter_notes": "Remarques",
    "chapter_opjects": "Objets",
    "chapter_premise": "prémisse",
    "chapter_scenes": "Scènes",
    "chapter_title": "titre",
    "char": "Personnages",
    "char_app": "Regarder",
    "char_app_body_type": "Type de corps",
    "char_app_charisma": "Charisme",
    "char_app_eye_color": "Couleur des yeux",
    "char_app_eye_shape": "Forme des yeux",
    "char_app_face_shape": "Forme du visage",
    "char_app_hair": "Cheveux",
    "char_app_hair_color": "Couleur des cheveux",
    "char_app_height": "Taille",
    "char_app_notes": "Remarques",
    "char_app_posture": "stature",
    "char_app_skin": "peau",
    "char_app_specials": "Caractéristiques spéciales",
    "char_app2": "Détails d'apparence",
    "char_app2_arms": "pauvre",
    "char_app2_buttocks": "fesses",
    "char_app2_chest": "Sein",
    "char_app2_feet": "Pieds",
    "char_app2_finger": "doigt",
    "char_app2_hands": "mains",
    "char_app2_head": "Tête",
    "char_app2_hip_waist": "hanches, taille",
    "char_app2_legs": "Jambes",
    "char_app2_notes": "Remarques",
    "char_app2_shoulder": "Épaule",
    "char_app2_toes": "orteils",
    "char_bas": "Données de base",
    "char_bas_age": "Vieux",
    "char_bas_born": "date de naissance",
    "char_bas_firstname": "Prénom",
    "char_bas_gender": "Genre",
    "char_bas_group": "groupe",
    "char_bas_name": "nom",
    "char_bas_nickname": "Surnom",
    "char_bas_notes": "Remarques",
    "char_bas_role": "rôle",
    "char_bas_sex_orientation": "orientation sexuelle",
    "char_bas_status": "statut",
    "char_btn": "Boutons",
    "char_btn_delete": "Supprimer",
    "char_btn_new": "Nouveau",
    "char_btn_next": "Avant",
    "char_btn_preview": "Dos",
    "char_btn_save": "Sauvegarder",
    "char_edu": "Entraînement",
    "char_edu_art_music": "Art/Musique",
    "char_edu_autodidactic": "autodidacte",
    "char_edu_job": "Profession",
    "char_edu_job_education": "Formation professionnelle",
    "char_edu_notes": "Remarques",
    "char_edu_school": "École",
    "char_edu_sport": "sport",
    "char_edu_technologie": "Technologie",
    "char_edu_unitversity": "université",
    "char_groups": "Groupes",
    "char_groups_des": "Description",
    "char_groups_title": "Désignation",
    "char_origin": "Origine",
    "char_origin_birthplace": "Lieu de naissance",
    "char_origin_father": "Père",
    "char_origin_mother": "Mère",
    "char_origin_notes": "Remarques",
    "char_origin_reference_person": "Personne de référence",
    "char_origin_siblings": "Frères et sœurs",
    "char_person": "personnalité",
    "char_person_behavior": "Se comporter",
    "char_person_beliefs": "Article de foi",
    "char_person_fears": "Peurs",
    "char_person_life_goals": "Objectif de vie",
    "char_person_motivaton": "motivation",
    "char_person_neg": "trait de caractère négatif",
    "char_person_notes": "Remarques",
    "char_person_pos": "trait de caractère positif",
    "char_person_strengths": "Renforcer",
    "char_person_talente": "Talents",
    "char_person_weakness": "Affaiblir",
    "char_psy": "Profil psychologique",
    "char_psy_aggression": "agressivité",
    "char_psy_diagnostics": "diagnostic",
    "char_psy_formative": "Gaufrage",
    "char_psy_humor": "humour",
    "char_psy_medication": "Médicaments",
    "char_psy_moral": "Morale",
    "char_psy_norms": "Normes",
    "char_psy_notes": "Remarques",
    "char_psy_selfimage": "Image de soi",
    "char_psy_socialization": "socialisation",
    "char_psy_symptoms": "Symptômes",
    "char_psy_taboos": "Tabous",
    "char_psy_temperament": "tempérament",
    "char_psy_therapy": "thérapie",
    "char_psy_trauma": "traumatisme",
    "char_psy_values": "Valeurs",
    "help": "Aide",
    "help_chapters": "Organisez votre histoire en chapitres et décrivez leur contenu.",
    "help_chars": "Définissez vos personnages : noms, rôles, caractéristiques et relations.",
    "help_editorwindow": "Fenêtre de l'éditeur",
    "help_helpwindow": "Fenêtre d'aide",
    "help_locations": "Décrivez les lieux utilisés dans votre histoire, y compris l’atmosphère et la pertinence.",
    "help_objects": "Identifier les objets importants et leur signification dans l’histoire.",
    "help_preferencewindow": "Effectuez les réglages souhaités",
    "help_project": "Fournissez des informations générales sur votre projet d’écriture, telles que le titre, le genre et les objectifs.",
    "help_projectwindow": "Sélectionnez le tableau que vous souhaitez modifier",
    "help_scenes": "Décrivez les scènes individuelles, leur objectif et leur cadre.",
    "help_startwindow": "Sélectionnez la fonction souhaitée",
    "help_storylines": "Décrivez les principales intrigues et leur évolution au fil du temps.",
    "location": "Lieux",
    "location_btn_delete": "Supprimer",
    "location_btn_new": "Nouveau",
    "location_btn_next": "Avant",
    "location_btn_preview": "Dos",
    "location_btn_save": "Sauvegarder",
    "location_title": "titre",
    "location_description": "Description",
    "location_notes": "Remarques",
    "menu": "menu",
    "menu_edit": "Modifier",
    "menu_file": "déposer",
    "menu_help": "Aide ",
    "menu_language": "Langue",
    "menu_settings": "Paramètres",
    "object_btn_delete": "Supprimer",
    "object_btn_new": "Nouveau",
    "object_btn_next": "Avant",
    "object_btn_preview": "Dos",
    "object_btn_save": "Sauvegarder",
    "object_notes": "Remarques",
    "object": "Objets",
    "object_title": "titre",
    "object_description": "Description",
    "preference_action_save": "Sauvegarder",
    "preference_action_cancel": "Annuler",
    "pro": "Projets",
    "pro_btn_project": "Projet",
    "pro_btn_characters": "Personnages",
    "pro_btn_storylines": "Lignes narratives",
    "pro_btn_chapters": "Chapitres",
    "pro_btn_scenes": "Scènes",
    "pro_btn_objects": "Objets",
    "pro_btn_locations": "Lieux",
    "pro_btn_exit": "Sortie",
    "pro_btn": "Boutons",
    "pro_btn_delete": "Supprimer",
    "pro_btn_new": "Nouveau",
    "pro_btn_next": "Avant",
    "pro_btn_preview": "Dos",
    "pro_btn_save": "Sauvegarder",
    "pro_detail": "Détails",
    "pro_detail_author": "auteur",
    "pro_detail_chapters": "Chapitre",
    "pro_detail_cover_image": "Image de couverture",
    "pro_detail_day": "Jours jusqu'à la livraison",
    "pro_detail_deadline": "Date de soumission",
    "pro_detail_form_label": "projet",
    "pro_detail_genre": "genre",
    "pro_detail_groups": "Groupes",
    "pro_detail_locations": "Lieux",
    "pro_detail_main_char": "Personnages principaux",
    "pro_detail_narrative_perpective": "Narrateur en perspective",
    "pro_detail_objects": "Objets",
    "pro_detail_premise": "prémisse",
    "pro_detail_scenes": "Scènes",
    "pro_detail_startdate": "Date de début",
    "pro_detail_storylines": "fils narratifs",
    "pro_detail_subtitle": "Sous-titres",
    "pro_detail_support_char": "personnages secondaires",
    "pro_detail_targetgroup": "Groupe cible",
    "pro_detail_timeline_": "Chronologie",
    "pro_detail_timline": "Chronologie",
    "pro_detail_title": "titre",
    "pro_detail_window_title": "bases de données",
    "pro_detail_words_count_day": "Mots par jour",
    "pro_detail_words_count_goal": "Nombre de mots cible",
    "scene": "Scènes",
    "scene_btn_delete": "Supprimer",
    "scene_btn_new": "Nouveau",
    "scene_btn_next": "Avant",
    "scene_btn_preview": "Dos",
    "scene_btn_save": "Sauvegarder",
    "scene_number": "Numéro",
    "scene_summary": "Résumé",
    "scene_title": "titre",
    "scene_characters": "Personnages",
    "scene_conflict": "conflit",
    "scene_duration": "Durée",
    "scene_goal": "But",
    "scene_locations": "Lieux",
    "scene_mood": "Humeur",
    "scene_notes": "Remarques",
    "scene_objects": "Objets",
    "scene_outcome": "Résultat",
    "scene_premise": "prémisse",
    "scene_type": "taper",
    "start": "csNova",
    "start_btn_exit": "Finition",
    "start_btn_help": "Aide et tutoriel",
    "start_btn_settings": "Paramètres",
    "start_btn_load_project": "Charger le projet...",
    "start_btn_new_project": "bases de données",
    "storyline": "fils narratifs",
    "storyline_btn_delete": "Supprimer",
    "storyline_btn_new": "Nouveau",
    "storyline_btn_next": "Avant",
    "storyline_btn_preview": "Dos",
    "storyline_btn_save": "Sauvegarder",
    "storyline_chapters": "Chapitre",
    "storyline_characters": "Personnages",
    "storyline_description": "Description",
    "storyline_notes": "Remarques",
    "storyline_objects": "Objets",
    "storyline_premise": "prémisse",
    "storyline_scenes": "Scènes",
    "storyline_timeline": "Chronologie",
    "storyline_title": "titre",
    "storyline_transformation": "transformation",
    "win": "Fenêtre",
    "win_editor_title": "Fenêtre de l'éditeur",
    "win_help_title": "Aide",
    "win_preference_title": "Paramètres",
    "win_start_title": "csNova"
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
    {"name": "pro_header", "label_key": "pro", "type": "header"},
    {"name": "title", "label_key": "pro_detail_title", "type": "text", "required": true, "max_length": 120},
    {"name": "subtitle", "label_key": "pro_detail_subtitle", "type": "text", "required": false, "max_length": 120},
    {"name": "author", "label_key": "pro_detail_author", "type": "text", "required": true, "max_length": 80},
    {"name": "premise", "label_key": "pro_detail_premise", "type": "text", "required": false, "max_length": 200},
    {"name": "genre", "label_key": "pro_detail_genre", "type": "text", "required": false, "max_length": 80},
    {"name": "narrative_perspective", "label_key": "pro_detail_narrative_perspective", "type": "text", "required": false, "max_length": 80},
    {"name": "timeline", "label_key": "pro_detail_timeline", "type": "text", "required": false, "max_length": 80},
    {"name": "target_group", "label_key": "pro_detail_targetgroup", "type": "text", "required": false, "max_length": 80},
    {"name": "start_date", "label_key": "pro_detail_startdate", "type": "date", "required": false},
    {"name": "deadline", "label_key": "pro_detail_deadline", "type": "date", "required": false},
    {"name": "words_count_goal", "label_key": "pro_detail_words_count_goal", "type": "spin", "required": false, "max": 1000000},
    {"name": "cover_image", "label_key": "pro_detail_cover_image", "type": "text", "required": false, "max_length": 120}
  ],
  "characters": [
    {"name": "char_header", "label_key": "char", "type": "header"},
    {"name": "char_bas_name", "label_key": "char_bas_name", "type": "text", "required": true, "max_length": 80},
    {"name": "char_bas_nickname", "label_key": "char_bas_nickname", "type": "text", "required": false, "max_length": 80},
    {"name": "char_bas_gender", "label_key": "char_bas_gender", "type": "text", "required": true},
    {"name": "char_bas_age", "label_key": "char_bas_age", "type": "spin", "required": false, "max": 120},
    {"name": "char_bas_role", "label_key": "char_bas_role", "type": "text", "required": false, "max_length": 80},
    {"name": "char_bas_notes", "label_key": "char_bas_notes", "type": "text", "required": false, "max_length": 200}
  ],
  "chapters": [
    {"name": "chapters_header", "label_key": "chapters", "type": "header"},
    {"name": "chapter_number", "label_key": "chapter_number", "type": "spin", "required": false, "max": 999},
    {"name": "chapter_title", "label_key": "chapter_title", "type": "text", "required": true, "max_length": 120},
    {"name": "chapter_summary", "label_key": "chapter_summary", "type": "text", "required": false, "max_length": 500}
  ],
  "locations": [
    {"name": "location_header", "label_key": "location", "type": "header"},
    {"name": "location_title", "label_key": "location_title", "type": "text", "required": true, "max_length": 120},
    {"name": "location_description", "label_key": "location_description", "type": "text", "required": false, "max_length": 500},
    {"name": "location_notes", "label_key": "location_notes", "type": "text", "required": false, "max_length": 200}
  ],
  "objects": [
    {"name": "object_header", "label_key": "objects", "type": "header"},
    {"name": "object_title", "label_key": "object_title", "type": "text", "required": true, "max_length": 120},
    {"name": "object_description", "label_key": "object_description", "type": "text", "required": false, "max_length": 500},
    {"name": "object_notes", "label_key": "object_notes", "type": "text", "required": false, "max_length": 200}
  ],
  "scenes": [
    {"name": "scene_header", "label_key": "scene", "type": "header"},
    {"name": "scene_number", "label_key": "scene_number", "type": "spin", "required": false, "max": 9999},
    {"name": "scene_title", "label_key": "scene_title", "type": "text", "required": true, "max_length": 120},
    {"name": "scene_summary", "label_key": "scene_summary", "type": "text", "required": false, "max_length": 500}
  ],
  "storylines": [
    {"name": "storyline_header", "label_key": "storyline", "type": "header"},
    {"name": "storyline_title", "label_key": "storyline_title", "type": "text", "required": true, "max_length": 120},
    {"name": "storyline_description", "label_key": "storyline_description", "type": "text", "required": false, "max_length": 500},
    {"name": "storyline_notes", "label_key": "storyline_notes", "type": "text", "required": false, "max_length": 200}
  ]
}
```

## 6. - Programmecode

In diesem Abschnitt sind alle Programmcodes zusammengefasst.

### 6.1 Hauptprogramm (csnova.py)

```python
import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication
from core.database import init_schema
from config.settings import load_settings, save_settings
from gui.start_window import StartWindow
from gui.styles.form_styles import load_global_stylesheet

# Import central logging functions
from core.logger import setup_logging, log_header, log_section, log_subsection, log_info, log_error, log_exception

def main():
    setup_logging()  # Only once at program start
    log_header()
    log_section("csnova.py")
    log_subsection("main")
    try:
        log_info("Initializing database schema.")
        try:
            init_schema()
        except Exception as e:
            log_exception("Error initializing database schema", e)

        log_info("Loading settings.")
        try:
            settings = load_settings()
        except Exception as e:
            log_exception("Error loading settings", e)
            settings = {"language": "en"}

        language = settings.get("language", "en")
        log_info(f"Language set to '{language}'.")

        try:
            app = QApplication(sys.argv)
            app.setStyleSheet(load_global_stylesheet())  # Apply global stylesheet
            window = StartWindow(default_language=language)
            window.show()
            log_info("StartWindow shown.")
            app.exec()
        except Exception as e:
            log_exception("Error initializing GUI", e)

        # Save updated language setting if changed
        try:
            if hasattr(window, "translator") and hasattr(window.translator, "lang"):
                updated_settings = load_settings()
                updated_settings["language"] = window.translator.lang
                save_settings(updated_settings)
                log_info(f"Language updated to '{window.translator.lang}' in settings.")
        except Exception as e:
            log_exception("Error saving updated language setting", e)

    except Exception as e:
        log_exception("An error occurred in main()", e)

if __name__ == "__main__":
    main()
```

### 6.2 Settings 
#### 6.2.1 setting.py

```python
import json
import os
from config.dev import SETTINGS_FILE

def load_settings():
    # Import logging only inside the function to avoid circular import
    try:
        from core.logger import log_info
    except ImportError:
        log_info = lambda msg: None
    try:
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                settings = json.load(f)
                log_info(f"Settings loaded from {SETTINGS_FILE}.")
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
        log_info(f"Saving settings to {SETTINGS_FILE}.")
        log_info(f"JSON preview:\n{json_str}")
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
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
SETTINGS_FILE    = CONFIG_DIR / "user_settings.json"
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
    def __init__(self, lang="en"):
        log_section("translator.py")
        log_subsection("__init__")
        self.lang = lang
        self.translations = {}
        self._load_translations()

    def _load_translations(self):
        log_subsection("_load_translations")
        try:
            path = TRANSLATIONS_DIR / "translations.json"
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for entry in data:
                if entry.get("ID") == self.lang:
                    self.translations = entry
                    break
            log_info(f"Translations loaded for language '{self.lang}'.")
        except Exception as e:
            log_exception("Error loading translations", e)
            self.translations = {}

    def set_language(self, lang_code):
        log_subsection("set_language")
        self.lang = lang_code
        self._load_translations()

    def tr(self, key):
        log_subsection("tr")
        return self.translations.get(key, key)

    def form_label(self, key):
        log_subsection("form_label")
        # Falls form_labels-Bereich existiert, sonst fallback auf Hauptbereich
        labels = self.translations.get("form_labels", {})
        if labels and key in labels:
            return labels[key]
        return self.translations.get(key, key)

    def help_text(self, key):
        log_subsection("help_text")
        # Falls help_texts-Bereich existiert, sonst fallback auf Hauptbereich
        helps = self.translations.get("help_texts", {})
        if helps and key in helps:
            return helps[key]
        return self.translations.get(key, key)
```

### 6.5 GUI
Module für das GUI.

#### 6.5.1 Styles

##### 6.5.1.1 base_style.py

```python
# Central default parameters for stylesheets
DEFAULTS = {
    "border_radius": 8,
    "font_size": 14,
    "input_width": 400,
}

# Central CSS templates for all GUI components
CSS_TEMPLATES = {
    "button": """
        QPushButton, QToolButton {{
            background-color: {button_bg};
            color: {button_fg};
            font-size: {font_size}px;
            border: 2px solid {border};
            border-radius: {border_radius}px;
        }}
        QPushButton:hover, QToolButton:hover {{
            background-color: {button_hover};
        }}
        QPushButton:pressed, QToolButton:pressed {{
            background-color: {button_active};
        }}
        QPushButton:disabled, QToolButton:disabled {{
            background-color: {border};
            color: {input_fg};
        }}
    """,

    "active_button": """
        QPushButton {{
            background-color: {highlight};
            color: {button_fg};
            font-size: {font_size}px;
            border: 2px solid {border};
            border-radius: {border_radius}px;
            font-weight: bold;
        }}
    """,

    "input": """
        QLineEdit, QTextEdit, QPlainTextEdit, QComboBox, QSpinBox, QDateEdit {{
            background-color: {input_bg};
            color: {input_fg};
            border: 1px solid {border};
            border-radius: 4px;
            font-size: {font_size}px;
            padding: 6px;
            min-width: {input_width}px;
            max-width: {input_width}px;
        }}
    """,

    "tab": """
        QTabWidget::pane {{
            border: 1px solid {border};
        }}
        QTabBar::tab {{
            background: {button_bg};
            color: {button_fg};
            border-radius: {border_radius}px;
            min-width: 120px;
            padding: 8px;
        }}
        QTabBar::tab:selected {{
            background: {highlight};
            color: {button_fg};
        }}
    """,

    "listview": """
        QListView, QTreeView {{
            background-color: {input_bg};
            color: {input_fg};
            border: 1px solid {border};
            selection-background-color: {highlight};
            selection-color: {button_fg};
        }}
    """,

    "label": """
        QLabel, QGroupBox {{
            color: {foreground};
            font-size: {font_size}px;
        }}
    """,

    "tooltip": """
        QToolTip {{
            background-color: {highlight};
            color: {background};
            border: 1px solid {border};
        }}
    """,

    "splitter": """
        QSplitter::handle {{
            background: {border};
            border: 1px solid {highlight};
            width: 8px;
        }}
        QSplitter::handle:hover {{
            background: {highlight};
        }}
    """,

    "panel": """
        QWidget#NavigationPanel, QWidget#HelpPanel, QWidget#CenterPanel {{
            background-color: {background};
            border: 1px solid {border};
            border-radius: {border_radius}px;
        }}
    """,

    "toolbar": """
        QToolBar {{
            background: {background};
            border-bottom: 1px solid {border};
            min-height: 44px;
            padding-top: 6px;
            padding-bottom: 6px;
        }}
        QToolButton {{
            min-width: 36px;
            min-height: 36px;
            padding: 6px 12px;
            font-size: {font_size}px;
            qproperty-toolButtonStyle: ToolButtonTextBesideIcon;
        }}
        QToolButton:hover {{
            background-color: {button_hover};
        }}
        QToolButton:pressed {{
            background-color: {button_active};
        }}
    """,

    "form": """
        QLineEdit, QDateEdit, QSpinBox {{
            padding: 6px;
            border: 1px solid {border};
            border-radius: 4px;
            background-color: {input_bg};
            color: {input_fg};
            font-size: {font_size}px;
            font-family: 'Segoe UI', sans-serif;
            min-width: {input_width}px;
            max-width: {input_width}px;
        }}
        QLabel {{
            font-size: {font_size}px;
            color: {foreground};
        }}
        QFormLayout {{
            margin: 12px;
        }}
    """,
}

def render_css(template_name, style_dict, defaults=DEFAULTS):
    """
    Renders the requested CSS template with style parameters and defaults.
    """
    params = {**defaults, **style_dict}
    # Map template parameters for compatibility with all style dicts
    params.update({
        "button_bg": style_dict.get("button", {}).get("background", style_dict.get("button_bg", "#e7eaf3")),
        "button_fg": style_dict.get("button", {}).get("foreground", style_dict.get("button_fg", "#1a1a1a")),
        "button_hover": style_dict.get("button", {}).get("hover", style_dict.get("button_hover", "#d0d6e6")),
        "button_active": style_dict.get("button", {}).get("active", style_dict.get("button_active", "#b6c2e1")),
        "input_bg": style_dict.get("input", {}).get("background", style_dict.get("input_bg", "#ffffff")),
        "input_fg": style_dict.get("input", {}).get("foreground", style_dict.get("input_fg", "#1a1a1a")),
    })
    return CSS_TEMPLATES[template_name].format(**params)
```

##### 6.5.1.2 themes_style.py

```python
# Central theme definitions for all styles and modes

THEMES = {
    "oldschool": {
        "light": {
            "background": "#ffffff",
            "foreground": "#222326",
            "button": {
                "background": "#f3f3f3",
                "foreground": "#222326",
                "hover": "#e5e5e5",
                "active": "#d0d0d0"
            },
            "input": {
                "background": "#f9f9f9",
                "foreground": "#222326"
            },
            "border": "#cfcfcf",
            "highlight": "#0078d7",
            "error": "#e81123"
        },
        "middle": {
            "background": "#f3f3f3",
            "foreground": "#222326",
            "button": {
                "background": "#e5e5e5",
                "foreground": "#222326",
                "hover": "#d0d0d0",
                "active": "#bcbcbc"
            },
            "input": {
                "background": "#ededed",
                "foreground": "#222326"
            },
            "border": "#bcbcbc",
            "highlight": "#0078d7",
            "error": "#e81123"
        },
        "dark": {
            "background": "#1e1e1e",
            "foreground": "#f3f3f3",
            "button": {
                "background": "#2d2d2d",
                "foreground": "#f3f3f3",
                "hover": "#3c3c3c",
                "active": "#0078d7"
            },
            "input": {
                "background": "#252526",
                "foreground": "#f3f3f3"
            },
            "border": "#3c3c3c",
            "highlight": "#0078d7",
            "error": "#e81123"
        }
    },
    "vintage": {
        "light": {
            "background": "#f5eee6",
            "foreground": "#5a4632",
            "button": {
                "background": "#e2d3c3",
                "foreground": "#5a4632",
                "hover": "#d6c3a3",
                "active": "#cbb393"
            },
            "input": {
                "background": "#f8f3ed",
                "foreground": "#5a4632"
            },
            "border": "#cbb393",
            "highlight": "#b48a78",
            "error": "#a94442"
        },
        "middle": {
            "background": "#e9e2d3",
            "foreground": "#5a4632",
            "button": {
                "background": "#d6c3a3",
                "foreground": "#5a4632",
                "hover": "#cbb393",
                "active": "#b48a78"
            },
            "input": {
                "background": "#ede6d6",
                "foreground": "#5a4632"
            },
            "border": "#b48a78",
            "highlight": "#a67c52",
            "error": "#a94442"
        },
        "dark": {
            "background": "#3b2c23",
            "foreground": "#e2d3c3",
            "button": {
                "background": "#5a4632",
                "foreground": "#e2d3c3",
                "hover": "#7c624a",
                "active": "#a67c52"
            },
            "input": {
                "background": "#4e3b2a",
                "foreground": "#e2d3c3"
            },
            "border": "#7c624a",
            "highlight": "#b48a78",
            "error": "#a94442"
        }
    },
    "modern": {
        "light": {
            "background": "#f3f6fd",
            "foreground": "#1a1a1a",
            "button": {
                "background": "#e7eaf3",
                "foreground": "#1a1a1a",
                "hover": "#d0d6e6",
                "active": "#b6c2e1"
            },
            "input": {
                "background": "#ffffff",
                "foreground": "#1a1a1a"
            },
            "border": "#cfd8dc",
            "highlight": "#2563eb",
            "error": "#ef4444"
        },
        "middle": {
            "background": "#e0e5ef",
            "foreground": "#23272f",
            "button": {
                "background": "#cfd8dc",
                "foreground": "#23272f",
                "hover": "#b6c2e1",
                "active": "#2563eb"
            },
            "input": {
                "background": "#f3f6fd",
                "foreground": "#23272f"
            },
            "border": "#b6c2e1",
            "highlight": "#2563eb",
            "error": "#ef4444"
        },
        "dark": {
            "background": "#181a20",
            "foreground": "#e7eaf3",
            "button": {
                "background": "#23272f",
                "foreground": "#e7eaf3",
                "hover": "#2563eb",
                "active": "#1e293b"
            },
            "input": {
                "background": "#23272f",
                "foreground": "#e7eaf3"
            },
            "border": "#2563eb",
            "highlight": "#60a5fa",
            "error": "#ef4444"
        }
    },
    "future": {
        "light": {
            "background": "rgba(245, 250, 255, 0.85)",
            "foreground": "#22223b",
            "button": {
                "background": "rgba(230, 240, 255, 0.95)",
                "foreground": "#22223b",
                "hover": "#b8c6db",
                "active": "#7f9acb"
            },
            "input": {
                "background": "rgba(255,255,255,0.95)",
                "foreground": "#22223b"
            },
            "border": "#a3bffa",
            "highlight": "#7f9acb",
            "error": "#ff6b6b"
        },
        "middle": {
            "background": "rgba(210, 220, 235, 0.90)",
            "foreground": "#22223b",
            "button": {
                "background": "#b8c6db",
                "foreground": "#22223b",
                "hover": "#7f9acb",
                "active": "#a3bffa"
            },
            "input": {
                "background": "rgba(240,245,250,0.95)",
                "foreground": "#22223b"
            },
            "border": "#7f9acb",
            "highlight": "#a3bffa",
            "error": "#ff6b6b"
        },
        "dark": {
            "background": "rgba(30, 34, 45, 0.92)",
            "foreground": "#e0eaff",
            "button": {
                "background": "#22223b",
                "foreground": "#e0eaff",
                "hover": "#7f9acb",
                "active": "#a3bffa"
            },
            "input": {
                "background": "rgba(40,44,54,0.95)",
                "foreground": "#e0eaff"
            },
            "border": "#7f9acb",
            "highlight": "#a3bffa",
            "error": "#ff6b6b"
        }
    },

    "minimal": {
        "light": {
            "background": "#ffffff",
            "foreground": "#222222",
            "button": {
                "background": "#f7f7f7",
                "foreground": "#222222",
                "hover": "#e0e0e0",
                "active": "#bdbdbd"
            },
            "input": {
                "background": "#fafafa",
                "foreground": "#222222"
            },
            "border": "#cccccc",
            "highlight": "#1976d2",
            "error": "#d32f2f"
        },
        "middle": {
            "background": "#ededed",
            "foreground": "#222222",
            "button": {
                "background": "#e0e0e0",
                "foreground": "#222222",
                "hover": "#bdbdbd",
                "active": "#1976d2"
            },
            "input": {
                "background": "#f5f5f5",
                "foreground": "#222222"
            },
            "border": "#bdbdbd",
            "highlight": "#1976d2",
            "error": "#d32f2f"
        },
        "dark": {
            "background": "#222222",
            "foreground": "#f7f7f7",
            "button": {
                "background": "#333333",
                "foreground": "#f7f7f7",
                "hover": "#1976d2",
                "active": "#424242"
            },
            "input": {
                "background": "#2c2c2c",
                "foreground": "#f7f7f7"
            },
            "border": "#424242",
            "highlight": "#1976d2",
            "error": "#d32f2f"
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

def get_current_style():
    """
    Loads the current style and mode from settings and returns the theme dictionary.
    Falls back to 'modern' and 'light' if not found.
    """
    settings = load_settings()
    style_code = settings.get("style", "modern")
    mode_code = settings.get("mode", "light")
    return get_theme(style_code, mode_code)
```

##### 6.5.1.4 form_styles.py

```python
from config.settings import load_settings
from gui.styles.base_style import render_css, DEFAULTS
from gui.styles.registry_style import get_current_style
from core.logger import log_section, log_subsection, log_info, log_exception

def load_global_stylesheet(font_size=14):
    """
    Loads the global stylesheet for the application using the current style and mode.
    """
    log_section("form_styles.py")
    log_subsection("load_global_stylesheet")
    try:
        style = get_current_style()
        style["font_size"] = font_size
        style["border_radius"] = DEFAULTS["border_radius"]
        style["input_width"] = DEFAULTS["input_width"]

        # Combine all relevant templates
        button_css = render_css("button", style)
        input_css = render_css("input", style)
        tab_css = render_css("tab", style)
        listview_css = render_css("listview", style)
        label_css = render_css("label", style)
        tooltip_css = render_css("tooltip", style)
        splitter_css = render_css("splitter", style)
        panel_css = render_css("panel", style)
        toolbar_css = render_css("toolbar", style)
        form_css = render_css("form", style)

        # Concatenate all CSS parts
        stylesheet = (
            button_css +
            input_css +
            tab_css +
            listview_css +
            label_css +
            tooltip_css +
            splitter_css +
            panel_css +
            toolbar_css +
            form_css
        )
        log_info("Global stylesheet loaded.")
        return stylesheet
    except Exception as e:
        log_exception("Error loading global stylesheet", e)
        return ""

def load_button_style(font_size=14):
    """
    Loads the stylesheet for buttons and toolbars.
    """
    log_section("form_styles.py")
    log_subsection("load_button_style")
    try:
        style = get_current_style()
        style["font_size"] = font_size
        style["border_radius"] = DEFAULTS["border_radius"]
        return render_css("button", style) + render_css("toolbar", style)
    except Exception as e:
        log_exception("Error loading button stylesheet", e)
        return ""

def load_active_button_style(font_size=16):
    """
    Loads the stylesheet for active buttons.
    """
    log_section("form_styles.py")
    log_subsection("load_active_button_style")
    try:
        style = get_current_style()
        style["font_size"] = font_size
        style["border_radius"] = DEFAULTS["border_radius"]
        return render_css("active_button", style)
    except Exception as e:
        log_exception("Error loading active button stylesheet", e)
        return ""

def load_form_style(input_font_size=14, label_font_size=14, input_width=400):
    """
    Loads the stylesheet for forms and input fields.
    """
    log_section("form_styles.py")
    log_subsection("load_form_style")
    try:
        style = get_current_style()
        style["font_size"] = input_font_size
        style["border_radius"] = DEFAULTS["border_radius"]
        style["input_width"] = input_width
        return render_css("form", style)
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
    def __init__(self, keys, translator, parent=None, callbacks=None):
        log_section("navigation_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.setObjectName("NavigationPanel")  # For stylesheet targeting
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
            # Reset all buttons to default style
            button_style = load_button_style()
            button_style_active = load_active_button_style()
            for k, btn in self.buttons.items():
                btn.setStyleSheet(button_style)
            # Set active button style
            self.buttons[key].setStyleSheet(button_style_active)
            self.active_key = key
            # Call the assigned callback
            if key in self.callbacks:
                self.callbacks[key]()
            log_info(f"Navigation button '{key}' clicked.")
        except Exception as e:
            log_exception(f"Error in navigation click handler for '{key}'", e)
```

##### 6.5.2.2 help_panel.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from gui.styles.form_styles import load_global_stylesheet
from core.logger import log_section, log_subsection, log_info, log_exception

class HelpPanel(QWidget):
    def __init__(self, help_text="", parent=None):
        log_section("help_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.setObjectName("HelpPanel")
            self.setStyleSheet(load_global_stylesheet())
            self.layout = QVBoxLayout()
            # Sicherstellen, dass help_text ein String ist
            self.help_label = QLabel(str(help_text), self)
            self.help_label.setWordWrap(True)
            self.layout.addWidget(self.help_label)
            self.setLayout(self.layout)
            log_info("HelpPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing HelpPanel", e)

    def set_help_text(self, text):
        log_subsection("set_help_text")
        try:
            # Sicherstellen, dass text ein String ist
            self.help_label.setText(str(text))
            log_info("HelpPanel help text updated.")
        except Exception as e:
            log_exception("Error updating help text in HelpPanel", e)
```

##### 6.5.2.3 center_panel.py

```python
from PySide6.QtWidgets import QWidget, QSplitter, QHBoxLayout
from gui.widgets.navigation_panel import NavigationPanel
from gui.styles.form_styles import load_global_stylesheet
from core.logger import log_section, log_subsection, log_info, log_exception

class CenterPanel(QWidget):
    def __init__(self, navigation_panel, content_widget, help_panel, parent=None):
        log_section("center_panel.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.setObjectName("CenterPanel")
            self.setStyleSheet(load_global_stylesheet())

            self.splitter = QSplitter(self)
            self.splitter.addWidget(navigation_panel)
            self.splitter.addWidget(content_widget)
            self.splitter.addWidget(help_panel)
            self.splitter.setSizes([200, 800, 200])  # Adjust as needed

            layout = QHBoxLayout(self)
            layout.addWidget(self.splitter)
            self.setLayout(layout)
            log_info("CenterPanel initialized successfully.")
        except Exception as e:
            log_exception("Error initializing CenterPanel", e)
```

#### 6.5.3 Widgets

##### 6.5.3.1 form_toolbar.py

```python
from PySide6.QtWidgets import QWidget, QToolBar, QHBoxLayout, QWidget
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize
from core.logger import log_section, log_subsection, log_info, log_exception
from gui.styles.form_styles import load_button_style

class FormToolbar(QWidget):
    def __init__(self, translator, form_prefix, parent=None):
        log_section("form_toolbar.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.toolbar = QToolBar(self)
            self.toolbar.setStyleSheet(load_button_style())
            self.toolbar.setIconSize(QSize(32, 32))

            # Spacer for left margin
            left_spacer = QWidget()
            left_spacer.setFixedWidth(10)
            self.toolbar.addWidget(left_spacer)

            self.translator = translator

            # Create actions with translated labels
            self.new_action = QAction(self.translator.form_label(f"{form_prefix}_btn_new"), self)
            self.delete_action = QAction(self.translator.form_label(f"{form_prefix}_btn_delete"), self)
            self.prev_action = QAction(self.translator.form_label(f"{form_prefix}_btn_preview"), self)
            self.next_action = QAction(self.translator.form_label(f"{form_prefix}_btn_next"), self)
            self.save_action = QAction(self.translator.form_label(f"{form_prefix}_btn_save"), self)

            # Optionally set icons if available
            # self.new_action.setIcon(QIcon("icons/new.png"))
            # self.delete_action.setIcon(QIcon("icons/delete.png"))
            # self.prev_action.setIcon(QIcon("icons/prev.png"))
            # self.next_action.setIcon(QIcon("icons/next.png"))
            # self.save_action.setIcon(QIcon("icons/save.png"))

            # Add actions and spacing between buttons
            actions = [
                self.new_action,
                self.delete_action,
                self.prev_action,
                self.next_action,
                self.save_action
            ]
            for i, action in enumerate(actions):
                self.toolbar.addAction(action)
                if i < len(actions) - 1:
                    spacer = QWidget()
                    spacer.setFixedWidth(8)  # Space between buttons
                    self.toolbar.addWidget(spacer)

            layout = QHBoxLayout(self)
            layout.addWidget(self.toolbar)
            self.setLayout(layout)
            log_info("FormToolbar initialized successfully.")
        except Exception as e:
            log_exception("Error initializing FormToolbar", e)
```

##### 6.5.3.2 base_form_widget.py

```python
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFormLayout,
    QLineEdit, QSpinBox, QDateEdit, QComboBox
)
from gui.widgets.form_toolbar import FormToolbar
from gui.styles.form_styles import load_form_style
from core.logger import log_section, log_subsection, log_info, log_exception

class BaseFormWidget(QWidget):
    def __init__(self, title, fields, toolbar_actions, form_prefix, translator, parent=None):
        log_section("base_form_widget.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator
            self.setStyleSheet(load_form_style())

            # Hauptlayout
            main_layout = QVBoxLayout()

            # Toolbar linksbündig über die gesamte Breite
            self.toolbar = FormToolbar(self.translator, form_prefix, self)
            if toolbar_actions:
                toolbar_actions(self.toolbar)
            main_layout.addWidget(self.toolbar)
            main_layout.addSpacing(12)

            # Formularfelder
            self.form_layout = QFormLayout()
            self.inputs = {}

            for field in fields:
                if field.get("type") == "header":
                    # Überschrift erzeugen (großes, fettes Label)
                    header_text = self.translator.tr(field["label_key"])
                    header_label = QLabel(header_text if header_text else field.get("default_label", ""), self)
                    header_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 12px;")
                    self.form_layout.addRow(header_label)
                    continue  # Keine Eingabe für Header-Felder

                label_text = self.translator.tr(field["label_key"])
                label = QLabel(label_text if label_text else field.get("default_label", ""), self)
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
                    for option in field.get("options", []):
                        input_widget.addItem(str(option))
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
```

##### 6.5.3.3 form_chapters.py

```python
import json
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error
from config.dev import FORM_FIELDS_FILE

class ChaptersForm(QWidget):
    """
    Form widget for chapter data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_chapters.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            # Felder zentral aus JSON laden (nur einmal!)
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                all_fields = json.load(f)
            fields = all_fields.get("chapters", [])

            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)

            self.form = BaseFormWidget(
                title=self.translator.tr("chapter"),
                fields=fields,
                toolbar_actions=toolbar_actions,
                form_prefix="chapter",
                translator=self.translator,
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("ChaptersForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing ChaptersForm: {str(e)}")

    def _on_save(self):
        log_subsection("_on_save")
        log_info("ChaptersForm save triggered.")
```

##### 6.5.3.4 form_characters.py

```python
import json
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error
from config.dev import FORM_FIELDS_FILE

class CharactersForm(QWidget):
    """
    Form widget for character data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_characters.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            # Felder zentral aus JSON laden
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                all_fields = json.load(f)
            fields = all_fields.get("characters", [])

            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)

            self.form = BaseFormWidget(
                title=self.translator.tr("char"),
                fields=fields,
                toolbar_actions=toolbar_actions,
                form_prefix="char",
                translator=self.translator,
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("CharactersForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing CharactersForm: {str(e)}")

    def _on_save(self):
        log_subsection("_on_save")
        log_info("CharactersForm save triggered.")
```

##### 6.5.3.5 form_locations.py

```python
import json
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error
from config.dev import FORM_FIELDS_FILE

class LocationsForm(QWidget):
    """
    Form widget for location data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_locations.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            # Felder zentral aus JSON laden
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                all_fields = json.load(f)
            fields = all_fields.get("locations", [])

            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)

            self.form = BaseFormWidget(
                title=self.translator.tr("location"),
                fields=fields,
                toolbar_actions=toolbar_actions,
                form_prefix="location",
                translator=self.translator,
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("LocationsForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing LocationsForm: {str(e)}")

    def _on_save(self):
        log_subsection("_on_save")
        log_info("LocationsForm save triggered.")
```

##### 6.5.3.6 form_objects.py

```python
import json
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_error
from config.dev import FORM_FIELDS_FILE

class ObjectsForm(QWidget):
    """
    Form widget for object data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_objects.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            # Felder zentral aus JSON laden
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                all_fields = json.load(f)
            fields = all_fields.get("objects", [])

            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)

            self.form = BaseFormWidget(
                title=self.translator.tr("object"),
                fields=fields,
                toolbar_actions=toolbar_actions,
                form_prefix="object",
                translator=self.translator,
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("ObjectsForm initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing ObjectsForm: {str(e)}")

    def _on_save(self):
        log_subsection("_on_save")
        log_info("ObjectsForm save triggered.")
```

##### 6.5.3.7 form_projects.py

```python
import json
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import FORM_FIELDS_FILE

class ProjectForm(QWidget):
    """
    Form widget for project data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_projects.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            # Felder zentral aus JSON laden
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                all_fields = json.load(f)
            fields = all_fields.get("projects", [])

            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)

            self.form = BaseFormWidget(
                title=self.translator.tr("pro"),
                fields=fields,
                toolbar_actions=toolbar_actions,
                form_prefix="pro",
                translator=self.translator,
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("ProjectForm initialized successfully.")
        except Exception as e:
            log_exception("Error initializing ProjectForm", e)

    def _on_save(self):
        log_subsection("_on_save")
        try:
            title = self.form.inputs.get("title", None)
            if title and hasattr(title, "text") and not title.text():
                log_info("Validation failed: title is empty.")
                return
            # ...save logic...
            log_info("ProjectForm save triggered.")
        except Exception as e:
            log_exception("Error during ProjectForm save", e)
```

##### 6.5.3.8 form_scenes.py

```python
import json
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import FORM_FIELDS_FILE

class ScenesForm(QWidget):
    """
    Form widget for scene data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_scenes.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            # Felder zentral aus JSON laden
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                all_fields = json.load(f)
            fields = all_fields.get("scenes", [])

            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)

            self.form = BaseFormWidget(
                title=self.translator.tr("scene"),
                fields=fields,
                toolbar_actions=toolbar_actions,
                form_prefix="scene",
                translator=self.translator,
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("ScenesForm initialized successfully.")
        except Exception as e:
            log_exception("Error initializing ScenesForm", e)

    def _on_save(self):
        log_subsection("_on_save")
        log_info("ScenesForm save triggered.")
```

##### 6.5.3.9 form_storylines.py

```python
import json
from PySide6.QtWidgets import QWidget, QVBoxLayout
from gui.widgets.base_form_widget import BaseFormWidget
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import FORM_FIELDS_FILE

class StorylinesForm(QWidget):
    """
    Form widget for storyline data entry.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_storylines.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            # Felder zentral aus JSON laden
            with open(FORM_FIELDS_FILE, "r", encoding="utf-8") as f:
                all_fields = json.load(f)
            fields = all_fields.get("storylines", [])

            def toolbar_actions(toolbar):
                toolbar.save_action.triggered.connect(self._on_save)

            self.form = BaseFormWidget(
                title=self.translator.tr("storyline"),
                fields=fields,
                toolbar_actions=toolbar_actions,
                form_prefix="storyline",
                translator=self.translator,
                parent=self
            )
            layout = QVBoxLayout(self)
            layout.addWidget(self.form)
            self.setLayout(layout)
            log_info("StorylinesForm initialized successfully.")
        except Exception as e:
            log_exception("Error initializing StorylinesForm", e)

    def _on_save(self):
        log_subsection("_on_save")
        log_info("StorylinesForm save triggered.")
```

##### 6.5.3.10 form_start.py
```python
from PySide6.QtWidgets import QWidget, QVBoxLayout
from core.translator import Translator
from core.logger import log_section, log_subsection, log_info, log_exception

class StartForm(QWidget):
    """
    Completely empty form widget for the start window.
    """
    def __init__(self, translator: Translator, parent=None):
        log_section("form_start.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            # Empty layout
            layout = QVBoxLayout()
            self.setLayout(layout)

            log_info("StartForm initialized successfully.")
        except Exception as e:
            log_exception("Error initializing StartForm", e)
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
from gui.styles.form_styles import load_button_style, load_global_stylesheet
import sys

from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import BG_IMAGE_PATH

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
            self.translator = Translator(default_language)
            self.setWindowTitle(self.translator.tr("win_start_title"))
            self.resize(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)
            self.setAutoFillBackground(False)
            self.bg_pixmap = QPixmap(str(BG_IMAGE_PATH))
            self.pref_window = None
            self._create_ui()
            self._retranslate_and_position()
            # Korrektur: Hilfetext als String holen und an HelpPanel übergeben
            help_text = self.translator.help_text("help_new_project")
            self.help_panel = HelpPanel(help_text, self)
            log_info("StartWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing StartWindow", e)

    def _create_ui(self):
        log_subsection("_create_ui")
        try:
            self.button_keys = [
                "start_btn_new_project",
                "start_btn_load_project",
                "start_btn_settings",
                "start_btn_help",
                "start_btn_exit"
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
            self._retranslate_and_position()
            log_info(f"Language changed to {code}.")
        except Exception as e:
            log_exception("Error changing language", e)

    def _retranslate_and_position(self):
        log_subsection("_retranslate_and_position")
        try:
            for key, btn in zip(self.button_keys, self.buttons):
                btn.setText(self.translator.tr(key))
            self.setWindowTitle(self.translator.tr("win_start_title"))
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
        app.setStyleSheet(load_global_stylesheet())
        window = StartWindow(default_language="en")
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
    QHBoxLayout, QVBoxLayout
)
from core.translator import Translator
from config.settings import load_settings, save_settings
from gui.styles.themes_style import THEMES, get_theme
from gui.styles.form_styles import load_button_style, load_global_stylesheet
from core.logger import log_section, log_subsection, log_info, log_exception

class PreferencesWindow(QDialog):
    DEFAULT_WIDTH  = 800
    DEFAULT_HEIGHT = 600

    LANGUAGE_NAMES = {
        "de": "Deutsch",
        "en": "English",
        "fr": "Français",
        "es": "Español"
    }

    STYLE_NAMES = {
        "oldschool": "Old-School",
        "vintage": "Vintage",
        "modern": "Modern",
        "future": "Future",
        "minimal": "Minimal"
    }

    MODE_NAMES = {
        "light": "Light",
        "middle": "Middle",
        "dark": "Dark"
    }

    def __init__(self, parent=None):
        log_section("preferences.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = parent.translator
            self.settings   = load_settings()
            self.original_language = self.translator.lang

            self.setWindowTitle(self.translator.tr("win_preference_title"))
            self.resize(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)
            self.setStyleSheet(load_global_stylesheet())
            self._init_ui()
            self._load_values()
            log_info("PreferencesWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing PreferencesWindow", e)

    def _init_ui(self):
        log_subsection("_init_ui")
        try:
            # Language selection
            self.lang_label = QLabel(self.translator.tr("win_preference_title"), self)
            self.lang_combo = QComboBox(self)
            for code, name in self.LANGUAGE_NAMES.items():
                self.lang_combo.addItem(name, userData=code)
            self.lang_combo.currentIndexChanged.connect(self._on_language_changed)

            # Style selection
            self.style_label = QLabel("Style", self)
            self.style_combo = QComboBox(self)
            for code, name in self.STYLE_NAMES.items():
                self.style_combo.addItem(name, userData=code)
            self.style_combo.currentIndexChanged.connect(self._on_style_or_mode_changed)

            # Mode selection
            self.mode_label = QLabel("Modus", self)
            self.mode_combo = QComboBox(self)
            for code, name in self.MODE_NAMES.items():
                self.mode_combo.addItem(name, userData=code)
            self.mode_combo.currentIndexChanged.connect(self._on_style_or_mode_changed)

            # Buttons
            self.ok_button     = QPushButton(self)
            self.cancel_button = QPushButton(self)
            self.ok_button.clicked.connect(self._on_ok)
            self.cancel_button.clicked.connect(self._on_cancel)

            btn_layout = QHBoxLayout()
            btn_layout.addStretch()
            btn_layout.addWidget(self.ok_button)
            btn_layout.addWidget(self.cancel_button)

            main_layout = QVBoxLayout(self)
            main_layout.addWidget(self.lang_label)
            main_layout.addWidget(self.lang_combo)
            main_layout.addWidget(self.style_label)
            main_layout.addWidget(self.style_combo)
            main_layout.addWidget(self.mode_label)
            main_layout.addWidget(self.mode_combo)
            main_layout.addLayout(btn_layout)
            self.setLayout(main_layout)
            log_info("UI initialized successfully.")
        except Exception as e:
            log_exception("Error initializing UI", e)

    def _load_values(self):
        log_subsection("_load_values")
        try:
            # Language
            lang = self.settings.get("language", "en")
            idx  = list(self.LANGUAGE_NAMES.keys()).index(lang) if lang in self.LANGUAGE_NAMES else 0
            self.lang_combo.setCurrentIndex(idx)
            # Style
            style = self.settings.get("style", "modern")
            idx = list(self.STYLE_NAMES.keys()).index(style) if style in self.STYLE_NAMES else 2
            self.style_combo.setCurrentIndex(idx)
            # Mode
            mode = self.settings.get("mode", "light")
            idx = list(self.MODE_NAMES.keys()).index(mode) if mode in self.MODE_NAMES else 0
            self.mode_combo.setCurrentIndex(idx)
            self._update_ui_texts()
            self._update_preview()
            log_info("Values loaded and UI texts updated.")
        except Exception as e:
            log_exception("Error loading values", e)

    def _on_language_changed(self):
        log_subsection("_on_language_changed")
        try:
            index = self.lang_combo.currentIndex()
            code = self.lang_combo.itemData(index)
            self.translator.set_language(code)
            self._update_ui_texts()
            log_info(f"Language changed to {code}.")
        except Exception as e:
            log_exception("Error changing language", e)

    def _on_style_or_mode_changed(self):
        log_subsection("_on_style_or_mode_changed")
        self._update_preview()

    def _update_ui_texts(self):
        log_subsection("_update_ui_texts")
        try:
            self.setWindowTitle(self.translator.tr("menu_settings"))
            self.lang_label.setText(self.translator.tr("menu_language"))
            self.style_label.setText("Style")
            self.mode_label.setText("Modus")
            self.ok_button.setText(self.translator.tr("preference_action_save"))
            self.cancel_button.setText(self.translator.tr("preference_action_cancel"))
            log_info("UI texts updated.")
        except Exception as e:
            log_exception("Error updating UI texts", e)

    def _update_preview(self):
        style_code = self.style_combo.itemData(self.style_combo.currentIndex())
        mode_code = self.mode_combo.itemData(self.mode_combo.currentIndex())
        style_dict = get_theme(style_code, mode_code)
        # Wende das Stylesheet auf das gesamte Fenster an
        self.setStyleSheet(load_global_stylesheet())

    def _on_ok(self):
        log_subsection("_on_ok")
        try:
            self.settings["language"] = self.lang_combo.itemData(self.lang_combo.currentIndex())
            self.settings["style"]    = self.style_combo.itemData(self.style_combo.currentIndex())
            self.settings["mode"]     = self.mode_combo.itemData(self.mode_combo.currentIndex())
            save_settings(self.settings)
            if self.parent() and hasattr(self.parent(), "_on_language_changed"):
                self.parent()._on_language_changed(self.settings["language"])
            self.accept()
            log_info("Settings saved and dialog accepted.")
        except Exception as e:
            log_exception("Error saving settings", e)

    def _on_cancel(self):
        log_subsection("_on_cancel")
        try:
            self.translator.set_language(self.original_language)
            if self.parent() and hasattr(self.parent(), "_on_language_changed"):
                self.parent()._on_language_changed(self.original_language)
            self.reject()
            log_info("Dialog canceled and language reverted.")
        except Exception as e:
            log_exception("Error canceling PreferencesWindow", e)
```

##### 6.5.4.3 project_window.py

```python
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSplitter, QHBoxLayout

from gui.styles.form_styles import load_button_style, load_active_button_style, load_global_stylesheet
from core.translator import Translator
from config.settings import load_settings, save_settings
from gui.widgets.navigation_panel import NavigationPanel
from gui.widgets.help_panel import HelpPanel

# Import modular forms
from gui.widgets.form_projects import ProjectForm
from gui.widgets.form_characters import CharactersForm
from gui.widgets.form_storylines import StorylinesForm
from gui.widgets.form_chapters import ChaptersForm
from gui.widgets.form_scenes import ScenesForm
from gui.widgets.form_objects import ObjectsForm
from gui.widgets.form_locations import LocationsForm
from gui.widgets.form_start import StartForm

# Import central logging functions
from core.logger import log_section, log_subsection, log_info, log_error, log_exception

class ProjectWindow(QWidget):
    BUTTON_WIDTH = 240
    BUTTON_HEIGHT = 70

    def __init__(self, translator=None, parent=None, start_window=None):
        log_section("project_window.py")
        log_subsection("__init__")
        try:
            self.translator = translator or Translator(lang="en")
            super().__init__(parent)
            self.resize(1600, 900)
            self.setWindowTitle(self.translator.tr("pro"))
            self.settings = load_settings()
            self.button_style = load_button_style(18)
            self.button_style_active = load_active_button_style(18)
            self.active_nav_key = None
            self.start_window = start_window

            # Initialisiere splitter direkt am Anfang!
            self.splitter = QSplitter(Qt.Horizontal)
            self.splitter.setObjectName("MainSplitter")   # For splitter styling

            self._set_background()
            self._init_ui()
            log_info("ProjectWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing ProjectWindow", e)

    def _set_background(self):
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
        log_subsection("_init_ui")
        try:
            keys = [
                "pro_btn_project", "pro_btn_characters", "pro_btn_storylines",
                "pro_btn_chapters", "pro_btn_scenes", "pro_btn_objects", "pro_btn_locations", "pro_btn_exit"
            ]
            callbacks = {
                "pro_btn_project": lambda: self._on_nav_clicked("pro_btn_project", self._show_project_form),
                "pro_btn_characters": lambda: self._on_nav_clicked("pro_btn_characters", self._show_characters_form),
                "pro_btn_storylines": lambda: self._on_nav_clicked("pro_btn_storylines", self._show_storylines_form),
                "pro_btn_chapters": lambda: self._on_nav_clicked("pro_btn_chapters", self._show_chapters_form),
                "pro_btn_scenes": lambda: self._on_nav_clicked("pro_btn_scenes", self._show_scenes_form),
                "pro_btn_objects": lambda: self._on_nav_clicked("pro_btn_objects", self._show_objects_form),
                "pro_btn_locations": lambda: self._on_nav_clicked("pro_btn_locations", self._show_locations_form),
                "pro_btn_exit": self._exit_application
            }
            # Korrigierter Aufruf: Nur die erlaubten Parameter übergeben!
            self.navigation_panel = NavigationPanel(
                keys, self.translator, self, callbacks
            )

            help_text = self.translator.help_text("help_new_project")
            self.help_panel = HelpPanel(help_text, self)
            # Start with project form
            self.form_widget = StartForm(self.translator, self)

            self.splitter.addWidget(self.navigation_panel)
            self.splitter.addWidget(self.form_widget)
            self.splitter.addWidget(self.help_panel)
            self.splitter.setSizes(self.settings.get("splitter_sizes", [300, 900, 300]))

            layout = QHBoxLayout(self)
            layout.addWidget(self.splitter)
            self.setLayout(layout)
            log_info("UI initialized successfully.")
        except Exception as e:
            log_exception("Error initializing UI", e)
    def _on_nav_clicked(self, key, handler):
        log_subsection(f"_on_nav_clicked: {key}")
        try:
            self.active_nav_key = key
            handler()
            log_info(f"Navigation button '{key}' clicked.")
        except Exception as e:
            log_exception(f"Error in navigation click handler for '{key}'", e)

    def _show_project_form(self):
        log_subsection("_show_project_form")
        try:
            form_widget = ProjectForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_project")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Project form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying project form", e)

    def _show_characters_form(self):
        log_subsection("_show_characters_form")
        try:
            form_widget = CharactersForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_chars")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Characters form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying characters form", e)

    def _show_storylines_form(self):
        log_subsection("_show_storylines_form")
        try:
            form_widget = StorylinesForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_storylines")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Storylines form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying storylines form", e)

    def _show_chapters_form(self):
        log_subsection("_show_chapters_form")
        try:
            form_widget = ChaptersForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_chapters")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Chapters form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying chapters form", e)

    def _show_scenes_form(self):
        log_subsection("_show_scenes_form")
        try:
            form_widget = ScenesForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_scenes")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Scenes form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying scenes form", e)

    def _show_objects_form(self):
        log_subsection("_show_objects_form")
        try:
            form_widget = ObjectsForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_objects")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Objects form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying objects form", e)

    def _show_locations_form(self):
        log_subsection("_show_locations_form")
        try:
            form_widget = LocationsForm(self.translator, self)
            self._replace_form_widget(form_widget)
            help_text = self.translator.help_text("help_locations")
            self.help_panel.set_help_text(help_text)
            self.splitter.setSizes([300, 900, 300])
            log_info("Locations form displayed successfully.")
        except Exception as e:
            log_exception("Error displaying locations form", e)

    def _replace_form_widget(self, new_widget):
        """
        Replace the current form widget in the splitter.
        """
        old_widget = self.splitter.widget(1)
        if old_widget:
            old_widget.setParent(None)
        self.splitter.insertWidget(1, new_widget)

    def _exit_application(self):
        log_subsection("_exit_application")
        try:
            if self.start_window:
                self.start_window.show()
            self.close()
            log_info("Application exit triggered, StartWindow shown.")
        except Exception as e:
            log_exception("Error during application exit", e)

    def closeEvent(self, event):
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
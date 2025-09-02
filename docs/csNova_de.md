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
    "Chapter": "Kapitel",
    "ChapterBtnDelete": "Löschen",
    "ChapterBtnNew": "Neu",
    "ChapterBtnNext": "Weiter",
    "ChapterBtnPreview": "Zurück",
    "ChapterBtnSave": "Speichern",
    "ChapterNumber": "Nummer",
    "ChapterSummary": "Zusammenfassung",
    "ChapterCharacters": "Charaktere",
    "ChapterLocations": "Orte",
    "ChapterNotes": "Notizen",
    "ChapterObjects": "Objekte",
    "ChapterPremise": "Prämisse",
    "ChapterScenes": "Szenen",
    "ChapterTitle": "Titel",
    "Char": "Charaktere",
    "CharApp": "Aussehen",
    "CharAppBodyType": "Körpertyp",
    "CharAppCharisma": "Ausstrahlung",
    "CharAppEyeColor": "Augenfarbe",
    "CharAppEyeShape": "Augenform",
    "CharAppFaceShape": "Gesichtsform",
    "CharAppHair": "Haare",
    "CharAppHairColor": "Haarfarbe",
    "CharAppHeight": "Größe",
    "CharAppNotes": "Notizen",
    "CharAppPosture": "Statur",
    "CharAppSkin": "Haut",
    "CharAppSpecials": "Besonderheiten",
    "CharApp2": "Aussehen Details",
    "CharApp2Arms": "Arme",
    "CharApp2Buttocks": "Gesäß",
    "CharApp2Chest": "Brust",
    "CharApp2Feet": "Füße",
    "CharApp2Finger": "Finger",
    "CharApp2Hands": "Hände",
    "CharApp2Head": "Kopf",
    "CharApp2HipWaist": "Hüfte, Taille",
    "CharApp2Legs": "Beine",
    "CharApp2Notes": "Notizen",
    "CharApp2Shoulder": "Schultern",
    "CharApp2Toes": "Zehen",
    "CharBas": "Grunddaten",
    "CharBasAge": "Alter",
    "CharBasBorn": "Geburtsdatum",
    "CharBasFirstname": "Vorname",
    "CharBasGender": "Geschlecht",
    "CharBasGroup": "Gruppe",
    "CharBasName": "Name",
    "CharBasNickname": "Spitzname",
    "CharBasNotes": "Notizen",
    "CharBasRole": "Rolle",
    "CharBasSexOrientation": "Sexuelle Orientierung",
    "CharBasStatus": "Status",
    "CharBtn": "Schaltflächen",
    "CharBtnDelete": "Löschen",
    "CharBtnNew": "Neu",
    "CharBtnNext": "Weiter",
    "CharBtnPreview": "Zurück",
    "CharBtnSave": "Speichern",
    "CharEdu": "Ausbildung",
    "CharEduArtMusic": "Kunst/Musik",
    "CharEduAutodidactic": "Autodidaktisch",
    "CharEduJob": "Beruf",
    "CharEduJobEducation": "Berufsausbildung",
    "CharEduNotes": "Notizen",
    "CharEduSchool": "Schule",
    "CharEduSport": "Sport",
    "CharEduTechnologie": "Technik",
    "CharEduUniversity": "Universität",
    "CharGroups": "Gruppen",
    "CharGroupsDes": "Beschreibung",
    "CharGroupsTitle": "Bezeichnung",
    "CharOrigin": "Herkunft",
    "CharOriginBirthplace": "Geburtsort",
    "CharOriginFather": "Vater",
    "CharOriginMother": "Mutter",
    "CharOriginNotes": "Notizen",
    "CharOriginReferencePerson": "Bezugsperson",
    "CharOriginSiblings": "Geschwister",
    "CharPerson": "Persönlichkeit",
    "CharPersonBehavior": "Verhalten",
    "CharPersonBeliefs": "Glaubensgrundsatz",
    "CharPersonFears": "Ängste",
    "CharPersonLifeGoals": "Lebensziel",
    "CharPersonMotivation": "Motivation",
    "CharPersonNeg": "Negative Charaktereigenschaft",
    "CharPersonNotes": "Notizen",
    "CharPersonPos": "Positive Charaktereigenschaft",
    "CharPersonStrengths": "Stärken",
    "CharPersonTalente": "Talente",
    "CharPersonWeakness": "Schwächen",
    "CharPsy": "Psychologie Profil",
    "CharPsyAggression": "Aggressivität",
    "CharPsyDiagnostics": "Diagnose",
    "CharPsyFormative": "Prägung",
    "CharPsyHumor": "Humor",
    "CharPsyMedication": "Medikamente",
    "CharPsyMoral": "Moral",
    "CharPsyNorms": "Normen",
    "CharPsyNotes": "Notizen",
    "CharPsySelfimage": "Selbstbild",
    "CharPsySocialization": "Sozialisation",
    "CharPsySymptoms": "Symptome",
    "CharPsyTaboos": "Tabus",
    "CharPsyTemperament": "Temperament",
    "CharPsyTherapy": "Therapie",
    "CharPsyTrauma": "Trauma",
    "CharPsyValues": "Werte",
    "Help": "Hilfe",
    "HelpNewProject": "Wählen Sie eine der Datenbanken, die Sie bearbeiten wollen.",
    "HelpChapters": "Organisieren Sie Ihre Geschichte in Kapitel und beschreiben Sie deren Inhalt.",
    "HelpChars": "Definieren Sie Ihre Charaktere: Namen, Rollen, Eigenschaften und Beziehungen.",
    "HelpEditorWindow": "Editor Fenster",
    "HelpHelpWindow": "Hilfe Fenster",
    "HelpLocations": "Beschreiben Sie die in Ihrer Geschichte verwendeten Orte, einschließlich Atmosphäre und Relevanz.",
    "HelpObjects": "Listen Sie wichtige Objekte und deren Bedeutung in der Geschichte auf.",
    "HelpPreferenceWindow": "Nehmen Sie die gewünschten Einstellungen vor.",
    "HelpProject": "Geben Sie allgemeine Informationen zu Ihrem Schreibprojekt an, wie Titel, Genre und Ziele.",
    "HelpProjectWindow": "Wählen Sie die Tabelle, die Sie bearbeiten wollen.",
    "HelpScenes": "Beschreiben Sie einzelne Szenen, deren Zweck und Umgebung.",
    "HelpStartWindow": "Wählen Sie die gewünschte Funktion.",
    "HelpStorylines": "Skizzieren Sie die Haupt-Handlungsstränge und deren Entwicklung im Laufe der Zeit.",
    "Location": "Orte",
    "LocationBtnDelete": "Löschen",
    "LocationBtnNew": "Neu",
    "LocationBtnNext": "Weiter",
    "LocationBtnPreview": "Zurück",
    "LocationBtnSave": "Speichern",
    "LocationTitle": "Titel",
    "LocationDescription": "Beschreibung",
    "LocationNotes": "Notizen",
    "Menu": "Menü",
    "MenuEdit": "Bearbeiten",
    "MenuFile": "Datei",
    "MenuHelp": "Hilfe",
    "MenuLanguage": "Sprache",
    "MenuSettings": "Einstellungen",
    "ObjectBtnDelete": "Löschen",
    "ObjectBtnNew": "Neu",
    "ObjectBtnNext": "Weiter",
    "ObjectBtnPreview": "Zurück",
    "ObjectBtnSave": "Speichern",
    "ObjectNotes": "Notizen",
    "Object": "Objekte",
    "ObjectTitle": "Titel",
    "ObjectDescription": "Beschreibung",
    "PreferenceActionSave": "Speichern",
    "PreferenceActionCancel": "Abbrechen",
    "PreferenceLanguage": "Sprache",
    "PreferenceStyle": "Stil",
    "PreferenceTheme": "Thema",
    "PreferenceThemeDark": "Dunkel",
    "PreferenceThemeNeutral": "Neutral",
    "PreferenceThemeLight": "Hell",
    "Preference": "Einstellungen",
    "Pro": "Projekte",
    "ProBtnProject": "Projekt",
    "ProBtnCharacters": "Charaktere",
    "ProBtnStorylines": "Erzählstränge",
    "ProBtnChapters": "Kapitel",
    "ProBtnScenes": "Szenen",
    "ProBtnObjects": "Objekte",
    "ProBtnLocations": "Orte",
    "ProBtnExit": "Beenden",
    "ProBtn": "Schaltflächen",
    "ProBtnDelete": "Löschen",
    "ProBtnNew": "Neu",
    "ProBtnNext": "Weiter",
    "ProBtnPreview": "Zurück",
    "ProBtnSave": "Speichern",
    "ProDetail": "Details",
    "ProDetailAuthor": "Autor",
    "ProDetailChapters": "Kapitel",
    "ProDetailCoverImage": "Titelbild",
    "ProDetailDay": "Tage bis Abgabe",
    "ProDetailDeadline": "Abgabedatum",
    "ProDetailFormLabel": "Projekt",
    "ProDetailGenre": "Genre",
    "ProDetailGroups": "Gruppen",
    "ProDetailLocations": "Orte",
    "ProDetailMainChar": "Hauptcharaktere",
    "ProDetailNarrativePerspective": "Perspektive Erzähler:in",
    "ProDetailObjects": "Objekte",
    "ProDetailPremise": "Prämisse",
    "ProDetailScenes": "Szenen",
    "ProDetailStartDate": "Startdatum",
    "ProDetailStorylines": "Erzählstränge",
    "ProDetailSubtitle": "Untertitel",
    "ProDetailSupportChar": "Nebencharaktere",
    "ProDetailTargetGroup": "Zielgruppe",
    "ProDetailTimeline": "Zeitlinie",
    "ProDetailTitle": "Titel",
    "ProDetailWindowTitle": "Datenbanken",
    "ProDetailWordsCountDay": "Wörter am Tag",
    "ProDetailWordsCountGoal": "Ziel Wortanzahl",
    "Scene": "Szenen",
    "SceneBtnDelete": "Löschen",
    "SceneBtnNew": "Neu",
    "SceneBtnNext": "Weiter",
    "SceneBtnPreview": "Zurück",
    "SceneBtnSave": "Speichern",
    "SceneTitle": "Titel",
    "SceneNumber": "Nummer",
    "SceneSummary": "Zusammenfassung",
    "SceneCharacters": "Charaktere",
    "SceneConflict": "Konflikt",
    "SceneDuration": "Dauer",
    "SceneGoal": "Ziel",
    "SceneLocations": "Orte",
    "SceneMood": "Stimmung",
    "SceneNotes": "Notizen",
    "SceneObjects": "Objekte",
    "SceneOutcome": "Ergebnis",
    "ScenePremise": "Prämisse",
    "SceneType": "Typ",
    "Start": "csNova",
    "StartBtnExit": "Beenden",
    "StartBtnHelp": "Hilfe && Tutorial",
    "StartBtnSettings": "Einstellungen",
    "StartBtnLoadProject": "Projekt laden ...",
    "StartBtnNewProject": "Neues Projekt",
    "Storyline": "Erzählstränge",
    "StorylineBtnDelete": "Löschen",
    "StorylineBtnNew": "Neu",
    "StorylineBtnNext": "Weiter",
    "StorylineBtnPreview": "Zurück",
    "StorylineBtnSave": "Speichern",
    "StorylineChapters": "Kapitel",
    "StorylineCharacters": "Charaktere",
    "StorylineDescription": "Beschreibung",
    "StorylineNotes": "Notizen",
    "StorylineObjects": "Objekte",
    "StorylinePremise": "Prämisse",
    "StorylineScenes": "Szenen",
    "StorylineTimeline": "Zeitlinie",
    "StorylineTitle": "Titel",
    "StorylineTransformation": "Transformation",
    "Win": "Fenster",
    "WinEditorTitle": "Editor Fenster",
    "WinHelpTitle": "Hilfe",
    "WinPreferenceTitle": "Einstellungen",
    "WinStartTitle": "csNova"
  },

  {
    "ID": "en",
    "Chapter": "Chapter",
    "ChapterBtnDelete": "Delete",
    "ChapterBtnNew": "New",
    "ChapterBtnNext": "Next",
    "ChapterBtnPreview": "Back",
    "ChapterBtnSave": "Save",
    "ChapterNumber": "Number",
    "ChapterSummary": "Summary",
    "ChapterCharacters": "Characters",
    "ChapterLocations": "Locations",
    "ChapterNotes": "Notes",
    "ChapterObjects": "Objects",
    "ChapterPremise": "Premise",
    "ChapterScenes": "Scenes",
    "ChapterTitle": "Title",
    "Char": "Characters",
    "CharApp": "Appearance",
    "CharAppBodyType": "Body Type",
    "CharAppCharisma": "Charisma",
    "CharAppEyeColor": "Eye Color",
    "CharAppEyeShape": "Eye Shape",
    "CharAppFaceShape": "Face Shape",
    "CharAppHair": "Hair",
    "CharAppHairColor": "Hair Color",
    "CharAppHeight": "Height",
    "CharAppNotes": "Notes",
    "CharAppPosture": "Posture",
    "CharAppSkin": "Skin",
    "CharAppSpecials": "Special Features",
    "CharApp2": "Appearance Details",
    "CharApp2Arms": "Arms",
    "CharApp2Buttocks": "Buttocks",
    "CharApp2Chest": "Chest",
    "CharApp2Feet": "Feet",
    "CharApp2Finger": "Fingers",
    "CharApp2Hands": "Hands",
    "CharApp2Head": "Head",
    "CharApp2HipWaist": "Hip, Waist",
    "CharApp2Legs": "Legs",
    "CharApp2Notes": "Notes",
    "CharApp2Shoulder": "Shoulders",
    "CharApp2Toes": "Toes",
    "CharBas": "Basic Data",
    "CharBasAge": "Age",
    "CharBasBorn": "Date of Birth",
    "CharBasFirstname": "First Name",
    "CharBasGender": "Gender",
    "CharBasGroup": "Group",
    "CharBasName": "Name",
    "CharBasNickname": "Nickname",
    "CharBasNotes": "Notes",
    "CharBasRole": "Role",
    "CharBasSexOrientation": "Sexual Orientation",
    "CharBasStatus": "Status",
    "CharBtn": "Buttons",
    "CharBtnDelete": "Delete",
    "CharBtnNew": "New",
    "CharBtnNext": "Next",
    "CharBtnPreview": "Back",
    "CharBtnSave": "Save",
    "CharEdu": "Education",
    "CharEduArtMusic": "Art/Music",
    "CharEduAutodidactic": "Autodidactic",
    "CharEduJob": "Job",
    "CharEduJobEducation": "Vocational Training",
    "CharEduNotes": "Notes",
    "CharEduSchool": "School",
    "CharEduSport": "Sport",
    "CharEduTechnologie": "Technology",
    "CharEduUniversity": "University",
    "CharGroups": "Groups",
    "CharGroupsDes": "Description",
    "CharGroupsTitle": "Designation",
    "CharOrigin": "Origin",
    "CharOriginBirthplace": "Place of Birth",
    "CharOriginFather": "Father",
    "CharOriginMother": "Mother",
    "CharOriginNotes": "Notes",
    "CharOriginReferencePerson": "Reference Person",
    "CharOriginSiblings": "Siblings",
    "CharPerson": "Personality",
    "CharPersonBehavior": "Behavior",
    "CharPersonBeliefs": "Beliefs",
    "CharPersonFears": "Fears",
    "CharPersonLifeGoals": "Life Goals",
    "CharPersonMotivation": "Motivation",
    "CharPersonNeg": "Negative Trait",
    "CharPersonNotes": "Notes",
    "CharPersonPos": "Positive Trait",
    "CharPersonStrengths": "Strengths",
    "CharPersonTalente": "Talents",
    "CharPersonWeakness": "Weaknesses",
    "CharPsy": "Psychological Profile",
    "CharPsyAggression": "Aggressiveness",
    "CharPsyDiagnostics": "Diagnosis",
    "CharPsyFormative": "Formative Influences",
    "CharPsyHumor": "Humor",
    "CharPsyMedication": "Medication",
    "CharPsyMoral": "Morals",
    "CharPsyNorms": "Norms",
    "CharPsyNotes": "Notes",
    "CharPsySelfimage": "Self-Image",
    "CharPsySocialization": "Socialization",
    "CharPsySymptoms": "Symptoms",
    "CharPsyTaboos": "Taboos",
    "CharPsyTemperament": "Temperament",
    "CharPsyTherapy": "Therapy",
    "CharPsyTrauma": "Trauma",
    "CharPsyValues": "Values",
    "Help": "Help",
    "HelpNewProject": "Select one of the databases you want to edit.",
    "HelpChapters": "Organize your story into chapters and describe their content.",
    "HelpChars": "Define your characters: names, roles, traits, and relationships.",
    "HelpEditorWindow": "Editor Window",
    "HelpHelpWindow": "Help Window",
    "HelpLocations": "Describe the locations used in your story, including atmosphere and relevance.",
    "HelpObjects": "List important objects and their significance in the story.",
    "HelpPreferenceWindow": "Make the desired settings.",
    "HelpProject": "Provide general information about your writing project, such as title, genre, and goals.",
    "HelpProjectWindow": "Select the table you want to edit.",
    "HelpScenes": "Describe individual scenes, their purpose and setting.",
    "HelpStartWindow": "Select the desired function.",
    "HelpStorylines": "Outline the main storylines and their development over time.",
    "Location": "Locations",
    "LocationBtnDelete": "Delete",
    "LocationBtnNew": "New",
    "LocationBtnNext": "Next",
    "LocationBtnPreview": "Back",
    "LocationBtnSave": "Save",
    "LocationTitle": "Title",
    "LocationDescription": "Description",
    "LocationNotes": "Notes",
    "Menu": "Menu",
    "MenuEdit": "Edit",
    "MenuFile": "File",
    "MenuHelp": "Help",
    "MenuLanguage": "Language",
    "MenuSettings": "Settings",
    "ObjectBtnDelete": "Delete",
    "ObjectBtnNew": "New",
    "ObjectBtnNext": "Next",
    "ObjectBtnPreview": "Back",
    "ObjectBtnSave": "Save",
    "ObjectNotes": "Notes",
    "Object": "Objects",
    "ObjectTitle": "Title",
    "ObjectDescription": "Description",
    "PreferenceActionSave": "Save",
    "PreferenceActionCancel": "Cancel",
    "PreferenceLanguage": "Language",
    "PreferenceStyle": "Style",
    "PreferenceTheme": "Theme",
    "PreferenceThemeDark": "Dark",
    "PreferenceThemeNeutral": "Neutral",
    "PreferenceThemeLight": "Light",
    "Preference": "Settings",
    "Pro": "Projects",
    "ProBtnProject": "Project",
    "ProBtnCharacters": "Characters",
    "ProBtnStorylines": "Storylines",
    "ProBtnChapters": "Chapters",
    "ProBtnScenes": "Scenes",
    "ProBtnObjects": "Objects",
    "ProBtnLocations": "Locations",
    "ProBtnExit": "Exit",
    "ProBtn": "Buttons",
    "ProBtnDelete": "Delete",
    "ProBtnNew": "New",
    "ProBtnNext": "Next",
    "ProBtnPreview": "Back",
    "ProBtnSave": "Save",
    "ProDetail": "Details",
    "ProDetailAuthor": "Author",
    "ProDetailChapters": "Chapters",
    "ProDetailCoverImage": "Cover Image",
    "ProDetailDay": "Days until Deadline",
    "ProDetailDeadline": "Deadline",
    "ProDetailFormLabel": "Project",
    "ProDetailGenre": "Genre",
    "ProDetailGroups": "Groups",
    "ProDetailLocations": "Locations",
    "ProDetailMainChar": "Main Characters",
    "ProDetailNarrativePerspective": "Narrative Perspective",
    "ProDetailObjects": "Objects",
    "ProDetailPremise": "Premise",
    "ProDetailScenes": "Scenes",
    "ProDetailStartDate": "Start Date",
    "ProDetailStorylines": "Storylines",
    "ProDetailSubtitle": "Subtitle",
    "ProDetailSupportChar": "Supporting Characters",
    "ProDetailTargetGroup": "Target Group",
    "ProDetailTimeline": "Timeline",
    "ProDetailTitle": "Title",
    "ProDetailWindowTitle": "Databases",
    "ProDetailWordsCountDay": "Words per Day",
    "ProDetailWordsCountGoal": "Word Count Goal",
    "Scene": "Scenes",
    "SceneBtnDelete": "Delete",
    "SceneBtnNew": "New",
    "SceneBtnNext": "Next",
    "SceneBtnPreview": "Back",
    "SceneBtnSave": "Save",
    "SceneTitle": "Title",
    "SceneNumber": "Number",
    "SceneSummary": "Summary",
    "SceneCharacters": "Characters",
    "SceneConflict": "Conflict",
    "SceneDuration": "Duration",
    "SceneGoal": "Goal",
    "SceneLocations": "Locations",
    "SceneMood": "Mood",
    "SceneNotes": "Notes",
    "SceneObjects": "Objects",
    "SceneOutcome": "Outcome",
    "ScenePremise": "Premise",
    "SceneType": "Type",
    "Start": "csNova",
    "StartBtnExit": "Exit",
    "StartBtnHelp": "Help && Tutorial",
    "StartBtnSettings": "Settings",
    "StartBtnLoadProject": "Load Project ...",
    "StartBtnNewProject": "New Project",
    "Storyline": "Storylines",
    "StorylineBtnDelete": "Delete",
    "StorylineBtnNew": "New",
    "StorylineBtnNext": "Next",
    "StorylineBtnPreview": "Back",
    "StorylineBtnSave": "Save",
    "StorylineChapters": "Chapters",
    "StorylineCharacters": "Characters",
    "StorylineDescription": "Description",
    "StorylineNotes": "Notes",
    "StorylineObjects": "Objects",
    "StorylinePremise": "Premise",
    "StorylineScenes": "Scenes",
    "StorylineTimeline": "Timeline",
    "StorylineTitle": "Title",
    "StorylineTransformation": "Transformation",
    "Win": "Window",
    "WinEditorTitle": "Editor Window",
    "WinHelpTitle": "Help",
    "WinPreferenceTitle": "Settings",
    "WinStartTitle": "csNova"
  },
  {
  "ID": "es",
  "Chapter": "Capítulo",
  "ChapterBtnDelete": "Eliminar",
  "ChapterBtnNew": "Nuevo",
  "ChapterBtnNext": "Siguiente",
  "ChapterBtnPreview": "Atrás",
  "ChapterBtnSave": "Guardar",
  "ChapterNumber": "Número",
  "ChapterSummary": "Resumen",
  "ChapterCharacters": "Personajes",
  "ChapterLocations": "Lugares",
  "ChapterNotes": "Notas",
  "ChapterObjects": "Objetos",
  "ChapterPremise": "Premisa",
  "ChapterScenes": "Escenas",
  "ChapterTitle": "Título",
  "Char": "Personajes",
  "CharApp": "Apariencia",
  "CharAppBodyType": "Tipo de cuerpo",
  "CharAppCharisma": "Carisma",
  "CharAppEyeColor": "Color de ojos",
  "CharAppEyeShape": "Forma de ojos",
  "CharAppFaceShape": "Forma de cara",
  "CharAppHair": "Cabello",
  "CharAppHairColor": "Color de cabello",
  "CharAppHeight": "Altura",
  "CharAppNotes": "Notas",
  "CharAppPosture": "Postura",
  "CharAppSkin": "Piel",
  "CharAppSpecials": "Características especiales",
  "CharApp2": "Detalles de apariencia",
  "CharApp2Arms": "Brazos",
  "CharApp2Buttocks": "Glúteos",
  "CharApp2Chest": "Pecho",
  "CharApp2Feet": "Pies",
  "CharApp2Finger": "Dedos",
  "CharApp2Hands": "Manos",
  "CharApp2Head": "Cabeza",
  "CharApp2HipWaist": "Cadera, cintura",
  "CharApp2Legs": "Piernas",
  "CharApp2Notes": "Notas",
  "CharApp2Shoulder": "Hombros",
  "CharApp2Toes": "Dedos de los pies",
  "CharBas": "Datos básicos",
  "CharBasAge": "Edad",
  "CharBasBorn": "Fecha de nacimiento",
  "CharBasFirstname": "Nombre",
  "CharBasGender": "Género",
  "CharBasGroup": "Grupo",
  "CharBasName": "Apellido",
  "CharBasNickname": "Apodo",
  "CharBasNotes": "Notas",
  "CharBasRole": "Rol",
  "CharBasSexOrientation": "Orientación sexual",
  "CharBasStatus": "Estado",
  "CharBtn": "Botones",
  "CharBtnDelete": "Eliminar",
  "CharBtnNew": "Nuevo",
  "CharBtnNext": "Siguiente",
  "CharBtnPreview": "Atrás",
  "CharBtnSave": "Guardar",
  "CharEdu": "Educación",
  "CharEduArtMusic": "Arte/Música",
  "CharEduAutodidactic": "Autodidacta",
  "CharEduJob": "Profesión",
  "CharEduJobEducation": "Formación profesional",
  "CharEduNotes": "Notas",
  "CharEduSchool": "Escuela",
  "CharEduSport": "Deporte",
  "CharEduTechnologie": "Tecnología",
  "CharEduUniversity": "Universidad",
  "CharGroups": "Grupos",
  "CharGroupsDes": "Descripción",
  "CharGroupsTitle": "Denominación",
  "CharOrigin": "Origen",
  "CharOriginBirthplace": "Lugar de nacimiento",
  "CharOriginFather": "Padre",
  "CharOriginMother": "Madre",
  "CharOriginNotes": "Notas",
  "CharOriginReferencePerson": "Persona de referencia",
  "CharOriginSiblings": "Hermanos",
  "CharPerson": "Personalidad",
  "CharPersonBehavior": "Comportamiento",
  "CharPersonBeliefs": "Creencias",
  "CharPersonFears": "Miedos",
  "CharPersonLifeGoals": "Meta de vida",
  "CharPersonMotivation": "Motivación",
  "CharPersonNeg": "Rasgo negativo",
  "CharPersonNotes": "Notas",
  "CharPersonPos": "Rasgo positivo",
  "CharPersonStrengths": "Fortalezas",
  "CharPersonTalente": "Talentos",
  "CharPersonWeakness": "Debilidades",
  "CharPsy": "Perfil psicológico",
  "CharPsyAggression": "Agresividad",
  "CharPsyDiagnostics": "Diagnóstico",
  "CharPsyFormative": "Influencias formativas",
  "CharPsyHumor": "Humor",
  "CharPsyMedication": "Medicamentos",
  "CharPsyMoral": "Moral",
  "CharPsyNorms": "Normas",
  "CharPsyNotes": "Notas",
  "CharPsySelfimage": "Autoimagen",
  "CharPsySocialization": "Socialización",
  "CharPsySymptoms": "Síntomas",
  "CharPsyTaboos": "Tabúes",
  "CharPsyTemperament": "Temperamento",
  "CharPsyTherapy": "Terapia",
  "CharPsyTrauma": "Trauma",
  "CharPsyValues": "Valores",
  "Help": "Ayuda",
  "HelpNewProject": "Seleccione una de las bases de datos que desea editar.",
  "HelpChapters": "Organice su historia en capítulos y describa su contenido.",
  "HelpChars": "Defina sus personajes: nombres, roles, características y relaciones.",
  "HelpEditorWindow": "Ventana del editor",
  "HelpHelpWindow": "Ventana de ayuda",
  "HelpLocations": "Describa los lugares utilizados en su historia, incluyendo atmósfera y relevancia.",
  "HelpObjects": "Enumere los objetos importantes y su significado en la historia.",
  "HelpPreferenceWindow": "Realice los ajustes deseados.",
  "HelpProject": "Proporcione información general sobre su proyecto de escritura, como título, género y objetivos.",
  "HelpProjectWindow": "Seleccione la tabla que desea editar.",
  "HelpScenes": "Describa escenas individuales, su propósito y entorno.",
  "HelpStartWindow": "Seleccione la función deseada.",
  "HelpStorylines": "Resuma las principales tramas y su desarrollo a lo largo del tiempo.",
  "Location": "Lugares",
  "LocationBtnDelete": "Eliminar",
  "LocationBtnNew": "Nuevo",
  "LocationBtnNext": "Siguiente",
  "LocationBtnPreview": "Atrás",
  "LocationBtnSave": "Guardar",
  "LocationTitle": "Título",
  "LocationDescription": "Descripción",
  "LocationNotes": "Notas",
  "Menu": "Menú",
  "MenuEdit": "Editar",
  "MenuFile": "Archivo",
  "MenuHelp": "Ayuda",
  "MenuLanguage": "Idioma",
  "MenuSettings": "Configuración",
  "ObjectBtnDelete": "Eliminar",
  "ObjectBtnNew": "Nuevo",
  "ObjectBtnNext": "Siguiente",
  "ObjectBtnPreview": "Atrás",
  "ObjectBtnSave": "Guardar",
  "ObjectNotes": "Notas",
  "Object": "Objetos",
  "ObjectTitle": "Título",
  "ObjectDescription": "Descripción",
  "PreferenceActionSave": "Guardar",
  "PreferenceActionCancel": "Cancelar",
  "PreferenceLanguage": "Idioma",
  "PreferenceStyle": "Estilo",
  "PreferenceTheme": "Tema",
  "PreferenceThemeDark": "Oscuro",
  "PreferenceThemeNeutral": "Neutro",
  "PreferenceThemeLight": "Claro",
  "Preference": "Configuración",
  "Pro": "Proyectos",
  "ProBtnProject": "Proyecto",
  "ProBtnCharacters": "Personajes",
  "ProBtnStorylines": "Tramas",
  "ProBtnChapters": "Capítulos",
  "ProBtnScenes": "Escenas",
  "ProBtnObjects": "Objetos",
  "ProBtnLocations": "Lugares",
  "ProBtnExit": "Salir",
  "ProBtn": "Botones",
  "ProBtnDelete": "Eliminar",
  "ProBtnNew": "Nuevo",
  "ProBtnNext": "Siguiente",
  "ProBtnPreview": "Atrás",
  "ProBtnSave": "Guardar",
  "ProDetail": "Detalles",
  "ProDetailAuthor": "Autor",
  "ProDetailChapters": "Capítulos",
  "ProDetailCoverImage": "Imagen de portada",
  "ProDetailDay": "Días hasta la fecha límite",
  "ProDetailDeadline": "Fecha límite",
  "ProDetailFormLabel": "Proyecto",
  "ProDetailGenre": "Género",
  "ProDetailGroups": "Grupos",
  "ProDetailLocations": "Lugares",
  "ProDetailMainChar": "Personajes principales",
  "ProDetailNarrativePerspective": "Perspectiva narrativa",
  "ProDetailObjects": "Objetos",
  "ProDetailPremise": "Premisa",
  "ProDetailScenes": "Escenas",
  "ProDetailStartDate": "Fecha de inicio",
  "ProDetailStorylines": "Tramas",
  "ProDetailSubtitle": "Subtítulo",
  "ProDetailSupportChar": "Personajes secundarios",
  "ProDetailTargetGroup": "Grupo objetivo",
  "ProDetailTimeline": "Cronología",
  "ProDetailTitle": "Título",
  "ProDetailWindowTitle": "Bases de datos",
  "ProDetailWordsCountDay": "Palabras por día",
  "ProDetailWordsCountGoal": "Meta de palabras",
  "Scene": "Escenas",
  "SceneBtnDelete": "Eliminar",
  "SceneBtnNew": "Nuevo",
  "SceneBtnNext": "Siguiente",
  "SceneBtnPreview": "Atrás",
  "SceneBtnSave": "Guardar",
  "SceneTitle": "Título",
  "SceneNumber": "Número",
  "SceneSummary": "Resumen",
  "SceneCharacters": "Personajes",
  "SceneConflict": "Conflicto",
  "SceneDuration": "Duración",
  "SceneGoal": "Meta",
  "SceneLocations": "Lugares",
  "SceneMood": "Ánimo",
  "SceneNotes": "Notas",
  "SceneObjects": "Objetos",
  "SceneOutcome": "Resultado",
  "ScenePremise": "Premisa",
  "SceneType": "Tipo",
  "Start": "csNova",
  "StartBtnExit": "Salir",
  "StartBtnHelp": "Ayuda y tutorial",
  "StartBtnSettings": "Configuración",
  "StartBtnLoadProject": "Cargar proyecto ...",
  "StartBtnNewProject": "Nuevo proyecto",
  "Storyline": "Tramas",
  "StorylineBtnDelete": "Eliminar",
  "StorylineBtnNew": "Nuevo",
  "StorylineBtnNext": "Siguiente",
  "StorylineBtnPreview": "Atrás",
  "StorylineBtnSave": "Guardar",
  "StorylineChapters": "Capítulos",
  "StorylineCharacters": "Personajes",
  "StorylineDescription": "Descripción",
  "StorylineNotes": "Notas",
  "StorylineObjects": "Objetos",
  "StorylinePremise": "Premisa",
  "StorylineScenes": "Escenas",
  "StorylineTimeline": "Cronología",
  "StorylineTitle": "Título",
  "StorylineTransformation": "Transformación",
  "Win": "Ventana",
  "WinEditorTitle": "Ventana del editor",
  "WinHelpTitle": "Ayuda",
  "WinPreferenceTitle": "Configuración",
  "WinStartTitle": "csNova"
},
{
  "ID": "fr",
  "Chapter": "Chapitre",
  "ChapterBtnDelete": "Supprimer",
  "ChapterBtnNew": "Nouveau",
  "ChapterBtnNext": "Suivant",
  "ChapterBtnPreview": "Retour",
  "ChapterBtnSave": "Enregistrer",
  "ChapterNumber": "Numéro",
  "ChapterSummary": "Résumé",
  "ChapterCharacters": "Personnages",
  "ChapterLocations": "Lieux",
  "ChapterNotes": "Notes",
  "ChapterObjects": "Objets",
  "ChapterPremise": "Prémisse",
  "ChapterScenes": "Scènes",
  "ChapterTitle": "Titre",
  "Char": "Personnages",
  "CharApp": "Apparence",
  "CharAppBodyType": "Type de corps",
  "CharAppCharisma": "Charisme",
  "CharAppEyeColor": "Couleur des yeux",
  "CharAppEyeShape": "Forme des yeux",
  "CharAppFaceShape": "Forme du visage",
  "CharAppHair": "Cheveux",
  "CharAppHairColor": "Couleur des cheveux",
  "CharAppHeight": "Taille",
  "CharAppNotes": "Notes",
  "CharAppPosture": "Posture",
  "CharAppSkin": "Peau",
  "CharAppSpecials": "Caractéristiques spéciales",
  "CharApp2": "Détails de l'apparence",
  "CharApp2Arms": "Bras",
  "CharApp2Buttocks": "Fessier",
  "CharApp2Chest": "Poitrine",
  "CharApp2Feet": "Pieds",
  "CharApp2Finger": "Doigts",
  "CharApp2Hands": "Mains",
  "CharApp2Head": "Tête",
  "CharApp2HipWaist": "Hanches, taille",
  "CharApp2Legs": "Jambes",
  "CharApp2Notes": "Notes",
  "CharApp2Shoulder": "Épaules",
  "CharApp2Toes": "Orteils",
  "CharBas": "Données de base",
  "CharBasAge": "Âge",
  "CharBasBorn": "Date de naissance",
  "CharBasFirstname": "Prénom",
  "CharBasGender": "Genre",
  "CharBasGroup": "Groupe",
  "CharBasName": "Nom",
  "CharBasNickname": "Surnom",
  "CharBasNotes": "Notes",
  "CharBasRole": "Rôle",
  "CharBasSexOrientation": "Orientation sexuelle",
  "CharBasStatus": "Statut",
  "CharBtn": "Boutons",
  "CharBtnDelete": "Supprimer",
  "CharBtnNew": "Nouveau",
  "CharBtnNext": "Suivant",
  "CharBtnPreview": "Retour",
  "CharBtnSave": "Enregistrer",
  "CharEdu": "Éducation",
  "CharEduArtMusic": "Art/Musique",
  "CharEduAutodidactic": "Autodidacte",
  "CharEduJob": "Profession",
  "CharEduJobEducation": "Formation professionnelle",
  "CharEduNotes": "Notes",
  "CharEduSchool": "École",
  "CharEduSport": "Sport",
  "CharEduTechnologie": "Technologie",
  "CharEduUniversity": "Université",
  "CharGroups": "Groupes",
  "CharGroupsDes": "Description",
  "CharGroupsTitle": "Désignation",
  "CharOrigin": "Origine",
  "CharOriginBirthplace": "Lieu de naissance",
  "CharOriginFather": "Père",
  "CharOriginMother": "Mère",
  "CharOriginNotes": "Notes",
  "CharOriginReferencePerson": "Personne de référence",
  "CharOriginSiblings": "Frères et sœurs",
  "CharPerson": "Personnalité",
  "CharPersonBehavior": "Comportement",
  "CharPersonBeliefs": "Croyances",
  "CharPersonFears": "Peurs",
  "CharPersonLifeGoals": "Objectif de vie",
  "CharPersonMotivation": "Motivation",
  "CharPersonNeg": "Trait négatif",
  "CharPersonNotes": "Notes",
  "CharPersonPos": "Trait positif",
  "CharPersonStrengths": "Forces",
  "CharPersonTalente": "Talents",
  "CharPersonWeakness": "Faiblesses",
  "CharPsy": "Profil psychologique",
  "CharPsyAggression": "Agressivité",
  "CharPsyDiagnostics": "Diagnostic",
  "CharPsyFormative": "Influences formatrices",
  "CharPsyHumor": "Humour",
  "CharPsyMedication": "Médicaments",
  "CharPsyMoral": "Morale",
  "CharPsyNorms": "Normes",
  "CharPsyNotes": "Notes",
  "CharPsySelfimage": "Image de soi",
  "CharPsySocialization": "Socialisation",
  "CharPsySymptoms": "Symptômes",
  "CharPsyTaboos": "Tabous",
  "CharPsyTemperament": "Tempérament",
  "CharPsyTherapy": "Thérapie",
  "CharPsyTrauma": "Traumatisme",
  "CharPsyValues": "Valeurs",
  "Help": "Aide",
  "HelpNewProject": "Sélectionnez l'une des bases de données que vous souhaitez modifier.",
  "HelpChapters": "Organisez votre histoire en chapitres et décrivez leur contenu.",
  "HelpChars": "Définissez vos personnages : noms, rôles, traits et relations.",
  "HelpEditorWindow": "Fenêtre d'édition",
  "HelpHelpWindow": "Fenêtre d'aide",
  "HelpLocations": "Décrivez les lieux utilisés dans votre histoire, y compris l'atmosphère et la pertinence.",
  "HelpObjects": "Listez les objets importants et leur signification dans l'histoire.",
  "HelpPreferenceWindow": "Effectuez les réglages souhaités.",
  "HelpProject": "Fournissez des informations générales sur votre projet d'écriture, telles que le titre, le genre et les objectifs.",
  "HelpProjectWindow": "Sélectionnez le tableau que vous souhaitez modifier.",
  "HelpScenes": "Décrivez les scènes individuelles, leur but et leur cadre.",
  "HelpStartWindow": "Sélectionnez la fonction souhaitée.",
  "HelpStorylines": "Présentez les principales intrigues et leur évolution au fil du temps.",
  "Location": "Lieux",
  "LocationBtnDelete": "Supprimer",
  "LocationBtnNew": "Nouveau",
  "LocationBtnNext": "Suivant",
  "LocationBtnPreview": "Retour",
  "LocationBtnSave": "Enregistrer",
  "LocationTitle": "Titre",
  "LocationDescription": "Description",
  "LocationNotes": "Notes",
  "Menu": "Menu",
  "MenuEdit": "Éditer",
  "MenuFile": "Fichier",
  "MenuHelp": "Aide",
  "MenuLanguage": "Langue",
  "MenuSettings": "Paramètres",
  "ObjectBtnDelete": "Supprimer",
  "ObjectBtnNew": "Nouveau",
  "ObjectBtnNext": "Suivant",
  "ObjectBtnPreview": "Retour",
  "ObjectBtnSave": "Enregistrer",
  "ObjectNotes": "Notes",
  "Object": "Objets",
  "ObjectTitle": "Titre",
  "ObjectDescription": "Description",
  "PreferenceActionSave": "Enregistrer",
  "PreferenceActionCancel": "Annuler",
  "PreferenceLanguage": "Langue",
  "PreferenceStyle": "Style",
  "PreferenceTheme": "Thème",
  "PreferenceThemeDark": "Sombre",
  "PreferenceThemeNeutral": "Neutre",
  "PreferenceThemeLight": "Clair",
  "Preference": "Paramètres",
  "Pro": "Projets",
  "ProBtnProject": "Projet",
  "ProBtnCharacters": "Personnages",
  "ProBtnStorylines": "Intrigues",
  "ProBtnChapters": "Chapitres",
  "ProBtnScenes": "Scènes",
  "ProBtnObjects": "Objets",
  "ProBtnLocations": "Lieux",
  "ProBtnExit": "Quitter",
  "ProBtn": "Boutons",
  "ProBtnDelete": "Supprimer",
  "ProBtnNew": "Nouveau",
  "ProBtnNext": "Suivant",
  "ProBtnPreview": "Retour",
  "ProBtnSave": "Enregistrer",
  "ProDetail": "Détails",
  "ProDetailAuthor": "Auteur",
  "ProDetailChapters": "Chapitres",
  "ProDetailCoverImage": "Image de couverture",
  "ProDetailDay": "Jours avant la date limite",
  "ProDetailDeadline": "Date limite",
  "ProDetailFormLabel": "Projet",
  "ProDetailGenre": "Genre",
  "ProDetailGroups": "Groupes",
  "ProDetailLocations": "Lieux",
  "ProDetailMainChar": "Personnages principaux",
  "ProDetailNarrativePerspective": "Perspective narrative",
  "ProDetailObjects": "Objets",
  "ProDetailPremise": "Prémisse",
  "ProDetailScenes": "Scènes",
  "ProDetailStartDate": "Date de début",
  "ProDetailStorylines": "Intrigues",
  "ProDetailSubtitle": "Sous-titre",
  "ProDetailSupportChar": "Personnages secondaires",
  "ProDetailTargetGroup": "Groupe cible",
  "ProDetailTimeline": "Chronologie",
  "ProDetailTitle": "Titre",
  "ProDetailWindowTitle": "Bases de données",
  "ProDetailWordsCountDay": "Mots par jour",
  "ProDetailWordsCountGoal": "Objectif de mots",
  "Scene": "Scènes",
  "SceneBtnDelete": "Supprimer",
  "SceneBtnNew": "Nouveau",
  "SceneBtnNext": "Suivant",
  "SceneBtnPreview": "Retour",
  "SceneBtnSave": "Enregistrer",
  "SceneTitle": "Titre",
  "SceneNumber": "Numéro",
  "SceneSummary": "Résumé",
  "SceneCharacters": "Personnages",
  "SceneConflict": "Conflit",
  "SceneDuration": "Durée",
  "SceneGoal": "Objectif",
  "SceneLocations": "Lieux",
  "SceneMood": "Ambiance",
  "SceneNotes": "Notes",
  "SceneObjects": "Objets",
  "SceneOutcome": "Résultat",
  "ScenePremise": "Prémisse",
  "SceneType": "Type",
  "Start": "csNova",
  "StartBtnExit": "Quitter",
  "StartBtnHelp": "Aide & Tutoriel",
  "StartBtnSettings": "Paramètres",
  "StartBtnLoadProject": "Charger le projet ...",
  "StartBtnNewProject": "Nouveau projet",
  "Storyline": "Intrigues",
  "StorylineBtnDelete": "Supprimer",
  "StorylineBtnNew": "Nouveau",
  "StorylineBtnNext": "Suivant",
  "StorylineBtnPreview": "Retour",
  "StorylineBtnSave": "Enregistrer",
  "StorylineChapters": "Chapitres",
  "StorylineCharacters": "Personnages",
  "StorylineDescription": "Description",
  "StorylineNotes": "Notes",
  "StorylineObjects": "Objets",
  "StorylinePremise": "Prémisse",
  "StorylineScenes": "Scènes",
  "StorylineTimeline": "Chronologie",
  "StorylineTitle": "Titre",
  "StorylineTransformation": "Transformation",
  "Win": "Fenêtre",
  "WinEditorTitle": "Fenêtre d'édition",
  "WinHelpTitle": "Aide",
  "WinPreferenceTitle": "Paramètres",
  "WinStartTitle": "csNova"
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
        self.key_map = {}
        self._load_translations()
        self._init_key_map()

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
            else:
                self.translations = {}
            log_info(f"Translations loaded for language '{self.lang}'.")
        except Exception as e:
            log_exception("Error loading translations", e)
            self.translations = {}

    def _init_key_map(self):
        # Explizites Mapping nach UI-Modul/Formular sortiert
        self.key_map = {
            # StartWindow
            "start_btn_new_project": "StartBtnNewProject",
            "start_btn_load_project": "StartBtnLoadProject",
            "start_btn_settings": "StartBtnSettings",
            "start_btn_help": "StartBtnHelp",
            "start_btn_exit": "StartBtnExit",
            "window_start_title": "WinStartTitle",

            # ProjectWindow
            "project": "Pro",
            "project_btn": "ProBtn",
            "project_btn_project": "ProBtnProject",
            "project_btn_characters": "ProBtnCharacters",
            "project_btn_storylines": "ProBtnStorylines",
            "project_btn_chapters": "ProBtnChapters",
            "project_btn_scenes": "ProBtnScenes",
            "project_btn_objects": "ProBtnObjects",
            "project_btn_locations": "ProBtnLocations",
            "project_btn_exit": "ProBtnExit",
            "project_btn_new": "ProBtnNew",
            "project_btn_delete": "ProBtnDelete",
            "project_btn_next": "ProBtnNext",
            "project_btn_preview": "ProBtnPreview",
            "project_btn_save": "ProBtnSave",
            "project_days_until_deadline": "ProDetailDay",
            "project_deadline": "ProDetailDeadline",
            "project_start_date": "ProDetailStartDate",
            "project_word_count": "ProDetailWordCount",
            "project_target_word_count": "ProDetailTargetWordCount",
            "project_title": "ProDetailTitle",
            "project_detail": "ProDetail",
            "project_detail_author": "ProDetailAuthor",
            "project_detail_chapters": "ProDetailChapters",
            "project_detail_cover_image": "ProDetailCoverImage",
            "project_detail_form_label": "ProDetailFormLabel",
            "project_detail_genre": "ProDetailGenre",
            "project_detail_groups": "ProDetailGroups",
            "project_detail_scenes": "ProDetailScenes",
            "project_detail_objects": "ProDetailObjects",
            "project_detail_locations": "ProDetailLocations",
            "project_detail_storylines": "ProDetailStorylines",
            "project_detail_main_char": "ProDetailMainChar",
            "project_detail_support_char": "ProDetailSupportChar",
            "project_detail_narrative_perspective": "ProDetailNarrativePerspective",
            "project_detail_premise": "ProDetailPremise",
            "project_detail_timeline": "ProDetailTimeline",
            "project_detail_subtitle": "ProDetailSubtitle",
            "project_detail_target_group": "ProDetailTargetGroup",
            "project_window_title": "ProDetailWindowTitle",
            "project_words_count_day": "ProDetailWordsCountDay",
            "project_words_count_goal": "ProDetailWordsCountGoal",

            # CharacterForm
            "character": "Char",
            "character_app": "CharApp",
            "character_app_body_type": "CharAppBodyType",
            "character_app_charisma": "CharAppCharisma",
            "character_app_eye_color": "CharAppEyeColor",
            "character_app_eye_shape": "CharAppEyeShape",
            "character_app_face_shape": "CharAppFaceShape",
            "character_app_hair": "CharAppHair",
            "character_app_hair_color": "CharAppHairColor",
            "character_app_height": "CharAppHeight",
            "character_app_notes": "CharAppNotes",
            "character_app_posture": "CharAppPosture",
            "character_app_skin": "CharAppSkin",
            "character_app_specials": "CharAppSpecials",
            "character_app2": "CharApp2",
            "character_app2_arms": "CharApp2Arms",
            "character_app2_buttocks": "CharApp2Buttocks",
            "character_app2_chest": "CharApp2Chest",
            "character_app2_feet": "CharApp2Feet",
            "character_app2_finger": "CharApp2Finger",
            "character_app2_hands": "CharApp2Hands",
            "character_app2_head": "CharApp2Head",
            "character_app2_hip_waist": "CharApp2HipWaist",
            "character_app2_legs": "CharApp2Legs",
            "character_app2_notes": "CharApp2Notes",
            "character_app2_shoulder": "CharApp2Shoulder",
            "character_app2_toes": "CharApp2Toes",
            "character_bas": "CharBas",
            "character_bas_age": "CharBasAge",
            "character_bas_born": "CharBasBorn",
            "character_bas_firstname": "CharBasFirstname",
            "character_bas_gender": "CharBasGender",
            "character_bas_group": "CharBasGroup",
            "character_bas_name": "CharBasName",
            "character_bas_nickname": "CharBasNickname",
            "character_bas_notes": "CharBasNotes",
            "character_bas_role": "CharBasRole",
            "character_bas_sex_orientation": "CharBasSexOrientation",
            "character_bas_status": "CharBasStatus",
            "character_btn": "CharBtn",
            "character_btn_delete": "CharBtnDelete",
            "character_btn_new": "CharBtnNew",
            "character_btn_next": "CharBtnNext",
            "character_btn_preview": "CharBtnPreview",
            "character_btn_save": "CharBtnSave",
            "character_edu": "CharEdu",
            "character_edu_art_music": "CharEduArtMusic",
            "character_edu_autodidactic": "CharEduAutodidactic",
            "character_edu_job": "CharEduJob",
            "character_edu_job_education": "CharEduJobEducation",
            "character_edu_notes": "CharEduNotes",
            "character_edu_school": "CharEduSchool",
            "character_edu_sport": "CharEduSport",
            "character_edu_technologie": "CharEduTechnologie",
            "character_edu_university": "CharEduUniversity",
            "character_groups": "CharGroups",
            "character_groups_des": "CharGroupsDes",
            "character_groups_title": "CharGroupsTitle",
            "character_origin": "CharOrigin",
            "character_origin_birthplace": "CharOriginBirthplace",
            "character_origin_father": "CharOriginFather",
            "character_origin_mother": "CharOriginMother",
            "character_origin_notes": "CharOriginNotes",
            "character_origin_reference_person": "CharOriginReferencePerson",
            "character_origin_siblings": "CharOriginSiblings",
            "character_person": "CharPerson",
            "character_person_behavior": "CharPersonBehavior",
            "character_person_beliefs": "CharPersonBeliefs",
            "character_person_fears": "CharPersonFears",
            "character_person_life_goals": "CharPersonLifeGoals",
            "character_person_motivation": "CharPersonMotivation",
            "character_person_neg": "CharPersonNeg",
            "character_person_notes": "CharPersonNotes",
            "character_person_pos": "CharPersonPos",
            "character_person_strengths": "CharPersonStrengths",
            "character_person_talente": "CharPersonTalente",
            "character_person_weakness": "CharPersonWeakness",
            "character_psy": "CharPsy",
            "character_psy_aggression": "CharPsyAggression",
            "character_psy_diagnostics": "CharPsyDiagnostics",
            "character_psy_formative": "CharPsyFormative",
            "character_psy_humor": "CharPsyHumor",
            "character_psy_medication": "CharPsyMedication",
            "character_psy_moral": "CharPsyMoral",
            "character_psy_norms": "CharPsyNorms",
            "character_psy_notes": "CharPsyNotes",
            "character_psy_selfimage": "CharPsySelfimage",
            "character_psy_socialization": "CharPsySocialization",
            "character_psy_symptoms": "CharPsySymptoms",
            "character_psy_taboos": "CharPsyTaboos",
            "character_psy_temperament": "CharPsyTemperament",
            "character_psy_therapy": "CharPsyTherapy",
            "character_psy_trauma": "CharPsyTrauma",
            "character_psy_values": "CharPsyValues",

            # ChaptersForm
            "chapter": "Chapter",
            "chapter_btn_delete": "ChapterBtnDelete",
            "chapter_btn_new": "ChapterBtnNew",
            "chapter_btn_next": "ChapterBtnNext",
            "chapter_btn_preview": "ChapterBtnPreview",
            "chapter_btn_save": "ChapterBtnSave",
            "chapter_number": "ChapterNumber",
            "chapter_summary": "ChapterSummary",
            "chapter_characters": "ChapterCharacters",
            "chapter_locations": "ChapterLocations",
            "chapter_notes": "ChapterNotes",
            "chapter_objects": "ChapterObjects",
            "chapter_premise": "ChapterPremise",
            "chapter_scenes": "ChapterScenes",
            "chapter_title": "ChapterTitle",

            # ScenesForm
            "scene": "Scene",
            "scene_btn_delete": "SceneBtnDelete",
            "scene_btn_new": "SceneBtnNew",
            "scene_btn_next": "SceneBtnNext",
            "scene_btn_preview": "SceneBtnPreview",
            "scene_btn_save": "SceneBtnSave",
            "scene_title": "SceneTitle",
            "scene_number": "SceneNumber",
            "scene_summary": "SceneSummary",
            "scene_characters": "SceneCharacters",
            "scene_conflict": "SceneConflict",
            "scene_duration": "SceneDuration",
            "scene_goal": "SceneGoal",
            "scene_locations": "SceneLocations",
            "scene_mood": "SceneMood",
            "scene_notes": "SceneNotes",
            "scene_objects": "SceneObjects",
            "scene_outcome": "SceneOutcome",
            "scene_premise": "ScenePremise",
            "scene_type": "SceneType",

            # ObjectsForm
            "object": "Object",
            "object_btn_delete": "ObjectBtnDelete",
            "object_btn_new": "ObjectBtnNew",
            "object_btn_next": "ObjectBtnNext",
            "object_btn_preview": "ObjectBtnPreview",
            "object_btn_save": "ObjectBtnSave",
            "object_title": "ObjectTitle",
            "object_description": "ObjectDescription",
            "object_notes": "ObjectNotes",

            # LocationsForm
            "location": "Location",
            "location_btn_delete": "LocationBtnDelete",
            "location_btn_new": "LocationBtnNew",
            "location_btn_next": "LocationBtnNext",
            "location_btn_preview": "LocationBtnPreview",
            "location_btn_save": "LocationBtnSave",
            "location_title": "LocationTitle",
            "location_description": "LocationDescription",
            "location_notes": "LocationNotes",

            # StorylinesForm
            "storyline": "Storyline",
            "storyline_btn_delete": "StorylineBtnDelete",
            "storyline_btn_new": "StorylineBtnNew",
            "storyline_btn_next": "StorylineBtnNext",
            "storyline_btn_preview": "StorylineBtnPreview",
            "storyline_btn_save": "StorylineBtnSave",
            "storyline_chapters": "StorylineChapters",
            "storyline_characters": "StorylineCharacters",
            "storyline_description": "StorylineDescription",
            "storyline_notes": "StorylineNotes",
            "storyline_objects": "StorylineObjects",
            "storyline_premise": "StorylinePremise",
            "storyline_scenes": "StorylineScenes",
            "storyline_timeline": "StorylineTimeline",
            "storyline_title": "StorylineTitle",
            "storyline_transformation": "StorylineTransformation",

            # Preferences
            "preference": "Preference",
            "preference_save": "PreferenceActionSave",
            "preference_cancel": "PreferenceActionCancel",
            "preference_language": "PreferenceLanguage",
            "preference_style": "PreferenceStyle",
            "preference_theme": "PreferenceTheme",
            "preference_theme_dark": "PreferenceThemeDark",
            "preference_theme_neutral": "PreferenceThemeNeutral",
            "preference_theme_light": "PreferenceThemeLight",
            "preference_title": "WinPreferenceTitle",

            # HelpPanel
            "help": "Help",
            "help_new_project": "HelpNewProject",
            "help_chapters": "HelpChapters",
            "help_chars": "HelpChars",
            "help_editor_window": "HelpEditorWindow",
            "help_help_window": "HelpHelpWindow",
            "help_locations": "HelpLocations",
            "help_objects": "HelpObjects",
            "help_preference_window": "HelpPreferenceWindow",
            "help_project": "HelpProject",
            "help_project_window": "HelpProjectWindow",
            "help_scenes": "HelpScenes",
            "help_start_window": "HelpStartWindow",
            "help_storylines": "HelpStorylines",

            # Menu
            "menu": "Menu",
            "menu_file": "MenuFile",
            "menu_edit": "MenuEdit",
            "menu_help": "MenuHelp",
            "menu_language": "MenuLanguage",
            "menu_settings": "MenuSettings",

            # Fenster-Titel
            "win": "Win",
            "win_editor_title": "WinEditorTitle",
            "win_help_title": "WinHelpTitle",

        }

    def set_language(self, lang_code):
        log_subsection("set_language")
        self.lang = lang_code
        self._load_translations()
        self._init_key_map()

    def tr(self, standard_key):
        log_subsection("tr")
        json_key = self.key_map.get(standard_key, standard_key)
        return self.translations.get(json_key, standard_key)

    def form_label(self, standard_key):
        log_subsection("form_label")
        return self.tr(standard_key)

    def help_text(self, standard_key):
        log_subsection("help_text")
        return self.tr(standard_key)
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
    "border_radius": 8,
    "font_size": 14,
    "input_width": 400,
    "border": "#b6c2e1",
    "highlight": "#ff0",
    "background": "#e7eaf3",
    "foreground": "#1a1a1a",
    "button_bg": "#e7eaf3",
    "button_fg": "#1a1a1a",
    "button_hover": "#d0d6e6",
    "button_active": "#b6c2e1",
    "input_bg": "#ffffff",
    "input_fg": "#1a1a1a",
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

def load_global_stylesheet(style_code=None, mode_code=None, font_size=14):
    """
    Loads the global stylesheet for the application using the given style and mode.
    If style_code or mode_code are not provided, uses current settings.
    """
    log_section("form_styles.py")
    log_subsection("load_global_stylesheet")
    try:
        style = get_current_style(style_code, mode_code)
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

def load_button_style(style_code=None, mode_code=None, font_size=14):
    """
    Loads the stylesheet for buttons and toolbars.
    """
    log_section("form_styles.py")
    log_subsection("load_button_style")
    try:
        style = get_current_style(style_code, mode_code)
        style["font_size"] = font_size
        style["border_radius"] = DEFAULTS["border_radius"]
        return render_css("button", style) + render_css("toolbar", style)
    except Exception as e:
        log_exception("Error loading button stylesheet", e)
        return ""

def load_active_button_style(style_code=None, mode_code=None, font_size=16):
    """
    Loads the stylesheet for active buttons.
    """
    log_section("form_styles.py")
    log_subsection("load_active_button_style")
    try:
        style = get_current_style(style_code, mode_code)
        style["font_size"] = font_size
        style["border_radius"] = DEFAULTS["border_radius"]
        return render_css("active_button", style)
    except Exception as e:
        log_exception("Error loading active button stylesheet", e)
        return ""

def load_form_style(style_code=None, mode_code=None, input_font_size=14, label_font_size=14, input_width=400):
    """
    Loads the stylesheet for forms and input fields.
    """
    log_section("form_styles.py")
    log_subsection("load_form_style")
    try:
        style = get_current_style(style_code, mode_code)
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

            # Standard-Keys für die Aktionen gemäß translator.py
            self.new_action = QAction(self.translator.tr(f"{form_prefix}_btn_new"), self)
            self.delete_action = QAction(self.translator.tr(f"{form_prefix}_btn_delete"), self)
            self.prev_action = QAction(self.translator.tr(f"{form_prefix}_btn_preview"), self)
            self.next_action = QAction(self.translator.tr(f"{form_prefix}_btn_next"), self)
            self.save_action = QAction(self.translator.tr(f"{form_prefix}_btn_save"), self)

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
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from gui.widgets.form_toolbar import FormToolbar
from core.logger import log_section, log_subsection, log_info, log_exception

class ChaptersForm(QWidget):
    def __init__(self, translator, parent=None):
        log_section("form_chapters.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            layout = QVBoxLayout(self)

            # Toolbar mit "chapter"-Prefix
            self.toolbar = FormToolbar(self.translator, "chapter", self)
            layout.addWidget(self.toolbar)

            # Beispiel für ein Label mit standard_key
            self.title_label = QLabel(self.translator.tr("chapter_title"), self)
            layout.addWidget(self.title_label)

            # Weitere Felder/Labels nach Bedarf, immer mit standard_key
            self.number_label = QLabel(self.translator.tr("chapter_number"), self)
            layout.addWidget(self.number_label)

            self.summary_label = QLabel(self.translator.tr("chapter_summary"), self)
            layout.addWidget(self.summary_label)

            self.setLayout(layout)
            log_info("ChaptersForm initialized successfully.")
        except Exception as e:
            log_exception("Error initializing ChaptersForm", e)
```

##### 6.5.3.4 form_characters.py

```python
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from gui.widgets.form_toolbar import FormToolbar
from core.logger import log_section, log_subsection, log_info, log_exception

class CharactersForm(QWidget):
    def __init__(self, translator, parent=None):
        log_section("form_characters.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            layout = QVBoxLayout(self)

            # Toolbar mit "character"-Prefix
            self.toolbar = FormToolbar(self.translator, "character", self)
            layout.addWidget(self.toolbar)

            # Beispiel für ein Label mit standard_key
            self.title_label = QLabel(self.translator.tr("character_title"), self)
            layout.addWidget(self.title_label)

            # Weitere Felder/Labels nach Bedarf, immer mit standard_key
            self.name_label = QLabel(self.translator.tr("character_name"), self)
            layout.addWidget(self.name_label)

            self.setLayout(layout)
            log_info("CharactersForm initialized successfully.")
        except Exception as e:
            log_exception("Error initializing CharactersForm", e)
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
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QDateEdit, QSpinBox,
    QPushButton, QFileDialog, QHBoxLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from gui.widgets.form_toolbar import FormToolbar
from core.logger import log_section, log_subsection, log_info, log_exception

class ProjectForm(QWidget):
    def __init__(self, translator, parent=None):
        log_section("form_projects.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            # Hauptlayout horizontal: links Formular, rechts Bild
            main_layout = QHBoxLayout(self)

            # Linkes Layout für Formular
            form_layout = QVBoxLayout()
            self.toolbar = FormToolbar(self.translator, "project", self)
            form_layout.addWidget(self.toolbar)

            self.heading_label = QLabel(self.translator.tr("project_window_title"), self)
            form_layout.addWidget(self.heading_label)

            self.title_label = QLabel(self.translator.tr("project_title"), self)
            form_layout.addWidget(self.title_label)
            self.title_edit = QLineEdit(self)
            form_layout.addWidget(self.title_edit)

            self.subtitle_label = QLabel(self.translator.tr("project_detail_subtitle"), self)
            form_layout.addWidget(self.subtitle_label)
            self.subtitle_edit = QLineEdit(self)
            form_layout.addWidget(self.subtitle_edit)

            self.author_label = QLabel(self.translator.tr("project_detail_author"), self)
            form_layout.addWidget(self.author_label)
            self.author_edit = QLineEdit(self)
            form_layout.addWidget(self.author_edit)

            self.genre_label = QLabel(self.translator.tr("project_detail_genre"), self)
            form_layout.addWidget(self.genre_label)
            self.genre_edit = QLineEdit(self)
            form_layout.addWidget(self.genre_edit)

            self.cover_label = QLabel(self.translator.tr("project_detail_cover_image"), self)
            form_layout.addWidget(self.cover_label)
            cover_path_layout = QHBoxLayout()
            self.cover_edit = QLineEdit(self)
            cover_path_layout.addWidget(self.cover_edit)
            self.cover_btn = QPushButton(self.translator.tr("project_detail_cover_image") + " ...", self)
            self.cover_btn.clicked.connect(self._load_cover_image)
            cover_path_layout.addWidget(self.cover_btn)
            form_layout.addLayout(cover_path_layout)

            self.start_date_label = QLabel(self.translator.tr("project_start_date"), self)
            form_layout.addWidget(self.start_date_label)
            self.start_date_edit = QDateEdit(self)
            form_layout.addWidget(self.start_date_edit)

            self.deadline_label = QLabel(self.translator.tr("project_deadline"), self)
            form_layout.addWidget(self.deadline_label)
            self.deadline_edit = QDateEdit(self)
            form_layout.addWidget(self.deadline_edit)

            self.words_goal_label = QLabel(self.translator.tr("project_words_count_goal"), self)
            form_layout.addWidget(self.words_goal_label)
            self.words_goal_spin = QSpinBox(self)
            self.words_goal_spin.setMaximum(1000000)
            form_layout.addWidget(self.words_goal_spin)

            self.narrative_label = QLabel(self.translator.tr("project_detail_narrative_perspective"), self)
            form_layout.addWidget(self.narrative_label)
            self.narrative_edit = QLineEdit(self)
            form_layout.addWidget(self.narrative_edit)

            self.premise_label = QLabel(self.translator.tr("project_detail_premise"), self)
            form_layout.addWidget(self.premise_label)
            self.premise_edit = QLineEdit(self)
            form_layout.addWidget(self.premise_edit)

            self.target_group_label = QLabel(self.translator.tr("project_detail_target_group"), self)
            form_layout.addWidget(self.target_group_label)
            self.target_group_edit = QLineEdit(self)
            form_layout.addWidget(self.target_group_edit)

            # Rechtes Layout für Bild
            image_layout = QVBoxLayout()
            image_layout.addStretch()
            self.cover_pixmap_label = QLabel(self)
            self.cover_pixmap_label.setFixedSize(300, 300)
            self.cover_pixmap_label.setScaledContents(True)
            image_layout.addWidget(self.cover_pixmap_label)
            image_layout.addStretch()

            # Layouts ins Hauptlayout einfügen
            main_layout.addLayout(form_layout, stretch=3)
            main_layout.addLayout(image_layout, stretch=1)

            self.setLayout(main_layout)
            log_info("ProjectForm initialized successfully.")
        except Exception as e:
            log_exception("Error initializing ProjectForm", e)

    def _load_cover_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, self.translator.tr("project_detail_cover_image"),
            "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if file_path:
            self.cover_edit.setText(file_path)
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
                self.cover_pixmap_label.setPixmap(pixmap.scaled(
                    self.cover_pixmap_label.size(),
                    Qt.KeepAspectRatio
                ))
            else:
                self.cover_pixmap_label.clear()
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
            self.setWindowTitle(self.translator.tr("window_start_title"))
            self.resize(self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT)
            self.setAutoFillBackground(False)
            self.bg_pixmap = QPixmap(str(BG_IMAGE_PATH))
            self.pref_window = None
            self._create_ui()
            self._retranslate_and_position()
            help_text = self.translator.help_text("help_new_project")
            self.help_panel = HelpPanel(help_text, self)
            log_info("StartWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing StartWindow", e)

    def _create_ui(self):
        log_subsection("_create_ui")
        try:
            # Standard-Keys für die Buttons gemäß translator.py
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
            self.setWindowTitle(self.translator.tr("window_start_title"))
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
from core.logger import log_section, log_subsection, log_info, log_exception

class PreferencesWindow(QDialog):
    def __init__(self, parent=None):
        log_section("preferences.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = parent.translator if parent and hasattr(parent, "translator") else Translator()
            self.setWindowTitle(self.translator.tr("preference_title"))
            self.settings = load_settings()
            self._init_ui()
            log_info("PreferencesWindow initialized successfully.")
        except Exception as e:
            log_exception("Error initializing PreferencesWindow", e)

    def _init_ui(self):
        log_subsection("_init_ui")
        try:
            layout = QVBoxLayout(self)

            # Sprache
            lang_label = QLabel(self.translator.tr("preference_language"), self)
            self.lang_combo = QComboBox(self)
            self.lang_combo.addItems(["de", "en", "es"])
            self.lang_combo.setCurrentText(self.settings.get("language", "de"))
            layout.addWidget(lang_label)
            layout.addWidget(self.lang_combo)

            # Theme
            theme_label = QLabel(self.translator.tr("preference_theme"), self)
            self.theme_combo = QComboBox(self)
            self.theme_combo.addItems(["modern", "vintage"])
            self.theme_combo.setCurrentText(self.settings.get("style", "modern"))
            layout.addWidget(theme_label)
            layout.addWidget(self.theme_combo)

            # Buttons
            btn_layout = QHBoxLayout()
            self.save_btn = QPushButton(self.translator.tr("preference_save"), self)
            self.cancel_btn = QPushButton(self.translator.tr("preference_cancel"), self)
            btn_layout.addWidget(self.save_btn)
            btn_layout.addWidget(self.cancel_btn)
            layout.addLayout(btn_layout)

            self.setLayout(layout)

            self.save_btn.clicked.connect(self._on_save)
            self.cancel_btn.clicked.connect(self._on_cancel)
            self.lang_combo.currentTextChanged.connect(self._on_language_changed)
            self.theme_combo.currentTextChanged.connect(self._on_theme_changed)
            log_info("UI initialized successfully.")
        except Exception as e:
            log_exception("Error initializing UI in PreferencesWindow", e)

    def _on_save(self):
        log_subsection("_on_save")
        try:
            self.settings["language"] = self.lang_combo.currentText()
            self.settings["style"] = self.theme_combo.currentText()
            save_settings(self.settings)
            self.accept()
            log_info("Settings saved and dialog accepted.")
        except Exception as e:
            log_exception("Error saving settings in PreferencesWindow", e)

    def _on_cancel(self):
        log_subsection("_on_cancel")
        try:
            self.reject()
            log_info("Dialog canceled and language reverted.")
        except Exception as e:
            log_exception("Error canceling PreferencesWindow", e)

    def _on_language_changed(self, code):
        log_subsection("_on_language_changed")
        try:
            self.translator.set_language(code)
            self.setWindowTitle(self.translator.tr("preference_title"))
            log_info(f"Language changed to {code}.")
        except Exception as e:
            log_exception("Error changing language in PreferencesWindow", e)

    def _on_theme_changed(self, theme):
        log_subsection("_on_theme_changed")
        try:
            # Theme-Änderung kann hier verarbeitet werden, falls nötig
            log_info(f"Theme changed to {theme}.")
        except Exception as e:
            log_exception("Error changing theme in PreferencesWindow", e)
```

##### 6.5.4.3 project_window.py

```python
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSplitter, QHBoxLayout

from gui.styles.form_styles import load_button_style, load_active_button_style
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

from core.logger import log_section, log_subsection, log_info, log_exception

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
            self.setWindowTitle(self.translator.tr("project_title"))
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
            # Standard-Keys für die Navigation gemäß translator.py
            keys = [
                "project_btn_project", "project_btn_characters", "project_btn_storylines",
                "project_btn_chapters", "project_btn_scenes", "project_btn_objects", "project_btn_locations", "project_btn_exit"
            ]
            callbacks = {
                "project_btn_project": lambda: self._on_nav_clicked("project_btn_project", self._show_project_form),
                "project_btn_characters": lambda: self._on_nav_clicked("project_btn_characters", self._show_characters_form),
                "project_btn_storylines": lambda: self._on_nav_clicked("project_btn_storylines", self._show_storylines_form),
                "project_btn_chapters": lambda: self._on_nav_clicked("project_btn_chapters", self._show_chapters_form),
                "project_btn_scenes": lambda: self._on_nav_clicked("project_btn_scenes", self._show_scenes_form),
                "project_btn_objects": lambda: self._on_nav_clicked("project_btn_objects", self._show_objects_form),
                "project_btn_locations": lambda: self._on_nav_clicked("project_btn_locations", self._show_locations_form),
                "project_btn_exit": self._exit_application
            }
            self.navigation_panel = NavigationPanel(
                keys, self.translator, self, callbacks
            )

            help_text = self.translator.help_text("help_new_project")
            self.help_panel = HelpPanel(help_text, self)
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
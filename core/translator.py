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
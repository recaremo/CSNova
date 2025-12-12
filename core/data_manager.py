"""
Datenverwaltungs-Module für CSNova.

Dieses Modul enthält:
- DataManager (Basis-Klasse für alle Datenmanager)
- Spezialisierte Manager-Klassen für verschiedene Datentypen
"""

import json
import copy
from pathlib import Path
from typing import Dict, List, Any, Optional
from core.references import validate_reference, check_duplicate_references
from core.logger import log_info, log_error


class DataManager:
    """Basis-Manager für die Verwaltung von JSON-Daten."""
    
    def __init__(self, data_path: str, default_template: Dict[str, Any]):
        """
        Initialisiert den DataManager.
        
        Args:
            data_path (str): Pfad zur JSON-Datei
            default_template (dict): Standard-Template für neue Einträge
        """
        self.data_path = Path(data_path)
        self.data = {}
        self.default_template = default_template
    
    def ensure_structure(self) -> bool:
        """Stellt sicher, dass die Datei existiert und korrekt strukturiert ist."""
        try:
            self.data_path.parent.mkdir(parents=True, exist_ok=True)
            
            if not self.data_path.exists():
                self._initialize_default_structure()
                log_info(f"✓ {self.data_path.name} erstellt")
            else:
                self.load()
                self.auto_complete_keys()
            
            return True
        except Exception as e:
            log_error(f"Fehler beim Sicherstellen der Struktur für {self.data_path.name}: {e}")
            return False
    
    def _initialize_default_structure(self) -> None:
        """Erstellt die Standard-Dateistruktur basierend auf dem Template."""
        self.data = {}
        self.save()
    
    def load(self) -> bool:
        """Lädt alle Daten aus der JSON-Datei."""
        try:
            if not self.data_path.exists():
                self.data = {}
                return False
            
            with open(self.data_path, 'r', encoding='utf-8') as f:
                file_data = json.load(f)
            
            # Unterscheide zwischen verschiedenen Datenstrukturen
            if isinstance(file_data, dict) and "references" in file_data:
                # Spezial-Format für References (Array-basiert)
                self.data = {ref["id"]: ref for ref in file_data.get("references", []) if "id" in ref}
            else:
                # Standard-Format (Dictionary-basiert)
                self.data = file_data if isinstance(file_data, dict) else {}
            
            return True
        except Exception as e:
            log_error(f"Fehler beim Laden von {self.data_path.name}: {e}")
            return False
    
    def save(self) -> bool:
        """Speichert alle Daten in die JSON-Datei."""
        try:
            if self.data_path.name == "data_references.json":
                data_to_save = {"references": list(self.data.values())}
            else:
                data_to_save = self.data
            
            with open(self.data_path, 'w', encoding='utf-8') as f:
                json.dump(data_to_save, f, ensure_ascii=False, indent=4)
            
            return True
        except Exception as e:
            log_error(f"Fehler beim Speichern von {self.data_path.name}: {e}")
            return False
    
    def auto_complete_keys(self) -> None:
        """Fügt fehlende Keys zu vorhandenen Einträgen basierend auf Template hinzu."""
        try:
            modified = False
            for entry_id, entry in self.data.items():
                if isinstance(entry, dict):
                    for key, default_value in self.default_template.items():
                        if key not in entry:
                            if isinstance(default_value, (dict, list)):
                                entry[key] = copy.deepcopy(default_value)
                            else:
                                entry[key] = default_value
                            modified = True
            
            if modified and self.data:
                self.save()
        except Exception as e:
            log_error(f"Fehler beim Auto-Complete für {self.data_path.name}: {e}")
    
    def get_all(self) -> Dict[str, Dict]:
        """Gibt alle Daten zurück."""
        return self.data
    
    def get(self, entry_id: str) -> Optional[Dict]:
        """Ruft einen Eintrag anhand seiner ID ab."""
        return self.data.get(entry_id)
    
    def add(self, entry: Dict, entry_id: Optional[str] = None) -> Optional[str]:
        """Fügt einen neuen Eintrag hinzu."""
        try:
            if entry_id is None:
                entry_id = self._generate_next_id()
            
            entry["id"] = entry_id
            self.data[entry_id] = entry
            self.save()
            return entry_id
        except Exception as e:
            log_error(f"Fehler beim Hinzufügen eines Eintrags zu {self.data_path.name}: {e}")
            return None
    
    def delete(self, entry_id: str) -> bool:
        """Löscht einen Eintrag."""
        try:
            if entry_id in self.data:
                del self.data[entry_id]
                self.save()
                return True
            return False
        except Exception as e:
            log_error(f"Fehler beim Löschen aus {self.data_path.name}: {e}")
            return False
    
    def _generate_next_id(self) -> str:
        """Generiert eine eindeutige neue ID."""
        if not self.data:
            return "ID_01"
        
        max_num = 0
        for key in self.data.keys():
            try:
                parts = str(key).split('_')
                if len(parts) > 1 and parts[-1].isdigit():
                    num = int(parts[-1])
                    max_num = max(max_num, num)
            except (ValueError, IndexError):
                pass
        
        return f"ID_{max_num + 1:02d}"


class ReferenceManager(DataManager):
    """Spezialisierter Manager für Referenzen (Fachliteratur)."""
    
    DEFAULT_TEMPLATE = {
        "id": "", "type": "", "title": "", "subtitle": "", "chapter_title": "",
        "authors": [{"firstname": "", "name": "", "initial": ""}],
        "editors": [{"firstname": "", "name": "", "initial": ""}],
        "publisher": "", "place": "", "year": "", "edition": "", "volume": "",
        "issue": "", "pages": "", "journal": "", "isbn": "", "issn": "",
        "doi": "", "url": "", "access_date": "", "conference_name": "",
        "conference_location": "", "conference_date": "", "institution": "",
        "degree_type": "", "newspaper": "", "medium": "", "series": "",
        "translator": "", "language": "", "keywords": [], "abstract": "", "notes": ""
    }
    
    def __init__(self, data_path: str = "data/references/data_references.json"):
        super().__init__(data_path, self.DEFAULT_TEMPLATE)
    
    def validate_all(self) -> Dict[str, List[str]]:
        """Validiert alle Referenzen auf Pflichtfelder."""
        validation_errors = {}
        for ref_id, reference in self.data.items():
            errors = validate_reference(reference)
            if errors:
                validation_errors[ref_id] = errors
        return validation_errors
    
    def check_duplicates(self) -> List[Dict]:
        """Prüft auf doppelte Referenzen."""
        refs_list = list(self.data.values())
        return check_duplicate_references(refs_list)


class ProjectManager(DataManager):
    """Spezialisierter Manager für Projekte."""
    
    DEFAULT_TEMPLATE = {
        "project_ID": "", "project_title": "", "project_subtitle": "", "project_author": "",
        "project_premise": "", "project_target_group": 0, "project_narrative_perspective": 0,
        "project_style": 0, "project_genre": 0, "project_work_type": 0, "project_motif": 0,
        "project_begin_date": "", "project_deadline": "", "project_status": 0,
        "project_word_goal": 0, "project_cover_image": "", "project_data_file": "",
        "project_notes": "", "project_publisher": 0, "project_editor": 0,
        "project_isbn": "", "project_issn": ""
    }
    
    def __init__(self, data_path: str = "data/projects/data_projects.json"):
        super().__init__(data_path, self.DEFAULT_TEMPLATE)


class CharacterManager(DataManager):
    """Spezialisierter Manager für Charaktere."""
    
    DEFAULT_TEMPLATE = {
        "character_ID": "", "character_name": "", "character_firstname": "", "character_nickname": "",
        "character_birthdate": "", "character_died": "", "character_gender": 0, "character_sexOrientation": 0,
        "character_role": 0, "character_group": 0, "character_development": "", "character_notes": "",
        "character_image": "", "character_images": [], "character_mother": "", "character_father": "",
        "character_referencePerson": "", "character_siblings": "", "character_placeOfBirth": "",
        "character_country": "", "character_ethnicity": "", "character_ancestryNotes": "",
        "character_school": "", "character_university": "", "character_vocationalTraining": "",
        "character_profession": "", "character_artMusic": "", "character_sports": "", "character_technology": "",
        "character_autodidact": "", "character_educationNotes": "", "character_positiveCharacteristics": "",
        "character_negativeCharacteristics": "", "character_fears": "", "character_weaknesses": "",
        "character_strengths": "", "character_talents": "", "character_beliefs": "", "character_lifeGoals": "",
        "character_motivation": "", "character_behavior": "", "character_personalityNotes": "",
        "character_height": 0, "character_bodyType": 0, "character_stature": 0, "character_faceshape": 0,
        "character_eyeshape": 0, "character_eyesColor": "", "character_hair": "", "character_hairColor": "",
        "character_skinType": "", "character_skinColor": "", "character_charisma": "", "character_specialFeatures": "",
        "character_lookNotes": "", "character_head": "", "character_neck": "", "character_breast": "",
        "character_back": "", "character_shoulder": "", "character_upperarm": "", "character_elbow": "",
        "character_lowerarm": "", "character_wrist": "", "character_hand": "", "character_finger": "",
        "character_hips": "", "character_buttocks": "", "character_upperleg": "", "character_knee": "",
        "character_lowerleg": "", "character_ankle": "", "character_foot": "", "character_toe": "",
        "character_bodyNotes": "", "character_diagnoses": "", "character_symptoms": "", "character_therapies": "",
        "character_medications": "", "character_temperament": "", "character_ethicValues": "", "character_moralValues": "",
        "character_strengthsOfCharacter": "", "character_weaknessesOfCharacter": "", "character_selfimage": "",
        "character_humor": "", "character_aggressiveness": "", "character_traumas": "", "character_Impressions": "",
        "character_socialization": "", "character_norms": "", "character_taboos": "", "character_psycheNotes": "",
        "character_status": 0, "character_mainCharacter": False
    }
    
    def __init__(self, data_path: str = "data/characters/data_characters.json"):
        super().__init__(data_path, self.DEFAULT_TEMPLATE)
    
    def get_main_characters(self) -> Dict[str, Dict]:
        """Gibt nur Hauptcharaktere zurück."""
        return {k: v for k, v in self.data.items() if v.get("character_mainCharacter", False)}


class LocationManager(DataManager):
    """Spezialisierter Manager für Schauplätze."""
    
    DEFAULT_TEMPLATE = {
        "location_ID": "", "location_title": "", "location_status": 0,
        "location_created": "", "location_modified": "", "location_notes": "", "location_titel": ""
    }
    
    def __init__(self, data_path: str = "data/locations/data_locations.json"):
        super().__init__(data_path, self.DEFAULT_TEMPLATE)


class ObjectManager(DataManager):
    """Spezialisierter Manager für Objekte."""
    
    DEFAULT_TEMPLATE = {
        "object_ID": "", "object_title": "", "object_status": 0,
        "object_created": "", "object_modified": "", "object_notes": ""
    }
    
    def __init__(self, data_path: str = "data/objects/data_objects.json"):
        super().__init__(data_path, self.DEFAULT_TEMPLATE)


class StorylineManager(DataManager):
    """Spezialisierter Manager für Handlungsstränge."""
    
    DEFAULT_TEMPLATE = {
        "storyline_ID": "", "storyline_title": "", "storyline_status": 0,
        "storyline_created": "", "storyline_modified": "", "storyline_notes": "", "storyline_titel": ""
    }
    
    def __init__(self, data_path: str = "data/storylines/data_storylines.json"):
        super().__init__(data_path, self.DEFAULT_TEMPLATE)


class IdeaManager(DataManager):
    """Spezialisierter Manager für Ideen."""
    
    DEFAULT_TEMPLATE = {"title": "", "description": ""}
    
    def __init__(self, data_path: str = "data/Ideas/data_ideas.json"):
        super().__init__(data_path, self.DEFAULT_TEMPLATE)


class ChapterManager(DataManager):
    """Spezialisierter Manager für Kapitel und Szenen."""
    
    DEFAULT_TEMPLATE = {
        "chapter_id": "", "chapter_title": "", "chapter_premise": "", "chapter_status": "",
        "chapter_begin": "", "chapter_edited": "", "chapter_excerpt": "", "chapter_notes": ""
    }
    
    def __init__(self, data_path: str = "data/chapters/data_project_00.json"):
        super().__init__(data_path, self.DEFAULT_TEMPLATE)


class CitationManager:
    """Verwaltet die Zitierformate und deren Definitionen."""
    
    def __init__(self, formats_path: str = "data/references/references.json"):
        """Initialisiert den CitationManager."""
        self.formats_path = Path(formats_path)
        self.formats = {}
    
    def load(self) -> bool:
        """Lädt alle Zitierformat-Definitionen."""
        try:
            if not self.formats_path.exists():
                log_error(f"Zitierformate nicht gefunden: {self.formats_path}")
                return False
            
            with open(self.formats_path, 'r', encoding='utf-8') as f:
                self.formats = json.load(f)
            
            return len(self.formats) > 0
        except Exception as e:
            log_error(f"Fehler beim Laden der Zitierformate: {e}")
            return False
    
    def get_citation(self, reference: Dict, format_style: str = "APA") -> str:
        """Generiert ein formatiertes Zitat."""
        from core.references import generate_citation
        return generate_citation(reference, format_style, self.formats)
    
    def list_supported_formats(self) -> List[str]:
        """Listet alle verfügbaren Zitierformate auf."""
        return list(self.formats.keys())
    
    def get_format_definition(self, format_style: str) -> Optional[Dict]:
        """Ruft die Definition eines Zitierformats ab."""
        return self.formats.get(format_style)

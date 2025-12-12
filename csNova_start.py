# csNova_main.py soll gestartet werden
import os
import json
import sys
from pathlib import Path

# Eigene Module
from core.data_manager import (
    ReferenceManager, ProjectManager, CharacterManager, LocationManager,
    ObjectManager, StorylineManager, IdeaManager, ChapterManager, CitationManager
)
from core.references import validate_reference, check_duplicate_references
from core.logger import log_info, log_error, log_header


def initialize_all_managers():
    """
    Initialisiert alle Daten-Manager für CSNova.
    
    Returns:
        dict: Dictionary mit allen Manager-Instanzen oder None bei Fehler
    """
    log_header()
    log_info("Initialisiere alle Daten-Manager")
    
    managers = {}
    
    try:
        # ========== REFERENZEN ==========
        log_info("\n--- Referenzen ---")
        ref_manager = ReferenceManager("data/references/data_references.json")
        
        log_info("Stelle Referenzdaten-Struktur sicher...")
        if not ref_manager.ensure_structure():
            log_error("Konnte Referenzdaten-Struktur nicht erstellen")
            return None
        log_info("✓ Referenzdaten-Struktur OK")
        
        log_info("Lade Referenzen...")
        if not ref_manager.load():
            log_error("Konnte Referenzen nicht laden")
            return None
        log_info(f"✓ {len(ref_manager.get_all())} Referenzen geladen")
        
        log_info("Validiere Referenzen...")
        validation_errors = ref_manager.validate_all()
        if validation_errors:
            log_info(f"⚠ {len(validation_errors)} Referenz(en) mit Validierungsfehlern")
        else:
            log_info("✓ Alle Referenzen validiert")
        
        log_info("Prüfe auf doppelte Referenzen...")
        duplicates = ref_manager.check_duplicates()
        if duplicates:
            log_info(f"⚠ {len(duplicates)} Duplikat(e) gefunden")
        else:
            log_info("✓ Keine Duplikate gefunden")
        
        managers["references"] = ref_manager
        
        # ========== ZITIERFORMATE ==========
        log_info("\n--- Zitierformate ---")
        cite_manager = CitationManager("data/references/references.json")
        
        if not cite_manager.load():
            log_error("Konnte Zitierformate nicht laden")
            return None
        
        supported_formats = cite_manager.list_supported_formats()
        log_info(f"✓ {len(supported_formats)} Zitierformate verfügbar")
        managers["citations"] = cite_manager
        
        # ========== PROJEKTE ==========
        log_info("\n--- Projekte ---")
        project_manager = ProjectManager("data/projects/data_projects.json")
        if project_manager.ensure_structure():
            project_manager.load()
            log_info(f"✓ {len(project_manager.get_all())} Projekte geladen")
            managers["projects"] = project_manager
        else:
            log_error("Konnte Projektstruktur nicht erstellen")
        
        # ========== CHARAKTERE ==========
        log_info("\n--- Charaktere ---")
        character_manager = CharacterManager("data/characters/data_characters.json")
        if character_manager.ensure_structure():
            character_manager.load()
            log_info(f"✓ {len(character_manager.get_all())} Charaktere geladen")
            managers["characters"] = character_manager
        else:
            log_error("Konnte Charakterstruktur nicht erstellen")
        
        # ========== SCHAUPLÄTZE ==========
        log_info("\n--- Schauplätze ---")
        location_manager = LocationManager("data/locations/data_locations.json")
        if location_manager.ensure_structure():
            location_manager.load()
            log_info(f"✓ {len(location_manager.get_all())} Schauplätze geladen")
            managers["locations"] = location_manager
        else:
            log_error("Konnte Schauplatz-Struktur nicht erstellen")
        
        # ========== OBJEKTE ==========
        log_info("\n--- Objekte ---")
        object_manager = ObjectManager("data/objects/data_objects.json")
        if object_manager.ensure_structure():
            object_manager.load()
            log_info(f"✓ {len(object_manager.get_all())} Objekte geladen")
            managers["objects"] = object_manager
        else:
            log_error("Konnte Objekt-Struktur nicht erstellen")
        
        # ========== HANDLUNGSSTRÄNGE ==========
        log_info("\n--- Handlungsstränge ---")
        storyline_manager = StorylineManager("data/storylines/data_storylines.json")
        if storyline_manager.ensure_structure():
            storyline_manager.load()
            log_info(f"✓ {len(storyline_manager.get_all())} Handlungsstränge geladen")
            managers["storylines"] = storyline_manager
        else:
            log_error("Konnte Handlungsstrang-Struktur nicht erstellen")
        
        # ========== IDEEN ==========
        log_info("\n--- Ideen ---")
        idea_manager = IdeaManager("data/Ideas/data_ideas.json")
        if idea_manager.ensure_structure():
            idea_manager.load()
            log_info(f"✓ {len(idea_manager.get_all())} Ideen geladen")
            managers["ideas"] = idea_manager
        else:
            log_error("Konnte Ideen-Struktur nicht erstellen")
        
        # ========== KAPITEL & SZENEN ==========
        log_info("\n--- Kapitel & Szenen ---")
        chapter_manager = ChapterManager("data/chapters/data_project_00.json")
        if chapter_manager.ensure_structure():
            chapter_manager.load()
            log_info(f"✓ {len(chapter_manager.get_all())} Kapitel geladen")
            managers["chapters"] = chapter_manager
        else:
            log_error("Konnte Kapitel-Struktur nicht erstellen")
        
        log_info("\n✓ Alle Daten-Manager erfolgreich initialisiert")
        return managers
        
    except Exception as e:
        log_error(f"Fehler bei Initialisierung der Daten-Manager: {e}")
        import traceback
        traceback.print_exc()
        return None


# Hauptprogramm starten
if __name__ == "__main__":
    log_header()
    log_info("CSNova Start")
    log_info(f"Python Version: {sys.version}")
    log_info(f"Arbeitsverzeichnis: {Path.cwd()}")
    
    # Initialisiere alle Manager
    managers = initialize_all_managers()
    
    if managers is None:
        log_error("Konnte Daten-Manager nicht initialisieren. Beende Anwendung.")
        sys.exit(1)
    
    log_info("Starte CSNova Hauptanwendung...")
    # Importiere und starte csNova_main
    import csNova_main
    csNova_main.main(managers)

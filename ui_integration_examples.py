"""
Beispiel UI-Integrations-Code für CSNova Manager

Dieses Modul zeigt, wie bestehende UI-Funktionen aktualisiert werden,
um die neuen Manager zu nutzen.
"""

# BEISPIEL 1: Referenzen anzeigen (aus show_references_window)
def load_references_list():
    """Lädt Referenzenliste in die UI."""
    from csNova_main import app_state
    from core.logger import log_info, log_error
    
    try:
        ref_manager = app_state.references
        if ref_manager is None:
            log_error("ReferenceManager nicht verfügbar")
            return []
        
        all_refs = ref_manager.get_all()
        
        # Konvertiere zu Liste für UI-Anzeige
        ref_list = []
        for ref_id, ref in all_refs.items():
            ref_list.append({
                "id": ref_id,
                "title": ref.get("title", "Untitled"),
                "authors": ", ".join([f"{a.get('name', '')} {a.get('firstname', '')}".strip() 
                                     for a in ref.get("authors", [])]),
                "year": ref.get("year", ""),
                "type": ref.get("type", "")
            })
        
        log_info(f"✓ {len(ref_list)} Referenzen geladen")
        return ref_list
    
    except Exception as e:
        log_error(f"Fehler beim Laden der Referenzen: {e}")
        return []


# BEISPIEL 2: Charaktere mit Filtering
def load_characters_filtered(filter_name="", main_only=False):
    """Lädt Charaktere mit optionalem Filter."""
    from csNova_main import app_state
    from core.logger import log_info, log_error
    
    try:
        char_manager = app_state.characters
        if char_manager is None:
            log_error("CharacterManager nicht verfügbar")
            return []
        
        # Hole alle oder nur Hauptcharaktere
        if main_only:
            characters = char_manager.get_main_characters()
        else:
            characters = char_manager.get_all()
        
        # Filter nach Name
        char_list = []
        for char_id, char in characters.items():
            name = char.get("character_name", "")
            
            if filter_name and filter_name.lower() not in name.lower():
                continue
            
            char_list.append({
                "id": char_id,
                "name": name,
                "firstname": char.get("character_firstname", ""),
                "role": char.get("character_role", 0),
                "main": char.get("character_mainCharacter", False)
            })
        
        log_info(f"✓ {len(char_list)} Charaktere geladen (Filter: {filter_name or 'keine'})")
        return char_list
    
    except Exception as e:
        log_error(f"Fehler beim Laden der Charaktere: {e}")
        return []


# BEISPIEL 3: Neue Referenz speichern
def save_reference_from_form(form_data):
    """Speichert eine neue Referenz aus dem Formular."""
    from csNova_main import app_state
    from core.logger import log_info, log_error
    
    try:
        ref_manager = app_state.references
        if ref_manager is None:
            log_error("ReferenceManager nicht verfügbar")
            return None
        
        # Baue Referenz-Dictionary aus Formular-Daten
        new_ref = {
            "type": form_data.get("ref_type", "book"),
            "title": form_data.get("title", ""),
            "subtitle": form_data.get("subtitle", ""),
            "authors": form_data.get("authors", []),
            "year": form_data.get("year", ""),
            "publisher": form_data.get("publisher", ""),
            "isbn": form_data.get("isbn", ""),
            "pages": form_data.get("pages", ""),
            "keywords": form_data.get("keywords", []),
            "abstract": form_data.get("abstract", ""),
            "notes": form_data.get("notes", "")
        }
        
        # Füge hinzu
        ref_id = ref_manager.add(new_ref)
        
        if ref_id:
            log_info(f"✓ Referenz {ref_id} gespeichert")
            return ref_id
        else:
            log_error("Konnte Referenz nicht speichern")
            return None
    
    except Exception as e:
        log_error(f"Fehler beim Speichern der Referenz: {e}")
        return None


# BEISPIEL 4: Projekt aktualisieren
def update_project_from_form(project_id, form_data):
    """Aktualisiert ein existierendes Projekt."""
    from csNova_main import app_state
    from core.logger import log_info, log_error
    
    try:
        proj_manager = app_state.projects
        if proj_manager is None:
            log_error("ProjectManager nicht verfügbar")
            return False
        
        # Hole aktuelles Projekt
        project = proj_manager.get(project_id)
        if not project:
            log_error(f"Projekt {project_id} nicht gefunden")
            return False
        
        # Aktualisiere Felder
        project.update({
            "project_title": form_data.get("title", ""),
            "project_subtitle": form_data.get("subtitle", ""),
            "project_author": form_data.get("author", ""),
            "project_premise": form_data.get("premise", ""),
            "project_status": form_data.get("status", 0),
            "project_word_goal": form_data.get("word_goal", 0),
            "project_notes": form_data.get("notes", "")
        })
        
        # Speichere
        proj_manager.data[project_id] = project
        proj_manager.save()
        
        log_info(f"✓ Projekt {project_id} aktualisiert")
        return True
    
    except Exception as e:
        log_error(f"Fehler beim Aktualisieren des Projekts: {e}")
        return False


# BEISPIEL 5: Charakter löschen mit Bestätigung
def delete_character_safe(char_id, confirm_callback=None):
    """Löscht einen Charakter mit optionaler Bestätigung."""
    from csNova_main import app_state
    from core.logger import log_info, log_error
    
    try:
        char_manager = app_state.characters
        if char_manager is None:
            log_error("CharacterManager nicht verfügbar")
            return False
        
        # Hole Charakter-Info für Bestätigung
        character = char_manager.get(char_id)
        if not character:
            log_error(f"Charakter {char_id} nicht gefunden")
            return False
        
        char_name = character.get("character_name", "Unknown")
        
        # Optionale Bestätigung
        if confirm_callback and not confirm_callback(f"Charakter '{char_name}' wirklich löschen?"):
            log_info("Löschung abgebrochen")
            return False
        
        # Lösche
        success = char_manager.delete(char_id)
        if success:
            log_info(f"✓ Charakter '{char_name}' gelöscht")
        else:
            log_error(f"Konnte Charakter {char_id} nicht löschen")
        
        return success
    
    except Exception as e:
        log_error(f"Fehler beim Löschen des Charakters: {e}")
        return False


# BEISPIEL 6: Zitate generieren
def generate_all_citations(ref_id, formats=None):
    """Generiert Zitate in verschiedenen Formaten."""
    from csNova_main import app_state
    from core.logger import log_info, log_error
    
    try:
        ref_manager = app_state.references
        cite_manager = app_state.citations
        
        if not ref_manager or not cite_manager:
            log_error("Manager nicht verfügbar")
            return {}
        
        reference = ref_manager.get(ref_id)
        if not reference:
            log_error(f"Referenz {ref_id} nicht gefunden")
            return {}
        
        # Standard-Formate wenn nicht angegeben
        if formats is None:
            formats = cite_manager.list_supported_formats()
        
        citations = {}
        for fmt in formats:
            try:
                citation = cite_manager.get_citation(reference, fmt)
                citations[fmt] = citation
            except Exception as e:
                log_error(f"Fehler bei Format {fmt}: {e}")
                citations[fmt] = None
        
        log_info(f"✓ {len(citations)} Zitate generiert")
        return citations
    
    except Exception as e:
        log_error(f"Fehler beim Generieren der Zitate: {e}")
        return {}


# BEISPIEL 7: Suche über alle Manager
def search_across_managers(query):
    """Sucht eine Query in mehreren Managern."""
    from csNova_main import app_state
    from core.logger import log_info
    
    results = {
        "references": [],
        "characters": [],
        "projects": [],
        "locations": [],
        "objects": []
    }
    
    try:
        # Suche in Referenzen
        if app_state.references:
            for ref_id, ref in app_state.references.get_all().items():
                if query.lower() in ref.get("title", "").lower():
                    results["references"].append(ref_id)
        
        # Suche in Charakteren
        if app_state.characters:
            for char_id, char in app_state.characters.get_all().items():
                if query.lower() in char.get("character_name", "").lower():
                    results["characters"].append(char_id)
        
        # Suche in Projekten
        if app_state.projects:
            for proj_id, proj in app_state.projects.get_all().items():
                if query.lower() in proj.get("project_title", "").lower():
                    results["projects"].append(proj_id)
        
        # Suche in Schauplätzen
        if app_state.locations:
            for loc_id, loc in app_state.locations.get_all().items():
                if query.lower() in loc.get("location_title", "").lower():
                    results["locations"].append(loc_id)
        
        # Suche in Objekten
        if app_state.objects:
            for obj_id, obj in app_state.objects.get_all().items():
                if query.lower() in obj.get("object_title", "").lower():
                    results["objects"].append(obj_id)
        
        total = sum(len(v) for v in results.values())
        log_info(f"✓ Suche nach '{query}': {total} Ergebnisse gefunden")
        
        return results
    
    except Exception as e:
        log_error(f"Fehler bei der Suche: {e}")
        return results


if __name__ == "__main__":
    # Test-Beispiele (nur wenn direkt aufgerufen)
    print("✓ UI-Integration Beispiele geladen")
    print("  Verwende diese Funktionen in deinen UI-Modulen")

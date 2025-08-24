# database.py
import sqlite3
from config.dev import DB_PATH  
from core.tables.gender_data import data_gender
from core.tables.sex_orientation_data import sex_orientation_data

# Importiere die Tabellenmodule
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
    project,
    project_storylines,
    project_chapters,
    project_chapters_scenes,
    project_scenes_objects,
    project_scenes_places
)

def init_schema():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Fremdschlüssel aktivieren
    cursor.execute("PRAGMA foreign_keys = ON")

    # Tabellen initialisieren
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
        project,
        project_storylines,
        project_chapters,
        project_chapters_scenes,
        project_scenes_objects,
        project_scenes_places
    ]:
        module.create_table(cursor)
    
    # Seed-Daten einfügen
    data_gender(cursor)
    data_sex_orientation(cursor)

    conn.commit()
    conn.close()
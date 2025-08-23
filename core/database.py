# database.py
import sqlite3
from config.dev import DB_PATH  # falls du den Pfad dort definiert hast

# Importiere die Tabellenmodule
from tables.character_main import create_character_main_table
from tables.gender import create_gender_table
from tables.sex_orientation import create_sex_orientation_table
from tables.character_psychological_profile import create_character_psychological_profile_table
from tables.character_origin import create_character_origin_table  
from tables.character_personality import create_character_personality_table  
from tables.character_appearance_detail import create_character_appearance_detail_table  
from tables.character_education import create_character_education_table
from tables.character_appearance_main import create_character_appearance_main_table

def init_schema():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Fremdschlüssel aktivieren
    cursor.execute("PRAGMA foreign_keys = ON")

    # Tabellen initialisieren
    create_character_main_table(cursor)
    create_gender_table(cursor)
    create_sex_orientation_table(cursor)
    create_character_psychological_profile_table(cursor)
    create_character_origin_table(cursor)
    create_character_education_table(cursor)
    create_character_personality_table(cursor)
    create_character_appearance_main_table(cursor)
    create_character_appearance_detail_table(cursor)

    conn.commit()
    conn.close()
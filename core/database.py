import sqlite3
from config.dev import DB_PATH  # falls du den Pfad dort definiert hast

def init_schema():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Fremdschlüssel aktivieren
    cursor.execute("PRAGMA foreign_keys = ON")

    # Haupttabelle: character_main
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_main (
        character_ID INTEGER PRIMARY KEY AUTOINCREMENT,
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

    # Referenztabellen
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gender (
        gender_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        gender TEXT,
        short_description TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sex_orientation (
        sex_orientation_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        sex_orientation TEXT,
        short_description TEXT
    );
    """)

    # Untertabellen (Beispiel: psychological_profile)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS psychological_profile (
        profile_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER,
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
        fears TEXT,
        notes TEXT,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID)
    );
    """)

    # Weitere Tabellen hier ergänzen (origin, education, morphology, etc.)

    conn.commit()
    conn.close()

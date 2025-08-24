# character_main.py
# table: character_main
# description: base stats for a character
# access to the tables: gender.py, sex_orientation.py
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_main (
        character_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        main_character BOOL,
        group_member TEXT,
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
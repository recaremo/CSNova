# character_groups.py
# table: subtable for character_main
# description: character membership in a group
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_groups (
        groups_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_ID INTEGER NOT NULL,
        FOREIGN KEY(character_ID) REFERENCES character_main(character_ID),
        groups_title TEXT,
        groups_description TEXT
    );
    """)
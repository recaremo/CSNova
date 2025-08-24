# character_groups.py
# table: subtable for character_main
# description: character memberchip in a group
# connected with: character_main
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS character_groups (
        character_groups_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        character_groups_title TEXT,
        character_groups_description TEXT
    );
    """)
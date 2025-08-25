# project.py
# table: project
# description: central project database, main statistic of work done
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project (
        project_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_premise TEXT,
        words_count_goal INTEGER,
        words_count_days INTEGER,
        deadlines DATE,
        chapters INTEGER,
        scenes INTEGER,
        story_lines INTEGER,
        main_characters INTEGER,
        supporting_characters INTEGER,
        groups_characters INTEGER,
        story_places INTEGER,
        story_objects INTEGER,
        timeline TEXT
    );
    """)
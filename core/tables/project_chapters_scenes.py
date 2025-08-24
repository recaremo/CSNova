# project_chapter_scenes.py
# # table: project_chapter_scenes
# description: scenes inside a chapter
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_chapters_scenes (
        project_chapters_scenes_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_chapters_ID INTEGER NOT NULL,
        project_chapters_scenes_premise TEXT,
        project_chapters_scenes_titel TEXT,
        project_chapters_scenes_main_characters TEXT,
        project_chapters_scenes_supporting_character TEXT,
        project_chapters_scenes_places TEXT,
        project_chapters_scenes_text TEXT,
        FOREIGN KEY(project_chapters_ID) REFERENCES project_chapters(project_chapters_ID)
    );
    """)
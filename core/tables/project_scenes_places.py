# project_scenes_places.py
# table: project_scenes_places
# description: places can be used in different scenes
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_scenes_places (
        scenes_places_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_chapters_scenes_ID INTEGER,
        scenes_places_titel TEXT,
        scenes_places_description TEXT,
        FOREIGN KEY(project_chapters_scenes_ID ) REFERENCES  project_chapters_scenes (project_chapters_scenes_ID)
    );
    """)
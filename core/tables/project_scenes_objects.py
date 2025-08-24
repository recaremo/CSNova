# project_scenes_objects.py
# table: project_scenes_sobjects
# description: objects can be used in different scenes
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_scenes_objects (
        project_scenes_object_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_chapters_scenes_ID INTEGER,
        project_scenes_objects_titel TEXT,
        project_scenes_objects_description TEXT,
        FOREIGN KEY(project_chapters_scenes_ID ) REFERENCES  project_chapters_scenes (project_chapters_scenes_ID)
    );
    """)
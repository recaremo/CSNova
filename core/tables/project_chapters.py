# project_chapters.py
# # table: project_chapters
# description: chapters inside a project
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_chapters (
        project_chapter_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_ID INTEGER NOT NULL,
        project_chapters_premise TEXT,
        project_chapters_titel TEXT,
        FOREIGN KEY(project_ID) REFERENCES project(project_ID)
    );
    """)
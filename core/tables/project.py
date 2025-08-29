# project.py
# table: project
# description: central project database, main statistic of work done
# 
def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project (
        project_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        project_premise TEXT,
        project_title TEXT,
        project_subtitle TEXT,
        project_author TEXT,
        project_genre TEXT,
        project_cover_image TEXT,
        project_target_group TEXT,
        project_narrative_perspective TEXT,
        project_deadline DATE,
        project_start_date DATE,     
        project_words_count_goal INTEGER,
        project_words_count_days INTEGER,
        project_days_count INTEGER,  
        project_chapters INTEGER,
        project_scenes INTEGER,
        project_story_lines INTEGER,
        project_main_characters INTEGER,
        project_supporting_characters INTEGER,
        project_groups_characters INTEGER,
        project_story_places INTEGER,
        project_story_objects INTEGER,
        project_timeline TEXT
    );
    """)
import sqlite3

# Import central logging functions
from core.logger import log_section, log_subsection, log_info, log_error

# Import the central database path
from config.dev import DB_PATH

from core.tables.gender_data import data_gender
from core.tables.sex_orientation_data import sex_orientation_data

# Import tables (these should use central paths if needed)
from core.tables import (
    character_main,
    gender,
    sex_orientation,
    character_psychological_profile,
    character_origin,
    character_education,
    character_personality,
    character_appearance_main,
    character_appearance_detail,
    project,
    project_storylines,
    project_chapters,
    project_chapters_scenes,
    project_objects,
    project_locations,
    project_scene_object_map,
    project_scene_location_map,
    project_scene_storyline_map,
    project_scene_character_map,
    project_character_storyline_map,
    project_character_group_map
)

def init_schema():
    log_section("database.py")
    log_subsection("init_schema")
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            log_info("Database connection established.")
            # Enable foreign key support
            cursor.execute("PRAGMA foreign_keys = ON")
            log_info("Foreign key support enabled.")

            # Initialize tables
            for module in [
                character_main,
                gender,
                sex_orientation,
                character_psychological_profile,
                character_origin,
                character_education,
                character_personality,
                character_appearance_main,
                character_appearance_detail,
                project,
                project_storylines,
                project_chapters,
                project_chapters_scenes,
                project_objects,
                project_locations,
                project_scene_object_map,
                project_scene_location_map,
                project_scene_storyline_map,
                project_scene_character_map,
                project_character_storyline_map,
                project_character_group_map
            ]:
                module.create_table(cursor)
                log_info(f"Table created: {module.__name__}")

            # Insert seed data
            data_gender(cursor)
            log_info("Seed data for gender inserted.")
            sex_orientation_data(cursor)
            log_info("Seed data for sex orientation inserted.")
            conn.commit()
            log_info("Database schema initialized and committed successfully.")
    except Exception as e:
        log_error(f"An error occurred during database initialization: {e}")
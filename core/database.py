import sqlite3
from core.logger import log_section, log_subsection, log_info, log_exception
from config.dev import DB_PATH

from core.tables.gender_data import data_gender
from core.tables.sex_orientation_data import sex_orientation_data

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
    character_groups,
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
                character_groups,
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
                try:
                    module.create_table(cursor)
                    log_info(f"Table created: {module.__name__}")
                except Exception as e:
                    log_exception(f"Error creating table {module.__name__}", e)

            # Insert seed data
            try:
                data_gender(cursor)
                log_info("Seed data for gender inserted.")
            except Exception as e:
                log_exception("Error inserting gender seed data", e)
            try:
                sex_orientation_data(cursor)
                log_info("Seed data for sex orientation inserted.")
            except Exception as e:
                log_exception("Error inserting sex orientation seed data", e)

            conn.commit()
            log_info("Database schema initialized and committed successfully.")
    except Exception as e:
        log_exception("An error occurred during database initialization", e)
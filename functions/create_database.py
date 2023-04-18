import logging as log
from pathlib import Path
from typing import List, Tuple

import aiosqlite as sql


async def database_creation(folder_name: str = "database", name: str = "winston", enabled: bool = True) -> None:
    """
    Create a SQLite database with the specified name in the specified folder if enabled.

    Defaults:
        folder_name: Default set to database.

        name: Default set to winston.

        enabled: Default set to true.

    Args:
        folder_name: The name of the folder in which to create the database file.
        name: The name of the database file to create.
        enabled: Whether to enable or disable the creation of the database file.
    """
    log.getLogger(__name__)
    log.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', )

    if enabled:
        try:
            db_file = Path(f"{folder_name}/{name}.db")
            if not db_file.exists():
                db_file.parent.mkdir(parents=True, exist_ok=True)
                db_file.touch()

            async with sql.connect(str(db_file)) as conn:
                cursor = await conn.cursor()

                tables: List[Tuple[str]] = [("""CREATE TABLE IF NOT EXISTS main (
                         guild_id INT PRIMARY KEY,
                         dns_api_key TEXT
                         )""",), ("""CREATE TABLE IF NOT EXISTS nations (
                         nation_id INT PRIMARY KEY,
                         nation_name TEXT,
                         alliance TEXT,
                         alliance_id INT,
                         joining_date DATE,
                         infrastructure INT,
                         land INT,
                         popolation INT,
                         stability INT,
                         power INT,
                         education INT,
                         commerce INT,
                         transportation INT,
                         employment INT,
                         tech INT,
                         protection_time DATE,
                         totalslots INT,
                         political INT,
                         rare INT,
                         uranium INT
                         )""",), ("""CREATE TABLE IF NOT EXISTS registered (
                         discord_id INT PRIMARY KEY,
                         alliance TEXT,
                         alliance_id INT,
                         nation_id INT,
                         nation_name TEXT,
                         score INT,
                         joining_date DATE,
                         infrastructure INT,
                         land INT,
                         core_land INT,
                         non_core_land INT,
                         popolation INT,
                         projects INT,
                         stability INT,
                         war INT,
                         tech INT,
                         education INT,
                         commerce INT,
                         transportation INT,
                         employment INT,
                         power INT,
                         last_online DATE,
                         devastation INT,
                         protection_time DATE,
                         leader_name STR
                         )""",), ("""CREATE TABLE IF NOT EXISTS alliances (
                         alliance_id INT PRIMARY KEY,
                         alliance_name TEXT,
                         leader_name TEXT,
                         member_counts INT,
                         creation_date DATE,
                         score INT,
                         alliance_income INT,
                         alliance_mineral_income INT,
                         alliance_tech_income INT,
                         alliance_uranium_income INT,
                         alliance_production_income INT,
                         alliance_rare_metal_income INT,
                         total_land
                         total_popolation
                         total_projects
                         average_war_index
                         average_stability_index
                         average_tech_index
                         average_education_index
                         average_commerce_index
                         average_employment_index
                         average_power_index
                         total_war_victories
                         total_war_defeats
                         average_transportation_index
                         alliance_fuel_income
                         )""",), ]

                for table in tables:
                    await cursor.execute(table)

                await conn.commit()
                log.info("Database has been created.")

        except sql.Error as e:
            log.error(f"Error while working with SQLite: {e}")
        except Exception as e:
            log.error(f"Unexpected error: {e}")
    else:
        log.info("Database already exists, disable this function.")

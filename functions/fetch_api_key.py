import logging as log
from typing import Any, Type

import aiosqlite as aiosql


async def retrieve_api_key(folder_name: str = "database", name: str = "winston") -> Type[Exception] | None | Any:
    """
    Fetch the Diplomacy and Strife api_key stored in the database.

    Defaults:
        folder_name: Default set to database.

        name: Default set to winston.


    Args:
        folder_name: The name of the folder in which the database file is stored.
        name: The name of the database file
    """
    log.getLogger(__name__)
    log.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', )
    try:
        async with aiosql.connect(f"{folder_name}/{name}.db") as database:
            async with database.execute("""SELECT dns_api_key FROM main""") as cursor:
                result = await cursor.fetchone()
                return result[0] if result else None
    except aiosql.Error as sqlExcept:
        log.error(f"Error fetching API key: {sqlExcept}")
        return None

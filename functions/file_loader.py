import logging as log
import json
from collections import defaultdict
from pathlib import Path
from typing import Dict

import tomlkit as toml


log.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=log.INFO)


async def file_loader(folder: str, file: str, extension: str) -> Dict[str, str]:
    """
    This function loads a file from a given folder.

    Args:
        folder: The name of the folder.
        file: The name of the file.
        extension: The extension of the file.

    Returns:
        A dictionary containing the contents of the loaded file.
    """
    try:
        file_path: Path = Path(f"{folder}/{file}.{extension}")
        file_loaded: Dict[str, str] = defaultdict(str, toml.loads(file_path.read_text()))
        return file_loaded
    except Exception as e:
        log.exception(f"Encountered the exception: {e}")

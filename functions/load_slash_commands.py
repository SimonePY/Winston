import logging as log
import os

from disnake.ext import commands


async def slash_commands(app, folder_name: str = "commands", enabled: bool = True) -> None:
    """
    This function loads slash commands from a given folder if enabled.

    Defaults:
        folder_name: Default set to commands.

        enabled: Default  set to true.

    Args:
        app: The name of your application start.
        folder_name: The name of the folder containing the slash commands.
        enabled: Whether to enable or disable loading of the slash commands.
    """

    log.getLogger(__name__)
    log.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', )

    try:
        if enabled:
            for filename in os.listdir(folder_name):
                if filename.endswith('.py'):
                    full_path = os.path.join(folder_name, filename)
                    app.load_extension(f"{full_path[:-3].replace('/', '.')}")
            log.info("Slash commands have been loaded.")
        else:
            log.info("Slash commands are disabled.")
    except (FileNotFoundError, commands.ExtensionError, Exception) as e:
        log.exception(f"Error loading slash commands: {str(e)}")

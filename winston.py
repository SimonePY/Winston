import logging as log
from collections import defaultdict
from pathlib import Path
from typing import Dict

import disnake as snake
import tomlkit as toml
from disnake.ext import commands

from functions.create_database import database_creation
from functions.load_slash_commands import slash_commands

CONFIG_FILE: Path = Path("files/config.toml")
KEYWORDS_FILE: Path = Path("files/keywords.toml")

if not CONFIG_FILE.exists():
    CONFIG_FILE.touch()
    CONFIG_FILE.write_text(
        "discord_bot_token= ''\nds_api_key= ''\ndiscord_bot_activity= ''\ndiscord_bot_prefix= '' "
        "\ndiscord_bot_description= ''\ndiscord_bot_owner= ''\ndiscord_bot_status="
        "''"
    )

config: Dict[str, str] = defaultdict(str, toml.loads(CONFIG_FILE.read_text()))

if not KEYWORDS_FILE.exists():
    KEYWORDS_FILE.touch()
    KEYWORDS_FILE.write_text(
        "discord_bot_name=''\ndiscord_bot_description=''\ndiscord_bot_github=''\ndiscord_bot_wiki"
        "=''\ndiscord_bot_support_server=''\ndiscord_bot_version=''\ndiscord_bot_invite_link=''")

log.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

log.getLogger(__name__)

bot: commands.Bot = commands.Bot(
    activity=snake.Activity(
        name=config.get("discord_bot_activity", "Configuring my self"), type=snake.ActivityType.playing
    ),
    command_prefix=config.get("discord_bot_prefix", "!"),
    description=config.get("discord_bot_description", "I'm a discord bot!"),
    owner_id=config.get("discord_bot_owner_id", None),
    status=config.get("discord_bot_status", "online"),
    case_insensitive=True,
    reload=True,
    strip_after_prefix=False,
    sync_commands_debug=True,
    help_command=None,
    intents=snake.Intents.all(),
)

if __name__ == "__main__":
    try:
        database_creation(folder_name="files")
        slash_commands(app=bot)
        bot.run(config.get("discord_bot_token"))
    except snake.LoginFailure as e:
        log.error(f"The provided bot token is invalid, exception: '{str(e)}'")
    except KeyError as e:
        log.error(f"The configuration file is missing the key exception: '{str(e)}'")
    except Exception as e:
        log.error(f"An unexpected error occurred:'{str(e)}'")

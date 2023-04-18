import logging as log
from typing import Dict

import disnake as snake
from disnake.ext import commands

from functions.file_loader import file_loader

log.getLogger(__name__)
log.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', )

keywords: Dict[str, str] = await file_loader(folder="files", file="keywords", extension="toml")


class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="invite", description="Return a bot invite", dm_permission=False, nsfw=False,
                            auto_sync=True)
    async def invite(self, invite: snake.ApplicationCommandInteraction):
        try:
            await invite.response.send_message(
                f"You can invite the bot by clicking on the application and using the blue bottom.\nYou can also "
                f"invite the bot by using this link : [Bot Invite]({keywords.get('discord_bot_invite_link', 'https://discord.com/api/oauth2/authorize?client_id=1097527654971879464&permissions=277025508352&scope=bot%20applications.commands')})")
        except Exception as e:
            await invite.response.send_message(e)
            log.error(f"Invite Command Exception: {e}")


def setup(bot):
    bot.add_cog(Invite(bot))

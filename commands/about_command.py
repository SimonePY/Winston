import datetime as date
import logging as log
from typing import Dict

import disnake as snake
from disnake.ext import commands

from functions.file_loader import file_loader

log.getLogger(__name__)
log.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', )

keywords: Dict[str, str] = await file_loader(folder="files", file="keywords", extension="toml")


class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="about", description="Return bot information", dm_permission=False, nsfw=False,
                            auto_sync=True, )
    async def about(self, about: snake.ApplicationCommandInteraction):
        try:
            about_embed = snake.embeds.Embed(title=keywords.get("discord_bot_name", "Winston"),
                                             description=keywords.get("discord_bot_description",
                                                                      "Winston is a Discord bot for Diplomacy and Strife"),
                                             color=snake.Color.green(), timestamp=date.datetime.now(), )
            about_embed.add_field(name="Github",
                                  value=f"[Github Page]({keywords.get('discord_bot_github', 'https://github.com/SimonePY/Winston')})",
                                  inline=True)
            about_embed.add_field(name="Wiki",
                                  value=f"[Wiki Page]({keywords.get('discord_bot_wiki', 'https://github.com/SimonePY/Winston/wiki')})",
                                  inline=True)
            about_embed.add_field(name="Support Server",
                                  value=f"[Discord Invite]({keywords.get('discord_bot_support', 'https://discord.gg/feBVcXVYhC')})",
                                  inline=True)
            about_embed.set_footer(text=keywords.get("discord_bot_version", "v0.0.1"))
            await about.response.send_message(embed=about_embed)
        except Exception as e:
            await about.response.send_message(e)
            log.error(f"About Command Exception: {e}")


def setup(bot):
    bot.add_cog(About(bot))

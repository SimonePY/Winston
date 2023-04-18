import datetime as date
import json
import logging as log
from typing import Dict

import disnake as snake
from disnake.ext import commands

from functions.file_loader import file_loader

log.getLogger(__name__)
log.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', )

keywords: Dict[str, str] = await file_loader(folder="files", file="keywords", extension="toml")

with open('files/links.json') as f:
    names_urls = json.load(f)


class Links(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="links", description="Return useful game links", dm_permission=False, nsfw=False,
                            auto_sync=True)
    async def links(self, links: snake.ApplicationCommandInteraction):
        try:
            links_embed = snake.Embed(title="Useful Game Links", description="Diplomacy and Strife useful links.",
                                      color=snake.Color.green(), timestamp=date.datetime.now())
            for name_url in names_urls['links']:
                links_embed.add_field(name=name_url["name"], value=f"[Redirect]({name_url['url']})", inline=True)
            links_embed.set_footer(text=keywords.get("discord_bot_version", "v0.0.1"))
            await links.response.send_message(embed=links_embed)
        except Exception as e:
            await links.response.send_message(e)
            log.error(f"Links Command Exception: {e}")


def setup(bot):
    bot.add_cog(Links(bot))

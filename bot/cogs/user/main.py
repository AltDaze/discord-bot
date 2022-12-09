# -*- coding: utf-8 -*-
import nextcord
from nextcord.ext import commands


# todo: UserCogs
class TestCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(description="Test command")
    async def test(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("This is a slash command in a cog!")


class VoiceStatistics(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def test_listener(self):
        pass


class Logs(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        author = message.author
        await message.channel.send(message.content)


class Manage(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(description='Количество удаляемых сообщений')
    async def clear(self, count: int):
        messages = []
        count = int(count)


def register_user_cogs(bot: commands.Bot) -> None:
    bot.add_cog(TestCog(bot))
    bot.add_cog(VoiceStatistics(bot))
    bot.add_cog(Logs(bot))
    bot.add_cog(Manage(bot))
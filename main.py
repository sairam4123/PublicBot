
import discord
from discord.ext import commands

bot = commands.Bot(
	command_prefix=".",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)



@bot.event 
async def on_ready():  # When the bot is ready
    print(bot.user+' is online')  # Prints the bot's username and identifier


extensions = [
	'cogs.trivia','cogs.LastFm','cogs.weather'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

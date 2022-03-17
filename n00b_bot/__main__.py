###########
# IMPORTS #
###########

# Standard Library Imports
import os
import logging

# Third Party Library Imports
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Local Library Imports


########
# MAIN #
########

def logger():
    """
    Logs errors and debug information from discord
    """
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

def main():
    logger()
    load_dotenv()
    
    bot = commands.Bot(command_prefix='.',
                       intents=discord.Intents.all())

if __name__ == '__main__':
    main()
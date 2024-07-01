import os
import logging
from logging.handlers import RotatingFileHandler
from pyrogram import Client, filters
from pyrogram.types import Message

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6749866325:AAEEIwO7-xYFiU5gGlM4Y07ADvN4XvfHY98")

# Your API ID and API Hash from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28737888"))
API_HASH = os.environ.get("API_HASH", "aa9fc525a5e5a837256c1f0b445af447")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001556818224"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1392184089"))

# Port
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://pinkybitlu:pinky7268@cluster0.dizew5m.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "nightclassesdb")

# Force sub channel id
FORCE_SUB_CHANNEL = {int(_id) for _id in os.environ.get('FORCE_SUB_CHANNEL', '-1001032417953').split() if _id and _id.startswith('-100')}

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nJoin 1.@Science2_0 2.@Digipoddi & https://t.me/+q97R_ztFeskwMzcx this 3 channels for unlimited 24/7 🔞Viral Videos🤤.")

# Admins list
ADMINS = [int(x) for x in os.environ.get("ADMINS", "5452354891 1392184089 5602172369 5685802336").split()]
ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

# Auto-delete messages
AUTO_DELETE_MESSAGE_1 = '<b><a href="https://graph.org/file/6ccb99990afdd242255e6.jpg">#PAID_PROMOTION</a> 👇✅\n\nHello Friend Take VIP MEMBERSHIP & ENJOY DIRECT VIDEOS #NO_LINKS & #NO_ADS CHECK DEMO NOW.\n\nhttps://t.me/+4ZslCNZmfvs4MWNl</b>'
AUTO_DELETE_MESSAGE_2 = '❗️❗️❗️IMPORTANT ❗️❗️❗️\n\nThis Files/Videos will be deleted in 10 mins (Due to report issues).\n\nPlease forward these files/videos to your Saved Messages or any other chat and start downloading them there.'

# Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join This Channel to get files. Please join this channel now👇👇👇</b>")

# Set custom caption here
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "24/7 non stop stuff 👻 Join 👇\n\nhttps://t.me/Science2_0")

# Protect content
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Disable channel post share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Sorry, don't send any msg or file. I only work for my admins!"

LOG_FILE_NAME = "filesharingbot.txt"

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

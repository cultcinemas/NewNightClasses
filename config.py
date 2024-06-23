#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7067424300:AAGsRKmOiPjzshRJ_0sDe7eSqu4K6SrSdCI")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28737888"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "aa9fc525a5e5a837256c1f0b445af447")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001987796987"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1392184089"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://srj726811:srj726811@cluster0.rvootx1.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "DIGIPODDIDB")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = {int(_id) for _id in os.environ.get('FORCE_SUB_CHANNEL', '-1001901321632').split() if _id and _id.startswith('-100')}

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI bro join 1.@Science2_0 2.@Digipoddi & https://t.me/+q97R_ztFeskwMzcx this 3 channels Unlimited 24/7 🔞Viral Videos🤤.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5452354891 1392184089 5602172369 5685802336").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

AUTO_DELETE_MESSAGE = '❗️❗️❗️IMPORTANT ❗️❗️\n\nThis Files/Videos will be deleted in 10 mins (Due Reports Issues).\n\nPlease Forward this Files/Videos to your Saved Messages Or Any Other Chat And Start Download There'

#Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join This Channel to get files Bitlu vasthayi Join Avvu Fast Ga\n\nPlease I Kindly Request Join This Channel Now👇👇👇</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Sorry Dont Send any msg or file I Only work for my admins!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

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

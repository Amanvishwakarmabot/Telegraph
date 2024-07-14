import re
import os
from os import getenv, environ
from Script import script 
from dotenv import load_dotenv

load_dotenv()


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
      
# Owner Information
API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
ADMINS = int(environ.get("ADMINS", ""))

# Database Informatio
DB_URI = environ.get("DB_URI", "")
DB_NAME = environ.get("DB_NAME", "vjbotz")

# Bot Information
BOT_TOKEN = environ.get("BOT_TOKEN", "")
BOT_USERNAME = environ.get("BOT_USERNAME", "") # your bot username without @
PICS = (environ.get('PICS', 'https://graph.org/file/82ef767ffebe3a948e476.jpg')).split() # Bot Start Picture

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))

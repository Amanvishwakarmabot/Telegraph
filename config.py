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
API_ID = int(environ.get("API_ID", "12380656"))
API_HASH = environ.get("API_HASH", "d927c13beaaf5110f25c505b7c071273")
ADMINS = int(environ.get("ADMINS", "5977931010"))

# Database Informatio
DB_URI = environ.get("DB_URI", "mongodb+srv://aman991932:aman@cluster0.ckuveks.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "Cluster0")

# Bot Information
BOT_TOKEN = environ.get("BOT_TOKEN", "7232006758:AAGV-HPIfJi3k-gz2_YR6_-1k7706NEPD-I")
BOT_USERNAME = environ.get("BOT_USERNAME", "AV_ADVANCE_BOT") # your bot username without @
PICS = (environ.get('PICS', 'https://graph.org/file/82ef767ffebe3a948e476.jpg')).split() # Bot Start Picture

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002114619001"))


class Var(object):
    MULTI_CLIENT = False
    name = str(getenv('name', 'AV_ADVANCE_BOT'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = ""
    else:
        URL = ""

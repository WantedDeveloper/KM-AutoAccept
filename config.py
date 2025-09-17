from os import environ

API_ID = int(environ.get("API_ID", "15479023"))
API_HASH = environ.get("API_HASH", "f8f6cf547822449c29fc60dae3b31dd4")
BOT_TOKEN = environ.get("BOT_TOKEN", "8060569801:AAEk1tmmpaUfIyydSe20TASfscafotRbqKA")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002937162790"))
ADMINS = int(environ.get("ADMINS", "1512442581"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://KM-AutoAccept:KM-AutoAccept123@km-autoaccept.restswy.mongodb.net/?retryWrites=true&w=majority&appName=KM-AutoAccept") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "autoacceptbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))

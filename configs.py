from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23120005"))
    API_HASH = getenv("API_HASH", "bd71931669ca54f628e9b4245f8bc4d4")
    BOT_TOKEN = getenv("BOT_TOKEN", "5728169519:AAFWifOQpN_NgZVI5Py30gCA5IFnjrt4XLI")

config = Config()

from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150000"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG" , "https://te.legra.ph/file/9d8c207b8ad08682e638f.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/9d8c207b8ad08682e638f.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/pyro_support_v2")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_abhiiii")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6863173634 6627630052").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

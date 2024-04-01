from os import environ as ev
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

API_TOKEN = ev.get('BOT_TOKEN')
ADMIN_ID = ev.get('ADMIN_TELEGRAM_ID')
CHANNEL_ID = ev.get('CHANNEL_ID')

feedback_channel_id = ev.get('FEEDBACK_CHANNEL_ID')
post_channel_id = ev.get('POST_CHANNEL_ID')
backup_channel_id = ev.get('BACKUP_CHANNEL_ID')
donation_links = ""

DB_HOST = "127.0.0.3"
DB_PORT = "5432"

DB_USERNAME = ev.get("DB_USERNAME")
DB_PWD = ev.get("DB_PWD")
DB_NAME = "sintia"
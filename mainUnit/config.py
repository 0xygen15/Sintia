from os import environ as ev
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

API_TOKEN = ev.get('BOT_TOKEN')
admin_id = ev.get('ADMIN_TELEGRAM_ID')
channel_id = ev.get('CHANNEL_ID')
feedback_channel_id = ev.get('FEEDBACK_CHANNEL_ID')
post_channel_id = ev.get('POST_CHANNEL_ID')
backup_channel_id = ev.get('BACKUP_CHANNEL_ID')
donation_links = ""
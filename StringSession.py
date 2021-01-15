from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    "Go To my.telegram.org"
)
APP_ID = int(input("APP ID: "))
API_HASH = input("API HASH: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())

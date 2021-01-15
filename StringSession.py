from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    "Go To my.telegram.org"
)
APP_ID = int(input("APP ID: "))
API_HASH = input("API HASH: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    try:
        session = client.session.save()
        client.send_message("me",
                            f"String Session : \n\n`{session}` \n\nMade with love by @vsyzchan")
        print("Check Saved Message at Your Telegram. Powered by @vsyzchan")
    except Exception as sed:
        print(f"Error : {sed}")

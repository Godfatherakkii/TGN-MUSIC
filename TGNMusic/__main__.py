import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from TGNMusic import LOGGER, app, userbot
from TGNMusic.core.call import TGN
from TGNMusic.plugins import ALL_MODULES
from TGNMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("TGNMusic").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("TGNMusic").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("TGNMusic.plugins" + all_module)
    LOGGER("TGNMusic.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await TGN.start()
    try:
        await TGN.stream_call(
            "https://graph.org/file/ec8a35dd5f1ef90947167.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("TGNMusic").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await TGN.decorators()
    LOGGER("TGNMusic").info("TGN Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("TGNMusic").info("Stopping TGN Music Bot! GoodBye")

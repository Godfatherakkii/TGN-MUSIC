from TGNMusic.core.bot import TGN
from TGNMusic.core.dir import dirr
from TGNMusic.core.git import git
from TGNMusic.core.userbot import Userbot
from TGNMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = TGN()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

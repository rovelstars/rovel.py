__version__ = "0.0.2"

import colorama, emoji, pydash, requests, aiohttp

from .functions import post_guild_stats, chat, base, download
from .api_npm import get_details, get_stat
from .did_you_mean import Matcher
from .approx import approximate_number

colorama.init(autoreset=True)
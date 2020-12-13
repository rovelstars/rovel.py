__version__ = "0.0.1"

import colorama, emoji, pydash, requests, aiohttp

from .functions import *
from .api_npm import *
from .approx import approximate_number

colorama.init(autoreset=True)
# rovel.py

![Discord - Join us](https://img.shields.io/discord/602906543356379156) ![PyPI - Downloads](https://img.shields.io/pypi/dd/rovel.py) ![Repo size](https://img.shields.io/github/repo-size/rovelstars/rovel.py) ![Lines of code](https://img.shields.io/tokei/lines/github/rovelstars/rovel.py)

## Install
```bat
pip install rovel.py
```
```bat
python -m pip install rovel.py
```

## Usage
```py
from rovel import *
from did_you_mean import Matcher

print(api_npm.get_details("rolve.js"))

m = Matcher("test")
print(m.get("tset"))
```

## List of packages
- colorama
- approx
- emoji
- api-npm
- pydash
- requests
- aiohttp
- did-you-mean

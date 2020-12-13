from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="rovel.py",
    version="0.0.1",
    description="rovel.js but it's Python",
    license="MIT",
    long_description=long_description,
    author="Dan23123",
    install_requires=[
        "colorama",
        "pydash",
        "emoji",
        "requests",
        "argparse",
        "aiohttp"
    ],
    keywords="rovel.py",
    long_description_content_type="markdown"
)

import json

from setuptools import find_packages, setup

meta = json.load(open("srt_shifter/meta.json", "r"))

setup(
    name=meta["name"],
    version=meta["version"],
    description=meta["description"],
    author=meta["author"],
    url=meta["url"],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": [
            "srt_shifter/meta.json",
        ],
    },
    entry_points={"console_scripts": ["srt-shifter = srt_shifter.main:main"]},
)

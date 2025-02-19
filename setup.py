from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nonebot-plugin-directlinker",
    version="2.1.0",
    author="Kl1nge5",
    description="A plugin based on NoneBot2 to extract direct links of files in qq group.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ninthseason/nonebot-plugin-directlinker",
    project_urls={
        "Bug Tracker": "https://github.com/ninthseason/nonebot-plugin-directlinker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=["nonebot_plugin_directlinker"],
    python_requires=">=3.7",
)

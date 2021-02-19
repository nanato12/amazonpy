from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="amazonpy",
    packages=["amazonpy"],
    version="2.0.0",
    license="MIT",
    install_requires=["bs4", "fake-useragent", "requests"],
    author="nanato12",
    author_email="admin@nanato12.info",
    url="https://github.com/nanato12/amazonpy",
    description="amazon scraping library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="amazon amazonpy amazon_scraping",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
)

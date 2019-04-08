from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="throwcolour",
    version="1.0.7",
    author="Jacky Zhao",
    author_email="j.zhao2k19@gmail.com",
    description="A small package to make printing pretty things easier!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jackyzha0/ThrowColour",
    packages=['throwcolour'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

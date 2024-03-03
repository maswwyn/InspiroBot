from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="InspiroBot",
    version="0.2.2",
    author="masswyn",
    author_email="maswwyn24@gmail.com",
    description="A web application for generating random motivational affirmations and inspiring quotes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maswwyn/InspiroBot",
    packages=find_packages(),
    install_requires=[
        "blinker==1.7.0",
        "certifi==2024.2.2",
        "charset-normalizer==3.3.2",
        "click==8.1.7",
        "colorama==0.4.6",
        "docutils==0.20.1",
        "Flask==3.0.2",
        "idna==3.6",
        "importlib-metadata==7.0.1",
        "InspiroBot==0.2.2",
        "itsdangerous==2.1.2",
        "jaraco.classes==3.3.1",
        "Jinja2==3.1.3",
        "keyring==24.3.1",
        "markdown-it-py==3.0.0",
        "MarkupSafe==2.1.5",
        "mdurl==0.1.2",
        "more-itertools==10.2.0",
        "nh3==0.2.15",
        "pip==24.0",
        "pkginfo==1.9.6",
        "Pygments==2.17.2",
        "pywin32-ctypes==0.2.2",
        "readme_renderer==43.0",
        "requests==2.31.0",
        "requests-toolbelt==1.0.0",
        "rfc3986==2.0.0",
        "rich==13.7.1",
        "setuptools==65.5.0",
        "twine==5.0.0",
        "urllib3==2.2.1",
        "Werkzeug==3.0.1",
        "wheel==0.42.0",
        "zipp==3.17.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)

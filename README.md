<div align=center>

# Typeform.py

A basic and simple Reddit CLI script meant for browsing [Reddit](https://reddit.com)

<sup>And yes this is actually my AP CSA final project. Will be maintained throughout the summer hopefully</sup>

<div align=left>

## Future Plans

- [x] Bundle script into a single executable using Nuikta or PyInstaller 
- [ ] Improved TUI using [Textual](https://textual.textualize.io/)
- [ ] Unit testing (Test Python 3.8 - 3.11)
- [ ] Making the whole project properly statically typed (check using [Pyright](https://pypi.org/project/pyright/))
- [ ] More commands
- [x] Global PRAW session management system
- [ ] Live Updates (Either this will be first developed on Kumiko or Akari, and then ported, or developed here first. The idea comes from here: https://github.com/No767/Kumiko/discussions/266)

## Running the script

There are two supported ways of running this script: locally, or <sup>the way that the project is supposed to be ran</sup> on CodingRooms.

**Note that this script needs to access Reddit, which is blocked on SFUSD networks. Please do this back home or use an proxy or VPN. If you are using CodingRooms to access Reddit, it should be fine since all CodingRooms instances run on AWS**

### Locally


Requirements:

- [Python 3](https://www.python.org/) (should work throughout 3.8, 3.9, 3.10, and 3.11). (not 3.7 or below since that is deprecated)
- [Poetry](https://python-poetry.org/)
- [Reddit Client ID and Secret](https://www.reddit.com/prefs/apps)

1. Create, and install the poetry development tools

    ```bash
    poetry env use 3.11 \
    poetry install
    ```
    Note that the dev group within the `pyproject.toml` only contains `pre-commit`, which is not needed

2. Open up a poetry shell

    ```bash
    poetry shell
    ```

3. Now run the script (`main.py`)

    ```bash
    python main.py --help
    ```


### CodingRooms

Requirements:
- Nothing! (just access to CodingRooms)

The CodingRooms workspace link will be shared on Piazza. Look out for my post on Piazza for it.

All you need to do before running the script is to install all deps. (Luckily all of these deps are Pure-Python based, not C or Rust based)

```bash
pip install -r requirements.txt
```

And then just run the script as per usual

### Replit

Open up the Replit provided in the Piazza link, and it should automatically install all of the stuff for you

## Troubleshooting

**Q: Why do I keep on getting a `ModuleNotFound` error?**
A: More than likely you forgot to install the libraries needed. Just run `pip install -r requirements.txt` to install it.

## License

MIT (mainly I don't want to have to deal with copyright)

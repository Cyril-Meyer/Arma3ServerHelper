# Arma3ServerHelper

Arma 3 Server Helper is a collection of scripts to simplify Arma 3 server
management.
For now this consists of an Arma 3 server install/update toolkit and mod list extractor.
Further improvements or scripts may be added in the future, do not hesitate to
contact me if you have any needs, even very specific ones.

## Minimal Example
```
python downloader.py
--path C:\Games\Arma3
--steamcmd C:\steamcmd\steamcmd.exe
--branch "233780 -beta creatordlc"
--modlist A3Preset.html
--steam-user="username"
--steam-pass="password"
```

```
python presetModList.py
--modlist A3Preset.html
```

## Usage
```
usage: downloader.py [-h] [--steam-user STEAM_USER] [--steam-pass STEAM_PASS]
                     [--path PATH] [--steamcmd STEAMCMD]
                     [--branch BRANCH [BRANCH ...]] [--appid APPID]
                     [--mods MODS [MODS ...]]
                     [--modlist MODLIST [MODLIST ...]]

optional arguments:
  -h, --help            show this help message and exit
  --steam-user STEAM_USER
                        steam account username
  --steam-pass STEAM_PASS
                        steam account password
  --path PATH           Arma3 server path
  --steamcmd STEAMCMD   path to steamcmd.exe
  --branch BRANCH [BRANCH ...]
                        Arma3 branch to install
  --appid APPID         Arma3 steam App ID
  --mods MODS [MODS ...]
                        Workshop items id
  --modlist MODLIST [MODLIST ...]
                        Arma3 preset file (.html)
```

### Requirements
* Python 3.7 or newer
  (should work with 3.x, but never tested with older than 3.7)

### Developer Documentation
Valve documentation
* [SteamCMD](https://developer.valvesoftware.com/wiki/SteamCMD)
* [Steam command line options](https://developer.valvesoftware.com/wiki/Command_line_options)

GitHub public documentations
* [davispuh/steam_console_params.txt](https://gist.github.com/davispuh/6600880)
* [dgibbs64/SteamCMD-Commands-List](https://github.com/dgibbs64/SteamCMD-Commands-List)

Interesting projects:
* [py-steamcmd-wrapper](https://pypi.org/project/py-steamcmd-wrapper/)
* [pysteamcmd](https://github.com/f0rkz/pysteamcmd)

### Acknowledgement
Thanks to [Drake-Feather](https://github.com/Drake-Feather) for providing me an
Arma 3 key.

# Arma3ServerHelper

## Minimal Example
```
python main.py
--path C:\Games\Arma3
--steamcmd C:\steamcmd\steamcmd.exe
--branch "233780 -beta creatordlc"
--modlist A3Preset.html
--steam-user="username"
--steam-pass="password"
```

## Usage
```
usage: main.py [-h] [--steam-user STEAM_USER] [--steam-pass STEAM_PASS]
               [--path PATH] [--steamcmd STEAMCMD]
               [--branch BRANCH [BRANCH ...]] [--appid APPID]
               [--mods MODS [MODS ...]] [--modlist MODLIST [MODLIST ...]]

optional arguments:
  -h, --help            show this help message and exit
  --steam-user STEAM_USER
                        steam account username
  --steam-pass STEAM_PASS
                        steam account password
  --path PATH           Arma3 server path, the folder must already exist
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

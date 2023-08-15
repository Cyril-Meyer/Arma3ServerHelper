import os
import argparse

import utils.logger
import utils.modlist
import utils.symlink
from utils.steamcmd import SteamCMD

log = utils.logger.default.log

parser = argparse.ArgumentParser()
parser.add_argument('--steam-user', type=str, default='anonymous',
                    help='steam account username')
parser.add_argument('--steam-pass', type=str, default='',
                    help='steam account password')
parser.add_argument('--path', type=str, default='C:\\Games\\Arma3\\A3Master',
                    help='Arma3 server path')
parser.add_argument('--path-mkdir', type=bool, default=False,
                    help=argparse.SUPPRESS)
parser.add_argument('--steamcmd', type=str, default='C:\\steamcmd\\steamcmd.exe',
                    help='path to steamcmd.exe')
parser.add_argument('--branch', type=str, nargs='+', default=[],  # e.g. '233780 -beta'
                    help='Arma3 branch to install')
parser.add_argument('--appid', type=int, default=107410,          # Arma3 appid
                    help='Arma3 steam App ID')
parser.add_argument('--mods', type=int, nargs='+', default=[],    # e.g. 894678801
                    help='Workshop items id')
parser.add_argument('--modlist', type=argparse.FileType('r'), nargs='+', default=[], # e.g. 'A3Preset.html'
                    help='Arma3 preset file (.html)')
args = parser.parse_args()

log(f'-----{"Arma3ServerHelper":^50}-----')

if not os.path.isfile(args.steamcmd):
    log("ERROR: steamcmd not found")
    raise FileNotFoundError
if not os.path.isdir(args.path):
    if args.path_mkdir:
        os.makedirs(args.path)
    else:
        log("ERROR: arma3 folder not found, the folder must already exist")
        raise FileNotFoundError

log(f'{"> steam user":16}{args.steam_user}')
log(f'{"> Arma3 path":16}{args.path}')
log(f'{"> steamcmd":16}{args.steamcmd}')
for branch in args.branch:
    log(f'{"-> branch":16}{branch}')
log(f'{"> appid":16}{args.appid}')
for mod in args.mods:
    log(f'{"-> mods":16}{mod}')
for mod_list_file in args.modlist:
    log(f'{"-> modlist":16}{mod_list_file.name}')

cmd = SteamCMD(args.steamcmd, args.steam_user, args.steam_pass, args.path)

input(f'---  {"Press Enter to continue...":^50}  ---')


log(f'-----{"Download Server":^50}-----')

for branch in args.branch:
    log(f'{"---> branch":16}{branch}')
    log(f'{"<---":16}{cmd.app_update(branch)}')


log(f'-----{"Download Mod":^50}-----')

for mod_id in args.mods:
    log(f'{"-> mods":16}{mod_id}')
    log(f'{"<---":16}{cmd.workshop_download_item(str(args.appid), mod_id)}')
    log(f'{"-> linking":16}{mod_id}')
    log(f'{"<---":16}{utils.symlink.link(args.path, str(args.appid), mod_id)}')


for mod_list_file in args.modlist:
    log(f'{"-> modlist":16}{mod_list_file.name}')
    for mod_id in utils.modlist.parse(mod_list_file):
        log(f'{"-> mods":16}{mod_id}')
        log(f'{"<---":16}{cmd.workshop_download_item(str(args.appid), mod_id)}')
        log(f'{"-> linking":16}{mod_id}')
        log(f'{"<---":16}{utils.symlink.link(args.path, str(args.appid), mod_id)}')


log(f'-----{"Process completed":^50}-----')
input(f'---  {"Press Enter to continue...":^50}  ---')

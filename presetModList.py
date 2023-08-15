import os
import argparse

import utils.modlist

parser = argparse.ArgumentParser()
parser.add_argument('--modlist', type=argparse.FileType('r'), nargs='+', default=[],
                    help='Arma3 preset file (.html)')
args = parser.parse_args()

for mod_list_file in args.modlist:
    modlist = ''
    print(mod_list_file.name)
    for mod_id in utils.modlist.parse(mod_list_file):
        modlist += f'@a3sh{mod_id};'
    print(modlist[:-1])

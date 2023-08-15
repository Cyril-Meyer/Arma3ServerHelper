import os


def link(path, appid, mod_id):
    if not os.path.isdir(f'{path}/steamapps/workshop/content/{appid}/{mod_id}'):
        raise FileNotFoundError
    try:
        os.symlink(f'{path}/steamapps/workshop/content/{appid}/{mod_id}', f'{path}/@A3SH{mod_id}')
    except FileExistsError:
        pass
    except Exception as e:
        raise e
    return f'@A3SH{mod_id}'

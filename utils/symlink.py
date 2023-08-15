import os


def link(path, appid, mod_id):
    try:
        os.symlink(f'{path}/steamapps/workshop/content/{appid}/{mod_id}', f'{path}/@A3SH{mod_id}')
    except FileExistsError:
        pass
    except Exception as e:
        raise e

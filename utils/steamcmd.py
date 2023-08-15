import subprocess


class SteamCMD:
    def __init__(self, steamcmd, username, password, install_dir):
        self.steamcmd = steamcmd
        self.username = username
        self.password = password
        self.install_dir = install_dir

    def app_update(self, app):
        """
        p = subprocess.run([self.steamcmd,
                            '+force_install_dir', self.install_dir,
                            '+login', self.username, self.password,
                            '+app_update', app,
                            'validate', '+quit'],
                           shell=True, check=True)
        """
        p = subprocess.Popen(f'{self.steamcmd} '
                             f'+force_install_dir {self.install_dir} '
                             f'+login {self.username} {self.password} '
                             f'+app_update {app} '
                             f'validate +quit',
                             creationflags=subprocess.CREATE_NEW_CONSOLE)

        if not p.wait() == 0:
            raise RuntimeError

        return p.returncode

    def workshop_download_item(self, app, mod):
        """
        p = subprocess.run([self.steamcmd,
                            '+force_install_dir', self.install_dir,
                            '+login', self.username, self.password,
                            '+workshop_download_item', app, mod,
                            'validate', '+quit'],
                           shell=True, check=True)
        """
        p = subprocess.Popen(f'{self.steamcmd} '
                             f'+force_install_dir {self.install_dir} '
                             f'+login {self.username} {self.password} '
                             f'+workshop_download_item {app} {mod} '
                             f'validate +quit',
                             creationflags=subprocess.CREATE_NEW_CONSOLE)

        if not p.wait() == 0:
            raise RuntimeError
        return p.returncode

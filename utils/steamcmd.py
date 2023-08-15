import subprocess


class SteamCMD:
    def __init__(self, steamcmd, username, password, install_dir):
        self.args = []
        self.steamcmd = steamcmd
        self.username = username
        self.password = password
        self.install_dir = install_dir
        self.reset()

    def reset(self):
        self.args = [self.steamcmd,
                     '+force_install_dir', self.install_dir,
                     '+login', self.username, self.password]

    def app_update(self, app, validate=True):
        self.args.append('+app_update')
        self.args.append(app)
        if validate:
            self.args.append('validate')

    def workshop_download_item(self, app, mod, validate=True):
        self.args.append('+workshop_download_item')
        self.args.append(app)
        self.args.append(str(mod))
        if validate:
            self.args.append('validate')

    def run(self, new_console=True):
        self.args.append('+quit')

        if new_console:
            p = subprocess.Popen(self.args,
                                 creationflags=subprocess.CREATE_NEW_CONSOLE)
            if not p.wait() == 0:
                raise RuntimeError
        else:
            p = subprocess.run(self.args,
                               shell=True, check=True)
            if not p.returncode == 0:  # not necessary as we use check=True
                raise RuntimeError

        self.reset()
        return p.returncode

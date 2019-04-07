import os
import json
from .config import *
from .mimes import *


class CMSRoutes:

    def __init__(self, e, d):
        self.d = d
        self.e = e

        self.core = cfg.static_core
        self.root = cfg.static_root
        self.path = e.path_info.strip('/')

        self.checkRouting()

    def checkRouting(self):

        if not self.d.exists:
            return self.sendfile(404, self.core + 'domain.html', 'text/html')

        file = os.path.join(self.root, self.path)
        if os.path.isfile(file):
            return self.sendfile(200, file)

        if self.path == 'acehcms.js':
            print(self.path)
            return self.sendfile(200, self.core + 'acehcms.js', 'text/javascript')

        if self.path == '':
            file = os.path.join(self.root, 'themes', self.d.theme_dir, 'index.html')
            return self.sendfile(200, file, 'text/html')

        if self.path.startswith('getjson'):
            path = self.path.replace('getjson/', '')
            file = os.path.join(self.root, 'json', self.d.json_dir, path)
            return self.sendfile(200, file, 'application/json')

        with open(os.path.join(self.core, 'structure.json'), 'r') as f:
            routes = json.load(f)
            self.structure(routes)

        jsonfile = os.path.join(self.root, 'themes', self.d.theme_dir, 'structure.json')
        if os.path.isfile(jsonfile):
            with open(jsonfile, 'r') as f:
                routes = json.load(f)
                self.structure(routes)

        self.notfound()

    def structure(self, routes):
        for key, file in routes.items():
            if key.strip('/').startswith(self.path):
                file = os.path.join(self.root, 'themes', self.d.theme_dir, file)
                if (os.path.isfile(file)):
                    return self.sendfile(200, file, 'text/html')
                else:
                    return self.notfound()
                break

    def notfound(self):
        file = os.path.join(self.root, 'themes', self.d.theme_dir, '404.html')
        if os.path.isfile(file):
            return self.sendfile(
                404, file,
                'text/html')
        else:
            return self.sendfile(
                404, self.core + 'page.html',
                'text/html')

    def sendfile(self, status, file, mime=None):
        s = {
            404: "404 Not Found",
            200: "200 OK"
        }
        self.status = s[status]
        self.filename = file
        self.mimetype = mime if mime else mimes(file)

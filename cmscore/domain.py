import json
from .config import *


class CMSDomain:

    exists = False

    def __init__(self, e):
        self.checkDomain(e)

    def checkDomain(self, e):
        with open(cfg.static_root + 'domain.json', 'r') as f:
            domains = json.load(f)

        for domain, information in domains.items():
            if (domain == e.http_host):

                for key, val in information.items():
                    setattr(self, key, val)

                self.exists = True
                break

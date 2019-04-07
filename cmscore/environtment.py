class CMSEnvirontment:

    all_keys = {}

    def __init__(self, e):
        self.buildEnv(e)

    def buildEnv(self, e):
        for key, val in e.items():
            if key.find(".") != -1:
                continue
            self.all_keys[key.lower()] = val
            setattr(self, key.lower(), val)

    def keys(self):
        return self.all_keys

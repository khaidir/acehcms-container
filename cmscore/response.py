class CMSResponse:

    def __init__(self, r):
        self.generateResponse(r)

    def generateResponse(self, r):
        self.resStatus = r.status
        with open(r.filename, 'rb') as f:
            content = f.read()
            self.resContent = content if content else b"\n"

        self.resHeaders = [
            ("Content-Type", r.mimetype),
            ("Content-Length", str(len(self.resContent)))
        ]

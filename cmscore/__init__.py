from .environtment import CMSEnvirontment
from .domain import CMSDomain
from .routes import CMSRoutes
from .response import CMSResponse


class AcehCMS:

    def __init__(self, e):
        self.buildResponse(e)

    def buildResponse(self, e):
        e = CMSEnvirontment(e)
        d = CMSDomain(e)
        r = CMSRoutes(e, d)

        self.cms = CMSResponse(r)

    def responseContent(self):
        return iter([self.cms.resContent])

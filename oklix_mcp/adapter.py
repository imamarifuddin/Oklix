from core.asp.service import ASPService


class MCPAdapter:
    def __init__(self):
        self.service = ASPService()

    def optimize(self, request):
        return self.service.optimize(request)
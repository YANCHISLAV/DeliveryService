from fastapi import Request

class DependsManager:
    def __init__(self, request: Request) -> None:
        self.db = request.app.state.db
        self.cache = request.app.state.cache



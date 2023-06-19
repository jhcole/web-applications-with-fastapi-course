from starlette.requests import Request

class ViewModelBase:

    def __init__(self, request: Request) -> None:
        self.request: Request = request
        self.error: str | None = None
        self.user_id: int | None = None

    def to_dict(self) -> dict:
        return self.__dict__
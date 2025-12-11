class DomainError(Exception):
    def __init__(self, reason: str,*args):
        self.reason = reason
        super().__init__(*args)




class AlreadyExistsError(DomainError):
    def __init__(self, reason, *args):
        super().__init__(f"Already exist: {reason}", *args)


class NotFoundError(DomainError):
    def __init__(self, reason, *args):
        super().__init__(f"Not found: {reason}", *args)


        
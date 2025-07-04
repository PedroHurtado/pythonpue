class NotFoundException(Exception):
    def __init__(self, message: str, code=404):
        self._code = code
        super().__init__(message)

    @property
    def code(self):
        return self._code

    @property
    def message(self):
        return self.args[0] if self.args else ""

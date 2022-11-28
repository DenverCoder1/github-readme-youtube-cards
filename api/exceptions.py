class StatusException(Exception):
    status: int


class ValidationError(StatusException, ValueError):
    """Exception raised when a validation error occurs."""

    def __init__(self, message, status=400):
        super().__init__(message)
        self.status = status

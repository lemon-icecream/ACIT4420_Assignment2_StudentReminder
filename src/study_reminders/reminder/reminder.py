class Reminder:
    """Represents a reminder with a message."""

    def __init__(self, message: str) -> None:
        """Initialize a reminder with the given message."""
        self.__message = message

    def __str__(self) -> str:
        return f"{self.__message}"

    @property
    def message(self) -> str:
        return self.__message

class Student:
    """Represents a student with contact and course information."""

    def __init__(self, name: str, email: str, course: str, preferred_time="08:00") -> None:
        self.__name = name
        self.__email = email
        self.__course = course
        self.__preferred_time = preferred_time

    def __str__(self) -> str:
        return f"Name: {self.__name}, Email: {self.__email}, Course: {self.__course}, Preferred Time: {self.__preferred_time}"

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def course(self) -> str:
        return self.__course

    @property
    def preferred_time(self) -> str:
        return self.__preferred_time

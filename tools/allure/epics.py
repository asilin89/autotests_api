from enum import Enum

class AllureEpics(str, Enum):
    LMS = "LMS service"
    STUDENT = "Student service"
    ADMINISTRATION = "Administration service"
from dataclasses import dataclass

@dataclass
class Education:
    """Profile education definition
    """
    qualification: str
    institute: str
    city: str = None
    startMonth: int = None
    startYear: int = None
    endMonth: int = None
    endYear: int = None
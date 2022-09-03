from dataclasses import dataclass

@dataclass
class Experience:
    """Profile experience definition
    """
    description: str
    company: str
    position: str = None
    startMonth: int = None
    startYear: int = None
    endMonth: int = None
    endYear: int = None
    city: str = None

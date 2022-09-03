from dataclasses import dataclass

@dataclass
class ProfileLanguage:
    """Language element definition
    """
    name: str
    languageLevel: str = None

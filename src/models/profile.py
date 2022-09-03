from dataclasses import dataclass, field
from dto.profile_skill import ProfileSkill
from dto.profile_language import ProfileLanguage
from dto.experience import Experience
from dto.education import Education
from dto.project import Project
from dto.profile_certificate import ProfileCertificate
from dto.social_media import SocialMedia

from typing import List

@dataclass
class Profile:
    """Profile information definition
    """
    firstName: str = None
    lastName: str = None
    email: str = None
    phoneNumber: str = None
    address: str = None
    address2: str = None
    city: str = None
    country: str = None
    birthDate: str = None
    citizenship: str = None
    gender: str = None
    profile: str = None
    contract: str = None
    tjm: float = None
    salary: float = None
    experienceInMonth: int = None
    mobility: str = None
    availability: str = None
    levelOfStudies: str = None
    aboutMe: str = None
    workStatus: str = None
    
    profileSkills: List[ProfileSkill] = field(default_factory=list)
    experiences: List[Experience] = field(default_factory=list)
    projects: List[Project] = field(default_factory=list)
    profileLanguages: List[ProfileLanguage] = field(default_factory=list)
    profileCertificates: List[ProfileCertificate] = field(default_factory=list)
    educations: List[Education] = field(default_factory=list)
    socialMedia: List[SocialMedia] = field(default_factory=list)

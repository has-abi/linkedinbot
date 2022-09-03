from dataclasses import dataclass
from dto.skill_category import SkillCategory

@dataclass
class ProfileSkill:
    """Profile Skill definition
    """
    name: str
    skillCategory: SkillCategory
    
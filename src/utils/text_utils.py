import re
from typing import List

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_emails(text: str) -> List[str]:
    """Extract emails addresses from text

    Args:
        text (str): Plain text

    Returns:
        List[str]: List of extracted Email addresses
    """
    email_regex = re.compile(r'[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-zA-Z]+')
    emails = email_regex.findall(text)
    
    return emails

def extract_phone_numbers(text: str) -> List[str]:
    """Extract phone numbers from text

    Args:
        text (str): Plain text

    Returns:
        List[str]: List of extracted Phone numbers
    """
    phone_regex = re.compile(r'[(]?[+]?[+]?[(]?[0-9][0-9 .\-\(\)]{8,}[0-9]')
    phone_numbers = phone_regex.findall(text)

    return phone_numbers
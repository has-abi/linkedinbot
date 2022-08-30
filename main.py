import re
import os
from typing import Any, List

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import argparse
from dotenv import load_dotenv

load_dotenv()

def parse_args():

    parser = argparse.ArgumentParser(description='LinkedIn Scrapper')

    parser.add_argument('--profile', help='LinkedIn profile',
                        required=True, type=str)
    parser.add_argument('--uname', help='LinkedIn username', type=str, default="")
    parser.add_argument('--pwd', help='LinkedIn username', type=str, default="")

    args = parser.parse_args()
    return args

def login(driver: Any, username: str, pwd: str) -> None:
    """Login to a LinkedIn account

    Args:
        driver (Any): The web driver
        username (str): LinkedIn username
        pwd (str): LinkedIn password
    """

    driver.get("https://www.linkedin.com/login")

    #Fill in a username
    username_elem = driver.find_element(By.ID, "username")
    username_elem.clear()
    username_elem.send_keys(username)

    # Fill in password
    pwd_elem = driver.find_element(By.ID, "password")
    pwd_elem.clear()
    pwd_elem.send_keys(pwd)

    driver.find_element(By.XPATH, "//button[@data-litms-control-urn='login-submit']").click()

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


def main():
    args = parse_args()
    env_username = os.environ.get("LINKEDIN_USERNAME")
    env_pwd = os.environ.get("LINKEDIN_PWD")

    username = args.uname if args.uname else env_username
    pwd = args.pwd if args.pwd else env_pwd

    if username and pwd:

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        login(driver=driver, username=username, pwd=pwd)
        
        driver.get(f"https://www.linkedin.com/in/{args.profile}/overlay/contact-info/")

        elems = driver.find_elements(By.CLASS_NAME, "pv-contact-info__ci-container")

        profile_infos = " ".join([elem.text for elem in elems])

        founded_emails = extract_emails(profile_infos)
        founded_phone_numbers = extract_phone_numbers(profile_infos)

        if founded_emails:
            print("Founded Emails: ", founded_emails)
        if founded_phone_numbers:
            print("Founded phone numbers: ", founded_phone_numbers)
        
        if not (founded_emails or founded_phone_numbers):
            print("No Emails or phone numbers founded!")
    else:
        raise ValueError("No username or password were provided!")

if __name__ == '__main__':
    main()

import json
import os
import time
from typing import Dict
from timeit import default_timer as timer

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from http_constants.status import HttpStatus
from flask import jsonify
from linkedin_api import Linkedin
from requests.cookies import cookiejar_from_dict

from ..scrapers.profile_scraper import Profile

def login(driver: ChromiumDriver, username: str, pwd: str) -> None:
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

def scrap_linkedin_profile(profile_username: str) -> Dict:

    start = timer()
    username = os.environ.get("LINKEDIN_USERNAME")
    pwd = os.environ.get("LINKEDIN_PWD")
    print(username)
    print(pwd)
    if username and pwd:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        login(driver=driver, username=username, pwd=pwd)
        
        profile_url = f"https://www.linkedin.com/in/{profile_username}/"

        profile = Profile(profile_url=profile_url, driver=driver)
        linkedin_profile = {}
        linkedin_profile["personal_infos"] = profile.get_personal_informations()
        linkedin_profile["experiences"] = profile.get_experiences()
        linkedin_profile["educations"] = profile.get_educations()
        linkedin_profile["certificats"] = profile.get_certification()
        linkedin_profile["skills"] = profile.get_skills()
        driver.close()
        print(f'Response Time: {timer() - start}')

        return linkedin_profile, HttpStatus.OK

    else:
        return jsonify({
            "error": "No credentials provided!"
        })

def scrap_p(profile_username):

    start = timer()
    username = os.environ.get("LINKEDIN_USERNAME")
    pwd = os.environ.get("LINKEDIN_PWD")
    cookies = cookiejar_from_dict(
    {
        "liap": "true",
        "li_at": os.environ["LINKEDIN_COOKIE_LI_AT"],
        "JSESSIONID": os.environ["LINKEDIN_COOKIE_JSESSIONID"],
    }
)
    # Authenticate using any Linkedin account credentials
    api = Linkedin(username, pwd, cookies=cookies)

    # GET a profile
    profile = api.get_profile(profile_username)
    contact_info = api.get_profile_contact_info(profile_username)
    print(f'Response Time: {timer() - start}')
    return profile

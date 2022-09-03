from typing import Dict, List
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from ..utils.text_utils import clean_text

class Profile:
    def __init__(self, profile_url: str, driver: ChromiumDriver) -> None:
        self.profile_url = profile_url
        self.driver = driver
        self.driver.get(profile_url)

    
    def get_personal_informations(self) -> Dict:
        time.sleep(1)
        source_page = BeautifulSoup(self.driver.page_source, "html.parser")
        
        full_name_elem = source_page.find("h1", class_="text-heading-xlarge")
        title_elem = source_page.find("div", class_="text-body-medium")
        # extra = source_page.find("div", class_="pv-text-details__left-panel")
        address_elem = source_page.find("span", class_="text-body-small inline t-black--light break-words")
      
        about_section = source_page.find("div",class_="pv-shared-text-with-see-more t-14 t-normal t-black display-flex align-items-center")
            
        full_name = clean_text(full_name_elem.text) if full_name_elem else ""
        title = clean_text(title_elem.text) if title_elem else ""
        address = clean_text(address_elem.text) if address_elem else ""
        
        about = clean_text(about_section.find("span", class_="visually-hidden").text) if about_section else ""

        profile = {
            "full name": full_name,
            "title": title,
            "address": address,
            "about": about 
            }

        print(profile)
        return profile

    def get_experiences(self) -> List[Dict]:
        self.driver.get(f"{self.profile_url}/details/experience/")
        time.sleep(5)
        source_page = BeautifulSoup(self.driver.page_source, "html.parser")
        main_experiences = source_page.find("main", class_="scaffold-layout__main")
        experiences_container = main_experiences.find("div", class_="pvs-list__container")
        experiences_scroller = experiences_container.find("div", class_="scaffold-finite-scroll scaffold-finite-scroll--infinite")
        experiences_list = experiences_scroller.find("ul", class_="pvs-list")
        experiences = []
        if experiences_list:
            experiences_list_elems = experiences_list.find_all("li", class_="pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated")
            for li in experiences_list_elems:
                try:
                    exp = {}
                 
                    position_span = li.find("span", class_="mr1 t-bold").find("span", class_="visually-hidden")
                    exp["position"] = clean_text(position_span.text)

                    company_span = li.find("span", class_="t-14 t-normal").find("span", class_="visually-hidden")
                    exp["company"] = clean_text(company_span.text)

                    extras = li.find_all("span", class_="t-14 t-normal t-black--light")

                    date_span = extras[0].find("span", class_="visually-hidden")
                    exp["date"] = clean_text(date_span.text)

                    if len(extras) > 1:
                        location_span = extras[1].find("span", class_="visually-hidden")
                        exp["location"] = clean_text(location_span.text)

                    desc_container = li.find("div", class_="pvs-list__outer-container")
                    description = []
                    if desc_container:
                        desc_list = desc_container.find("ul", class_="pvs-list")
                        desc_list_items = desc_list.find_all("li", class_="pvs-list__item--with-top-padding")
                        for li in desc_list_items:
                            desc_elem = li.find("span", class_="visually-hidden")
                            if desc_elem:
                                description.append(clean_text(desc_elem.text))
                    
                    exp["description"] = " ".join(description)

                    experiences.append(exp)
                except Exception:
                    pass
            return experiences

    def get_educations(self) -> List[Dict]:
        self.driver.get(f"{self.profile_url}/details/education/")
        time.sleep(5)
        source_page = BeautifulSoup(self.driver.page_source, "html.parser")
        main_educations = source_page.find("main", class_="scaffold-layout__main")
        educations_container = main_educations.find("div", class_="pvs-list__container")
        education_scroller = educations_container.find("div", class_="scaffold-finite-scroll scaffold-finite-scroll--infinite")
        educations_list = education_scroller.find("ul", class_="pvs-list")
        educations = []
        if educations_list:
            educations_list_elems = educations_list.find_all("li", class_="pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated")
            for li in educations_list_elems:
                # try:
                    education = {}
                 
                    institute_span = li.find("span", class_="mr1 hoverable-link-text t-bold").find("span", class_="visually-hidden")
                    education["institute"] = clean_text(institute_span.text)

                    qualification_span = li.find("span", class_="t-14 t-normal")
                    if qualification_span:
                        education["qualification"] = clean_text(qualification_span.find("span", class_="visually-hidden").text)

                    extras = li.find_all("span", class_="t-14 t-normal t-black--light")

                    date_span = extras[0].find("span", class_="visually-hidden")
                    education["date"] = clean_text(date_span.text)

                    desc_container = li.find("div", class_="pvs-list__outer-container")
                    description = []
                    if desc_container:
                        desc_list = desc_container.find("ul", class_="pvs-list")
                        desc_list_items = desc_list.find_all("li")
                        for li in desc_list_items:
                            desc_elem = li.find("span", class_="visually-hidden")
                            if desc_elem:
                                description.append(clean_text(desc_elem.text))
                    
                    education["description"] = " ".join(description)

                    educations.append(education)
                # except Exception:
                #     pass
            return educations
    
    def get_certification(self) -> List[Dict]:
        self.driver.get(f"{self.profile_url}/details/certifications/")
        time.sleep(5)
        source_page = BeautifulSoup(self.driver.page_source, "html.parser")
        main_certification = source_page.find("main", class_="scaffold-layout__main")
        certification_container = main_certification.find("div", class_="pvs-list__container")
        certification_scroller = certification_container.find("div", class_="scaffold-finite-scroll scaffold-finite-scroll--infinite")
        certification_list = certification_scroller.find("ul", class_="pvs-list")
        certificats = []
        if certification_list:
            educations_list_elems = certification_list.find_all("li", class_="pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated")
            for li in educations_list_elems:
                try:
                    certificate = {}
                 
                    title_span = li.find("span", class_="mr1 t-bold").find("span", class_="visually-hidden")
                    certificate["title"] = clean_text(title_span.text)

                    issuer_span = li.find("span", class_="t-14 t-normal").find("span", class_="visually-hidden")
                    certificate["issuer"] = clean_text(issuer_span.text)

                    extras = li.find_all("span", class_="t-14 t-normal t-black--light")

                    date_span = extras[0].find("span", class_="visually-hidden")
                    certificate["issued"] = clean_text(date_span.text)

                    certificats.append(certificate)
                except Exception:
                    pass
            return certificats

    def get_skills(self) -> List[str]:
        self.driver.get(f"{self.profile_url}/details/skills/")
        time.sleep(5)
        source_page = BeautifulSoup(self.driver.page_source, "html.parser")
        main_skills = source_page.find("main", class_="scaffold-layout__main")
        skills_container = main_skills.find("div", class_="pvs-list__container")
        skills_scroller = skills_container.find("div", class_="scaffold-finite-scroll scaffold-finite-scroll--infinite")
        skills_list = skills_scroller.find("ul", class_="pvs-list")
        skills = []

        if skills_list:
            educations_list_elems = skills_list.find_all("li", class_="pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated")
            for li in educations_list_elems:
                try:
                    skill_span = li.find("span", class_="mr1 t-bold").find("span", class_="visually-hidden")
                    skill = clean_text(skill_span.text)
                    skills.append(skill)
                except Exception:
                    pass

        return skills
        










import time
import random
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from typing import List

from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions


class LinkedinCrawlException(Exception):
    pass


class LinkedinAuthException(Exception):
    pass


class LinkedInProfile:

    name_xpath = '//ul[@class="pv-top-card--list inline-flex align-items-center"]//li[@class="inline t-24 t-black t-normal break-words"]'

    org_xpath = '//a[@class="pv-top-card--experience-list-item"]//span[@class="text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view"]'

    designation_xpath = '//h3[@class="t-16 t-black t-bold"]'

    profile_not_found_class = "pv-profile-unavailable"

    def __init__(self, name_element=None, desig_element=None, org_element=None):

        self.name = name_element[0].text
        self.designation = desig_element[0].text
        self.org_name = org_element[0].text
        pass


class LinkedinCrawler:

    li_auth_cookie = {'domain': 'www.linkedin.com',
                      'expiry': 1633092767,
                      'httpOnly': True,
                      'name': 'li_at',
                      'path': '/',
                      'sameSite': 'None',
                      'secure': True,
                      'value': ''
                      }

    LinkedinHomePage = "https://www.linkedin.com"

    def __init__(self, li_at=None, chromedriver=None):

        if li_at is None:
            raise LinkedinCrawlException(
                "Linkedin Auth token is required for crawling")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        if chromedriver is not None:
            self.driver = webdriver.Chrome(
                chromedriver, chrome_options=chrome_options)
        else:
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(self.LinkedinHomePage)
        self.driver.add_cookie(self.get_cookie_with_li_at(li_at))

    def destroy_driver(self):
        if self.driver is not None:
            self.driver.close()

    def get_cookie_with_li_at(self, li_at):
        new_cookie = self.li_auth_cookie.copy()
        new_cookie["value"] = li_at
        return new_cookie

    def get_profile_objects(self, profile_urls: List[str]):
        profiles = {}
        for profile_url in profile_urls:
            try:
                profiles[profile_url] = self.get_profile_obj(profile_url)
                sleep_time = random.random() + 1
                time.sleep(sleep_time)
            except LinkedinCrawlException as e:
                print(f"Error getting data for profile {profile_url}")
                profiles[profile_url] = e
            except LinkedinAuthException as e:
                print(f"Error getting data for profile {profile_url}")
                profiles[profile_url] = e
        return profiles

    def get_profile_obj(self, profile_url):
        self.driver.get(profile_url)

        if "authwall" in self.driver.current_url:
            raise LinkedinAuthException(
                "[LINKEDIN] [PROFILE] [CRAWLING] Linkedin auth issue")
        if len(self.driver.find_elements_by_class_name(LinkedInProfile.profile_not_found_class)) > 0:
            raise LinkedinCrawlException(
                f"[LINKEDIN] [PROFILE] [CRAWLING] Linkedin profile not found {profile_url}")
        if self.driver.current_url in ["https://www.linkedin.com/in/unavailable/", "http://www.linkedin.com/in/unavailable/"]:
            raise LinkedinCrawlException(
                f"[LINKEDIN] [PROFILE] [CRAWLING] Linkedin profile not found {profile_url}")
        try:
            name_element = self.driver.find_elements_by_xpath(
                LinkedInProfile.name_xpath)
            org_element = self.driver.find_elements_by_xpath(
                LinkedInProfile.org_xpath)
            designation_element = self.driver.find_elements_by_xpath(
                LinkedInProfile.designation_xpath)

            profile_object = LinkedInProfile(name_element=name_element, org_element=org_element,
                                             desig_element=designation_element)
        except Exception as e:
            raise LinkedinCrawlException(
                f"Probable issue parsing the page {self.driver.current_url}")

        return profile_object

    def wait_for_page_load(self, driver, delay=5):

        try:
            myElem = WebDriverWait(driver, delay).until(
                expected_conditions.presence_of_element_located((By.ID, 'ember1021')))
        except TimeoutException:
            raise LinkedinCrawlException(
                "Timed out waiting for right element to appear")
        pass

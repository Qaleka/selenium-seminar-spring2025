from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ui.locators import people_locators
from ui.pages.base_page import BasePage
from ui.pages.user_page import UserPage
from urllib.parse import quote

class PeoplePage(BasePage):
    url = "https://education.vk.company/people/"
    locators = people_locators.PeoplePageLocators()

    def find_user(self, username):
        search_bar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.SEARCH_BAR)
        )
        search_bar.clear()
        search_bar.send_keys(username)
        search_bar.send_keys(Keys.ENTER)

        encoded_username = quote(username)
        expected_url_part = f"?q={encoded_username}"

        WebDriverWait(self.driver, 10).until(
            lambda d: expected_url_part in d.current_url
        )

        link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.USER_LINK)
        )
        
        WebDriverWait(self.driver, 10).until(
            lambda d: username.lower() in d.find_element(*self.locators.USER_LINK).text.lower()
        )

        href = link.get_attribute("href")
        link.click()

        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(href)
        )

        return UserPage(self.driver)
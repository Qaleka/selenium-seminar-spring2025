from ui.locators import user_locators
from ui.pages.base_page import BasePage
from dotenv import load_dotenv
load_dotenv()

class UserPage(BasePage):
    check_url = False
    locators = user_locators.UserPageLocators()

    def get_about(self):
        about_info = self.find(self.locators.ABOUT_INFO)
        return about_info.text
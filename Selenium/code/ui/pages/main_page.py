import time

from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.lesson_page import LessonPage
from ui.pages.people_page import PeoplePage


class MainPage(BasePage):
    url = "https://education.vk.company/feed/"
    locators = basic_locators.MainPageLocators()

    def close_popup(self):
        self.click(self.locators.CLOSE_POPUP_BUTTON)
        return

    def go_to_people_page(self):
        self.click(self.locators.PEOPLE_PAGE_LINK)
        return PeoplePage(self.driver)

    def open_lesson(self, date):
        locator = self.locators.get_lesson_link(date)
        while True:
            if len(self.driver.find_elements(*locator)) > 0:
                break
            self.click(self.locators.LESSONS_SLIDER_LEFT_BTN)
            

        link = self.find(locator)
        lesson_url = link.get_attribute("href")
        link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == lesson_url, \
            f"Expected URL: {lesson_url}, actual URL: {self.driver.current_url}"
        return LessonPage(self.driver)
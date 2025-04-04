from base import BaseCase
from _pytest.fixtures import FixtureRequest

class TestLogin(BaseCase):
    authorize = False

    def test_login(self, request:FixtureRequest):
        credentials = request.getfixturevalue("credentials")
        print(credentials)
        self.login_page.login(*credentials)
        assert "Лента" in self.driver.title


class TestLK(BaseCase):
    authorize = True
    def test_user_about_info(self):
        # Открываем страницу "Люди"
        self.main_page.close_popup()
        self.people_page = self.main_page.go_to_people_page()

        self.user_page = self.people_page.find_user("Балюк")
        about = self.user_page.get_about()
        assert "Балюк Андрей, ученик группы ИУ5-83Б" in about

    def test_audience(self):
        self.main_page.close_popup()
        self.lesson_page = self.main_page.open_lesson("чт, 3 апреля")

        # Проверяем аудиторию
        audition = self.lesson_page.get_audition()
        assert "Аудитория 395 - зал 1,2 (МГТУ)" in audition
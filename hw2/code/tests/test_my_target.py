import datetime
from time import sleep

import pytest
from selenium.common.exceptions import TimeoutException

from tests.base import BaseCase


class TestClass(BaseCase):
    @pytest.mark.UI
    def test_auth(self, auth):
        user_login = self.config['email']
        assert auth.find(auth.locator.CHECK_AUTH(user_login))

    @pytest.mark.UI
    def test_auth_negative(self, incorrect_input):
        main_page = incorrect_input
        main_page.find(main_page.locator.ERROR)
        user_login = self.config['fake_email']
        with pytest.raises(TimeoutException):
            main_page.find(main_page.locator.CHECK_AUTH(user_login))

    @pytest.mark.UI
    def test_create_company(self, auth, generated_data):
        main_page = auth
        path, name = generated_data
        main_page.create_company(path)
        main_page.check_company_created(name)
        main_page.delete_company(name)

    @pytest.mark.UI
    def test_segment_create(self, auth):
        name = 'New segment ' + str(datetime.datetime.now())
        self.segment_page.create_segment(name)
        self.segment_page.find(self.segment_page.locator.NAME_LOCATOR(name))
        self.segment_page.delete_segment(name)

    @pytest.mark.UI
    def test_segment_delete(self, auth):
        name = 'New segment ' + str(datetime.datetime.now())
        self.segment_page.create_segment(name)
        self.segment_page.delete_segment(name)
        sleep(3)
        with pytest.raises(TimeoutException):
            self.segment_page.find(self.segment_page.locator.NAME_LOCATOR(name), timeout=5)

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
        try:
            main_page.find(main_page.locator.ERROR)
        except TimeoutException:
            assert False

    @pytest.mark.UI
    def test_create_company(self, auth, generated_data):
        path, name = generated_data
        main_page = auth
        main_page.create_company(path)
        main_page.find(main_page.locator.CHECK(name))
        try:
            main_page.delete_company(name)
        except TimeoutException:
            pass

    @pytest.mark.UI
    def test_segment_create(self, auth, generated_data):
        name = generated_data[1]
        self.segment_page.create_segment(name)
        try:
            self.segment_page.find(self.segment_page.locator.NAME_LOCATOR(name))
        except TimeoutException:
            assert False
        self.segment_page.delete_segment(name)

    @pytest.mark.UI
    def test_segment_delete(self, auth, generated_data):
        name = generated_data[1]
        self.segment_page.create_segment(name)
        try:
            self.segment_page.find(self.segment_page.locator.NAME_LOCATOR(name))
        except TimeoutException:
            assert False
        self.segment_page.delete_segment(name)
        self.segment_page.find(self.segment_page.locator.NAME_LOCATOR(name))




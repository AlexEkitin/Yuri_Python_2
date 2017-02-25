from selenium import webdriver

from fixture.group_helper import GroupHelper
from fixture.session_helper import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome("C:\Windows\SysWOW64\chromedriver.exe")
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

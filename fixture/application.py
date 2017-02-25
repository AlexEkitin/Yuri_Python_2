from selenium import webdriver

from fixture.contact_helper import ContactHelper
from fixture.group_helper import GroupHelper
from fixture.session_helper import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome("C:\Windows\SysWOW64\chromedriver.exe")  # inicializaciya WebDriver
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def go_to_home_page(self):
        wd = self.wd  # izvlechenie ssilki na WebDriver
        wd.find_element_by_link_text("home page").click()


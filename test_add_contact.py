import unittest

from selenium import webdriver

from contact import Contact


class test_add_contact(unittest.TestCase):
    def setUp(self):
        # wd - zapusk WebDriver (brouser)
        self.wd = webdriver.Chrome("C:\Windows\SysWOW64\chromedriver.exe")
        self.wd.implicitly_wait(60)

    def test_add_contact(self):  # self - obekt, v kotorom vizivaetsa metod
        success = True
        wd = self.wd  # izvlechenie ssilki na WebDriver
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Contact(firstname="fsdgsdfg", lastname="xcbsv", address="cfhdsfh", home_phone="fdghsdfh",
                                      email_1="sdfgh"))
        self.logout(wd)

    def test_add_empty_contact(self):  # self - obekt, v kotorom vizivaetsa metod
        success = True
        wd = self.wd  # izvlechenie ssilki na WebDriver
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Contact(firstname="", lastname="", address="", home_phone="", email_1=""))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def go_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_group(self, wd, contact):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.go_to_home_page(wd)

    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()

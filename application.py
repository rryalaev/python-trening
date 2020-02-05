from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def login(self, username, password):
        self.driver.get("http://localhost/addressbook/")
        self.driver.set_window_size(1050, 708)
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.NAME, "pass").send_keys(Keys.ENTER)

    def create_group(self, group):
        self.driver.find_element(By.LINK_TEXT, "groups").click()
        self.driver.find_element(By.NAME, "new").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        self.driver.find_element(By.NAME, "submit").click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def destroy(self):
        self.driver.quit()
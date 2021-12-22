from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def click_login_button(self):
        element: WebElement = self.driver.find_element(By.ID, "emp-button")
        return element

    def click_request_reimbursement_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "request")
        return element


    def click_submit_reimbursement_button(self):
        element: WebElement = self.driver.find_element(By.CLASS_NAME, "submit-button")
        return element


    def click_view_reimbursement_button(self):
        element: WebElement = self.driver.find_element(By.ID, "view")
        return element


    def click_logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "emp-logout")
        return element
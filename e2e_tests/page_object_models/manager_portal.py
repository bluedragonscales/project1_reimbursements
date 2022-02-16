from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ManagerPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def select_manager_username_input(self):
        element: WebElement = self.driver.find_element(By.ID, "mana-username")
        return element

    def select_manager_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "mana-password")
        return element

    def select_manager_login_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/div[2]/button")
        return element

    def select_manager_pending_reimburse_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/nav/button[2]")
        return element

    def select_manager_reimburse_id_input(self):
        element: WebElement = self.driver.find_element(By.ID, "r-id")
        return element

    def select_reimburse_id_for_approval(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[1]/td[1]")
        return element

    def select_manager_reason_input(self):
        element: WebElement = self.driver.find_element(By.ID, "status-reason")
        return element

    def select_manager_approve_button(self):
        element: WebElement = self.driver.find_element(By.ID, "approve-status")
        return element

    def select_status_change_message(self):
        element: WebElement = self.driver.find_element(By.ID, "status-message")
        return element
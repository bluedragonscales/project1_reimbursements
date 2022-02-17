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
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/section/div[2]/button")
        return element

    def select_manager_pending_reimburse_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/nav/button[2]")
        return element

    def select_manager_reimburse_id_input(self):
        element: WebElement = self.driver.find_element(By.ID, "r-id")
        return element

    def select_reimburse_id_for_approval(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/section[2]/div/table/tbody/tr[1]/td[1]")
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

    def select_reimburse_id_for_denial(self):
        element: WebElement = self.driver.find_element(By.XPATH, "html/body/section[2]/div/table/tbody/tr[2]/td[1]")
        return element

    def select_manager_deny_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deny-status")
        return element

    def select_past_reimbursements_tab(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/nav/button[3]")
        return element

    def select_already_approved_reimbursement(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/section[3]/div[1]/table/tbody/tr[1]/td[3]")
        return element

    def select_already_denied_reimbursement(self):
        element: WebElement = self.driver.find_element(By.XPATH, "html/body/section[3]/div[2]/table/tbody/tr[1]/td[3]")
        return element

    def select_manager_logout_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "mana-logout")
        return element
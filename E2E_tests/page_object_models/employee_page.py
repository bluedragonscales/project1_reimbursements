from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class EmployeePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # TO LOG IN
    # This method is to select the input box needed for the employee to enter their employee id.
    def select_input_id_box(self):
        element: WebElement = self.driver.find_element(By.ID, "emp-username")
        return element

    # This method is to select the input box needed for the employee to enter their password.
    def select_input_password_box(self):
        element: WebElement = self.driver.find_element(By.ID, "emp-password")
        return element

    # This method is to select the login button so that the employee can be logged in.
    def click_login_button(self):
        element: WebElement = self.driver.find_element(By.ID, "emp-button")
        return element



    # Methods to submit a new reimbursement request.
    # This method takes employee to the request form.
    def click_request_reimbursement_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "request")
        return element


    # This method selects the request purpose input box.
    def select_request_purpose_input(self):
        element: WebElement = self.driver.find_element(By.ID, "purpose")
        return element

    # This method selects the amount input box.
    def select_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "amount")
        return element


    # This method selects the submit reimbursement button.
    def click_submit_reimbursement_button(self):
        element: WebElement = self.driver.find_element(By.ID, "r-submit")
        return element


    # Method to look at reimbursements
    # This method selects the view reimbursements tab.
    def click_view_reimbursement_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "view")
        return element



    # Method to logout
    # This method selects the logout button.
    def click_logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "emp-logout")
        return element
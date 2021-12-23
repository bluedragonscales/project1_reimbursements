from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ReimbursementPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # TO LOG IN EMPLOYEES
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



    # FOR EMPLOYEES TO SUBMIT A NEW REIMBURSEMENT REQUEST
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


    # FOR EMPLOYEES TO LOOK AT THEIR REIMBURSEMENT REQUESTS
    # This method selects the view reimbursements tab.
    def click_view_reimbursement_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "view")
        return element



    # FOR EMPLOYEES TO LOG OUT
    # This method selects the logout button.
    def click_logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "emp-logout")
        return element





    # FOR MANAGERS TO LOG IN
    # This method is to select the input box needed for the manager to enter their employee id.
    def select_manager_id_box(self):
        element: WebElement = self.driver.find_element(By.ID, "mana-username")
        return element

    # This method is to select the input box needed for the manager to enter their password.
    def select_manager_password_box(self):
        element: WebElement = self.driver.find_element(By.ID, "mana-password")
        return element

    # This method is to select the login button so that the manager can be logged in.
    def click_manager_login_button(self):
        element: WebElement = self.driver.find_element(By.ID, "mana-button")
        return element



    # FOR MANAGERS TO ASSIGN A STATUS ON A REIMBURSEMENT
    # This method takes the manager to the submit status form.
    def click_status_reimbursement_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "status")
        return element

    # This method selects the reimburse id input box.
    def select_reimburse_id_input(self):
        element: WebElement = self.driver.find_element(By.ID, "r-id")
        return element

    # This method selects the option for approve or deny.
    def select_option_input(self):
        element: WebElement = self.driver.find_element(By.ID, "denied")
        return element

    # This method selects the reason input box.
    def select_reason_input(self):
        element: WebElement = self.driver.find_element(By.ID, "status-reason")
        return element


    # This method selects the submit reimbursement button.
    def click_submit_status_button(self):
        element: WebElement = self.driver.find_element(By.ID, "submit-status")
        return element




    # FOR MANAGERS TO VIEW ALL REIMBURSEMENT REQUESTS
    def click_all_reimbursements_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "view")
        return element





    # FOR MANAGERS TO VIEW ALL REIMBURSEMENT STATISTICS
    # This method takes the manager to the view statistics form.
    def click_reimbursement_statistics_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "stats")
        return element

    # This method selects the option from the dropdown list.
    def select_statistic_option(self):
        element: WebElement = self.driver.find_element(By.ID, "count")
        return element


    # This method selects the submit statistic button.
    def click_statistic_submit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "submit-stats")
        return element



    # FOR MANAGERS TO LOG OUT
    # This method selects the logout button.
    def click_manager_logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "mana-logout")
        return element
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


# Use this page object model (POM) to grab the elements the driver needs to activate and push along selenium.
class EmployeePage:

    # Use the POM class constructor to inject a Chrome web driver that Selenium can use to drive the web pages.
    def __init__(self, driver: WebDriver):
        self.driver = driver


    # This method is creating a selenium web element, using the driver to find the element we want by its ID selector,
    # and then storing it inside the web element object. Lastly, it returns the element so that the steps can implement
    # the element we grabbed with the driver.
    def select_emp_username_input(self):
        element: WebElement = self.driver.find_element(By.ID, "emp-username")
        return element

    def select_emp_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "emp-password")
        return element


    # XPATH is the direct route of getting to the element from the DOM, starting at the top of the DOM and working down.
    # The path for this button starts at the root element, the html doc. Then it goes to the body (instead of the head),
    # then to the first instance of a button which is inside the section element, and inside the first div child of that
    # section.
    def select_emp_login_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/section/div[1]/button")
        return element


    def select_new_reimburse_tab(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/nav/button[2]")
        return element

    def select_reason_input(self):
        element: WebElement = self.driver.find_element(By.CSS_SELECTOR, 'textarea[cols="50"]')
        return element

    def select_amount_input(self):
        element: WebElement = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Amount"')
        return element

    def select_new_reimbursement_submit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "r-submit")
        return element

    def select_new_reimbursement_success_message(self):
        element: WebElement = self.driver.find_element(By.ID, "request-created")
        return element

    def select_pending_reimburse_tab(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/nav/button[3]")
        return element

    def select_populated_pending_reimbursement(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/section[3]/div/table/tbody/tr[1]/td[1]")
        return element

    def select_approved_reimburse_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "approved")
        return element

    def select_populated_approved_reimbursement(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/section[4]/div/table/tbody/tr[1]/td[1]")
        return element

    def select_denied_reimburse_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "denied")
        return element

    def select_populated_denied_reimbursement(self):
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/section[5]/div/table/tbody/tr[1]/td[1]")
        return element

    def select_logout_tab(self):
        element: WebElement = self.driver.find_element(By.ID, "emp-logout")
        return element
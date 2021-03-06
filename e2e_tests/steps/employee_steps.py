from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# STEPS TO LOG IN
@Given(u'the employee is on the login page')
def get_reimbursement_login_page(context):
    context.driver.get("file:///C:/Users/kckar/Desktop/Websites/project1_reimbursements/front-end/index.html")


@When(u'the employee types their username into the username input')
def employee_inputs_username(context):
    context.emp_home.select_emp_username_input().send_keys("JHal")
    # The "click()" and "send_keys()" functions are called ELEMENT FUNCTIONS.


@When(u'the employee types their password into the password input')
def employee_inputs_password(context):
    context.emp_home.select_emp_password_input().send_keys("DwightIsWeird")


@When(u'the employee clicks on the login button')
def employee_clicks_login_button(context):
    context.emp_home.select_emp_login_button().click()


@Then(u'the employee is redirected to the employee portal home page')
def employee_redirected_to_employee_portal_page(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.title_is("Employee Home"))
    assert context.driver.title == "Employee Home"



# STEPS TO REQUEST NEW REIMBURSEMENT
@Given(u'the employee is on the employee portal home page')
def employee_starts_on_emp_portal(context):
    assert context.driver.title == "Employee Home"


@When(u'the employee clicks the new reimbursement tab')
def employee_clicks_new_reimburse_tab(context):
    context.emp_home.select_new_reimburse_tab().click()


@When(u'the employee types the reason into the reason input')
def employee_inputs_reason(context):
    context.emp_home.select_reason_input().send_keys("Office supplies E2E test.")


@When(u'the employee types the amount into the amount input')
def employee_inputs_amount(context):
    context.emp_home.select_amount_input().send_keys("58.29")


@When(u'the employee clicks the submit button')
def employee_clicks_submit_button(context):
    context.emp_home.select_new_reimbursement_submit_button().click()


@Then(u'a success message will populate')
def success_message_populates(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.ID, "request-created"), "Your request has been submitted."))
    assert context.emp_home.select_new_reimbursement_success_message().text == "Your request has been submitted."




# STEPS TO VIEW PAST REIMBURSEMENTS
@When(u'the employee clicks the Pending reimbursements tab')
def employee_clicks_pending_tab(context):
    context.emp_home.select_pending_reimburse_tab().click()


@Then(u'the Pending reimbursements will populate')
def pending_reimbursements_populate(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element(
        (By.XPATH, "/html/body/section[3]/div/table/tbody/tr[1]/td[1]"), "Office supplies E2E test."
    ))
    assert context.emp_home.select_populated_pending_reimbursement().text == "Office supplies E2E test."



# STEPS TO VIEW APPROVED REIMBURSEMENTS
@When(u'the employee clicks the Approved reimbursements tab')
def employee_clicks_approved_tab(context):
    context.emp_home.select_approved_reimburse_tab().click()


@Then(u'the Approved reimbursements will populate')
def approved_reimbursements_populate(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element(
        (By.XPATH, "/html/body/section[4]/div/table/tbody/tr[1]/td[1]"), "Office supplies testing"
    ))
    assert context.emp_home.select_populated_approved_reimbursement().text == "Office supplies testing"



# STEPS TO VIEW DENIED REIMBURSEMENTS
@When(u'the employee clicks the Denied reimbursements tab')
def employee_clicks_denied_tab(context):
    context.emp_home.select_denied_reimburse_tab().click()


@Then(u'the Denied reimbursements will populate')
def denied_reimbursements_populate(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element(
        (By.XPATH, "/html/body/section[5]/div/table/tbody/tr[1]/td[1]"), "Jello mix"
    ))
    assert context.emp_home.select_populated_denied_reimbursement().text == "Jello mix"



# STEPS TO LOG OUT
@When(u'the employee clicks the log out tab')
def employee_clicks_logout_tab(context):
    context.emp_home.select_logout_tab().click()


@Then(u'the employee will be redirected to the login page')
def employee_redirected_to_login_page(context):
    assert context.driver.title == "Home"

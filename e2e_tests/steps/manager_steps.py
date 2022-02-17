from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# MANAGER LOGIN STEPS
@Given(u'the manager is on the login page')
def get_home_login_page(context):
    context.driver.get("file:///C:/Users/kckar/Desktop/Websites/project1_reimbursements/front-end/index.html")


@When(u'the manager types their username into the username input')
def manager_inputs_username(context):
    context.mana_home.select_manager_username_input().send_keys("agentscarn")


@When(u'the manager types their password into the password input')
def manager_inputs_password(context):
    context.mana_home.select_manager_password_input().send_keys("office1234")


@When(u'the manager clicks the login button')
def manager_clicks_login_button(context):
    context.mana_home.select_manager_login_button().click()


@Then(u'the manager will be redirected to the manager portal home page')
def manager_redirected_to_manager_portal(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.title_is("Manager Home"))
    assert context.driver.title == "Manager Home"




# MANAGER APPROVE REIMBURSEMENT STEPS
@Given(u'the manager is on the manager portal home page')
def manager_starts_on_home_page(context):
    assert context.driver.title == "Manager Home"


@When(u'the manager clicks on the pending reimbursements tab')
def manager_clicks_pending_reimburse_tab(context):
    context.mana_home.select_manager_pending_reimburse_button().click()


@When(u'the manager types the reimbursement id into the id input')
def manager_inputs_reimburse_id(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element((
        By.XPATH, "/html/body/section[2]/div/table/tbody/tr[1]/td[1]"
    ), context.mana_home.select_manager_reimburse_id_input().text))
    approve_reimburse = context.mana_home.select_reimburse_id_for_approval().text
    context.mana_home.select_manager_reimburse_id_input().send_keys(approve_reimburse)


@When(u'the manager types their reasoning into the reason input')
def manager_inputs_reasoning(context):
    context.mana_home.select_manager_reason_input().send_keys("Approved for e2e tests.")


@When(u'the manager clicks the approve button')
def manager_clicks_approve_button(context):
    context.mana_home.select_manager_approve_button().click()


@Then(u'an approved message appears')
def manager_approval_message_populates(context):
    approve_reimburse = context.mana_home.select_reimburse_id_for_approval().text
    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element((
        By.ID, "status-message"
    ), f"Reimbursement ID {approve_reimburse} has been approved."))
    assert context.mana_home.select_status_change_message().text == f"Reimbursement ID {approve_reimburse} has been " \
                                                                    f"approved."




# MANAGER DENY REIMBURSEMENT STEPS
@When(u'the manager types the bad reimburse id into the id input')
def manager_inputs_bad_id(context):
    context.mana_home.select_manager_reimburse_id_input().clear()
    deny_reimburse = context.mana_home.select_reimburse_id_for_denial().text
    context.mana_home.select_manager_reimburse_id_input().send_keys(deny_reimburse)


@When(u'the manager types a reason for denial into the reason input')
def manager_inputs_deny_reason(context):
    context.mana_home.select_manager_reason_input().clear()
    context.mana_home.select_manager_reason_input().send_keys("Denied for e2e tests.")


@When(u'the manager clicks the deny button')
def manager_clicks_deny_button(context):
    context.mana_home.select_manager_deny_button().click()


@Then(u'a denied message appears')
def denied_message_populates(context):
    deny_reimbursement = context.mana_home.select_reimburse_id_for_denial().text
    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element((
        By.ID, "status-message"
    ), f"Reimbursement ID {deny_reimbursement} has been denied."))
    assert context.mana_home.select_status_change_message().text == f"Reimbursement ID {deny_reimbursement} has " \
                                                                    f"been denied."




# MANAGER VIEW PAST REIMBURSEMENTS STEPS
@When(u'the manager clicks on the past reimbursements tab')
def manager_clicks_past_reimburse_tab(context):
    context.mana_home.select_past_reimbursements_tab().click()


@Then(u'the past approved reimbursements populate')
def past_approved_reimbursements_populate(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.text_to_be_present_in_element((
        By.XPATH, "/html/body/section[3]/div[1]/table/tbody/tr[1]/td[3]"
    ), context.mana_home.select_already_approved_reimbursement().text))
    assert context.mana_home.select_already_approved_reimbursement().text == "Sales trip that was not in FL"


@Then(u'the past denied reimbursements populate')
def past_denied_reimbursements_populate(context):
    assert context.mana_home.select_already_denied_reimbursement().text == "girl scout cookies"




# MANAGER LOGOUT STEPS
@When(u'the manager clicks on the log out tab')
def manager_clicks_logout_tab(context):
    context.mana_home.select_manager_logout_tab().click()


@Then(u'the manager is redirected to the login page')
def manager_redirected_to_login_page(context):
    WebDriverWait(context.driver, 10).until(expected_conditions.title_is("Home"))
    assert context.driver.title == "Home"

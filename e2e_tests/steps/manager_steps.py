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
    assert context.mana_home.select_status_change_message().text == f"Reimbursement ID {approve_reimburse} has been " \
                                                                    f"approved."




# MANAGER DENY REIMBURSEMENT STEPS
@When(u'the manager types the bad reimburse id into the id input')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the manager types the bad reimburse id into the id input')


@When(u'the manager types a reason for denial into the reason input')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the manager types a reason for denial into the reason input')


@When(u'the manager clicks the deny button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the manager clicks the deny button')


@Then(u'a denied message appears')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a denied message appears')




# MANAGER VIEW PAST REIMBURSEMENTS STEPS
@When(u'the manager clicks on the past reimbursements tab')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the manager clicks on the past reimbursements tab')


@Then(u'the past approved reimbursements populate')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the past approved reimbursements populate')


@Then(u'the past denied reimbursements populate')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the past denied reimbursements populate')




# MANAGER LOGOUT STEPS
@When(u'the manager clicks on the log out tab')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the manager clicks on the log out tab')


@Then(u'the manager is redirected to the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the manager is redirected to the login page')

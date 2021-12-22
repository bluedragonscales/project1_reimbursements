from behave import Given, When, Then


# TO LOG IN
@Given(u'the manager is on the login page.')
def get_login_page(context):
    context.driver.get("file:///C:/Users/kckar/Desktop/Revature/project1_reimbursements/front-end/index.html")


@When(u'the manager fills in id in the input space.')
def fill_manager_id(context):
    raise NotImplementedError(u'STEP: When the employee fills in the employee id.')


@When(u'the manager fills in password in the input space.')
def fill_manager_password(context):
    raise NotImplementedError(u'STEP: When the employee fills in the password.')


@When(u'the manager clicks the login button.')
def select_login_button(context):
    context.manager_page.click_login_button().click()


@Then(u'the manager will be redirected to the manager home page.')
def get_employee_home_page(context):
    title = context.driver.title
    assert title == "Manager Home"





# APPROVING AND DENYING REIMBURSEMENT REQUESTS
@Given(u'the manager is on the manager home page.')
def get_manager_home_page(context):
    context.driver.get("file:///C:/Users/kckar/Desktop/Revature/project1_reimbursements/front-end/manager-home.html")


@When(u'the manager clicks on the submit reimbursement status tab.')
def select_reimbursement_status_tab(context):
    context.manager_page.click_submit_reimbursement_status_tab().click()


@When(u'the manager fills out the reimbursement id.')
def fill_reimburse_id(context):
    raise NotImplementedError(u'STEP: When the employee fills in the request purpose.')


@When(u'the manager selects approved or denied from the drop down options.')
def select_status(context):
    raise NotImplementedError(u'STEP: When the employee fills in the amount.')


@When(u'the manager fills out the reason input.')
def fills_out_reason(context):
    pass


@When(u'the manager clicks the submit status button.')
def select_submit_status_button(context):
    context.manager_page.click_submit_status_button().click()


@Then(u'the status will be submitted.')
def request_submitted(context):
    title = context.driver.title
    assert title == "Manager Home"




# VIEWING REIMBURSEMENT STATISTICS
@Given(u'the manager is on the manager home page.')
def get_manager_home_page(context):
    context.driver.get("file:///C:/Users/kckar/Desktop/Revature/project1_reimbursements/front-end/manager-home.html")


@When(u'the manager clicks the view reimbursement statistics tab.')
def select_view_reimbursement_statistics_tab(context):
    context.manager_page.click_view_reimbursement_statistics_tab().click()


@When(u'the manager selects the statistics option from the dropdown.')
def select_statistics_option(context):
    pass


@When(u'the manager clicks the statistics submit button.')
def select_statistics_submit_button(context):
    context.manager_page.click_statistics_submit_button().click()


@Then(u'the statistics are shown.')
def reimburse_statistics_are_shown(context):
    title = context.driver.title
    assert title == "Manager Home"




# LOGGING OUT
@Given(u'the manager is on the manager home page.')
def get_manager_home_page(context):
    context.driver.get("file:///C:/Users/kckar/Desktop/Revature/project1_reimbursements/front-end/manager-home.html")

@When(u'the manager clicks on the logout button.')
def select_logout_button(context):
    context.manager_page.click_logout_button().click()


@Then(u'the manager is redirected to the login page.')
def manager_is_logged_out(context):
    title = context.driver.title
    assert title == "Home"

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

driver = None

@given('I open the website "{url}" on "{browser}"')
def open_website(context, url, browser):
    print(browser)
    global driver
    options = ChromeOptions() if 'chrome' in browser.lower() else EdgeOptions()
    context.driver = webdriver.Chrome(options=options) if 'chrome' in browser.lower() else webdriver.Edge(options=options)
    context.driver.get(url)

@when('I click on the login button')
def click_login_button(context):
    context.driver.find_element(By.ID, 'pt-login-2').click()

@when('I enters valid login credentials')
def enter_valid_credentials(context):
    login_input = context.driver.find_element(By.ID, 'wpName1')
    login_input.send_keys('krzychu@onet.pl')

    password_input = context.driver.find_element(By.ID, 'wpPassword1')
    password_input.send_keys('jtcnw')

@when('I click the "Zaloguj się" button')
def click_login(context):
    context.driver.find_element(By.ID, 'wpLoginAttempt').click()

@then('I should see an error message "{expected_error}"')
def check_error_message(context, expected_error):
    error_popup = context.driver.find_element(By.CLASS_NAME, 'cdx-message__content')
    actual_error = error_popup.text
    assert expected_error in actual_error, f"Expected: '{expected_error}'. Got: '{actual_error}.'"
    context.driver.quit()
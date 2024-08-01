from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import given, when, then

@given('I am on the login page')
def open_login_page(driver):
    driver.get('https://magento.softwaretestingboard.com/customer/account/login/')

@when('I enter valid credentials')
def enter_login_credentials(driver):
    driver.find_element(By.ID, 'email').send_keys('sammohan23@gmail.com')
    driver.find_element(By.ID, 'pass').send_keys('Swim@123')

@when('I submit the login form')
def submit_login_form(driver):
    driver.find_element(By.CSS_SELECTOR, 'button.action.login.primary').click()

@then('I should be redirected to the dashboard')
def verify_login_success(driver):
    assert 'Welcome, Samyugtha Mohan' in driver.page_source

from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import given, when, then

@given('I am on the registration page')
def open_registration_page(driver):
    driver.get('https://magento.softwaretestingboard.com/customer/account/create/')

@when('I fill in the registration form with valid data')
def fill_registration_form(driver):
    driver.find_element(By.ID, 'firstname').send_keys('Samyugtha')
    driver.find_element(By.ID, 'lastname').send_keys('Mohan')
    driver.find_element(By.ID, 'email_address').send_keys('sammohan23@gmail.com')
    driver.find_element(By.ID, 'password').send_keys('Swim@123')
    driver.find_element(By.ID, 'password-confirmation').send_keys('Swim@123')

@when('I submit the form')
def submit_registration_form(driver):
    driver.find_element(By.CSS_SELECTOR, 'button.action.submit.primary').click()

@then('I should see a confirmation of registration')
def verify_registration_confirmation(driver):
    assert 'Thank you for registering with' in driver.page_source

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from git.hillel_python.homework_28.registration_page_locators import RegistrationPage

@pytest.fixture
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def registration_page(driver):
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(RegistrationPage.signup_btn)
    )
    driver.find_element(*RegistrationPage.signup_btn).click()
    return RegistrationPage()

@pytest.fixture
def fill_registration_form(driver, registration_page):
    def _fill_form(name, last_name, email, password, cnf_password):
        driver.find_element(*registration_page.name).send_keys(name)
        driver.find_element(*registration_page.last_name).send_keys(last_name)
        driver.find_element(*registration_page.email).send_keys(email)
        driver.find_element(*registration_page.password).send_keys(password)
        driver.find_element(*registration_page.cnf_password).send_keys(cnf_password)
    return _fill_form

@pytest.fixture
def submit_registration(driver, registration_page):
    def _submit():
        driver.find_element(*registration_page.register_btn).click()
    return _submit
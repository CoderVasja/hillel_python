import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_successful_registration(driver, registration_page, fill_registration_form, submit_registration):
    test_name = "Fname"
    test_last_name = "LName"
    test_email = f"testuser_{random.randint(1000,9999)}@test.com"
    test_password = "TestPass123!"
    test_cnf_password = "TestPass123!"


    fill_registration_form(test_name,test_last_name, test_email, test_password,test_cnf_password)
    submit_registration()


    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(registration_page.message)
    )
    success_message = driver.find_element(*registration_page.message).text
    assert "Garage" in success_message




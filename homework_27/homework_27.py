from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

def test_tracking_status():
    driver.get("https://tracking.novaposhta.ua/#/uk")

    tracking_number = "20451105701136"
    expected_result = "Отримана"

    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    input_field.send_keys(tracking_number)

    input_field.send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, 10)
    status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header__status-text")))

    status_element = driver.find_element(By.CSS_SELECTOR, ".header__status-text")
    actualy_result = status_element.text.strip()

    assert actualy_result == expected_result




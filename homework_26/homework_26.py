import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/dz.html")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize("frame_id, input_id, secret_text", [
    ("frame1", "input1", "Frame1_Secret"),
    ("frame2", "input2", "Frame2_Secret")
])
def test_frame_verification(driver, frame_id, input_id, secret_text):

    driver.switch_to.default_content()

    driver.switch_to.frame(frame_id)

    input_field = driver.find_element(By.ID, input_id)
    input_field.send_keys(secret_text)


    check_button = driver.find_element(By.TAG_NAME, "button")
    check_button.click()


    time.sleep(2)


    alert = Alert(driver)
    alert_text = alert.text
    print(f"Повідомлення з {frame_id}: {alert_text}")
    assert alert_text == "Верифікація пройшла успішно!", f"Помилка верифікації у {frame_id}!"
    alert.accept()

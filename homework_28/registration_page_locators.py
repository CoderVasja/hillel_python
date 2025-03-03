from selenium.webdriver.common.by import By
class RegistrationPage:
    signup_btn = (By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/section/div/div/div[1]/div/button")
    name = (By.ID, "signupName")
    last_name = (By.ID, "signupLastName")
    email = (By.ID, "signupEmail")
    password = (By.ID, "signupPassword")
    cnf_password = (By.ID, "signupRepeatPassword")
    register_btn = (By.XPATH, "/html/body/ngb-modal-window/div/div/app-signup-modal/div[3]/button")
    message = (By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[1]/h1")
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#configuration
# BASE_URL="https://www.saucedemo.com/"os
# USERNAME="standard_user"
# PASSWORD="secret_sauce"



# WAIT_TIME=20

# SCREENSHOT_DIR="screenshots"
# REPORT_FILES="automation_test.txt"
# os.makedirs(SCREENSHOT_DIR,exist_ok=True)


# #brower setup
# def create_driver():
#     """configure and start chrome"""
#     options=webdriver.ChromeOptions() #open chrome
    
    
#     options.add_argument("--start-maximized")  # full screen
    
    
#     #attempting to prevent the password -- manager
    
#     options.add_experimental_option(
        
#         "prefs",
#         {
#             "credential_enable_sevice":False,
#             "porfile.password_manager_enabled":False,
#             "porfile.password_manager_leak_detection":False,
            
#         }
        
        
#     )
    
#     browser=webdriver.Chrome(options=options)
    
    
    
#     return browser
# driver=create_driver()
# wait=WebDriverWait(driver,WAIT_TIME)


# test_results=[]    
    
    
BASE_URL = "https://www.saucedemo.com/"
USERNAME_VALID = "standard_user"
PASSWORD_VALID = "secret_sauce"
PASSWORD_INVALID = "wrong_password"


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_sauce_login_success(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME_VALID)
    driver.find_element(By.ID, "password").send_keys(PASSWORD_VALID)
    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))
    heading = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert heading.text == "Products"


def test_sauce_login_failure(driver):
    """Test login failure with invalid credentials."""
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME_VALID)
    driver.find_element(By.ID, "password").send_keys(PASSWORD_INVALID)
    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 10)
    error_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )

    assert "Username and password do not match any user in this service" in error_element.text
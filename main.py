from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time
import sys


load_dotenv()
MY_URL = os.getenv("INTERVUE_URL")
MY_USERNAME = os.getenv("INTERVUE_USERNAME")
MY_PASSWORD = os.getenv("INTERVUE_PASSWORD")

def main():
    # Check for the -headless argument
    headless = False
    if "-headless" in sys.argv:
        headless = True
        print("Running in headless mode")
    else:
        print("Running in headed mode (default)")

    
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    if headless:
        options.add_argument('--headless=new')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(MY_URL)
        print(f"Opened website: {MY_URL}")

        wait = WebDriverWait(driver, 20)

        # Step 1: Click the first Login button
        login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "loginBtn")))
        driver.execute_script("arguments[0].removeAttribute('target')", login_button)
        login_button.click()
        print("Clicked first Login button")

        # Step 2: Click green login button for company
        green_login = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='AccessAccount-ColoredButton' and @href='/login']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", green_login)
        driver.execute_script("arguments[0].click();", green_login)
        print("Clicked green Login button for companies")

        # Step 3: Fill in credentials
        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))

        email_input.clear()
        email_input.send_keys(MY_USERNAME)
        print("Entered email")

        password_input.clear()
        password_input.send_keys(MY_PASSWORD)
        print("Entered password")

        # Step 4: Click "Login with Email"
        login_with_email_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            "button.LoginDarkButton-sc-1ertvag-0.ant-btn-primary"
        )))
        driver.execute_script("arguments[0].scrollIntoView(true);", login_with_email_btn)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", login_with_email_btn)
        print("Clicked 'Login with Email' button")

        # Step 5: Wait for page transition after login
        print("Waiting for post-login page to load...")
        time.sleep(5)  # extra buffer, adjust if needed

        # Step 6: Wait for and click the search icon
        search_icon = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            "div[class*='HeaderSearch__Wrapper'] span[class*='HeaderSearch__SearchLensIconWrap']"
        )))
        driver.execute_script("arguments[0].scrollIntoView(true);", search_icon)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", search_icon)
        print("Clicked on search bar icon")

        # Step 7: Wait for input box and type “hello”
        search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='SearchBox__StyledInput-ctnsh0-4 lhwsuL']")))
        time.sleep(1)
        search_input.send_keys("hello")
        print("Typed 'hello' into the correct search bar")
        time.sleep(2)  # Allow time for search results to appear

        # Step 8: Click the div with the specified class
        target_div = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.SearchThrough__PlaceholderText-sc-8f4vh4-0.fEvpzS")))
        target_div.click()
        print("Clicked the div with the specified class")
        time.sleep(2) # Allow time for potential page changes

        # Step 9: Wait for and click the div with class "ProfileHeader__UsernameWrap-sc-1gwp6c1-2 jRhmUi"
        profile_username_wrap = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.ProfileHeader__UsernameWrap-sc-1gwp6c1-2.jRhmUi")))
        profile_username_wrap.click()
        print("Clicked the div with class 'ProfileHeader__UsernameWrap-sc-1gwp6c1-2 jRhmUi'")
        time.sleep(2) # Allow time for the dropdown to appear

        # Step 10: Wait for and click the Logout button
        logout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.Dropdown__DropdownItemLink-k60emx-2.hHnuKn[href='/logout']")))
        logout_button.click()
        print("Clicked the Logout button")

        time.sleep(5)

    except Exception as e:
        print("Error occurred:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta

# ✅ Replace with actual login credentials
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"

# ✅ Path to ChromeDriver (make sure it's installed)
chromedriver_path = "/usr/local/bin/chromedriver"

# ✅ Set up Selenium WebDriver
service = Service(chromedriver_path)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Opens browser maximized
driver = webdriver.Chrome(service=service, options=options)

try:
    # 1️⃣ Open the website
    driver.get("https:YOUR-URL.COM")

    # 2️⃣ Click the "Log In" button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log In')]"))
    )
    driver.execute_script("arguments[0].click();", login_button)
    time.sleep(2)  # Allow time for the modal to appear

    # 3️⃣ Wait for login modal and enter credentials
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "form-group"))
    )

    username_field = driver.find_element(By.XPATH, "//input[@type='text']")
    username_field.send_keys(USERNAME)

    password_field = driver.find_element(By.XPATH, "//input[@type='password']")
    password_field.send_keys(PASSWORD)

    # 4️⃣ Click Log In button inside the modal
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary login col-xs-12 col-md-2']"))
    )
    driver.execute_script("arguments[0].click();", submit_button)

    print("✅ Successfully logged in!")

    # 5️⃣ Wait for login to process
    time.sleep(2)

    # 6️⃣ Click the "Members" button
    members_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Members')]"))
    )
    driver.execute_script("arguments[0].click();", members_button)
    
    print("✅ Clicked on the 'Members' button!")

    # 7️⃣ Wait for the date picker to load
    date_picker = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "datepicker-days"))
    )

    # ✅ Find all available (clickable) days - these will have just the 'day' class without 'disabled'
    available_days = date_picker.find_elements(By.XPATH, "//td[contains(@class, 'day') and not(contains(@class, 'disabled'))]")

    if available_days:
        # Get the last clickable day
        last_available_day = available_days[-1]
        print(f"✅ Selecting the last available day: {last_available_day.text}")
        driver.execute_script("arguments[0].click();", last_available_day)
    else:
        print("❌ No available days found in the calendar!")

    def book_tee_time(time_str):
        """Finds and books a specific tee time."""
        print(f"⏳ Looking for {time_str} tee time...")

        tee_times_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "time-tile-ob"))
        )

        tee_times = driver.find_elements(By.CLASS_NAME, "time-tile-ob")
        selected_tee_time = None

        for tee_time in tee_times:
            time_label = tee_time.find_element(By.CLASS_NAME, "times-booking-start-time-label")
            if time_label.text.strip() == time_str:
                selected_tee_time = tee_time
                break

        if selected_tee_time:
            print(f"✅ {time_str} tee time found!")
            # Click the "Reserve" button
            reserve_button = selected_tee_time.find_element(By.CLASS_NAME, "time-summary-ob-reserve-button")
            driver.execute_script("arguments[0].click();", reserve_button)
            print(f"✅ Clicked 'Reserve' for {time_str}!")

            # Select 18 holes
            holes_18 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "holes-eighteen"))
            )
            driver.execute_script("arguments[0].click();", holes_18)
            print("✅ Selected 18 holes")

            # Select 4 players
            players_4 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "players-four"))
            )
            driver.execute_script("arguments[0].click();", players_4)
            print("✅ Selected 4 players")

            # Select "Yes" for cart
            cart_yes_label = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//label[@for='cart-yes']"))
            )
            driver.execute_script("arguments[0].click();", cart_yes_label)
            print("✅ Selected cart")

            # Click the "Book Time" button
            book_time_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "ob-book-time-continue-button"))
            )
            driver.execute_script("arguments[0].click();", book_time_button)
            print(f"✅ Clicked 'Book Time' for {time_str}!")

            # Wait before going back to the main page
            time.sleep(3)
            driver.get("https://foreupsoftware.com/index.php/booking/22203#/teetimes")
            print("✅ Navigated back to the tee times page!")

        else:
            print(f"❌ {time_str} tee time not found.")

    # Book 12:00 PM
    book_tee_time("12:00pm")

    # Book 12:08 PM
    book_tee_time("12:08pm")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    # Keep browser open for verification, then close
    time.sleep(5)
    driver.quit()

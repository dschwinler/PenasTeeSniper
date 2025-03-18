# Penas Tee Sniper

## Overview

Penas Tee Sniper is an automated bot that secures tee times. It allows you to schedule and book desired tee times in advance, running whenever you choose.

## Features

- **Automated Login**: The bot logs into the ForeUP booking system using provided credentials.
- **Member Access**: Navigates to the member booking section.
- **Date Selection**: Selects the latest available date before any disabled dates in the calendar.
- **Tee Time Booking**:
  - Finds and reserves the designated tee times.
  - Selects 18 holes, 4 players, and a golf cart.
  - Confirms and books the tee time.
  - Waits a few seconds and navigates back to the tee times page.
  - Repeats the process for additonal designated tee times. 
- **Error Handling**: Implements error handling to prevent script failure due to delays or minor page inconsistencies.

## Technologies Used

- **Python**: Main programming language.
- **Selenium**: Used for web automation.
- **ChromeDriver**: Enables automated interactions with the ForeUP website.
- **Automator + Calendar** (Mac)\*\*: Scheduled to run automatically on macOS without needing a cloud server.

## Installation & Setup

### Prerequisites

- Install Python 3.
- Install Selenium:
  ```sh
  pip install selenium
  ```
- Download and install ChromeDriver:\
  [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

### Running the Script Manually

Run the script using:

```sh
python3 penas_tee_sniper.py
```

### Automating Execution (MacOS)

1. Open **Automator** > Applications > Run Shell Script
   ```sh
   /usr/bin/python3 /path/to/penas_tee_sniper.py
   ```
2. Create a new **Calendar Event** and add an alert.
3. Alert > Custom > Open file > Other > /path/to/penas_tee_sniper.py
4. Optional: To record the start and end time, calculate the duration, and enable logging, use:
   
  ```sh
  echo "[$(date)] Script started" >> /path/to/automator_log.txt
  START_TIME=$(date +%s)  # Capture the start time

  /usr/bin/python3 /path/to/penas_tee_sniper.py >> /path/to/automator_log.txt 2>&1

  END_TIME=$(date +%s)  # Capture the end time
  DURATION=$((END_TIME - START_TIME))  # Calculate duration

  echo "[$(date)] Script finished (Duration: ${DURATION} seconds)" >> /path/to/automator_log.txt
  ```
   
## Configuration

Update the following variables with your login credentials and URL before running:

```python
USERNAME = "your_email@example.com"
PASSWORD = "your_secure_password"
```

```python
driver.get("https://YOUR-URL.COM")
```
Select which tee times you would like to book:

```python
# Book 12:00 PM
book_tee_time("12:00pm")

# Book 12:08 PM
book_tee_time("12:08pm")
```

Choose how far in advance you want to book by updating this snippet:

```python
# ✅ Find all available (clickable) days - these will have just the 'day' class without 'disabled'
    available_days = date_picker.find_elements(By.XPATH, "//td[contains(@class, 'day') and not(contains(@class, 'disabled'))]")

    if available_days:
        # Get the last clickable day
        last_available_day = available_days[-1]
        print(f"✅ Selecting the last available day: {last_available_day.text}")
        driver.execute_script("arguments[0].click();", last_available_day)
    else:
        print("❌ No available days found in the calendar!")
```

## Notes

- Ensure your Mac does not go to sleep during execution. System Preferences > Battery > Schedule.
- The script must be updated if ForeUP changes its website structure.

## License

This project is for personal use only. Unauthorized use on other platforms is not recommended.


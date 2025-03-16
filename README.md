# Penas Tee Sniper

## Overview

Penas Tee Sniper is an automated bot that books tee times. The script is designed to run every Friday at 00:00 and automatically book the 12:00 PM and 12:08 PM tee times for a game scheduled 14 days in advance.

## Features

- **Automated Login**: The bot logs into the ForeUP booking system using provided credentials.
- **Member Access**: Navigates to the member booking section.
- **Date Selection**: Selects the latest available date before any disabled dates in the calendar.
- **Tee Time Booking**:
  - Finds and reserves the 12:00 PM tee time.
  - Selects 18 holes, 4 players, and a golf cart.
  - Confirms and books the tee time.
  - Waits a few seconds and navigates back to the tee times page.
  - Repeats the process for the 12:08 PM tee time.
- **Automated Navigation**: After booking, it returns to the main tee times page and repeats the process for the next scheduled time.
- **Error Handling**: Implements robust error handling to prevent script failure due to delays or minor page inconsistencies.

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

1. Open **Automator**.
2. Create a new **Calendar Alarm**.
3. Add **Run Shell Script** action and input:
   ```sh
   /usr/bin/python3 /path/to/penas_tee_sniper.py
   ```
4. Save and schedule it in **Calendar** to run every Friday at 00:00.

## Configuration

Update the following variables with your login credentials before running:

```python
USERNAME = "your_email@example.com"
PASSWORD = "your_secure_password"
```

## Notes

- Ensure your Mac does not go to sleep during execution.
- The script must be updated if ForeUP changes its website structure.

## License

This project is for personal use only. Unauthorized use on other platforms is not recommended.


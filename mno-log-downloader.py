from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
from datetime import datetime, timezone, timedelta

# Create a new Chrome WebDriver instance
browser = webdriver.Chrome()  # Change this line for Chrome

# Ask the user for the time input
start_time_input = input("Enter the start time (XX hours): ")
end_time_input = input("Enter the end time (YY hours): ")

# Convert the user input to integers
try:
    start_time = int(start_time_input)
    end_time = int(end_time_input)
except ValueError:
    print("Invalid time input. Please use numeric values for XX and YY.")
    browser.quit()
    exit()

# Create a time zone object for GMT+6 (Central Asia Standard Time)
tz = timezone(timedelta(hours=6))

# Get the current time in the desired time zone
current_time = datetime.now(tz)

# Handle the special case when start time is 23 and end time is 00
if start_time == 23 and end_time == 0:
    start_datetime = current_time.replace(hour=start_time, minute=0, second=0, microsecond=0)
    end_datetime = current_time.replace(hour=end_time, minute=0, second=0, microsecond=0) + timedelta(days=1)
else:
    # Construct the start and end times based on the user input and current date
    start_datetime = current_time.replace(hour=start_time, minute=0, second=0, microsecond=0)
    end_datetime = current_time.replace(hour=end_time, minute=0, second=0, microsecond=0)

# Subtract 6 hours from the start and end times
start_datetime -= timedelta(hours=6)
end_datetime -= timedelta(hours=6)

# Construct the URL with the user-specified time range
url = f"https://loganalyzerdc.mnpspbd.com/app/dashboards#/view/1660bf70-ebc4-11ed-a74c-695ee4226aa8?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:'{start_datetime.year}-{start_datetime.month:02d}-{start_datetime.day:02d}T{start_datetime.hour:02d}:00:00.000Z',to:'{end_datetime.year}-{end_datetime.month:02d}-{end_datetime.day:02d}T{end_datetime.hour:02d}:00:00.000Z'))"

browser.get(url)

# Wait briefly for the authentication prompt to appear
time.sleep(5)

# Use pyautogui to type in the username and password
username = "<enter-username>"
password = "<enter-password>"

pyautogui.write(username)
pyautogui.press('tab')
pyautogui.write(password)

# Press Enter to submit the login credentials
pyautogui.press('enter')

# Wait for the page to load (adjust the time as needed)
time.sleep(90)

# Locate and click the "Panel Options" button using Selenium
panel_options = browser.find_element(By.XPATH, "//button[@aria-label='Panel options for MNO Failed HTTP Hit Count']")
panel_options.click()

# Locate and click the "More" button using Selenium
more_button = browser.find_element(By.XPATH, "//span[@class='euiContextMenuItem__text' and text()='More']")
more_button.click()

# Locate and click the "Download as CSV" button using Selenium
download_csv_button = browser.find_element(By.XPATH, "//span[@class='euiContextMenuItem__text' and text()='Download as CSV']")
download_csv_button.click()

# Wait before closing the browser (adjust the time as needed)
time.sleep(180)

# Close the browser
browser.quit()

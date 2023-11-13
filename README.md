# Web-Task-Optimizer

<div align="center">
  <img src="https://infotelebd.com/wp-content/uploads/2019/06/Logo-1.png" alt="Infozillion Logo">
</div>

This repository contains two Python scripts developed at Infozillion Teletech BD Ltd. to automate web-based tasks using Selenium and PyAutoGUI. The scripts facilitate the automation of logging into a web dashboard, navigating to specific panels, and downloading data in CSV format. Additionally, a third script, named **Telecom-Error-Analyzer** and available in a separate repository, complements these automation scripts. Telecom-Error-Analyzer combines and analyzes the data downloaded by the first two scripts from Mobile Network Operator (MNO) and Internet Protocol Telephony Service Provider (IPTSP) files, generating a comprehensive summary table.

---

## Script 1: mno-log-downloader.py

- **Functionality:**
  - Automates the login and data download process for the "MNO Failed HTTP Hit Count" panel on the specified dashboard.
    
- **User Input:**
  - Requests user input for the start and end times to define the time range for data retrieval.
    
- **Dependencies:**
  - Selenium
  - PyAutoGUI
    
- **Execution Steps:**
  - Opens the Chrome browser and navigates to the provided URL.
  - Waits for the authentication prompt.
  - Uses PyAutoGUI to input username and password.
  - Clicks through the dashboard to access panel options and downloads data as a CSV file.
  - Waits for a specified time before closing the browser.

---

## Script 2: iptsp-log-downloader.py

- **Functionality:**
  - Similar to Script 1 but tailored for the "IPTSP Failed HTTP Hit Count" panel on a different dashboard.
    
- **User Input:**
  - Requests user input for the start and end times to define the time range for data retrieval.
    
- **Dependencies:**
  - Selenium
  - PyAutoGUI
    
- **Execution Steps:**
  - Opens the Chrome browser and navigates to the provided URL.
  - Waits for the authentication prompt.
  - Uses PyAutoGUI to input username and password.
  - Clicks through the dashboard to access panel options and downloads data as a CSV file.
  - Waits for a specified time before closing the browser.

---

## Telecom-Error-Analyzer

- For data processing and analysis, refer to the [Telecom-Error-Analyzer](https://github.com/iftekharmickey/Telecom-Error-Analyzer).

---

## Usage

1. **Clone Repository:**

   ```python
   git clone https://github.com/iftekharmickey/Web-Task-Optimizer/
   ```

2. **Install Dependencies:**

   ```python
   pip install selenium pyautogui
   ```

3. **Set up Chrome WebDriver:**

   [ChromeDriver - WebDriver for Chrome](https://sites.google.com/chromium.org/driver/)

4. **Run Scripts:**

    Execute scripts following the provided user prompts.

---

## Important Notes

- **Security Measures:**

  - The username and password for the web application have been removed from the scripts for security reasons. Users must manually input their credentials during script execution.
  - Ensure the confidentiality of your credentials and avoid sharing them in any publicly accessible space.

- **Adjusting Script Parameters:**

  - Some scripts may have parameters such as time intervals and URLs hardcoded. Adjust these parameters based on your specific requirements before running the scripts.

- **Web Browser Compatibility:**

  - The scripts are developed for Chrome. If you are using a different browser, update the WebDriver accordingly. 

---

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/iftekharmickey/Web-Task-Optimizer/blob/main/LICENSE) file for details.

---

## Author

- Iftekhar Tahir
- Email: iftekhar.tahir@proton.me
- GitHub: https://github.com/iftekharmickey
- LinkedIn: https://www.linkedin.com/in/iftekharmickey/

---

## Disclaimer

These scripts have been created and tested for use with a specific web application with appropriate permissions. The author and contributors are not responsible for any misuse of the tools. It is essential to use these tools only with prior permission and in compliance with all relevant laws and regulations.

Please ensure that you have the necessary authorizations to access and automate interactions with web applications before using these scripts.

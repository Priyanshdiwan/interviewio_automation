# Selenium Web Automation Script

This project is a Python-based Selenium script designed to automate interactions with a website.

## Features

* **Automated Web Interaction:** The script automates the following actions:
    * Opens a specified URL in a Chrome browser.
    * Locates and clicks the login button.
    * Enters login credentials (username and password) from a configuration file.
    * Clicks the "Login with Email" button.
    * Navigates to and interacts with the search functionality.
    * Clicks on a profile element.
    * Logs out of the website.

* **Credential Management:** The script uses a `.env` file to store sensitive information (like usernames and passwords) securely, keeping them separate from the main script.

* **Headless Execution:** The script supports both headed (visible browser) and headless (background browser) modes.

* **Command-Line Argument:** The script accepts a command-line argument to control whether the browser runs in headless mode. [-head (defult) and -headless]

* **Clear Output:** The script provides informative output to the console, indicating the steps it's performing.

## Unique Features

* **Robust Element Handling:** The script uses `WebDriverWait` with `expected_conditions` to ensure that elements are fully loaded and interactable before attempting to interact with them. This makes the script more reliable and less prone to errors due to timing issues.
* **Modular Design:** The main logic of the script is encapsulated in a `main()` function, promoting better organization and readability.
* **Secure Credential Management:** By using a `.env` file and the `python-dotenv` library, the script follows security best practices for handling sensitive information.
* **Flexible Execution:** The script can be run in both headed and headless modes, providing flexibility for different use cases (e.g., debugging vs. background automation).
* **Detailed Logging:** The script includes print statements to log its actions, which can be helpful for debugging and understanding the script's execution flow.

## Prerequisites

Before running the script, ensure you have the following installed:

* **Python 3.6 or later:** You can download it from [python.org](https://www.python.org/).
* **pip:** Python's package installer.  It usually comes with Python.
* **Selenium:** Install it using pip:
    ```bash
    pip install selenium
    ```
* **python-dotenv:** Install it using pip:
    ```bash
    pip install python-dotenv
    ```
* **ChromeDriver:** Download the ChromeDriver executable that matches your Chrome browser version from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).  Make sure to add the ChromeDriver executable to your system's PATH or place it in the same directory as your Python script.
* **.env file:** Create a `.env` file in the same directory as your Python script.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your_repository_url>
    cd <your_repository_directory>
    ```
2.  **Create a `.env` file:**
    * Create a file named `.env` in the same directory as the `main.py` script.
    * Add your website URL, username, and password to the `.env` file, using the following format:
        ```
        INTERVUE_URL=your_website_url
        INTERVUE_USERNAME=your_username
        INTERVUE_PASSWORD=your_password
        ```
        * Replace `your_website_url`, `your_username`, and `your_password` with your actual credentials.  **Do not use quotes around the values.**

## Running the Script

1.  **Open your terminal or command prompt.**
2.  **Navigate to the directory** containing the `main.py` script and the `.env` file.
3.  **Run the script:**

    * To run the script in headed mode (with a visible browser window):
        ```bash
        python3 main.py
        ```
        or
        ```bash
        python main.py
        ```
    * To run the script in headless mode (without a visible browser window):
        ```bash
        python3 main.py -headless
        ```
        or
        ```bash
        python main.py -headless
        ```

## Video Demonstrations

* **Headed Mode:** A video demonstration showing the script running with a visible browser is available [link to headed video].
* **Headless Mode:** A video demonstration showing the script running in the background (headless mode) is available [link to headless video].


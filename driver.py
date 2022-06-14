from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager, ChromeType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MEROSHARE_URL = "https://meroshare.cdsc.com.np/#/{}"


def get_driver():
    # currently supporting only one browser.
    # later, different browser's driver can be installed based on the args provided while running the program
    # for example python --driver=firefox main.py
    return webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())


class IpoBot:
    def __init__(self):
        self.__driver = get_driver()
        self.__driver.get(MEROSHARE_URL.format("login"))

    def login(self, login_details):
        # Wait until the loginForm is loaded.
        # Better approach than putting time.sleep()
        WebDriverWait(self.__driver, 30).until(EC.presence_of_all_elements_located((By.NAME, "loginForm")))

        # For DP ID selection
        self.__driver.find_element(By.ID, "selectBranch").click()
        dp_input = self.__driver.find_element(By.CLASS_NAME, "select2-search__field")
        dp_input.click()
        dp_input.send_keys(login_details["dp_id"])
        dp_input.send_keys(Keys.ENTER)

        # For username
        username_field = self.__driver.find_element(By.ID, "username")
        username_field.send_keys(login_details["username"])

        # For password
        password_field = self.__driver.find_element(By.ID, "password")
        password_field.send_keys(login_details["password"])

        # Login Button
        login_button = self.__driver.find_element(By.XPATH, "//button[text()='Login']")
        login_button.click()

        WebDriverWait(self.__driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "app-dashboard")))

        logger.info(f"Signed up successful for {login_details['alias']}")

    def navigate(self, path):
        self.__driver.get(MEROSHARE_URL.format(path))
        WebDriverWait(self.__driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "app-asba")))
        print(f"Loaded...")
        time.sleep(5)

    def parse_open_issues(self, type="all"):
        WebDriverWait(self.__driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "app-applicable-issue")))
        open_issues = self.__driver.find_elements(By.CLASS_NAME, "company-name")
        for open_issue in open_issues:
            print(f"Open issue: {open_issue.text}")




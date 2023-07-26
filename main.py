from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "\D:Development\chromedriver.exe"
chromedriver_autoinstaller.install()
service = Service(CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

IG_URL = 'https://www.instagram.com/'
SIMILAR_ACCOUNT = 'houseofhighlights'
EMAIL = 'shotokillua55@gmail.com'
USERNAME = '***'
PASSWORD = '***'

# driver = webdriver.Chrome(service=service, options=options)
#
# driver.get(IG_URL)
# driver.fullscreen_window()
# time.sleep(2)
#
# # Login
# email_bar = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
# email_bar.click()
# email_bar.send_keys(USERNAME)
#
# pw_bar = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
# pw_bar.click()
# pw_bar.send_keys(PASSWORD)
# pw_bar.send_keys(Keys.ENTER)
# time.sleep(3)
#
# # Find followers
# driver.fullscreen_window()
# time.sleep(2)
#
# not_now = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
# not_now.click()
# time.sleep(2)
#
# not_now_again = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
# not_now_again.click()
# time.sleep(2)
# driver.fullscreen_window()
# time.sleep(2)
#
# search_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div')
# search_button.click()
# time.sleep(2)
#
# search_bar = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
# search_bar.send_keys(SIMILAR_ACCOUNT)
# time.sleep(5)
# search_bar.click()
# time.sleep(3)
# search_bar.send_keys(Keys.ENTER)
# time.sleep(2)
#
# ig_page = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div/div/div/div[2]')
# ig_page.click()
# time.sleep(10)
#
# followers = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a')
# followers.click()
# time.sleep(2)
#
# bar = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
#
# for i in range(5):
#
#     driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', bar)
#     time.sleep(2)
# # Follow
#     follow_buttons = driver.find_elements(By.XPATH, '//*[@id="mount_0_0_M3"]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button')
#
#     for button in follow_buttons:
#         try:
#             button.click()
#             time.sleep(2)
#         except ElementClickInterceptedException:
#             cancel_button = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
#             cancel_button.click()
#             time.sleep(2)

class InstaFollower():
    def __init__(self, CHROME_DRIVER_PATH):
        self.path = CHROME_DRIVER_PATH
        self.username = USERNAME
        self.password = PASSWORD
        self.similar = SIMILAR_ACCOUNT
        self.service = Service(self.path)
        self.options = webdriver.ChromeOptions().add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)


    def login(self):
        # Go to IG page
        self.driver.get(IG_URL)
        self.driver.fullscreen_window()
        time.sleep(2)

        # Login
        email_bar = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_bar.click()
        email_bar.send_keys(self.username)

        pw_bar = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        pw_bar.click()
        pw_bar.send_keys(self.password)
        pw_bar.send_keys(Keys.ENTER)
        time.sleep(3)


    def find_followers(self):
        # Find followers
        self.driver.fullscreen_window()
        time.sleep(2)

        not_now = self.driver.find_element(By.XPATH,
                                      '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        not_now.click()
        time.sleep(2)

        not_now_again = self.driver.find_element(By.XPATH,
                                            '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        not_now_again.click()
        time.sleep(2)
        self.driver.fullscreen_window()
        time.sleep(2)

        search_button = self.driver.find_element(By.XPATH,
                                            '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div')
        search_button.click()
        time.sleep(2)

        search_bar = self.driver.find_element(By.XPATH,
                                         '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
        search_bar.send_keys(self.similar)
        time.sleep(5)
        search_bar.click()
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)

        ig_page = self.driver.find_element(By.XPATH,
                                      '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div/div/div/div[2]')
        ig_page.click()
        time.sleep(10)

        followers = self.driver.find_element(By.XPATH,
                                        '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)

        bar = self.driver.find_element(By.XPATH,
                                  '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')

        for i in range(5):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', bar)
            time.sleep(2)


    def follow(self):
        follow_buttons = self.driver.find_elements(By.XPATH,
                                              '//*[@id="mount_0_0_M3"]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button')

        for button in follow_buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
                time.sleep(2)

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()

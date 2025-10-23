# ===== 自動登入高科大 elearning ======
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

class Bot:
    def __init__(self, url, acc):
        self.url = url
        self.acc = acc
        self.__pwd = "8XFPW3"
    
    # 進入 context 時啟動 driver
    def __enter__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)  # 登入後不關閉
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.url)
        return self

    # 離開 context 時關閉 driver
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.driver:
            self.driver.quit()

    # 主要功能
    def bot(self, accid, pwdid):
        # ====== 設定 ======
        driver = self.driver
        print('\r\n ====== 開始登入:', self.url ,' ======= \r\n')

        time.sleep(3)

        # ====== 檢查網路 ======
        if not self.check_internet():
            print("\r\n ====== 無法連接到網路 ====== \r\n")
            return False

        # ====== 點登入按鈕 (僅高科大Elearning 但不影響) ======
        login_btn = driver.find_element(By.CLASS_NAME, "mat-button-wrapper")
        login_btn.click()

        time.sleep(2)

        # ====== 輸入帳號密碼 (需看實際 id/name) ======
        driver.find_element(By.ID, accid).send_keys(self.acc)
        driver.find_element(By.ID, pwdid).send_keys(self.__pwd)

        # ====== 送出表單 ======
        wait = WebDriverWait(driver, 10)
        login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_btn.click()

        # ====== 回傳結束 ======
        print('======= 任務結束 =======')
        return True

    def check_internet(self):
        try:
            requests.get(self.url, timeout=5)
            return True
        except requests.ConnectionError:
            return False
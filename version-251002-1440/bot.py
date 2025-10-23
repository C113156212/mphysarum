# ===== 自動登入高科大 elearning ======
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

class Bot:
    # ====== 初始化 ======
    def __init__(self):
        self.url = ""
        self.acc = ""
        self.__pwd = ""
        self.driver = self.create_driver()
    
    # ====== 建立 driver ======
    def create_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)  # 執行完不自動關閉
        driver = webdriver.Chrome(options=options)
        return driver

    # ====== 設定帳號密碼 ======
    def set_pwd(self, pwd):
        self.__pwd = pwd

    # ====== 主要功能 ======
    def bot(self, accid, pwdid):

        # ====== 檢查網路 ======
        self.check_internet()

        # ====== 開始登入 ======
        print(f'======= 開始登入: {self.url} =======')
        driver = self.driver
        driver.get(self.url)

        # ====== 點登入按鈕 (僅高科大Elearning 但不影響) ======
        try:
            login_btn = driver.find_element(By.CLASS_NAME, "mat-button-wrapper")
            login_btn.click()
        except:
            pass

        # ====== 輸入帳號密碼 (需看實際 id/name) ======
        driver.find_element(By.ID, accid).send_keys(self.acc)
        driver.find_element(By.ID, pwdid).send_keys(self.__pwd)

        # ====== 送出表單 ======
        login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_btn.click()

        # ====== 回傳結束 ======
        print('======= 任務結束 ======= \r\n')
        return True
    
    # ====== 檢查連線 ======
    def check_internet(self):
        try:
            requests.get(self.url, timeout=5)
            print(f"====== 網站:{self.url}連線成功 ======")
            return True
        except requests.ConnectionError:
            print(f"====== 網站:{self.url}無法連線 ======")
            return False
    
    # ====== 開新分頁 ======
    def open_tab(self, url, acc):
        if not url: print("open_tab: URL 無效，已跳過"); return

        self.acc = acc
        self.url = url
        self.driver.execute_script(f"window.open('{url}', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
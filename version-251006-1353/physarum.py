# ====== 黏菌 ======

import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Physarum:
    def __new__():
        
    
    def __init__(self, config_path='mapping.json'):
        # ====== 黏菌誕生 ======
        print('\r\n ====== 黏菌成功誕生 ====== \r\n')
        self.config_path = config_path
        self.config = self.open_file()
        self.driver = self.create_driver()

    def set_config_path(self, config_path):
        """切換設定檔"""

        self.config_path = config_path
        self.config = self.open_file()
        # 切換到最新的瀏覽器分頁
        if self.driver:
            self.driver.switch_to.window(self.driver.window_handles[-1])

    def create_driver(self):
        # ====== 建立 driver ======
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)  # 執行完不自動關閉
        driver = webdriver.Chrome(options=options)
        return driver

    def open_file(self):
        # ====== 讀取設定檔 ======
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                config = json.load(f)
            print('\r\n ====== 成功讀取設定檔 ====== \r\n')
            return config
        except FileNotFoundError:
            print(f"找不到設定檔：{self.config_path}")
            return None
        except json.JSONDecodeError:
            print(f"設定檔格式錯誤：{self.config_path}")
            return None

    def do(self):
        if not self.config:
            print("沒有載入設定檔，黏菌無法出發")
            return None

        driver = self.driver
        try:
            print('\r\n ====== 黏菌開始任務 ====== \r\n')

            for step in self.config["steps"]:
                action = step["action"]
                selector = step.get("selector")
                value = step.get("value")

                if action == "goto":
                    driver.get(step["target"])
                    print('黏菌抵達網頁')

                elif action == "input":
                    element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    element.clear()
                    element.send_keys(value)
                    print(f'黏菌輸入完成')

                elif action == "click":
                    element = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    element.click()
                    print('黏菌點擊按鈕')

                elif action == "wait":
                    timeout = step.get("timeout", 10)
                    WebDriverWait(driver, timeout).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    print(f'黏菌等待元素 {selector}')

                else:
                    print(f"未知的 action: {action}")
            
            print("\r\n ====== 黏菌已完成任務 ====== \r\n")
            return driver

        except Exception as e:
            print("\r\n ====== 黏菌散架了 ====== \r\n")
            print(f"錯誤訊息: {e}")
            driver.quit()
            return None

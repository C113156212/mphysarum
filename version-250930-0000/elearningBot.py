# ===== 自動登入高科大 elearning ======
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ====== 設定 ======
username = "username"  # ← 換成正確帳號
password = "your_password_here"  # ← 換成正確密碼

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # 登入後不關閉
driver = webdriver.Chrome(options=options)

# ====== 打開網站 ======
driver.get("https://elearning.nkust.edu.tw")  # ← 換成正確登入頁

time.sleep(3)

# ====== 點登入按鈕 (mat-button-wrapper) ======
login_btn = driver.find_element(By.CLASS_NAME, "mat-button-wrapper")
login_btn.click()

time.sleep(2)

# ====== 輸入帳號密碼 (需看實際 id) ======
driver.find_element(By.ID, "account").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)

# ====== 送出表單 ======
wait = WebDriverWait(driver, 10)
login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
login_btn.click()

# ====== 回傳結束 ======
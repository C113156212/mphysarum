from selenium.webdriver.common.by import By
from core.base import IAction
import time

class OpenPageAction(IAction):
    def __init__(self, driver, target):
        self.driver = driver
        self.target = target

    def run(self):
        print(f"[OpenPageAction] 開啟 {self.target}")
        self.driver.get(self.target)

class WaitAction(IAction):
    def __init__(self, driver, target=None, timeout=1):
        self.driver = driver
        self.target = target
        self.timeout = timeout

    def run(self):
        print(f"[WaitAction] 等待 {self.timeout} 秒")
        time.sleep(self.timeout)

class ClickAction(IAction):
    def __init__(self, driver, target):
        self.driver = driver
        self.target = target

    def run(self):
        print(f"[ClickAction] 點擊 {self.target}")
        element = self.driver.find_element(By.CSS_SELECTOR, self.target)
        element.click()

class InputAction(IAction):
    def __init__(self, driver, target, value):
        self.driver = driver
        self.target = target
        self.value = value

    def run(self):
        print(f"[InputAction] 輸入 {self.value} 到 {self.target}")
        element = self.driver.find_element(By.CSS_SELECTOR, self.target)
        element.send_keys(self.value)


class PrintAction(IAction):
    def __init__(self, message):
        self.message = message

    def run(self):
        print(f"[PrintAction] {self.message}")

# ====== BasicConfig ======
import json

class BasicConfig:
    """單例模式：讀取與管理設定檔"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("[BasicConfig] 單例建立成功")
        return cls._instance

    def __init__(self):
        self.json_path = ''
        self.json_content = ''

    def _load_file(self):
        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                print("[BasicConfig] 成功讀取設定檔")
                return json.load(f)
        except FileNotFoundError:
            print(f"[BasicConfig] 找不到設定檔：{self.json_path}")
            return None
        except json.JSONDecodeError:
            print(f"[BasicConfig] JSON 格式錯誤：{self.json_path}")
            return None

    def set_config_path(self, path):
        self.json_path = path
        self.json_content = self._load_file()

# ====== WebConfig ======
from selenium import webdriver


class WebConfig:
    """單例模式：管理 Selenium driver"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("[WebConfig] 單例建立成功")
        return cls._instance

    def __init__(self):
        self.driver = self._create_driver()

    def _create_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        return driver
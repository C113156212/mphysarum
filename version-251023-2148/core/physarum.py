from core.config import BasicConfig, WebConfig
from core.base import IAction, ActionComposite
from core.factory import ActionFactory
from actions.basic import PrintAction  # 如果需要

# ====== Physarum 主體 ======
class Physarum:
    """外觀模式：整合設定、瀏覽器與行動"""
    def __init__(self):
        print("🧫 黏菌誕生！")
        self.config = BasicConfig()
        self.web = WebConfig()
        self.action_root = ActionComposite()

        # 初始化預設行動
        self._load_default_actions()

    def _load_default_actions(self):
        self.action_root.add(PrintAction("黏菌開始蠕動..."))

    def load_json(self, json_path=None):
        """讀取 JSON 並加入行動"""
        if json_path:
            self.config.set_config_path(json_path)

        if not self.config.json_content:
            print("[Physarum] 無有效 JSON，跳過載入")
            return
        
        # 切換到最新的瀏覽器分頁
        if self.web.driver:
            self.web.driver.execute_script("window.open('about:blank');")  # 新增分頁
            self.web.driver.switch_to.window(self.web.driver.window_handles[-1])    # 切換到新分頁


        factory = ActionFactory(self.web.driver)
        for act_data in self.config.json_content.get("actions", []):
            action = factory.create_action(act_data)
            self.action_root.add(action)

    def add_action(self, action: IAction):
        """動態加入行動"""
        self.action_root.add(action)

    def run(self):
        """執行所有行動"""
        print("[Physarum] 🧬 開始行動！")
        self.action_root.run()
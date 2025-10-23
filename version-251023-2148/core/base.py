from abc import ABC, abstractmethod
import time

# 定義行動介面與基本行為
class IAction(ABC):
    @abstractmethod
    def run(self):
        pass


# 組合節點（可以放入多個 IAction）
class ActionComposite(IAction):
    def __init__(self):
        self.actions = []

    def add(self, action: IAction):
        print(f"[Composite] 加入行動：{action.__class__.__name__}")
        self.actions.append(action)

    def run(self):
        print("[Composite] 執行所有行動：")
        for action in self.actions:
            action.run()

import actions.basic

class ActionFactory:
    def __init__(self, driver):
        self.driver = driver
        # 將 actions.basic 所有 class 收集到字典
        self.class_dict = {cls.__name__: cls for cls in actions.basic.__dict__.values() if isinstance(cls, type)}
        

    def create_action(self, data: dict):
        if len(data) != 1:
            raise ValueError("每個 step JSON 只能有一個行動")
        class_name, params = next(iter(data.items()))
        cls = self.class_dict.get(class_name)
        if not cls:
            raise ValueError(f"未知行動類型：{class_name}")
        return cls(self.driver, **params)

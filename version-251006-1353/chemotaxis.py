# ====== 趨化性 ======

import json

steps = []
def chemotaxis():

    while True:
        action = input("請輸入動作 (goto/input/click/wait/exit): ")

        if action == "exit":
            break

        step = {"action": action}

        if action == "goto":
            step["target"] = input("輸入網址: ")

        elif action == "input":
            step["selector"] = input("輸入 selector: ")
            step["value"] = input("輸入要填的值: ")

        elif action == "click":
            step["selector"] = input("輸入 selector: ")

        elif action == "wait":
            step["selector"] = input("輸入 selector: ")
            step["timeout"] = int(input("輸入等待秒數 (預設10): ") or 10)

        steps.append(step)

    with open("mapping.json", "w", encoding="utf-8") as f:
        json.dump({"steps": steps}, f, indent=2, ensure_ascii=False)

print("已成功產生 mapping.json")

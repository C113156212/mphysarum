# ===== 引入 =====
from bot import Bot

# ====== 建立 Bot 物件 ======
mbot = Bot()

mbot.set_pwd('your_password_here')  # 設定密碼

# ====== 高科大 elearning ======
mbot.open_tab("https://elearning.nkust.edu.tw", "your_account_here")
mbot.bot("account", "password")

# ====== 切換到新分頁開 Zuvio ======
mbot.open_tab("https://irs.zuvio.com.tw", "your_email_here")
mbot.bot("email", "password")


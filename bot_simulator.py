import pyautogui
import time

print("Đang chạy Bot Simulator... Sẽ di chuyển chuột sau 3 giây.")
time.sleep(3)

# Bot di chuyển chuột từ điểm A đến B trong đúng 2 giây (Rất đều và thẳng)
pyautogui.moveTo(100, 100)
time.sleep(0.5)
pyautogui.moveTo(800, 500, duration=2.0)

print("Bot đã di chuyển xong.")
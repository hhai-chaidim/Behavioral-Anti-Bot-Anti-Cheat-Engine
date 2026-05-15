import os

# --- CẤU HÌNH ĐƯỜNG DẪN (PATHS) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_LOGS_DIR = os.path.join(DATA_DIR, 'raw_logs')

# Tự động tạo thư mục nếu chưa tồn tại
os.makedirs(RAW_LOGS_DIR, exist_ok=True)

# --- CẤU HÌNH LOGIC (THRESHOLDS) ---
TRUST_SCORE_INITIAL = 100       # Điểm tin cậy khởi đầu
TRUST_SCORE_MIN = 50            # Ngưỡng kích hoạt cảnh báo Bot

# --- CẤU HÌNH CHUỘT (MOUSE PROFILER) ---
MOUSE_LOG_FILE = os.path.join(RAW_LOGS_DIR, 'mouse_movement.log')
MIN_DISTANCE_TO_LOG = 1.0       # Chỉ ghi log nếu chuột nhích hơn 1 pixel để tránh nhiễu
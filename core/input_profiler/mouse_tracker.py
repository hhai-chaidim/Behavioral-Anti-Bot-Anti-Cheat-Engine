from pynput import mouse
import time
import math
import config  # Gọi file cấu hình ở thư mục gốc

class MouseProfiler:
    def __init__(self):
        self.last_time = time.time()
        self.last_x = None
        self.last_y = None

    def on_move(self, x, y):
        current_time = time.time()
        delta_time = current_time - self.last_time
        
        if self.last_x is not None and self.last_y is not None:
            distance = math.sqrt((x - self.last_x)**2 + (y - self.last_y)**2)
            
            if distance > config.MIN_DISTANCE_TO_LOG:
                velocity = distance / delta_time if delta_time > 0 else 0
                log_entry = f"{current_time:.4f},{x:04.0f},{y:04.0f},{delta_time:.4f},{distance:.2f},{velocity:.2f}\n"
                
                # In ra màn hình để quan sát
                print(f"[Mouse] Tọa độ: ({x:04.0f}, {y:04.0f}) | Vận tốc: {velocity:.2f} px/s")
                
                # Ghi vào file log thô
                with open(config.MOUSE_LOG_FILE, "a") as f:
                    f.write(log_entry)
        
        self.last_time = current_time
        self.last_x = x
        self.last_y = y

    def start_tracking(self):
        print(f"[*] Đang khởi động Mouse Profiler... Log lưu tại: {config.MOUSE_LOG_FILE}")
        with mouse.Listener(on_move=self.on_move) as listener:
            try:
                listener.join()
            except KeyboardInterrupt:
                print("\n[!] Đã dừng Mouse Profiler.")
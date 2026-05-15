import math
import statistics
import os
import config

class MouseBehaviorAnalyzer:
    def __init__(self):
        self.log_file = config.MOUSE_LOG_FILE

    def _read_logs(self):
        """Đọc dữ liệu từ file log và trả về danh sách các điểm"""
        if not os.path.exists(self.log_file):
            print("[-] Không tìm thấy file log. Hãy chạy Mouse Profiler trước.")
            return []

        data_points = []
        with open(self.log_file, "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 6:
                    # Cấu trúc: Timestamp, X, Y, Delta Time, Distance, Velocity
                    timestamp, x, y, dt, dist, vel = map(float, parts)
                    data_points.append({"x": x, "y": y, "distance": dist, "velocity": vel})
        return data_points

    def analyze(self):
        data = self._read_logs()
        if len(data) < 10:
            print("[!] Dữ liệu quá ít để phân tích (Cần ít nhất 10 điểm ghi nhận).")
            return

        print("\n" + "="*40)
        print(" BÁO CÁO PHÂN TÍCH HÀNH VI CHUỘT")
        print("="*40)

        # 1. PHÂN TÍCH TÍNH TUYẾN TÍNH (LINEARITY)
        start_point = data[0]
        end_point = data[-1]
        
        # Khoảng cách đường thẳng tuyệt đối từ A đến B
        straight_distance = math.sqrt((end_point['x'] - start_point['x'])**2 + 
                                      (end_point['y'] - start_point['y'])**2)
        
        # Tổng quãng đường thực tế con trỏ đã đi
        total_distance = sum(point['distance'] for point in data)

        linearity_ratio = total_distance / straight_distance if straight_distance > 0 else 1.0
        
        # 2. PHÂN TÍCH VẬN TỐC (VELOCITY VARIANCE)
        velocities = [point['velocity'] for point in data]
        velocity_std_dev = statistics.stdev(velocities) if len(velocities) > 1 else 0

        # --- IN KẾT QUẢ ---
        print(f"[*] Tỷ lệ Tuyến tính (Linearity Ratio): {linearity_ratio:.4f}")
        print(f"[*] Độ lệch chuẩn Vận tốc (Velocity StdDev): {velocity_std_dev:.2f}")

        # --- ĐÁNH GIÁ LOGIC ---
        trust_score = config.TRUST_SCORE_INITIAL

        if linearity_ratio < 1.02:
            print("    [!] Cảnh báo: Quỹ đạo quá thẳng (Dấu hiệu Bot). Trừ 30 điểm.")
            trust_score -= 30
        
        if velocity_std_dev < 100:  # Ngưỡng test, con người thường > 300
            print("    [!] Cảnh báo: Vận tốc quá đều (Dấu hiệu Bot). Trừ 30 điểm.")
            trust_score -= 30

        print("-" * 40)
        if trust_score <= config.TRUST_SCORE_MIN:
            print(f"[X] KẾT LUẬN: HỆ THỐNG PHÁT HIỆN GIAN LẬN! (Điểm an toàn: {trust_score}/100)")
        else:
            print(f"[V] KẾT LUẬN: Thao tác của Con người. (Điểm an toàn: {trust_score}/100)")
        print("="*40 + "\n")
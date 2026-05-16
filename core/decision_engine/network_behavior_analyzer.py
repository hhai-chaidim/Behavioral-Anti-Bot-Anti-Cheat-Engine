import os
import statistics
import config

class NetworkBehaviorAnalyzer:
    def __init__(self):
        self.log_file = config.NETWORK_LOG_FILE

    def _read_logs(self):
        """Đọc dữ liệu Delta Time từ file log"""
        if not os.path.exists(self.log_file):
            print("[-] Không tìm thấy file log mạng. Hãy chạy Network Sniffer trước.")
            return []

        delta_times = []
        with open(self.log_file, "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    # Cấu trúc: Timestamp, Delta Time
                    delta_times.append(float(parts[1]))
        return delta_times

    def analyze(self):
        delta_times = self._read_logs()
        if len(delta_times) < 20:
            print("[!] Dữ liệu quá ít để phân tích (Cần ít nhất 20 gói tin).")
            return

        print("\n" + "="*40)
        print(" BÁO CÁO PHÂN TÍCH JITTER MẠNG")
        print("="*40)

        # Tính toán Độ lệch chuẩn của độ trễ (Jitter Variance)
        jitter_std_dev = statistics.stdev(delta_times)
        avg_delay = sum(delta_times) / len(delta_times)

        print(f"[*] Độ trễ trung bình (Avg Delay): {avg_delay:.4f}s")
        print(f"[*] Độ lệch chuẩn Jitter (StdDev): {jitter_std_dev:.6f}")

        trust_score = config.TRUST_SCORE_INITIAL

        # Nếu Jitter quá nhỏ (Dưới 5 mili-giây) -> Bot spam
        if jitter_std_dev < 0.005:
            print("    [!] Cảnh báo: Tần suất gửi gói tin phi vật lý (Dấu hiệu Bot/Tool Auto). Trừ 40 điểm.")
            trust_score -= 40

        print("-" * 40)
        if trust_score <= config.TRUST_SCORE_MIN:
            print(f"[X] KẾT LUẬN: Mạng có dấu hiệu bị thao túng bởi Tool! (Điểm: {trust_score}/100)")
        else:
            print(f"[V] KẾT LUẬN: Lưu lượng mạng bình thường. (Điểm: {trust_score}/100)")
        print("="*40 + "\n")
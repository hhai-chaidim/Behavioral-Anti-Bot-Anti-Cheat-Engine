from scapy.all import sniff
import config

class NetworkProfiler:
    def __init__(self):
        self.last_packet_time = 0

    def packet_callback(self, packet):
        # Lấy Timestamp thực tế của gói tin từ card mạng
        current_time = float(packet.time)
        
        if self.last_packet_time != 0:
            delta_time = current_time - self.last_packet_time
            
            # Lọc nhiễu: Chỉ ghi nhận các gói tin cách nhau > 1ms 
            # (Tránh việc HĐH đẩy 1 cục nhiều gói tin cùng lúc do buffer)
            if delta_time > 0.001:
                log_entry = f"{current_time:.6f},{delta_time:.6f}\n"
                
                # In ra màn hình (Comment lại nếu thấy quá rối)
                print(f"[Network] Gói tin gửi đi! Jitter (Độ trễ): {delta_time:.4f}s")
                
                # Ghi vào file log
                with open(config.NETWORK_LOG_FILE, "a") as f:
                    f.write(log_entry)
        
        self.last_packet_time = current_time

    def start_sniffing(self):
        print(f"[*] Đang khởi động Network Sniffer... Log lưu tại: {config.NETWORK_LOG_FILE}")
        print("[!] LƯU Ý: Yêu cầu chạy Terminal bằng quyền Administrator/Root.")
        
        # Bắt các gói tin TCP hoặc UDP đi ra từ máy tính
        # Để tránh nhiễu, trong thực tế ta sẽ lọc theo IP hoặc Port của Game/App cụ thể
        print("[*] Hệ thống sẽ tự động thu thập gói tin trong 15 giây...")
        sniff(prn=self.packet_callback, filter="tcp or udp", store=False, timeout=15)
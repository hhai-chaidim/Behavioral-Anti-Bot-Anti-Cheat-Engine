import socket
import time

def start_udp_spam():
    # Tạo một kết nối UDP ảo
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    target_ip = "8.8.8.8"  # Gửi đến DNS Google (chỉ để tạo traffic đi ra)
    target_port = 80
    
    print("Đang chạy Network Bot Simulator...")
    print("Bot sẽ gửi 30 gói tin UDP với khoảng cách chính xác tuyệt đối là 0.1 giây.")
    
    for i in range(30):
        # Nội dung gói tin rác
        message = b"BOT_SPAM_PACKET_TEST"
        sock.sendto(message, (target_ip, target_port))
        print(f"[Bot] Đã gửi gói tin thứ {i+1}")
        
        # Ngủ ĐÚNG 0.1 giây (Tạo ra độ trễ hoàn hảo)
        time.sleep(0.1)

    sock.close()
    print("Bot đã dừng gửi.")

if __name__ == "__main__":
    start_udp_spam()
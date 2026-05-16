from core.network_analyzer.packet_sniffer import NetworkProfiler
from core.decision_engine.network_behavior_analyzer import NetworkBehaviorAnalyzer

def main():
    print("="*50)
    print(" HỆ THỐNG BEHAVIORAL ANTI-BOT ĐANG KHỞI ĐỘNG")
    print("="*50)
    
    net_profiler = NetworkProfiler()
    try:
        net_profiler.start_sniffing()
    except KeyboardInterrupt:
        print("\n[!] Đã dừng Network Sniffer.")
        
        # Phân tích ngay sau khi dừng
        print("\n[*] Đang tiến hành phân tích Jitter mạng...")
        analyzer = NetworkBehaviorAnalyzer()
        analyzer.analyze()

if __name__ == "__main__":
    main()
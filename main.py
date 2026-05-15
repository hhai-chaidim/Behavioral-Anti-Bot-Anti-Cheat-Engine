from core.input_profiler.mouse_tracker import MouseProfiler

def main():
    print("="*50)
    print(" HỆ THỐNG BEHAVIORAL ANTI-BOT ĐANG KHỞI ĐỘNG")
    print("="*50)
    
    # Khởi tạo và chạy cảm biến chuột
    profiler = MouseProfiler()
    profiler.start_tracking()

# Cập nhật lại file main.py
from core.input_profiler.mouse_tracker import MouseProfiler
from core.decision_engine.behavior_analyzer import MouseBehaviorAnalyzer

def main():
    print("="*50)
    print(" HỆ THỐNG BEHAVIORAL ANTI-BOT ĐANG KHỞI ĐỘNG")
    print("="*50)
    
    profiler = MouseProfiler()
    profiler.start_tracking()

    # --- ĐOẠN NÀY CHẠY SAU KHI BẤM CTRL+C ---
    print("\n[*] Đang tiến hành phân tích dữ liệu log...")
    analyzer = MouseBehaviorAnalyzer()
    analyzer.analyze()

if __name__ == "__main__":
    main()
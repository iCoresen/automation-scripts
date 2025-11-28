import time
import webbrowser
import pygetwindow as gw
import threading
from datetime import datetime
import json
import os
import pyautogui

	
class StudyEnforcer:
    def __init__(self):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file = os.path.join(self.script_dir, "study_enforcer_config.json")
        self.load_config()

        self.is_active = False
        self.monitor_thread = None

    # ------------------- 配置管理 -------------------
    def load_config(self):
        default_config = {
            "active_start": "21:30",
            "active_end": "07:00",
            "check_interval": 3,
            "study_site": "https://weread.qq.com/",
            "bilibili_keywords": ["bilibili", "B站", "哔哩哔哩"],
            "learning_keywords": ["学习", "教程", "课程", "教学", "education", "tutorial", "lecture"],
            "test_mode": True,
            "test_duration": 120,
            "test_start_delay": 3
        }

        if not os.path.exists(self.config_file):
            self.config = default_config
            self.save_config()
            return

        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                user_config = json.load(f)

            merged_config = user_config.copy()
            config_changed = False

            for key, default_value in default_config.items():
                if key not in merged_config:
                    merged_config[key] = default_value
                    config_changed = True

            self.config = merged_config

            if config_changed:
                self.save_config()

        except Exception:
            self.config = default_config

    def save_config(self):
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)
        except Exception:
            pass

    # ------------------- 时间控制 -------------------
    def is_active_time(self):
        if self.config.get("test_mode", False):
            return True
        now = datetime.now().time()
        start_time = datetime.strptime(self.config["active_start"], "%H:%M").time()
        end_time = datetime.strptime(self.config["active_end"], "%H:%M").time()
        if start_time <= end_time:
            return start_time <= now <= end_time
        else:
            return now >= start_time or now <= end_time

    # ------------------- 检测逻辑 -------------------
    def is_bilibili_window(self, title):
        if not title:
            return False
        title = title.lower()
        for keyword in self.config["bilibili_keywords"]:
            if keyword.lower() in title:
                return True
        return False

    def is_learning_content(self, title):
        if not title:
            return False
        title = title.lower()
        for keyword in self.config.get("learning_keywords", []):
            if keyword.lower() in title:
                return True
        return False

    def close_browser_tab(self, window):
        try:
            window.activate()
            time.sleep(0.2)
            pyautogui.hotkey("ctrl", "w")
            return True
        except Exception:
            return False

    def redirect_to_study(self):
        try:
            webbrowser.open(self.config["study_site"])
        except Exception:
            pass

    def enforce_study_mode(self):
        try:
            windows = gw.getAllTitles()
            bilibili_windows = []

            for title in windows:
                if not title.strip():
                    continue
                if self.is_bilibili_window(title):
                    bilibili_windows.append(title)

            if not bilibili_windows:
                return

            for title in bilibili_windows:
                if self.is_learning_content(title):
                    continue

                try:
                    win_obj = [w for w in gw.getWindowsWithTitle(title) if w.isActive or w.isVisible][0]
                except IndexError:
                    continue

                if not self.close_browser_tab(win_obj):
                    try:
                        win_obj.close()
                    except Exception:
                        pass

                self.redirect_to_study()
                time.sleep(1)

        except Exception:
            pass

    # ------------------- 监控 -------------------
    def monitor_loop(self):
        start_time = time.time()

        while self.is_active:
            if self.is_active_time():
                self.enforce_study_mode()

                if self.config.get("test_mode", False):
                    if time.time() - start_time > self.config.get("test_duration", 60):
                        break
            else:
                break
            time.sleep(self.config["check_interval"])

        self.is_active = False

    # ------------------- 启动与计划 -------------------
    def start_monitoring(self):
        if self.is_active:
            return

        self.is_active = True
        delay = self.config.get("test_start_delay", 0)
    
        if delay > 0:
            print(f"将在 {delay} 秒后开始监控...")
            time.sleep(delay)
    
        self.monitor_thread = threading.Thread(target=self.monitor_loop, daemon=True)
        self.monitor_thread.start()

    def run(self):
        if not self.is_active_time():
            return

        self.start_monitoring()

# ------------------- 主程序 -------------------

def main():
    enforcer = StudyEnforcer()
    enforcer.run()
    
    # 保持主线程运行
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("程序已停止")


if __name__ == "__main__":
    main()

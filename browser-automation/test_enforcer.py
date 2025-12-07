import json
import time
import subprocess
import sys

def enable_test_mode():
    """启用测试模式"""
    config_file = "study_enforcer_config.json"

    # 读取当前配置
    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # 启用测试模式
    config["test_mode"] = True
    config["test_start_delay"] = 3  # 3秒后开始
    config["test_duration"] = 30  # 测试30秒

    # 保存配置
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

    print("测试模式已启用")
    print("3秒后开始测试，将持续30秒")
    return config


def disable_test_mode():
    """禁用测试模式"""
    config_file = "study_enforcer_config.json"

    # 读取当前配置
    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # 禁用测试模式
    config["test_mode"] = False

    # 保存配置
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

    print("测试模式已禁用")


def run_test():
    """运行测试"""
    print("启动测试...")

    # 启用测试模式
    enable_test_mode()

    try:
        # 启动主程序
        process = subprocess.Popen([sys.executable, "study_enforcer.pyw"])

        # 等待测试完成
        time.sleep(35)  # 略长于测试时间

        # 终止进程
        process.terminate()
        process.wait()

    except Exception as e:
        print(f"测试过程中出错: {e}")
    finally:
        # 禁用测试模式
        disable_test_mode()
        print("测试完成")


if __name__ == "__main__":
    run_test()
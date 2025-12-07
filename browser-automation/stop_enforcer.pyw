"""
一键关闭 StudyEnforcer 程序
双击即可关闭后台运行的监控程序
"""
import psutil
import os
import sys

def kill_study_enforcer():
    """查找并关闭所有 StudyEnforcer 相关进程"""
    script_name = "study_enforcer.pyw"  # 你的主程序文件名
    killed_count = 0
    found_processes = []
    
    print("=" * 60)
    print("正在查找 StudyEnforcer 进程...")
    print("=" * 60)
    
    try:
        # 遍历所有进程
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                # 检查是否是 Python 进程
                if proc.info['name'] in ['python.exe', 'pythonw.exe', 'python3.exe']:
                    cmdline = proc.info['cmdline']
                    if cmdline:
                        # 检查命令行参数中是否包含目标脚本
                        cmdline_str = ' '.join(cmdline)
                        if script_name in cmdline_str:
                            found_processes.append({
                                'pid': proc.info['pid'],
                                'cmdline': cmdline_str
                            })
                            
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        
        if not found_processes:
            print("❌ 未找到运行中的 StudyEnforcer 进程")
            print("\n可能的原因:")
            print("1. 程序未运行")
            print("2. 脚本名称不匹配（当前查找: {})".format(script_name))
            print("\n提示: 请检查你的主程序文件名")
        else:
            print(f"✅ 找到 {len(found_processes)} 个相关进程:\n")
            
            for i, proc_info in enumerate(found_processes, 1):
                print(f"{i}. PID: {proc_info['pid']}")
                print(f"   命令: {proc_info['cmdline'][:80]}...")
                
                try:
                    # 终止进程
                    proc = psutil.Process(proc_info['pid'])
                    proc.terminate()  # 优雅终止
                    
                    # 等待进程结束
                    try:
                        proc.wait(timeout=3)
                        print(f"   状态: ✅ 已成功关闭")
                        killed_count += 1
                    except psutil.TimeoutExpired:
                        # 如果优雅终止失败，强制杀死
                        proc.kill()
                        print(f"   状态: ✅ 已强制关闭")
                        killed_count += 1
                        
                except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                    print(f"   状态: ❌ 关闭失败 ({e})")
                
                print()
            
            print("=" * 60)
            print(f"共关闭 {killed_count}/{len(found_processes)} 个进程")
            
    except Exception as e:
        print(f"❌ 发生错误: {e}")
    
    print("=" * 60)
    input("按回车键退出...")

if __name__ == "__main__":
    kill_study_enforcer()
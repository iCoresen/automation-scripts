# 🎯 Study Enforcer

一个自动化脚本，帮助你在指定时间段内专注学习，自动检测并关闭非学习类 B 站视频，跳转到学习网站。

CSDN博客：https://blog.csdn.net/i_Coresen/article/details/152666689

## 💡 功能特点

- **智能检测**：实时监控浏览器窗口标题，识别 B 站页面
- **内容过滤**：自动识别学习类视频（含"学习"、"教程"等关键词），保留这些标签
- **自动跳转**：关闭娱乐内容后自动打开微信读书等学习网站
- **时间控制**：可设置生效时间段（如晚上 21:30 - 早上 7:00）
- **灵活配置**：通过 JSON 配置文件自定义所有参数

## 🚀 快速开始

### 环境要求
- Python 3.7+
- Windows 系统（使用了 `pygetwindow`）

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行脚本
```bash
python study_enforcer.py
```

首次运行会自动生成配置文件 `study_enforcer_config.json`。

## ⚙️ 配置说明

编辑 `study_enforcer_config.json` 自定义行为：

```json
{
    "active_start": "21:30",        // 开始监控时间
    "active_end": "07:00",          // 结束监控时间
    "check_interval": 3,            // 检测间隔（秒）
    "study_site": "https://weread.qq.com/",  // 跳转的学习网站
    "bilibili_keywords": [          // B站关键词识别
        "bilibili", "B站", "哔哩哔哩"
    ],
    "learning_keywords": [          // 学习内容关键词（这些不会被关闭）
        "学习", "教程", "课程", "教学", 
        "education", "tutorial", "lecture"
    ],
    "test_mode": true,              // 测试模式（立即生效）
    "test_duration": 120,           // 测试模式运行时长（秒）
    "test_start_delay": 3           // 启动延迟（秒）
}
```

### 配置说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `active_start` | 每天开始监控的时间 | "21:30" |
| `active_end` | 每天结束监控的时间 | "07:00" |
| `check_interval` | 窗口检测间隔（秒） | 3 |
| `study_site` | 关闭 B 站后跳转的网站 | 微信读书 |
| `test_mode` | 是否启用测试模式（忽略时间限制） | true |

## 📝 使用场景

### 场景1：晚上学习时段
设置 21:30 - 07:00 监控，这个时间段打开娱乐视频会自动跳转到学习网站。

### 场景2：保留学习视频
如果 B 站标题包含"Python教程"、"算法讲解"等关键词，不会被关闭。

### 场景3：测试模式
首次使用建议开启 `test_mode`，设置 `test_duration` 为 60 秒测试效果。

## 🛠️ 工作原理

1. **窗口监控**：每隔 N 秒扫描所有打开的窗口标题
2. **关键词匹配**：检测标题是否包含 B 站相关关键词
3. **内容过滤**：如果标题包含学习类关键词，则跳过
4. **执行操作**：
   - 激活目标窗口
   - 发送 `Ctrl+W` 快捷键关闭标签页
   - 打开预设的学习网站

## ⚠️ 注意事项

- **仅支持 Windows 系统**（Mac/Linux 需要修改窗口控制部分）
- **浏览器兼容性**：Chrome、Edge 等支持 `Ctrl+W` 关闭标签的浏览器
- **权限要求**：脚本需要有控制窗口和模拟键盘输入的权限
- **误判处理**：如果学习视频被误关，可以在配置中添加关键词

## 🔧 常见问题

**Q: 脚本没有生效？**  
A: 检查是否在配置的时间段内，或开启 `test_mode` 测试。

**Q: 学习视频也被关了？**  
A: 在 `learning_keywords` 中添加视频标题的关键词。

**Q: 想要关闭其他网站（如抖音、YouTube）？**  
A: 参考 `bilibili_keywords` 添加对应关键词即可。

**Q: 如何停止脚本？**  
A: 按 `Ctrl+C` 或直接关闭命令行窗口。

## 📦 依赖说明

- `pygetwindow`：获取和控制窗口
- `pyautogui`：模拟键盘操作

## 🎓 扩展思路

- 添加更多网站的监控（YouTube、抖音等）
- 接入番茄钟功能，定时提醒休息
- 记录每天被关闭的娱乐内容次数，生成学习报告
- 支持跨平台（Mac 用 `AppKit`，Linux 用 `wmctrl`）

## 📄 许可证

MIT License

---

💪 **自律即自由，祝你学习顺利！**
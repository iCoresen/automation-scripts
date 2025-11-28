# 📥 Batch Image Downloader - 批量图片下载器

一个简洁高效的批量图片下载工具，支持按页码顺序下载指定范围的图片资源。

> **PS：** 我是用来下载学习通课件PPT（图片），使用24 pdf tools 图片转 PDF，最后通过福昕 PDF 编辑器实现OCR 识别文字。

## 💡 功能特点

- ✅ 批量下载指定页码范围的图片
- ✅ 自动创建保存目录
- ✅ 实时显示下载进度
- ✅ 错误处理和重试机制
- ✅ 超时保护（10秒超时）
- ✅ 状态码检测，跳过失效资源

## 🚀 快速开始

### 环境要求
- Python 3.6+
- requests 库

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行脚本
```bash
python image_downloader.py
```

运行后根据提示输入页数范围，脚本会自动下载。

## ⚙️ 使用说明

### 基本用法

1. **运行脚本**
   ```bash
   python image_downloader.py
   ```

2. **输入页数**
   ```
   输入页数：50
   ```
   脚本将下载第 1 页到第 50 页的所有图片

3. **查看结果**
   下载的图片保存在 `downloaded_images/` 目录下

### 输出示例

```
正在下载：https://example.com/images/1.png
✅ 已保存：downloaded_images/1.png
正在下载：https://example.com/images/2.png
✅ 已保存：downloaded_images/2.png
...
全部下载完成！
```

## 🔧 自定义配置

### 修改下载 URL

编辑脚本中的 `base_url`：

```python
# 原始 URL 格式（大括号 {} 代表页码占位符）
base_url = "https://example.com/images/{}.png"

# 示例1：其他文件格式
base_url = "https://example.com/docs/{}.jpg"

# 示例2：带前缀的页码
base_url = "https://example.com/page_{}.png"

# 示例3：多级目录
base_url = "https://example.com/folder1/folder2/{}.png"
```

### 修改起始页码

```python
start_page = 1   # 改成你想要的起始页，比如从第10页开始
end_page = int(input("输入页数："))
```

### 修改保存目录

```python
save_folder = "my_images"  # 改成你想要的文件夹名
```

### 修改超时时间

```python
response = requests.get(url, timeout=10)  # 改成你想要的秒数
```

## 📁 文件结构

```
web-scraper/
├── image_downloader.py       # 主程序
├── requirements.txt          # 依赖列表
├── README.md                # 说明文档
└── downloaded_images/       # 下载目录（自动创建）
    ├── 1.png
    ├── 2.png
    └── ...
```

## 🛠️ 工作原理

1. **URL 构造** - 使用 Python 字符串格式化，将页码插入 URL 模板
2. **HTTP 请求** - 通过 `requests.get()` 发送 GET 请求获取图片数据
3. **状态检测** - 检查响应状态码，200 表示成功
4. **二进制写入** - 以 `wb` 模式写入文件，保存原始图片数据
5. **异常捕获** - 捕获网络错误、超时等异常，避免程序中断

## 📝 常见应用场景

### 场景1：漫画/小说章节下载
下载在线漫画或小说的连续页面图片

### 场景2：图库批量备份
备份图片网站的指定分页内容

### 场景3：缩略图采集
批量下载商品、文章的缩略图

### 场景4：数据集收集
为机器学习项目收集图片数据集

## ⚠️ 注意事项

- **遵守网站规则** - 使用前请检查目标网站的 `robots.txt` 和服务条款
- **请求频率控制** - 大量下载时建议添加延时（`time.sleep()`）避免被封 IP
- **版权问题** - 仅用于个人学习和研究，不得用于商业用途
- **网络稳定性** - 不稳定的网络可能导致部分下载失败，可重新运行脚本
- **存储空间** - 下载前确保硬盘有足够空间

## 🔧 常见问题

**Q: 下载速度很慢？**  
A: 可能是网络问题或服务器限速，可以尝试添加代理或更换网络环境。

**Q: 部分图片下载失败？**  
A: 检查 URL 格式是否正确，或该页码的资源是否存在。

**Q: 如何添加下载延迟？**  
A: 在循环中添加：
```python
import time
time.sleep(0.5)  # 每次下载间隔0.5秒
```

**Q: 如何断点续传？**  
A: 修改脚本检查文件是否已存在：
```python
if os.path.exists(save_path):
    print(f"⏭️ 跳过已存在文件：{save_path}")
    continue
```

**Q: 下载后如何合并 PDF？**  
A: 可以使用 `Pillow` 库或 `img2pdf` 库合并图片为 PDF：
```python
from PIL import Image
# 或使用 img2pdf 库
```

## 📦 依赖说明

- **requests** - HTTP 请求库，用于下载图片
  - 安装：`pip install requests`
  - 功能：发送 HTTP 请求、处理响应

## 🔐 安全建议

1. **不要硬编码敏感信息** - URL 中如含 token 应使用环境变量
2. **验证文件类型** - 检查响应头确认是图片格式
3. **限制文件大小** - 避免下载超大文件占用过多空间
4. **使用 HTTPS** - 优先使用加密连接

## 📄 许可证

MIT License - 仅供学习使用，请遵守目标网站的服务条款
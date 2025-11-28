import os
import requests

# === 参数设置 ===
base_url = "https://s3.cldisk.com/sv-w9/doc/01/23/33/8249edd138907ccc78df1a6628f85273/thumb/{}.png"
save_folder = "downloaded_images"
start_page = 1
end_page = int(input("输入页数："))  # 你可以自己改页数

# === 创建保存目录 ===
os.makedirs(save_folder, exist_ok=True)

# === 循环下载 ===
for i in range(start_page, end_page + 1):
    url = base_url.format(i)
    save_path = os.path.join(save_folder, f"{i}.png")

    try:
        print(f"正在下载：{url}")
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(response.content)
            print(f"✅ 已保存：{save_path}")
        else:
            print(f"❌ 第{i}页下载失败，状态码：{response.status_code}")
    except Exception as e:
        print(f"⚠️ 下载第{i}页出错：{e}")

print("\n全部下载完成！")

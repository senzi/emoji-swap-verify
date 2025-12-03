import os
import urllib.request
import time

# ================= 配置区域 =================
# 1. 保存路径 (会自动创建)
SAVE_DIR = "assets/emojis"

# 2. Twemoji CDN 基础 URL (版本 14.0.2)
BASE_URL = "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/svg/"

# 3. 精选“小黄脸” Unicode 列表 (十六进制，不带 0x)
# 这些是挑选出来的适合做消消乐的、辨识度高的表情
EMOJI_CODES = [
    # --- 开心/大笑 ---
    "1f600", # Grinning Face
    "1f603", # Grinning Face with Big Eyes
    "1f604", # Grinning Face with Smiling Eyes
    "1f606", # Grinning Squinting Face
    "1f609", # Winking Face
    "1f60a", # Smiling Face with Smiling Eyes
    
    # --- 搞怪/调皮 ---
    "1f61b", # Face with Tongue
    "1f61c", # Winking Face with Tongue
    "1f61d", # Squinting Face with Tongue
    "1f92a", # Zany Face (滑稽眼)
    "1f911", # Money-Mouth Face (钱眼)
    "1f929", # Star-Struck (星星眼)
    
    # --- 喜爱 ---
    "1f60d", # Smiling Face with Heart-Eyes
    "1f970", # Smiling Face with Hearts
    "1f618", # Face Blowing a Kiss
    
    # --- 酷/思考 ---
    "1f60e", # Smiling Face with Sunglasses (墨镜)
    "1f913", # Nerd Face (眼镜/书呆子)
    "1f914", # Thinking Face (思考)
    "1f928", # Face with Raised Eyebrow (挑眉)
    
    # --- 负面/难过/生气 ---
    "1f610", # Neutral Face (面无表情)
    "1f612", # Unamused Face (不爽)
    "1f644", # Face with Rolling Eyes (翻白眼)
    "1f622", # Crying Face (哭)
    "1f62d", # Loudly Crying Face (大哭)
    "1f620", # Angry Face (生气)
    "1f621", # Pouting Face (愤怒)
    "1f92c", # Face with Symbols on Mouth (脏话)
    
    # --- 惊讶/恐惧/不适 ---
    "1f631", # Screaming Face (尖叫/呐喊)
    "1f633", # Flushed Face (脸红/瞪眼)
    "1f635", # Dizzy Face (晕)
    "1f922", # Nauseated Face (恶心/绿脸)
    "1f92f", # Exploding Head (脑子炸了)
    "1f637", # Face with Medical Mask (口罩)
]

# ================= 主逻辑 =================

def download_emojis():
    # 1. 检查并创建目录
    if not os.path.exists(SAVE_DIR):
        try:
            os.makedirs(SAVE_DIR)
            print(f"📁 已创建目录: {SAVE_DIR}")
        except OSError as e:
            print(f"❌ 创建目录失败: {e}")
            return

    print(f"🚀 开始下载 {len(EMOJI_CODES)} 个表情...")
    print("-" * 30)

    success_count = 0

    for code in EMOJI_CODES:
        file_name = f"{code}.svg"
        file_path = os.path.join(SAVE_DIR, file_name)
        url = f"{BASE_URL}{file_name}"

        # 如果文件已存在，跳过
        if os.path.exists(file_path):
            print(f"⏭️  [跳过] 已存在: {file_name}")
            success_count += 1
            continue

        try:
            # 下载文件
            print(f"⬇️  正在下载: {file_name} ...", end="", flush=True)
            
            # 设置 User-Agent 防止被某些服务器拦截 (CDN通常不需要，但为了保险)
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            
            with urllib.request.urlopen(req) as response, open(file_path, 'wb') as out_file:
                data = response.read()
                out_file.write(data)
                
            print(" ✅")
            success_count += 1
            
            # 礼貌性延时，避免请求过快
            time.sleep(0.1) 

        except Exception as e:
            print(f" ❌ 失败 ({e})")

    print("-" * 30)
    print(f"🎉 任务完成! 成功获取: {success_count}/{len(EMOJI_CODES)}")
    print(f"📂 文件保存在: {os.path.abspath(SAVE_DIR)}")

if __name__ == "__main__":
    download_emojis()
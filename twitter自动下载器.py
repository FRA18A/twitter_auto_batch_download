
#首先F12网页，network下点击Img，然后上面有一个小下载，下载har文件。
import json
import requests
import os
import re
# Path to your .har file
har_file_path = "XXX.har"  # Replace with your .har file path
save_folder = "downloaded_images"  # Folder to save images

# Create save folder if it doesn't exist
os.makedirs(save_folder, exist_ok=True)

# Load the .har file
with open(har_file_path, "r", encoding="utf-8") as f:
    har_data = json.load(f)

# Extract image URLs
image_urls = []
for entry in har_data["log"]["entries"]:
    request = entry["request"]
    response = entry["response"]
    # Check if the response is an image
    content_type = response.get("content", {}).get("mimeType", "")
    if content_type.startswith("image/"):
        url = request["url"]
        image_urls.append(url)


# 删除末尾为svg的元素
filtered_list = [item for item in image_urls if not item.endswith('.svg')]

# 将每个元素的'&name=???'替换为'&name=medium'
modified_list = [re.sub(r'&name=[^&]*', '&name=medium', item) for item in filtered_list]

# 每99条数据保存为一个txt文件
output_dir = "output_files"
os.makedirs(output_dir, exist_ok=True)

for i in range(0, len(modified_list), 99):
    chunk = modified_list[i:i+99]
    file_number = i // 99 + 1
    with open(f"{output_dir}/output_{file_number}.txt", 'w', encoding='utf-8') as f:
        for item in chunk:
            f.write(item + '\n')

#然后放进Bulk Image Downloader里

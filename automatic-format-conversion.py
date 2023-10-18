import os
import json

# 1. 读取文件夹中的所有文件名
folder_path = "/Users/leah/Documents/es-icons/icons_list"  # 替换为你的文件夹路径
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 2. 根据文件名，决定加入到JSON中的哪一个键（icons或insets）
icons_list = []
insets_list = []

# 假设文件名中包含"icon"的加入到icons，包含"inset"的加入到insets
for file_name in file_names:
    if "icon" in file_name:
        icons_list.append(file_name)
    elif "inset" in file_name:
        insets_list.append(file_name)

# 3. 读取已有的JSON文件，然后加入新的内容
json_file_path = "/Users/leah/Documents/es-icons/json/ecp-dashboard.json"  # 替换为你的JSON文件路径
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    data['icons'].extend(icons_list)
    data['insets'].extend(insets_list)

# 4. 保存修改后的JSON文件
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

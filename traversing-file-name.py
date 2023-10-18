import os
# 遍历文件夹中的所有文件，并按照Json要求的“”格式输出
folder_path = "/Users/leah/Documents/工作文件/graph-resouce-services/source/insets"
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

formatted_names = ',\n'.join([f'"{name}"' for name in file_names])
print(formatted_names)
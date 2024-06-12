import os
import shutil
from PIL import Image


def move_files_to_directory(source_directory, target_directory):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            source_path = os.path.join(root, file)
            # 构建目标文件路径
            _file = file.replace(".jpg", ".png")
            target_path = os.path.join(target_directory, _file)
            # 移动文件
            jpg_image = Image.open(source_path)
            # 将 JPG 图像保存为 PNG 格式
            jpg_image.save(target_path, "PNG")
            print(f"Moved {source_path} to {target_path}")


# 指定源文件夹和目标文件夹的路径
source_directory_path = (
    "C:/Users/37359/OneDrive/under-graduate/大三上学期课件/机器学习实验/大作业/dataset/Others"
)
target_directory_path = (
    "C:/Users/37359/OneDrive/under-graduate/大三上学期课件/机器学习实验/大作业/dataset/Others"
)

# 移动源文件夹中的所有文件到目标文件夹
move_files_to_directory(source_directory_path, target_directory_path)

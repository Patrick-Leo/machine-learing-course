from PIL import Image
import os


def resize_image(input_image_path, output_image_path, width, height):
    for root, dirs, files in os.walk(input_image_path):
        for file in files:
            source_path = os.path.join(root, file)
            original_image = Image.open(source_path)
            resized_image = original_image.resize((width, height), Image.LANCZOS)
            target_path = os.path.join(output_image_path, file)
            resized_image.save(target_path)


# 指定输入图像路径和输出图像路径以及目标宽度和高度
input_path = "C:/Users/37359/OneDrive/under-graduate/大三上学期课件/机器学习实验/大作业/pic"
output_path = "C:/Users/37359/OneDrive/under-graduate/大三上学期课件/机器学习实验/大作业/dataset/Owner"
target_width = 250
target_height = 250

# 调用函数来缩放图像
resize_image(input_path, output_path, target_width, target_height)

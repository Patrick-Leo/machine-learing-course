# %pip install -U yolov5

import yolov5
import torch
from PIL import Image

# load model
model = yolov5.load("fcakyon/yolov5s-v7.0")

# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1000  # maximum number of detections per image


def get_face_crop_img_path(ori_img_path, dest_path):
    # set image
    img = ori_img_path

    # perform inference
    results = model(img)

    # inference with test time augmentation
    results = model(img, augment=True)

    # parse results
    predictions = results.pred[0]
    boxes = predictions[:, :4]  # x1, y1, x2, y2
    scores = predictions[:, 4]
    categories = predictions[:, 5]

    face_indexes = []
    for i in range(len(results.pred[0])):
        record = results.pred[0][i]
        cata = record[5]
        if cata == 0:
            face_indexes.append(i)

    # 无人脸
    if face_indexes == []:
        return ""
    else:
        # 取概率最大的人脸
        max_idx = -1
        max_score = 0
        for i in face_indexes:
            record = results.pred[0][i]
            posibility = record[4]
            if posibility > max_score:
                max_score = posibility
                max_idx = i

    # show detection bounding boxes on image
    results.show()

    # save results into "results/" folder
    results.save(save_dir="results/")

    # return cliped face fig
    box_cordinates = results.pred[0][max_idx][:4].tolist()
    print(box_cordinates)

    def crop_and_save_image(input_image_path, output_image_path, coordinates):
        # 打开输入图像
        original_image = Image.open(input_image_path)

        # 根据提供的坐标截取图像的部分
        left, upper, right, lower = coordinates
        cropped_image = original_image.crop((left, upper, right, lower))

        # 保存截取的图像为新的文件
        cropped_image.save(output_image_path)

    # 指定输入图像路径和输出图像路径
    input_path = img
    output_path = dest_path

    # 指定截取的坐标 (left, upper, right, lower)
    coordinates_to_crop = tuple(box_cordinates)

    # 调用函数进行截取和保存
    crop_and_save_image(input_path, output_path, coordinates_to_crop)

    return output_path

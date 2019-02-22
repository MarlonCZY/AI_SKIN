import os
from PIL import Image


def resizeImage(imagePath,imageName):
    path = imagePath
    name = imageName

    im = Image.open(path)
    im224 = im.resize((224, 224))
    im224.save("/Users/ziyuancui/Desktop/liang/request_img/inference_img_224/" + imageName)

    im299 = im.resize((229, 229))
    im299.save("/Users/ziyuancui/Desktop/liang/request_img/inference_img_299/" + imageName)

    f = open("/Users/ziyuancui/Desktop/liang/request_img/test.txt", "w")
    print >> f, "image, (case), type, age, has_age, sex, has_sex, (melanoma), (keratosis), (schedule), (weight)"

    print >> f, imageName[:-4] + ", , d, 30, 1, male, 1, 0, 0, 0, 0"

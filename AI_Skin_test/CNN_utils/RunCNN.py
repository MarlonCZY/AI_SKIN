import os
import ResizeImage

def runCNN(imagePath, imageName):
    os.system("mkdir /Users/ziyuancui/Desktop/liang/request_img/inference_img_299")
    os.system("mkdir /Users/ziyuancui/Desktop/liang/request_img/inference_img_224")
    os.system("mkdir /Users/ziyuancui/Desktop/liang/request_img/test.224.tfr")
    os.system("mkdir /Users/ziyuancui/Desktop/liang/request_img/test.299.tfr")
    os.system("mkdir /Users/ziyuancui/Desktop/liang/request_img/test.features")

    os.system("echo \'generate test data\'")

    ResizeImage.resizeImage(imagePath,imageName)

    os.system("echo \'generate features\'")

    os.system("python /Users/ziyuancui/Desktop/liang/datasets/convert_skin_lesions.py " 
              "TEST /Users/ziyuancui/Desktop/liang/request_img/test.txt "
              "/Users/ziyuancui/Desktop/liang/request_img/inference_img_299 "
              "/Users/ziyuancui/Desktop/liang/request_img/test.299.tfr /Users/ziyuancui/Desktop/liang/data/no-blacklist.txt")

    os.system("python /Users/ziyuancui/Desktop/liang/datasets/convert_skin_lesions.py "
              "TEST /Users/ziyuancui/Desktop/liang/request_img/test.txt "
              "/Users/ziyuancui/Desktop/liang/request_img/inference_img_224 "
              "/Users/ziyuancui/Desktop/liang/request_img/test.224.tfr /Users/ziyuancui/Desktop/liang/data/no-blacklist.txt")

    os.system("/Users/ziyuancui/Desktop/liang/etc/predict_all_component_models_isbi.sh "
              "/Users/ziyuancui/Desktop/liang/request_img/test.299.tfr "
              "/Users/ziyuancui/Desktop/liang/request_img/test.224.tfr test "
              "/Users/ziyuancui/Desktop/liang/request_img/test.features")

    os.system("echo \'merge features\'")

    os.system("python /Users/ziyuancui/Desktop/liang/etc/assemble_meta_features.py ALL_LOGITS "
              "/Users/ziyuancui/Desktop/liang/request_img/test.features "
              "/Users/ziyuancui/Desktop/liang/request_img/test.features/isbitest.metall.features")

    os.system(
        "python /Users/ziyuancui/Desktop/liang/predict_svm_layer.py --input_model /Users/ziyuancui/Desktop/liang/running/svm.models/metall.svm --input_test  /Users/ziyuancui/Desktop/liang/request_img/test.features/isbitest.metall.features --pool_by_id xtrm > /Users/ziyuancui/Desktop/liang/request_img/result.txt")

    os.system("rm -r /Users/ziyuancui/Desktop/liang/request_img/inference_img_299")
    os.system("rm -r /Users/ziyuancui/Desktop/liang/request_img/inference_img_224")
    os.system("rm -r /Users/ziyuancui/Desktop/liang/request_img/test.224.tfr")
    os.system("rm -r /Users/ziyuancui/Desktop/liang/request_img/test.299.tfr")
    os.system("rm -r /Users/ziyuancui/Desktop/liang/request_img/test.features")


    with open("/Users/ziyuancui/Desktop/liang/request_img/result.txt", 'r') as file:
        result  = file.readline()
        return result.split(',')


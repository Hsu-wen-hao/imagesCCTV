import xml.etree.ElementTree as ET
import os
import shutil

class_dict = {"Motorcycle":0, "MotorcycleWithRiderWithHelmet":1, "MotorcycleWithRiderWithoutHelmet":2, "Bicycle":3, "BicycleWithRider":4, "Bus":5, "Sedan": 6, "Taxi":7, "SmallTruck":8, "Truck":9, "TrailerWithCargo":10, "TrailerWithoutCargo":11, "PoliceCar":12, "Ambulance":13, "FireEngine":14, "ConstructionVehicle": 15,"SpecialPurposeVehicle":16, "Cart":17, "OtherTransport":18, "AdultUnderUmbrella":19, "Adult":20, "ChildUnderUmbrella":21, "Child":22, "TrafficController":23, "ConstructionWorker":24, "Animal":25, "Litter":26, "Roadblock":27, "TrafficLight":28, "Others":29}

dataset_ori_root = "C:/Users/TMS-Product/Desktop/Hao電腦資料/[技轉資料] 技轉景翊科技/2020/[項次1-3] 機車、大客車、一般房車影像物件標記資料庫 V1.0/2020_技轉景翊日間物件45萬筆_交付版"
dataset_new_root = "C:/Users/TMS-Product/Desktop/T 大使/dataset_2020"

for i, dir_name in enumerate(os.listdir(dataset_ori_root)):
    print("[%d / %d] is processing..." % (i, len(os.listdir(dataset_ori_root))))
    # 複製圖片
    for img_name in os.listdir(os.path.join(dataset_ori_root, dir_name, "images")):
        img_ori_path = os.path.join(dataset_ori_root, dir_name, "images", img_name)
        img_new_path = os.path.join(dataset_new_root, "images", img_name)
        shutil.copyfile(img_ori_path, img_new_path)
    
    for xml_name in os.listdir(os.path.join(dataset_ori_root, dir_name, "xml")):
        # 讀取 xml 檔並轉成 txt 檔
        tree = ET.parse(os.path.join(dataset_ori_root, dir_name, "xml", xml_name))
        root = tree.getroot()
        image_width = int(root.find("size").find("width").text)
        image_height = int(root.find("size").find("height").text)
            
        txt_name = xml_name[:-4] + ".txt"     # txt 檔名
        with open(os.path.join(dataset_new_root, "labels", txt_name), "w") as f:
            for element in root:
                if element.tag == "object":  # 找出道路物件
                    class_name = element.find("name").text
                    xmin = int(element.find("bndbox")[0].text)
                    ymin = int(element.find("bndbox")[1].text)
                    xmax = int(element.find("bndbox")[2].text)
                    ymax = int(element.find("bndbox")[3].text)
                    
                    f.write(str(class_dict[class_name]) + " ")                # class
                    f.write(str(((xmin + xmax) / 2.) / image_width) + " ")    # x_center
                    f.write(str(((ymin + ymax) / 2.) / image_height) + " ")   # y_center
                    f.write(str((xmax - xmin) / image_width) + " ")           # width
                    f.write(str((ymax - ymin) / image_height) + "\n")         # height
                    
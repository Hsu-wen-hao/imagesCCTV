import os
import shutil
import random

root = "C:/Users/TMS-Product/Desktop/T 大使/dataset_2020/train/images"
total_list = os.listdir(root)
total_size = len(total_list)
val_size = int(total_size * 0.1)
test_size = int(total_size * 0.1)

dataset_root = "C:/Users/TMS-Product/Desktop/T 大使/dataset_2020/"
train_root = dataset_root + "train/"
val_root = dataset_root + "val/"
test_root = dataset_root + "test/"
# train -> val
for i in range(val_size):
    image_name = random.choice(total_list)
    total_list.remove(image_name)
    label_name = image_name[:-4] + ".txt"
    shutil.move(train_root + "images/" + image_name, val_root + "images/" + image_name)
    shutil.move(train_root + "labels/" + label_name, val_root + "labels/" + label_name)
    print("\r[val][%d/%d] done..." % (i+1, val_size), end="")
# train -> test
for i in range(test_size):
    image_name = random.choice(total_list)
    total_list.remove(image_name)
    label_name = image_name[:-4] + ".txt"
    shutil.move(train_root + "images/" + image_name, test_root + "images/" + image_name)
    shutil.move(train_root + "labels/" + label_name, test_root + "labels/" + label_name)
    print("\r[test][%d/%d] done..." % (i+1, val_size), end="")

# mylist = ["11", "22", "33"]
# cc = random.choice(mylist)
# mylist.remove(cc)
# print(cc)
# print(mylist)
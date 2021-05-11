# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:50:09 2021

@author: rudrasomeshwar
"""

import base64
import json
import os

from labelme import utils


def main():
    out_dir = '.\png_labels'  # all .png labels must be stored in a directory with given name
    if not os.path.exists(out_dir):  # if directory does not exist, create a new one
        os.mkdir(out_dir)

    for root, dirs, files in os.walk('.'):  # top-down walk function in the root directory to iterate over each file
        for file in files:
            if os.path.splitext(file)[1] == '.json':  # check if file is .json format

                data = json.load(open(file))  # load the .json file
                imageData = data.get("imageData")

                if not imageData:  # if imageData key not found, find img using imagePath and encode it in base64 format
                    imagePath = os.path.join(os.path.dirname(file), data["imagePath"])
                    with open(imagePath, "rb") as f:
                        imageData = f.read()
                        imageData = base64.b64encode(imageData).decode("utf-8")
                img = utils.img_b64_to_arr(imageData)  # save base64 image in array

                label_name_to_value = {"_background_": 0}  # using labelme library to plot label shape
                for shape in sorted(data["shapes"], key=lambda x: x["label"]):
                    label_name = shape["label"]
                    if label_name in label_name_to_value:
                        label_value = label_name_to_value[label_name]
                    else:
                        label_value = len(label_name_to_value)
                        label_name_to_value[label_name] = label_value

                lbl, _ = utils.shapes_to_label(
                    img.shape, data["shapes"], label_name_to_value
                )

                filename = os.path.splitext(file)[0] + '.png'  # save image as .png with original name of .json
                utils.lblsave(os.path.join(out_dir, filename), lbl)


if __name__ == "__main__":
    main()

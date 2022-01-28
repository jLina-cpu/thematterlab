import os
import cv2
import numpy as np

replaced_material_dir = "/Users/jolinali/Desktop/Blender/obj2gltf/images_nm"
coloured_material_dir = "/Users/jolinali/Desktop/Blender/obj2gltf/images_colordiff"
concatenated_img_dir = "/Users/jolinali/Desktop/Blender/obj2gltf/images_concatenate"
rmd = os.listdir(replaced_material_dir)
cmd = os.listdir(coloured_material_dir)

for i in range(len(rmd)):
    """
    Concatenate the image with replaced material and the same image with 
    coloured material. Save the concatenated image in the concatenated_img_dir 
    folder.
    """
    if rmd[i] != '.DS_Store':
        rm_img = replaced_material_dir + "/" + rmd[i]
        cm_img = coloured_material_dir + "/" + cmd[i]
        rmi = cv2.imread(rm_img)
        cmi = cv2.imread(cm_img)
        img = np.concatenate([rmi, cmi], axis=1)

        concatenated_img_path = concatenated_img_dir + "/" + rmd[i]
        cv2.imwrite(concatenated_img_path, img)

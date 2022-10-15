import os
import cv2
import numpy as np

original_material_dir = "/Users/jolinali/Desktop/Blender/obj2gltf/images"
replaced_material_dir = "/Users/jolinali/Desktop/Blender/obj2gltf/images_nm"
coloured_material_dir = "/Users/jolinali/Desktop/Blender/obj2gltf/images_colordiff"
concatenated_img_dir = "/Users/jolinali/Desktop/Blender/obj2gltf/og_rm_col"
omd = os.listdir(original_material_dir)
rmd = os.listdir(replaced_material_dir)
cmd = os.listdir(coloured_material_dir)

for i in range(len(omd)):
    """Concatenate the original image with the image with replaced material 
    and the same image with coloured material. Save the concatenated image in 
    the concatenated_img_dir folder. 
    """
    if omd[i] != '.DS_Store':
        om_img = original_material_dir + "/" + omd[i]
        rm_img = replaced_material_dir + "/" + omd[i]
        cm_img = coloured_material_dir + "/" + omd[i]
        omi = cv2.imread(om_img)
        rmi = cv2.imread(rm_img)
        cmi = cv2.imread(cm_img)
        if rmi is not None:
            img = np.concatenate([omi, rmi, cmi], axis=1)

            concatenated_img_path = concatenated_img_dir + "/" + omd[i]
            cv2.imwrite(concatenated_img_path, img)

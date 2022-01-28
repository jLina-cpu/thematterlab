import numpy as np
import cv2
import os
import random


def output_annotations():
    """Read from images_nm dataset and output images with color/number
    annotations into the images_colordiff and images_numdiff folders.
    """
    a = Annotations()
    a.grey_diff()
    a.color_segment()
    a.num_segment()


class Annotations:
    """
    Color and number annotations for material segmentation.
    """

    # constructor
    def __init__(self):
        self.wbfolder = "/Users/jolinali/Desktop/Blender/obj2gltf" \
                        "/images_whiteblack"
        self.greyfolder = "/Users/jolinali/Desktop/Blender/obj2gltf" \
                          "/images_graydiff"
        self.cdiffolder = "/Users/jolinali/Desktop/Blender/obj2gltf" \
                          "/images_colordiff"
        self.numdiffolder = "/Users/jolinali/Desktop/Blender/obj2gltf" \
                            "/images_numdiff"

    def grey_diff(self):
        """
        Create a new image, for each material, that contains the difference
        between black and white (i.e. grey).
        """
        random.shuffle(os.listdir(self.wbfolder))
        for obj in os.listdir(self.wbfolder):
            if obj != '.DS_Store':
                obj_folder = self.wbfolder + '/' + obj
                dif_objpath = self.greyfolder + '/' + obj
                os.mkdir(dif_objpath)
                images = os.listdir(obj_folder)
                images.sort()
                for i in range(len(images)):
                    x1 = images[i][-10]
                    if (i + 1) < len(images):
                        x2 = images[i + 1][-10]
                        if x1 == x2:
                            img_path1 = obj_folder + '/' + images[i]
                            img_path2 = obj_folder + '/' + images[i + 1]
                            i1 = cv2.imread(img_path1)
                            i2 = cv2.imread(img_path2)

                            dif = np.abs(i1 - i2)
                            dif = (dif > 0).astype(np.uint8) * 100
                            dif_path = dif_objpath + '/' + obj + '_' + x1 + 'gray.png'
                            cv2.imwrite(dif_path, dif)

    # annotate material by color
    def color_segment(self):
        """
        Segment the material by colour.
        """
        colors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255),
                  (255, 255, 0),
                  (0, 255, 255), (255, 0, 255), (192, 192, 192),
                  (128, 128, 128),
                  (128, 0, 0), (128, 128, 0), (0, 128, 0), (128, 0, 128),
                  (0, 128, 128),
                  (0, 0, 128)]

        for obj in os.listdir(self.greyfolder):
            if obj != '.DS_Store':
                obj_folder = self.greyfolder + '/' + obj
                images = os.listdir(obj_folder)
                images.sort()
                rgb_im = np.zeros([1080, 1920, 3], dtype=np.uint8)
                for im_title in images:
                    im_path = obj_folder + '/' + im_title
                    im = cv2.imread(im_path, 0)
                    bool_matrix = (im > 0)
                    i = random.randint(0, len(colors) - 1)
                    rgb_im[bool_matrix] = colors[i]
                save_path = self.cdiffolder + '/' + obj + '.png'
                cv2.imwrite(save_path, rgb_im)

    # annotate material by number
    def num_segment(self):
        """
        Segment the material by number.
        """
        for obj in os.listdir(self.greyfolder):
            if obj != '.DS_Store':
                obj_folder = self.greyfolder + '/' + obj
                images = os.listdir(obj_folder)
                images.sort()
                uimg = np.zeros([1080, 1920], dtype=np.uint8)
                i = 1
                for im_title in images:
                    im_path = obj_folder + '/' + im_title
                    im = cv2.imread(im_path, 0)
                    bool_matrix = (im > 0)
                    uimg[bool_matrix] = i
                    i += 1
                save_path = self.numdiffolder + '/' + obj + '.png'
                cv2.imwrite(save_path, uimg)


if __name__ == '__main__':
    output_annotations()

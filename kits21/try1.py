import numpy as np
import os
import nibabel as nib
from nibabel.testing import data_path
import SimpleITK as tk
import skimage.io as io
import matplotlib.pyplot as plt
np.set_printoptions(precision = 2, suppress = True)
example0 = os.path.join(data_path, "F:\k21\kits21\kits21\data\case_00000\imaging.nii.gz")
img0 = nib.load(example0)
print(img0.shape)

def itk_read(path):
    img = tk.ReadImage(path)
    data = tk.GetArrayFromImage(img)
    return data
'''def itk_show_one(ori_img):
    io.imshow(ori_img[90], cmap = 'inferno')
    io.show()'''
def itk_show_all(data):
    plt.imshow(data[0,:,:], cmap = 'inferno')
    plt.show()
path = "F:\k21\kits21\kits21\data\case_00000\imaging.nii.gz"
path1 = "F:\k21\kits21\kits21\data\case_00000\segmentations\kidney_instance-1_annotation-1.nii.gz"
#data = itk_read(path)
#itk_show_all(data)
I = tk.ReadImage(path)
img1 = tk.GetArrayFromImage(I)
print(img1.shape)
plt.imshow(img1[69,:,:], cmap = 'inferno', interpolation = 'bicubic')
plt.show()

I1 = tk.ReadImage(path1)
img2 = tk.GetArrayFromImage(I1)
print(img2.shape)
plt.imshow(img2[511,:,:], cmap = 'inferno', interpolation = 'bicubic')
plt.show()
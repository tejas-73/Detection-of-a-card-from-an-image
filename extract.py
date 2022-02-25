from cv2 import cv2 #Better method to extract card
from sklearn.cluster import KMeans
import numpy as np
from copy import deepcopy
from PIL import Image as img
import time
np.set_printoptions(threshold=np.inf, suppress=True)


#Method 1: Continuous K-Means Clustering with reducing patches by quadruple

path = "Images/card (48).jpg"
start_time = time.time()
patches_size = 2**6 #Make sure this is even power of 2


def create_image(patch_matrices_list, show_image=True):
    if len(patch_matrices_list) == 1:
        temp_matrix2 = patch_matrices_list[0]
    for i in range(len(patch_matrices_list)):
        if i % np.sqrt(len(patch_matrices_list)) == 0:
            temp_matrix1 = patch_matrices_list[i]
        else:
            temp_matrix1 = np.append(temp_matrix1, patch_matrices_list[i], axis=1)
            if i == np.sqrt(len(patch_matrices_list)) - 1:
                temp_matrix2 = temp_matrix1
            elif (i+1) % np.sqrt(len(patch_matrices_list)) == 0:
                temp_matrix2 = np.append(temp_matrix2, temp_matrix1, axis=0)
    if show_image:
        #img.fromarray(temp_matrix2).show()
        img.fromarray(temp_matrix2).save("1.jpg")
    return temp_matrix2


def get_patches(image_matrix, patches_size=64, if_create_image=False):
    size = int(np.sqrt(patches_size))
    if size == 1:
        patches = []
        patches.append(image_matrix)
        return patches
    height, width, _ = np.shape(image_matrix)
    patch_width = int(width/size)
    patch_height = int(height/size)
    patch_adjust_width = width - (size - 1)*patch_width
    patch_adjust_height = height - (size - 1)*patch_height
    patches = [] #This will contain the cropped matrices which form partition of image, the starting point and the ending points of crops
    for i in range(size - 1):
        for j in range(size - 1):
            temp = image_matrix[(i*patch_height):((i+1)*patch_height), (j*patch_width):((j+1)*patch_width), :]
            patches.append((temp, i*patch_height, j*patch_width, (i+1)*patch_height-1, (j+1)*patch_width-1))
            if i == (size - 2) and j < (size - 2):
                temp = image_matrix[((i+1)*patch_height):((i+1)*patch_height + patch_adjust_height), (j*patch_width):((j+1)*patch_width), :]
                patches.append((temp, (i+1)*patch_height, j*patch_width, (i+1)*patch_height + patch_adjust_height, (j+1)*patch_width))
            elif j == (size - 2) and i < (size - 2):
                temp = image_matrix[(i*patch_height):((i+1)*patch_height), ((j+1)*patch_width):((j+1)*patch_width + patch_adjust_width), :]
                patches.append((temp, i*patch_height, (j+1)*patch_width, (i+1)*patch_height-1, (j+1)*patch_width + patch_adjust_width))
            elif i == (size - 2) and j == (size - 2):
                temp = image_matrix[(i * patch_height):((i + 1) * patch_height), ((j+1) * patch_width):((j + 1) * patch_width + patch_adjust_width), :]
                patches.append((temp, i * patch_height, (j + 1) * patch_width, (i + 1) * patch_height - 1, (j + 1) * patch_width + patch_adjust_width))
                temp = image_matrix[((i+1)*patch_height):((i+1)*patch_height + patch_adjust_height), (j*patch_width):((j+1)*patch_width), :]
                patches.append((temp, (i+1)*patch_height, j*patch_width, (i+1)*patch_height + patch_adjust_height, (j+1)*patch_width))
                temp = image_matrix[((i+1)*patch_height):((i+1)*patch_height + patch_adjust_height), ((j+1)*patch_width):((j+1)*patch_width + patch_adjust_width), :]
                patches.append((temp, (i+1)*patch_height, (j+1)*patch_width, (i+1)*patch_height + patch_adjust_height, (j+1)*patch_width + patch_adjust_width))
    temp1 = patches[patches_size - 2*size][1]
    temp_list1 = []
    temp_list2 = []
    for i in range((patches_size - 2*size), patches_size):
        if patches[i][1] == temp1:
            temp_list1.append(patches[i])
        else:
            temp_list2.append(patches[i])
    patches = patches[0:(patches_size - 2*size)]
    patches = patches + temp_list1 + temp_list2
    patches1 = deepcopy(patches)
    patches_list = []
    for i in range(patches_size):
        patches_list.append(patches1[i][0])
    if if_create_image:
        create_image(patches_list)
    return patches_list


def clustering(patches, clusters=2):
    mat_list1 = []
    for i in range(len(patches)):
        h, w, c = patches[i].shape
        test = patches[i].reshape((h*w, c))
        kmeans = KMeans(n_clusters=clusters).fit(test)
        classification_array = kmeans.predict(test).reshape((h, w))
        image_mats1 = np.zeros(patches[i].shape)
        image_mats2 = np.zeros(patches[i].shape)
        non_zero1 = np.count_nonzero(classification_array == 1)
        non_zero2 = np.count_nonzero(classification_array == 0)
        loc1 = np.where(classification_array == 1)
        loc2 = np.where(classification_array == 0)
        if len(loc1[0]) == 0 or len(loc2[0]) == 0:
            mat_list1.append(patches[i])
            continue
        for j in range(c):
            image_mats1[:, :, j][loc1] = round(np.sum(patches[i][:, :, j][loc1])/non_zero1)
        for j in range(c):
            image_mats2[:, :, j][loc2] = round(np.sum(patches[i][:, :, j][loc2])/non_zero2)
        mat_list1.append(image_mats1.astype(np.uint8) + image_mats2.astype(np.uint8))
    create_image(mat_list1)
    return mat_list1


def increase_patch_size(patches):
    mat_list = []
    i = 0
    while i in range(0, len(patches)-int(np.sqrt(len(patches)))):
        if i % np.sqrt(len(patches)) == 0 and i != 0:
            i = i + int(np.sqrt(len(patches)))
        mat_list.append(np.append(np.append(patches[i], patches[i+1], axis=1), np.append(patches[i + int(np.sqrt(len(patches)))], patches[i+int(np.sqrt(len(patches)))+1], axis=1), axis=0))
        i += 2
    return mat_list


def method1(): #Considering commands for method 1
    patches = get_patches(np.array(img.open(path)), patches_size=patches_size)
    #img.open(path).show()
    for i in range(int(np.log2(patches_size))//2):
        patches = increase_patch_size(clustering(patches))
    clustering(patches)


#Method 2 for decomposing image into two partitions directly, with considering intensity effects
def method2():  # Considering commands for method 2
    h, w, _ = np.array(np.array(img.open(path))).shape
    test_size = (h+w)//10        #This is to avoid unneccesary background effects or overfitting
    illuminance_factor = 20     #Based on image illumination, but kept constant in general, but depends on image for results
    kmeans_testing_size = (h+w)//4 #for getting higher accuracy of card detection

    temp = cv2.cvtColor(np.array(img.open(path)), cv2.COLOR_BGR2YUV)
    width, height, channel = temp.shape
    temp[:, :, 0] = temp[:, :, 0]//illuminance_factor
    image_mats = cv2.cvtColor(temp, cv2.COLOR_YUV2BGR) #This is in accordance with reducing intensity effects

    image_mats1 = np.array(img.fromarray(image_mats).resize(size=(test_size, test_size)))
    image_mat0 = (image_mats1[:, :, 0]).flatten()
    image_mat1 = (image_mats1[:, :, 1]).flatten()
    image_mat2 = (image_mats1[:, :, 2]).flatten()
    test = []

    for i in range(test_size**2):
        test.append(tuple(np.array([image_mat0[i], image_mat1[i], image_mat2[i]])))

    kmeans = KMeans(n_clusters=2).fit(np.array(test))
    img1 = np.array(img.Image.resize(img.fromarray(image_mats), (kmeans_testing_size, kmeans_testing_size), resample=img.BILINEAR)) #This is to increase processing speed with a cost of decrease in the prediction accuracy of card
    h, w, _ = img1.shape

    image_mat0 = img1[:, :, 0].flatten()
    image_mat1 = img1[:, :, 1].flatten()
    image_mat2 = img1[:, :, 2].flatten()
    test.clear()

    for i in range(h*w):
        test.append(tuple(np.array([image_mat0[i], image_mat1[i], image_mat2[i]])))

    classification_array = kmeans.predict(test)
    classification_array = classification_array.reshape((h, w))
    final_classification_array = np.round_(np.array(img.Image.resize(img.fromarray(classification_array), (height, width), resample=img.BILINEAR)))
    image_mats1 = np.zeros(image_mats.shape)

    #This is to form Image! So no issues here as of now
    image_mats = np.array(img.open(path))
    for i in range(3):
        image_mats1[:, :, i] = np.multiply(image_mats[:, :, i], final_classification_array)
    for i in range(3):
        image_mats[:, :, i] = np.multiply(image_mats[:, :, i], 1 - final_classification_array)
    # img.fromarray(image_mats1.astype(np.uint8)).show()
    img.fromarray(image_mats1.astype(np.uint8)).save("2.jpg")
    # img.fromarray(image_mats.astype(np.uint8)).show()
    img.fromarray(image_mats.astype(np.uint8)).save("3.jpg")
    print(time.time() - start_time)


if __name__ == "__main__":
    method1()
    method2()

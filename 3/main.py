import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def plot_multiple_kernel_3_3(first,second):
    plt.subplot(121),plt.imshow(first),plt.title('One time')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(second),plt.title('Multiple')
    plt.xticks([]), plt.yticks([])
    plt.show()

def results_of_different_kernels():
    rows = 3
    columns = 2
    fig = plt.figure(figsize=(50, 50))

    fig.add_subplot(rows, columns, 1)
    plt.imshow(img,cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
    plt.title("Raw IMG")
    fig.add_subplot(rows, columns, 2)
    plt.imshow(dst1,cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
    plt.title("3*3 Kernel")
    fig.add_subplot(rows, columns, 3)
    plt.imshow(dst2,cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
    plt.title("5*5 Kernel")
    fig.add_subplot(rows, columns, 4)
    plt.imshow(dst3,cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
    plt.title("7*7 Kernel")
    fig.add_subplot(rows, columns, 5)
    plt.imshow(dst4,cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
    plt.title("9*9 Kernel")
    fig.add_subplot(rows, columns, 6)
    plt.imshow(dst5,cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
    plt.title("15*15 Kernel")
    plt.show()

img = cv.imread('test.tif')
kernel1 = np.ones((3,3),np.float32)/9
kernel2 = np.ones((5,5),np.float32)/25
kernel3 = np.ones((7,7),np.float32)/49
kernel4 = np.ones((9,9),np.float32)/81
kernel5 = np.ones((15,15),np.float32)/225
# kernel1 = kernel1/(kernel1.shape[0]*kernel1.shape[1])
dst1 = cv.filter2D(img,-1,kernel1)
dst2 = cv.filter2D(img,-1,kernel2)
dst3 = cv.filter2D(img,-1,kernel3)
dst4 = cv.filter2D(img,-1,kernel4)
dst5 = cv.filter2D(img,-1,kernel5)
dest6= cv.filter2D(dst1,-1,kernel1)
dest6= cv.filter2D(dest6,-1,kernel1)
dest6= cv.filter2D(dest6,-1,kernel1)
dest6= cv.filter2D(dest6,-1,kernel1)
dest6= cv.filter2D(dest6,-1,kernel1)
dest6= cv.filter2D(dest6,-1,kernel1)
dest6= cv.filter2D(dest6,-1,kernel1)

results_of_different_kernels()
plot_multiple_kernel_3_3(dst1,dest6)
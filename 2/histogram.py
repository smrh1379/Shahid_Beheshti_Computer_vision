import time
import matplotlib.pyplot as plt #importing matplotlib
import numpy as np
from PIL import Image, ImageOps
rawimg = Image.open('snow.jpg').convert('L')
img=np.array(rawimg)
amounts=[]
for i in range(0,256):
    amounts.append((img.flatten()==i).sum())
amounts=np.array(amounts)
cumsum=amounts.cumsum()
final=cumsum/amounts.sum()
transform_map = np.floor(255 * final).astype(np.uint8)
shape=img.shape
img_list = list(img.flatten())
equal_img_list = [transform_map[p] for p in img_list]
equal_img_array = np.reshape(np.asarray(equal_img_list), shape)
equal_img = Image.fromarray(equal_img_array, mode='L')
im2 = ImageOps.equalize(rawimg)
rows = 2
columns = 2
fig = plt.figure(figsize=(20, 20))

fig.add_subplot(rows, columns, 1)
plt.imshow(img,cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.title("First")
fig.add_subplot(rows, columns, 2)
plt.imshow(equal_img,cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.title("Histogram by me")
fig.add_subplot(rows, columns, 3)
plt.imshow(im2,cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.title("Histogram by pillow")
plt.show()

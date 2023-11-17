import cv2
import matplotlib.pyplot as plt
img = cv2.imread("img3.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blured_img = cv2.GaussianBlur(img_gray, (65, 65),0, 0)
final_img = cv2.divide(img_gray, blured_img, scale=255)
plt.figure(figsize=(7,7))
plt.imshow(final_img,cmap="gray")
plt.axis("off")
plt.title("Final Sketch Image")
plt.show()
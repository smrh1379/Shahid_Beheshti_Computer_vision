from PIL import Image
from PIL import ImageDraw
img=Image.open('cv.jpeg')
I1 = ImageDraw.Draw(img)
I1.text((18, 20), "Computer Vision Course Sbu", fill=(255, 255, 255))
img.show()
Img2= Image.open('cv.jpeg')
Img1_size = img.size
Img2_size = Img2.size
new_image = Image.new('RGB',(2*Img1_size[0], Img1_size[1]), (250,250,250))
new_image.paste(img,(0,0))
new_image.paste(Img2,(Img1_size[0],0))
new_image.save("merged_image.jpg","JPEG")
new_image.show()

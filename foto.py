from PIL import Image
from PIL.ImageDraw import ImageDraw

width = 340
height= 340
color= (255,0,0)
image=Image.new("RGB",(width,height),color)

# for y in range(height):
#     for x in range(width):
#         red = int(255*x/width)
#         green=0
#         blue=0
#         image.putpixel(x,y),(red,green,blue)

from PIL import imageDraw

draw=ImageDraw.Draw(image)
# draw.rectangle((50,50,250,250),fill=(0,255,0))
# draw.ellipse((100,100,200,200),fill=(0,0,255))
# draw.line((0,0,300,300), fill=(255,0,0))


image.show()

image.save("Umar.png")
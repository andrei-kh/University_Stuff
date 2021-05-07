import numpy as np
from PIL import Image, ImageOps

im1 = Image.open("XOR_my_flag.png")
im2 = Image.open("XOR_my_zoo.png")

im1np = np.array(im1)
im2np = np.array(im2)

result = np.bitwise_xor(im2np, im1np).astype(np.uint8)

resultImage = Image.fromarray(result)

resultImage = ImageOps.invert(resultImage)

resultImage.save('XOR_result.png')

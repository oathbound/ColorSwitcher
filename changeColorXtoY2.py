from PIL import Image
import numpy as np

im = Image.open('avatar_large_1.png')
im = im.convert('RGBA')

#data = np.array(im)   # "data" is a height x width x 4 numpy array
red, green, blue, alpha = data.T # Temporarily unpack the bands for readability

# Replace white with red... (leaves alpha values alone...)
select_areas = (red == 255) & (blue == 0) & (green == 77)
data[..., :-1][select_areas] = (3, 36, 77)

im2 = Image.fromarray(data)
im2.show()

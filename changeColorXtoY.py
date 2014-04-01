from PIL import Image
import numpy as np
import glob


r1, g1, b1 = 255, 77, 0 # Original value
r2, g2, b2, a2 = 0xFF, 0x43, 0x26, 255 # Value that we want to replace it with



def recolorImage(imagename):
    im = Image.open(imagename)
    im = im.convert('RGBA')

    data = np.array(im)

    im.info

    for i in data:
        for j in i:
            r,g,b,a =  j[0], j[1],j[2],j[3]
            if r > 242:
                if r==r1 and g==g1 and b==b1:
                    j[0], j[1],j[2],j[3]=r2,g2,b2,a2                
                elif r==b and r==g:
                    pass               
                else:               
                    #print "{},{},{},".format(r,g,b)
                    j[0], j[1],j[2],j[3]=r2,g2,b2,a2

    im2 = Image.fromarray(data)
    im2.show()
    im2.info
    im2name, im2ext = imagename.split('.')
    im2.save('G&C/cAxis/img/{}.{}'.format(im2name, im2ext))

if __name__ == "__main__":
    files = glob.glob("icons.png")
    #files = glob.glob("avatar_*.png")
    print files

    for f in files:
        recolorImage(f)
        

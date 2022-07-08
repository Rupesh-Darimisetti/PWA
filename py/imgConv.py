from PIL import Image
# import PIL
# import os
import glob
from tkinter import filedialog as tkfd

class imgCov:
    # PNG to WEBP
    def png_webp(self,img):
        self.img = img
        file_path = img
        image = Image.open(file_path)
        image = image.convert('RGB')
        name = self.img.split('.')[0]
        image.save(f'{name}.webp', 'webp')
        print("image saved:"+self.img.split('.')[0])
    # JPG to WEBP
    def jpg_webp(self,img):
        self.img = img
        file_path = self.img
        image = Image.open(file_path)
        image = image.convert('RGB')
        name = self.img.split('.')[0]
        image.save(f'{name}.webp', 'webp')
    
    # PNG to JPG
    def png_jpg(self,img):
        self.img = img
        file_path = self.img
        image = Image.open(file_path)
        image = image.convert('RGB')
        name = self.img.split('.')[0]
        image.save(f'{name}.jpg', 'jpeg')
        
    # JPG to PNG
    def jpg_png(self,img):
        file_path = self.img
        image = Image.open(file_path)
        image = image.convert('RGB')
        name = self.img.split('.')[0]
        image.save(f'{name}.png', 'png')
   
    # WebP to PNG
    def webp_png(self,img):
        file_path = self.img
        image = Image.open(file_path)
        image = image.convert('RGB')
        name = self.img.split('.')[0]
        image.save(f'{name}.png', 'png')
    
    #WebP to JPG
    def webp_jpg(self,img):
        file_path = self.img
        image = Image.open(file_path)
        image = image.convert('RGB')
        name = self.img.split('.')[0]
        image.save(f'{name}.jpg', 'jpeg')
if __name__ == '__main__':
    obj = imgCov()
    obj.jpg_webp(tkfd.askopenfile())
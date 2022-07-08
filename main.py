
from py import imgConv as ic
from tkinter import filedialog as tkfd

if __name__ == '__main__':
    print("Welcome to image file converter")
    print("Select a option to convert images")
    print("type 1 PNG to WEBP")
    print("type 2 JPG to WEBP")
    print("type 3 PNG to JPG")
    print("type 4 JPG to PNG")
    print("type 5 WEBP to PNG")
    print("type 6 WEBP to JPG")

    option = int(input())
    file = tkfd.askopenfile()
    file_path = file
    if option == 1:
        print("you enter png image")
        ic.png_webp(file_path)
        print("webp image saved")
    elif option == 2:
        ic.jpg_webp(file_path)
    elif option == 3:
        ic.png_jpg(file_path)
    elif option == 4:
        ic.jpg_webp(file_path)
    elif option == 5:
        ic.webp_png(file_path)
    elif option == 6:
        ic.webp_jpg(file_path)



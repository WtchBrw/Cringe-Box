from PIL import Image
import os
import cv2
import sys

#ASCII chars used to create video output
ASCII_CHARS = ["@", "#", "0", "%", "?", "*", "+", ";", ":", ".", ","]

#Converts image to greyscale image
def gray_image(image, new_width=210):
    width, height = image.size
    aspect_ratio = height/width
    new_height = int(aspect_ratio * new_width)
    gray_image = image.resize((new_width, new_height)).convert("L")
    return gray_image

#Converts greyscale image to ascii chars
def pix2chars(image):
    pixels = image.getdata()
    character = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return character

#Generates ascii image frames and prints to console
def generate_frame(image, new_width=210):
    new_image_data = pix2chars(gray_image(image))
    total_pixels = len(new_image_data)
    ascii_vid = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, total_pixels, new_width)])
    sys.stdout.write(ascii_vid)
    os.system("cls")

#Display ahegao art and then show numbers corresponfding with different player chices (which ftp server, what file path, what url, quit, etc)

vid_source = cv2.VideoCapture("E:\YTDL\Anime\Canaan.mp4") #Grab url or file path to video

while 1 == 1:
    ret, frame = vid_source.read()
    cv2.imshow("frame", frame)
    generate_frame(Image.fromarray(frame))
    cv2.waitKey(10)
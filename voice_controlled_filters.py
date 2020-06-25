"""
File: voice_controlled_filters.py
----------------
Take an image. Generate the reflection of it, or apply sepia filter just by giving voice command...!!
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage
import time

import speech_recognition as sr
import pyaudio

pic='images/mt-rainier.jpg'


def make_reflected(filename):
    image = SimpleImage(filename)
    w=image.width
    h=image.height
    reflect=SimpleImage.blank(w*2,h)
    for y in range(h):
        for x in range(w):
            pixel=image.get_pixel(x,y)
            reflect.set_pixel(x,y,pixel)
            reflect.set_pixel((w*2)-(x+1),y,pixel)
    final=SimpleImage.blank(w,h)
    z=2*w
    for y in range(h):
        for x in range(z):
            pixel=reflect.get_pixel(x,y)
            if pixel.x>=w:
                final.set_pixel(x-w,y,pixel)
    return final

''' Create Sepia Filter'''
def sepia(filename):
    image = SimpleImage(filename)
    for pixel in image:
        pixel.red= pixel.red * 0.393 + pixel.green * 0.769 + pixel.blue * 0.189
        pixel.green=pixel.red * 0.349 + pixel.green * 0.686 + pixel.blue * 0.168
        pixel.blue=pixel.red * 0.272 + pixel.green * 0.534 + pixel.blue * 0.131
    return image

def voice_command():
    r = sr.Recognizer()
    mic = sr.Microphone()

    print("Do you want Image Reflection or Sepia Filter?")
    print("When prompted say 'Reflection' if you want to see the mirror image")
    print("When prompted say 'Apply Filter' if you want to see the sepia filtered image")
    print("Say something now...!!")
    with mic as source:

        audio = r.listen(source)
    print(r.recognize_google(audio))
    return r.recognize_google(audio)


def main():
    """
    This part makes use of the speech recognition output
    """


    x=voice_command()
    #time.delay(3)
    if x=='apply filter':
        original = SimpleImage(pic)
        original.show()
        sepia_filter=sepia(pic)
        sepia_filter.show()

    if x=='reflection':
        original = SimpleImage(pic)
        original.show()
        reflected = make_reflected(pic)
        reflected.show()




if __name__ == '__main__':
    main()

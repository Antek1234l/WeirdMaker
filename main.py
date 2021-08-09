import time, random
from PIL import Image, ImageFont, ImageDraw
from tkinter.filedialog import *

fonts = ['arial.ttf','timesnewroman.tff']
texts = ['generations','this is computer generated','it is not real']

def add_text(image):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(random.choice(fonts),random.randint(30, 51))


def main():
    base_image = askopenfile(filetypes=(('JPEG files','jpg.*'),('PNG files','png.*')))


if __name__=='__main__':
    main()
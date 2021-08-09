import time, random, PIL, math
from PIL import Image, ImageFont, ImageDraw
from tkinter.filedialog import *
from tkinter import *
from tkinter import filedialog

fonts = ['arial.ttf','times.ttf']
texts = ['generations','this is computer generated','it is not real']


def add_text(img):
    #image = PIL.Image.open(img)
    font = PIL.ImageFont.truetype(random.choice(fonts),random.randint(30,51))
    draw = ImageDraw.Draw(img)
    h, w = img.size
    x_coord = int(random.randint(x1,x2))
    y_coord = int(random.randint(y1,y2))
    redval = int(random.choice(['0','255']))
    greenval = int(random.choice(['0','255']))
    blueval = int(random.choice(['0','255']))
    draw.text(xy=(x_coord,y_coord),text = random.choice(texts), fill=(redval,greenval,blueval), font=font)
    return img

def crop(img):
    img = PIL.Image.open(img)
    h, w = img.size
    #ratio = w/h
    global x1,x2,y1,y2
    x1 = random.randint(0,int(w/3))
    x2 = random.randint(int(h-h/3),h)
    y1 = random.randint(0,int(h/3))
    y2 = random.randint(int(w-w/3),w)
    return img.crop((x1,y1,x2,y2))


def main():
    print('Select the base image: ')
    time.sleep(1.5)
    filetypes = (('JPEG images', '*.jpg'),('PNG images', '*.png'))
    base_image_dir = filedialog.askopenfilename(filetypes=filetypes)
    times = time.time()
    print('Making weirdcore...')
    cropped = crop(base_image_dir)
    with_text = add_text(cropped)
    timend = time.time()
    print(f'Done in {round(timend-times,3)} seconds')
    print('Select save path: ')
    time.sleep(1.5)
    path = askdirectory()
    with_text.save(path+'/GeneratedWC.jpg',quality = random.randint(18,30))


if __name__=='__main__':
    main()
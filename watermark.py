import os
import sys
from datetime import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def watermark_text(input_image_path,
                   output_image_path,
                   text):
    photo = Image.open(input_image_path)
    drawing = ImageDraw.Draw(photo)
    w, h = photo.size
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 50)
    text_w, text_h = drawing.textsize(text, font)
    pos = w - text_w - 25, (h - text_h) - 25
    c_text = Image.new('RGB', (text_w, (text_h)), color='#000000')
    drawing = ImageDraw.Draw(c_text)
    drawing.text((0, 0), text, fill="#ffffff", font=font)
    c_text.putalpha(100)
    photo.paste(c_text, pos, c_text)
    photo.save(output_image_path)


def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    w, h = base_image.size
    img_w, img_h = watermark.size
    pos = w - img_w - 25, (h - img_h) - 25
    transparent = Image.new('RGBA', (w, h), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, pos, mask=watermark)
    transparent.save(output_image_path)


if __name__ == '__main__':
    os.system('clear')
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
    print('░██╗░░░░░░░██╗░█████╗░████████╗███████╗██████╗░███╗░░░███╗░█████╗░██████╗░██╗░░██╗░')
    print('░██║░░██╗░░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗████╗░████║██╔══██╗██╔══██╗██║░██╔╝░')
    print('░╚██╗████╗██╔╝███████║░░░██║░░░█████╗░░██████╔╝██╔████╔██║███████║██████╔╝█████═╝░░')
    print('░░████╔═████║░██╔══██║░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗░░')
    print('░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║░░██║██║░░██║██║░╚██╗░')
    print('░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░')
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print('{0} | Developer: Daniil Mironyk'.format(dt_string))
    print('{0} | Version: 1.0.4'.format(dt_string))
    print('{0} | Required packages: pillow tkinter'.format(dt_string))

    choice_image = {'image'}
    choice_text = {'text'}
    print('{0} | Do you want to add a watermark as "text" or "image":'.format(dt_string), end=' ')
    choice = input().lower()
    if choice in choice_image:
        Tk().withdraw()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('{0} |'.format(dt_string), end=' ')
        img_input = askopenfilename(filetypes=[('JPEG pictures', '*.jpg'), ('PNG pictures', '*.png')],
                              title="Please select a Image")
        print('Image: {0}'.format(img_input))
        Tk().withdraw()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('{0} |'.format(dt_string), end=' ')
        watermark_img = askopenfilename(filetypes=[sg.In()],
                             title="Please select a Watermark")
        print('Watermark: {0}'.format(watermark_img))
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('{0} |'.format(dt_string), end=' ')
        output_file = input("Output file name: ") + '.png'
        watermark_with_transparency(img_input, output_file, watermark_img)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('{0} |'.format(dt_string), end=' ')
        pwd = os.getcwd()
        print('Saved file: {0}/{1}'.format(pwd, output_file))
    elif choice in choice_text:
        Tk().withdraw()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('{0} |'.format(dt_string), end=' ')
        img = askopenfilename(filetypes=[('JPEG pictures', '*.jpg'), ('PNG pictures', '*.png')],
                              title="Please select a Image")
        print('Input file: {0}'.format(img))
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('{0} |'.format(dt_string), end=' ')
        ans = input("Watermark text: ")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('{0} |'.format(dt_string), end=' ')
        output_file = input("Output file name: ") + '.png'
        watermark_text(img, output_file, text=ans)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('{0} |'.format(dt_string), end=' ')
        pwd = os.getcwd()
        print('Saved file: {0}/{1}'.format(pwd, output_file))
    else:
      sys.stdout.write("{0} | Please respond with 'image' or 'text'\n".format(dt_string))

      window.close()

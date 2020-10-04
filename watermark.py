from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

print('Привет, мой дорогой пользователь если ты хочешь зделать водяной знак напиши \n 1) "+" \n 2)"-" ')
otwet = input()


def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path,
                                position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size

    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save(output_image_path)
    Tk().withdraw()
    filename = askopenfilename()

while otwet == "+":
 if __name__ == '__main__':
    import easygui
    img = easygui.fileopenbox(filetypes=["*.jpg"])
    watermark_with_transparency(img, 'Img1.png','watermark.png', position=(0,0))
 break
else:
     print("Вы ввели не тот символ или вы перехотели проводить эту операцию)")

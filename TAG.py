from PIL import Image, ImageDraw, ImageFont

img = Image.new(mode="RGB", size=(128, 72), color=(34, 32, 52, 255))

draw = ImageDraw.Draw(img)

fnt = ImageFont.truetype("arial.ttf", size = 22)

draw.text(xy=(10, 20), text="Hello World", size=12,font=fnt)

img.save(
    'frame_1.png',
    save_all=True,
    #for animation
    #append_images = list
    #duration = int
    #loop = int
)
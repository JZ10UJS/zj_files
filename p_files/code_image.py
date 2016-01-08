#!/usr/bin/python
# coding: utf-8

"""
当前目录下，生成code.jpg
"""

import random

from PIL import Image, ImageDraw, ImageFont, ImageFilter


def rndChar():
    return chr(random.randint(65,90))


def rndColor():
    return (random.randint(64,255), random.randint(64,255),
            random.randint(64,255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127),
            random.randint(32, 127))


def main():
    # 建一个240*60的全白的RGB image
    width = 240
    height = 60
    image = Image.new('RGB', (width, height), (255,255,255))
    print '240*60 image has been initialized...'

    font = ImageFont.truetype('arial', 36)

    draw = ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    print 'fill color...'

    for t in range(4):
        draw.text((60*t+10, 10), rndChar(), font=font, fill=rndColor2())
    print 'fill code...'

    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg','jpeg')
    print 'code image done!'


if __name__ == '__main__':
    main()

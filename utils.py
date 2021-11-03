from hashlib import sha256
from PIL import Image, ImageDraw


def hash_data(data):
    return sha256(data.encode('utf-8')).hexdigest()


def rounded_image(image):
    empty_image = Image.new('RGBA', image.size, 0)
    circle_mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(circle_mask)
    draw.ellipse((0, 0, *image.size), fill=255)
    empty_image.paste(image, (0, 0), circle_mask)
    return empty_image

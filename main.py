"""
Лабораторная 8 Вариант 9
Написать функцию, которая принимает путь к изображению и список пикселей и заменяет полученные пиксели прозрачным
цветом, сохраняя изображение в той же директории.
"""

from PIL import Image

def replace_all_pixels_with_transparent_color(image_path):
    image = Image.open(image_path)
    transparent_color = (0, 0, 0, 0)  # RGBA цвет прозрачности

    width, height = image.size
    for x in range(width):
        for y in range(height):
            image.putpixel((x, y), transparent_color)

    image.save(image_path)


image_path = "Image.jpg"
replace_all_pixels_with_transparent_color(image_path)
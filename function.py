from random import randint
from PIL import Image


def stenography(path_keys, path_image_base, path_image_new, text):
    keys = []
    img = Image.open(path_image_base)
    width = img.size[0]
    height = img.size[1]
    pix = img.load()
    for elem in [ord(el) for el in text]:
        key = (randint(0, width - 1), randint(0, height - 1))
        ind = randint(0, 2)
        while (key[0], key[1], ind) in keys:
            key = (randint(0, width - 1), randint(0, height - 1))
            ind = randint(0, 2)
        r, g, b = pix[key][:3]
        res = [r, g, b]
        res[ind] = elem
        pix[key] = tuple(res)
        keys.append((key[0], key[1], ind))
        print(elem)
    keys = [';'.join(list(map(str, el))) for el in keys]

    with open(path_keys + '/keys.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(keys))
    img.save(path_image_new + '/newimage.png', "PNG")


def destenography(path_keys, path_image):
    img = Image.open(path_image)
    pix = img.load()
    with open(path_keys, 'r', encoding='utf-8') as file:
        keys = file.read().split('\n')

    text = ''
    keys = [list(map(int, el.split(';'))) for el in keys]
    for key in keys:
        coord = tuple(key[:2])
        elem = chr(pix[coord][key[2]])
        text += elem
    return text


if __name__ == '__main__':
    if input() == '1':
        stenography()
    else:
        destenography()

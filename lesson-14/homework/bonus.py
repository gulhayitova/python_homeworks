import numpy as np
from PIL import Image

def flip_horizontal(file_path, newfile_name):
    image = np.array(Image.open(file_path))
    hor_flip = np.fliplr(image)
    Image.fromarray(hor_flip).save(newfile_name)

def flip_vertical(file_path, newfile_name):
    image = np.array(Image.open(file_path))
    ver_flip = np.flipud(image)
    Image.fromarray(ver_flip).save(newfile_name)

def noise(file_path, newfile):
    image = np.array(Image.open(file_path))
    noise = np.random.randint(0, 50, image.shape, dtype = np.uint8)
    noisy_image = np.clip(image + noise, 0, 255)
    Image.fromarray(noisy_image).save(newfile)

def brighten(file_path, newfile):
    image = np.array(Image.open(file_path))
    bright_image = np.clip(image + 20, 0, 255)
    Image.fromarray(bright_image).save(newfile)

def mask_it(file_path, newfile, mask_size):
    image = np.array(Image.open(file_path))
    h, w, _ = image.shape
    centery, centerx = h/2, w/2
    masked_image = image.copy()
    masked_image[int(centery - mask_size//2) : int(centery + mask_size//2),
                int(centerx - mask_size//2) : int(centerx + mask_size//2)] = (0, 0, 0)
    Image.fromarray(masked_image).save(newfile)
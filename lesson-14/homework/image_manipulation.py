import numpy as np
from PIL import Image

image = np.array(Image.open("birds.jpg"))
hor_flip = np.fliplr(image)
ver_flip = np.flipud(image)
Image.fromarray(hor_flip).save("flipped_h.jpg")
Image.fromarray(ver_flip).save("flipped_v.jpg")

noise = np.random.randint(0, 50, image.shape, dtype = np.uint8)
noisy_image = np.clip(image + noise, 0, 255)
Image.fromarray(noisy_image).save("noisy_birds.jpg")

bright_image = np.clip(image + 20, 0, 255)
Image.fromarray(bright_image).save("birght_birds.jpg")

h, w, _ = image.shape
centery, centerx = h/2, w/2
masked_image = image.copy()
masked_image[int(centery - 50) : int(centery + 50),
             int(centerx - 50) : int(centerx + 50)] = (0, 0, 0)
Image.fromarray(masked_image).save("masked_image.jpg")
import tensorflow as tf
import numpy as np
import cv2

model = tf.keras.models.load_model('static/generator_model')


def generate_images(num_images):
    random_noise = np.random.randn(num_images, 100)
    generated_images = model.predict(random_noise, verbose=0)
    generated_images = (generated_images * 127.5 + 127.5).astype('uint8')
    return generated_images


def resize_images(images, size):
    resized_images = []

    for image in images:
        image = cv2.resize(image, size)
        resized_images.append(image)

    return resized_images

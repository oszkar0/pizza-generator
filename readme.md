# Pizza Generator Project

## Description

The Pizza Generator is an application that uses Deep Convolutional Generative Neural Networks to generate pizza images. This project includes model training and an API with a simple front-end.

## Model Training

The core of the project involves training a neural network to generate pizza images. I used Google Colab to build and train the model, consisting of a generator and a critic network. The critic network improves its ability to distinguish real from generated images with each training epoch, while the generator network aims to produce more convincing pizza images. Libraries like `numpy`, `matplotlib`, and `tensorflow` were utilized for this phase.

To view the training process, visit the following link: [Pizza Generator Model Training](model-training/pizza-image-generator-training.ipynb).

## API and Front-end Development

I implemented an API using Flask, offering a single endpoint, `/generate_images`, for generating pizza images. Users can specify the image size (default is 64x64, but resizing is possible using `cv2.resize`) and the number of images to generate.

Upon calling the endpoint, the application generates pizza images, resizes them, encodes them using base64, and delivers the results. The recipient is a web page that displays four pizza images of the chosen size when the "Generate" button is pressed.

For a live demonstration of the API and front-end code, please visit: [Pizza Generator API and Front-end](api/pizza-image-generator).

## Deployment

The Pizza Generator website is deployed on Heroku, making it accessible to users. You can experience the Pizza Generator by visiting the following link: [Pizza Generator on Heroku](https://pizza-generator-2b4db2d6c6e8.herokuapp.com/).

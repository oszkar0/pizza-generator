from flask import Flask, render_template, request, jsonify
import image_generating_and_processing as imgp

# Create a Flask Instance
app = Flask(__name__)


# Create a route decorator for main page
@app.route('/')
def index():
    return render_template('index.html')


# Create a route decorator for generating images
@app.route('/generate_images', methods=['GET'])
def generate_images():
    # generate images with model.predict
    num_images = int(request.args.get('num_images', default=4))
    size = int(request.args.get('image_size', default=64))

    generated_images = imgp.generate_images(num_images)
    resized_images = imgp.resize_images(generated_images, size=(size, size))
    encoded_images = imgp.b64_encode_images(resized_images)

    return jsonify({"images": encoded_images})

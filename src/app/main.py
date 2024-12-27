import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from process import convert_to_grayscale, identify_shading_patterns  # Import processing functions
import cv2

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return jsonify(message="Welcome to the Artist Shading App API!")

@app.route('/process-image', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify(error="No file provided"), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify(error="No file selected"), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Process the image
    try:
        grayscale = convert_to_grayscale(filepath)
        shading = identify_shading_patterns(grayscale)

        # Save processed images (optional)
        grayscale_path = os.path.join(app.config['UPLOAD_FOLDER'], f"grayscale_{filename}")
        shading_path = os.path.join(app.config['UPLOAD_FOLDER'], f"shading_{filename}")
        cv2.imwrite(grayscale_path, grayscale)
        cv2.imwrite(shading_path, shading)

        return jsonify(
            message="File processed successfully",
            grayscale_path=grayscale_path,
            shading_path=shading_path
        )
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)

import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from process import convert_to_grayscale, identify_shading_patterns  # Import processing functions
import cv2

app = Flask(__name__)

# Configure upload folders
UPLOAD_FOLDER = 'uploads'
ORIGINAL_FOLDER = os.path.join(UPLOAD_FOLDER, 'original')
PROCESSED_FOLDER = os.path.join(UPLOAD_FOLDER, 'processed')
os.makedirs(ORIGINAL_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def clear_folder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Clear previous files
        clear_folder(ORIGINAL_FOLDER)
        clear_folder(PROCESSED_FOLDER)

        if 'file' not in request.files:
            return "No file provided", 400

        file = request.files['file']
        if file.filename == '':
            return "No file selected", 400

        filename = secure_filename(file.filename)
        filepath = os.path.join(ORIGINAL_FOLDER, filename)
        file.save(filepath)

        # Process the uploaded file
        try:
            grayscale = convert_to_grayscale(filepath)
            shading = identify_shading_patterns(grayscale)

            # Save processed images
            grayscale_path = os.path.join(PROCESSED_FOLDER, f"grayscale_{filename}")
            shading_path = os.path.join(PROCESSED_FOLDER, f"shading_{filename}")
            cv2.imwrite(grayscale_path, grayscale)
            cv2.imwrite(shading_path, shading)

            return f"""
                <h1>File processed successfully!</h1>
                <p>Grayscale Image: <a href="/{grayscale_path}" target="_blank">View</a></p>
                <p>Shading Image: <a href="/{shading_path}" target="_blank">View</a></p>
                <a href="/">Upload another file</a>
            """
        except Exception as e:
            return f"Error: {str(e)}", 500

    # Serve the upload form
    return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Upload File</title>
        </head>
        <body>
            <h1>Upload an Image</h1>
            <form action="/" method="post" enctype="multipart/form-data">
                <label for="file">Choose an image:</label>
                <input type="file" name="file" id="file" accept="image/*" required>
                <button type="submit">Upload and Process</button>
            </form>
        </body>
        </html>
    """

@app.route('/process-image', methods=['POST'])
def process_image():
    # Clear previous files
    clear_folder(ORIGINAL_FOLDER)
    clear_folder(PROCESSED_FOLDER)

    if 'file' not in request.files:
        return jsonify(error="No file provided"), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify(error="No file selected"), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(ORIGINAL_FOLDER, filename)
    file.save(filepath)

    # Process the uploaded file
    try:
        grayscale = convert_to_grayscale(filepath)
        shading = identify_shading_patterns(grayscale)

        # Save processed images
        grayscale_path = os.path.join(PROCESSED_FOLDER, f"grayscale_{filename}")
        shading_path = os.path.join(PROCESSED_FOLDER, f"shading_{filename}")
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

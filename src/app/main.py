import os
from flask import Flask, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename
from process import convert_to_grayscale, identify_shading_patterns
import cv2

app = Flask(__name__)

# Configure upload folders
UPLOAD_FOLDER = 'uploads'
ORIGINAL_FOLDER = os.path.join(UPLOAD_FOLDER, 'original')
PROCESSED_FOLDER = os.path.join(UPLOAD_FOLDER, 'processed')
os.makedirs(ORIGINAL_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Utility function for processing a single image
def process_file(filepath, filename):
    grayscale = convert_to_grayscale(filepath)
    shading = identify_shading_patterns(grayscale)

    # Save processed images
    grayscale_path = os.path.join(PROCESSED_FOLDER, f"grayscale_{filename}")
    shading_path = os.path.join(PROCESSED_FOLDER, f"shading_{filename}")
    cv2.imwrite(grayscale_path, grayscale)
    cv2.imwrite(shading_path, shading)

    return {
        "original": filepath,
        "grayscale": f"/static/{grayscale_path}",
        "shading": f"/static/{shading_path}"
    }

# Serve static files (processed images)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
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
            processed = process_file(filepath, filename)
            return f"""
                <h1>File processed successfully!</h1>
                <p>Grayscale Image: <a href="{processed['grayscale']}" target="_blank">View</a></p>
                <p>Shading Image: <a href="{processed['shading']}" target="_blank">View</a></p>
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

@app.route('/process-images', methods=['GET'])
def process_images():
    files = os.listdir(ORIGINAL_FOLDER)
    processed_files = []

    for file in files:
        file_path = os.path.join(ORIGINAL_FOLDER, file)
        if os.path.isfile(file_path):
            filename = secure_filename(file)
            try:
                processed_files.append(process_file(file_path, filename))
            except Exception as e:
                return jsonify(error=f"Error processing {file}: {str(e)}"), 500

    return jsonify(
        message="All files processed successfully",
        processed_files=processed_files
    )

if __name__ == '__main__':
    app.run(debug=True)

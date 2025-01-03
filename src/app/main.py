# filepath: /Users/alejandrodiaz/Documents/GitHub/shadeaid/src/app/main.py
import os
from flask import Flask, request, jsonify
from utils import clear_folder, process_uploaded_file

app = Flask(__name__)

# Configure upload folders
UPLOAD_FOLDER = 'uploads'
ORIGINAL_FOLDER = os.path.join(UPLOAD_FOLDER, 'original')
PROCESSED_FOLDER = os.path.join(UPLOAD_FOLDER, 'processed')
os.makedirs(ORIGINAL_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        clear_folder(ORIGINAL_FOLDER)
        clear_folder(PROCESSED_FOLDER)

        if 'file' not in request.files:
            return "No file provided", 400

        file = request.files['file']
        result, status_code = process_uploaded_file(file, ORIGINAL_FOLDER, PROCESSED_FOLDER)
        if status_code == 200:
            return f"""
                <h1>{result['message']}</h1>
                <p>Grayscale Image: <a href="/{result['grayscale_path']}" target="_blank">View</a></p>
                <p>Shading Image: <a href="/{result['shading_path']}" target="_blank">View</a></p>
                <a href="/">Upload another file</a>
            """
        else:
            return f"Error: {result['error']}", status_code

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
    clear_folder(ORIGINAL_FOLDER)
    clear_folder(PROCESSED_FOLDER)

    if 'file' not in request.files:
        return jsonify(error="No file provided"), 400

    file = request.files['file']
    result, status_code = process_uploaded_file(file, ORIGINAL_FOLDER, PROCESSED_FOLDER)
    if status_code == 200:
        return jsonify(
            message=result['message'],
            grayscale_path=result['grayscale_path'],
            shading_path=result['shading_path']
        )
    else:
        return jsonify(error=result['error']), status_code

if __name__ == '__main__':
    app.run(debug=True)
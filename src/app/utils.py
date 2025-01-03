import os
import cv2
from werkzeug.utils import secure_filename
from process import convert_to_grayscale, identify_shading_patterns

def clear_folder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

def process_uploaded_file(file, original_folder, processed_folder):
    if file.filename == '':
        return "No file selected", 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(original_folder, filename)
    file.save(filepath)

    try:
        grayscale = convert_to_grayscale(filepath)
        shading = identify_shading_patterns(grayscale)

        grayscale_path = os.path.join(processed_folder, f"grayscale_{filename}")
        shading_path = os.path.join(processed_folder, f"shading_{filename}")
        cv2.imwrite(grayscale_path, grayscale)
        cv2.imwrite(shading_path, shading)

        return {
            "message": "File processed successfully",
            "grayscale_path": grayscale_path,
            "shading_path": shading_path
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500
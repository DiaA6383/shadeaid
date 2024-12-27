from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Artist Shading App API!"

# Endpoint for image processing (placeholder for now)
@app.route("/process-image", methods=["POST"])
def process_image():
    # Placeholder logic for image processing
    return jsonify({"message": "Image processed successfully!"})

if __name__ == "__main__":
    app.run(debug=True)

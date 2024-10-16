from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    image = request.files.get('image')
    if image:
        # Here you'd process the image (e.g., apply virtual try-on)
        return jsonify({"message": "Image received!"}), 200
    return jsonify({"error": "No image uploaded!"}), 400

if __name__ == '__main__':
    app.run(debug=True)

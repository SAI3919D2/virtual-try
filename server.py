from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    return jsonify({'message': 'Image received!'})

if __name__ == '__main__':
    app.run(debug=True)

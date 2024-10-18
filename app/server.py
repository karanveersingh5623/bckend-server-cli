from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
STORAGE_FOLDER = 'app/storage'
app.config['STORAGE_FOLDER'] = STORAGE_FOLDER

# Ensure the storage folder exists
os.makedirs(STORAGE_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "VehicleToolsChallenge - backend"

@app.route('/files/<filename>', methods=['POST'])
def upload_file(filename):
    if 'file' not in request.files:
        return 'No file part in the request', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    filename = secure_filename(filename)
    file_path = os.path.join(app.config['STORAGE_FOLDER'], filename)
    if os.path.exists(file_path):
        return 'File already exists', 409
    file.save(file_path)
    return 'File uploaded successfully', 201

@app.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    filename = secure_filename(filename)
    file_path = os.path.join(app.config['STORAGE_FOLDER'], filename)
    if not os.path.exists(file_path):
        return 'File not found', 404
    os.remove(file_path)

    return 'File deleted successfully', 200

@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir(app.config['STORAGE_FOLDER'])
    return jsonify(files), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

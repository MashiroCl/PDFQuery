from flask import Flask, jsonify, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "data"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello pdfquery"}), 200


@app.route("api/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "File not selected"}), 400

    if file and file.filename.endswith(".pdf"):
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

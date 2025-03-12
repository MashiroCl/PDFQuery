import pathlib
from flask import Flask, jsonify, request
from core import load_split_pdf

app = Flask(__name__)

UPLOAD_FOLDER = pathlib.Path("pdfdata")

if not UPLOAD_FOLDER.exists:
    UPLOAD_FOLDER.mkdir()


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
        file_path = UPLOAD_FOLDER.joinpath(file.filename)
        file.save(file_path)

        load_split_pdf(file_path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
